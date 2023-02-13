from pathlib import Path
import pandas as pd
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from random import randint


@task(retries=3)
def fetch(dataset_url: str) -> pd.DataFrame:
    """Read taxi data from web into pandas DataFrame"""
    # if randint(0, 1) > 0:
    #     raise Exception

    df = pd.read_csv(dataset_url)
    return df


@task(log_prints=True)
def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Fix dtype issues"""
    df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])
    df["dropOff_datetime"] = pd.to_datetime(df["dropOff_datetime"])
    df["PUlocationID"] = df["PUlocationID"].astype('Int32')
    df["DOlocationID"] = df["DOlocationID"].astype('Int32')
    df["SR_Flag"] = df["SR_Flag"].astype('Int32')

    print(df.head(2))
    print(f"columns: {df.dtypes}")
    print(f"rows: {len(df)}")
    return df


@task()
def write_local(df: pd.DataFrame, dataset_file: str) -> Path:
    """Write DataFrame out locally as parquet file"""
    Path(f"data").mkdir(parents=True, exist_ok=True)
    path = Path(f"data/{dataset_file}.csv.gz")
    df.to_csv(path, compression="gzip")
    return path


@task()
def write_gcs(path: Path) -> None:
    """Upload local csv.gz file to GCS"""
    gcp_cloud_storage_bucket_block = GcsBucket.load("week3-data-warehouse")
    gcp_cloud_storage_bucket_block.upload_from_path(
        from_path=path, to_path=path)


@flow()
def etl_web_to_gcs(year: int, month: int) -> int:
    """The ETL function"""

    dataset_file = f"fhv_tripdata_{year}-{month:02}"

    dataset_url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/{dataset_file}.csv.gz"

    df = fetch(dataset_url)
    df_clean = clean(df)
    path = write_local(df_clean, dataset_file)
    write_gcs(path)
    return len(df_clean)


@flow()
def etl_parent_flow(year: int, months: list[int]) -> None:
    """Main Flow for iteration of ETL"""

    df_len = 0
    for month in months:
        df_len = df_len + etl_web_to_gcs(year, month)
    print(f"Count for fhv vehicle records for year 2019: {df_len}")


if __name__ == '__main__':
    months = list(range(1, 13))
    year = 2019
    etl_parent_flow(year, months)
