import pandas as pd
from pathlib import Path
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials


@task(retries=3)
def extract_from_gcs(color: str, year: int, month: int) -> Path:
    """Download trip data from GCS"""
    gcs_path = f'data/{color}/{color}_tripdata_{year}-{month:02}.parquet'
    gcs_block = GcsBucket.load("de-zoomcamp-gcs")
    gcs_block.get_directory(from_path=gcs_path, local_path='./')
    return Path(gcs_path)


@task()
def transform(path: Path) -> pd.DataFrame:
    """No Transformation here just Extract and Load"""
    df = pd.read_parquet(path)
    return df


@task()
def write_bq(df: pd.DataFrame) -> None:
    """Write DataFrame to BigQuery"""
    gcp_credentials_block = GcpCredentials.load("de-zoomcamp-gcp-creds")
    df.to_gbq(
        destination_table='dezoomcamp.rides_q3',
        project_id='prefect-dezoomcamp',
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists='append'
    )


@flow(log_prints=True)
def etl_gcs_to_bq(year: int, month: int, color: str) -> int:
    """ETL Flow to load data into BigQuery"""
    path = extract_from_gcs(color, year, month)
    df = transform(path)
    write_bq(df)
    return len(df)


@flow(log_prints=True)
def etl_parent_flow(months: list[int], year: int, color: str) -> None:
    """Main Flow to iterate over loading data into BigQuery"""
    df_len = 0
    for month in months:
        df_len = df_len + etl_gcs_to_bq(year, month, color)
    print(f"No of rows processed:{df_len}")

if __name__ == '__main__':
    color = "yellow"
    months = [2, 3]
    year = 2019

    etl_parent_flow(months, year, color)
