## Data Warehousing
   ```
    Operating System:               Windows
    Code:                           https://github.com/praveenbalijepalli/DE_Zoomcamp/blob/main/Week2/week_3_data_warehouse/week_3_data_warehouse.ipynb
    Environment Setup:              conda create -n DPhi-DE python=3.9
                                    conda activate DPhi-DE
                                    pip install -r requirements.txt
                                    
    GCP:                            Google Cloud Platform
    Current Project:                prefect-dezoomcamp 
    GCS Bucket:                     week3_data_warehouse
   
    Prefect:                        Workflow Orchestration tool
    Prefect Blocks:                 GCP-Credentials and GCS-Bucket
    GCP-Credentials Block Name:     ## Name of the credential block can be anything - Ex: #GCP-somecredentials
    GCS-Bucket Block Name:          week3-data-warehouse
    Run Prefect:                    prefect orion start
    Other Prefect Information:      Configure Prefect to communicate with the server with: prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
                                    View the API reference documentation at http://127.0.0.1:4200/docs
                                    Check out the dashboard at http://127.0.0.1:4200
   ```
