from prefect.deployments import Deployment
from prefect.filesystems import GitHub
import etl_web_to_gcs_q5


github_block = GitHub.load("git-q4")

deployment = Deployment.build_from_flow(
    flow=etl_web_to_gcs_q5,
    name="q5 ",
    storage=github_block,
    entrypoint="week2/week_2_workflow_orchestration/etl_web_to_gcs_q5.py:etl_web_to_gcs_q5")

if __name__ == "__main__":
    deployment.apply()
