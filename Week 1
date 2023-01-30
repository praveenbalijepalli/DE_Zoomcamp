a. Docker-SQL:
    ```
    Operating System:               Linux(Ubuntu)
    Code:                           week_1_docker_sql.ipynb
    Environment Setup:              conda create -n DE python=3.9
                                    conda activate DE
                                    conda install -c conda-forge pandas sqlalchemy jupyter pgcli
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
   b. GCP-Terraform:
