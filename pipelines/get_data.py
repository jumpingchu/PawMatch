import os

import pandas as pd
import pandas_gbq
import requests
from dotenv import load_dotenv
from models import ApiUrls


def get_data(url, params: dict):
    response = requests.get(url, params=params)
    return response.json()


# https://data.moa.gov.tw/api/v1/AnimalRecognition?animal_opendate=2025-03-10&$top=10
# https://data.moa.gov.tw/Service/OpenData/TransService.aspx?UnitId=QcbUEzN6E6DL&animal_opendate=2025-03-16


def create_params(date_str: str):
    params = {"UnitId": "QcbUEzN6E6DL", "animal_opendate": date_str}
    return params


def upload_bq(df, dest_table_id, project_id):
    pandas_gbq.to_gbq(df, dest_table_id, project_id)
    return f"Data uploaded to {dest_table_id}"


def flow_adoption_data():
    load_dotenv()
    date_str = "2025-03-10"
    params = create_params(date_str)
    url = ApiUrls.PetAdoption.value
    data = get_data(url, params)
    df = pd.DataFrame(data)
    df = df.astype(str)
    df["animal_opendate"] = df["animal_opendate"].apply(pd.to_datetime)

    project_id = os.getenv("GCP_PROJECT_ID")
    dataset_id = "paw_match"
    table_id = "adoption_opendata"

    upload_bq(df, f"{dataset_id}.{table_id}", project_id)


if __name__ == "__main__":
    flow_adoption_data()
