## Workflow Orchestration with Prefect
   ```
    Operating System:               Linux(Ubuntu)/Windows
    Code:                           https://github.com/praveenbalijepalli/DE_Zoomcamp/blob/main/Week%201/week_2_workflow_orchestration/week_2_workflow_orchestration.ipynb
    Environment Setup:              conda create -n DE python=3.9
                                    conda activate DE
                                    pip install -r requirements.txt
    
    Prefect:                        Workflow Orchestration tool
    Run Prefect:                    prefect orion start
    Other Prefect Information:      Configure Prefect to communicate with the server with: prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api
                                    View the API reference documentation at http://127.0.0.1:4200/docs
                                    Check out the dashboard at http://127.0.0.1:4200
 
 
 
    Run Postgres Docker Container:  docker run -it \
                                    -e POSTGRES_USER="root" \
                                    -e POSTGRES_PASSWORD="root" \
                                    -e POSTGRES_DB="ny_taxi" \
                                    -v {$pwd}/data/ny_taxi_postgres_data: /var/lib/postgresql/data \
                                    -p 5432:5432 \
                                    postgres:13
  
    # NOTE: I use fishshell(https://fishshell.com/) which recommends $pwd in {}, i.e {$pwd}. 
    # However, in most cases simply using the absolute path will always works.                                   
                                    
   Command to run pgcli          :  pgcli -h localhost -p 5432 -u root -W root -d ny_taxi
   ```   
   
## GCP-Terraform
