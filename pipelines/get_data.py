import os
import pandas as pd
import pandas_gbq
import requests
from models import ApiUrls
from dotenv import load_dotenv


def get_data(url):
    response = requests.get(url)
    return response.json()


def upload_bq(df, dest_table_id, project_id):
    pandas_gbq.to_gbq(
        dataframe=df, destination_table=dest_table_id, project_id=project_id
    )
    return f"Data uploaded to {dest_table_id}"


def flow_adoption_data():
    load_dotenv()
    project_id = os.getenv("GCP_PROJECT_ID")
    dataset_id = "paw_match"
    table_id = "adoption_opendata"
    
    data = get_data(ApiUrls.PetAdoption.value)
    df = pd.DataFrame(data)[:10]
    upload_bq(df, f"{dataset_id}.{table_id}", project_id)

if __name__ == "__main__":
    flow_adoption_data()
