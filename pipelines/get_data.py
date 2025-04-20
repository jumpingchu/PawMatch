import io
import os
from datetime import datetime, timedelta

import pyarrow as pa
import pyarrow.parquet as pq
import requests
from dotenv import load_dotenv
from google.cloud import storage
from models import ApiUrls
from prefect import flow, task


def data_to_gcs_parquet(data, bucket_name, blob_name):
    # 將 Python 字典轉換為 PyArrow Table
    table = pa.Table.from_pylist(data)

    # 將 PyArrow Table 寫入 bytes buffer
    buffer = io.BytesIO()
    pq.write_table(table, buffer)
    buffer.seek(0)

    # 上傳 bytes buffer 到 GCS
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_file(buffer, content_type="application/octet-stream")
    print(f"DataFrame 已儲存為 Parquet 檔案到 gs://{bucket_name}/{blob_name}")


def get_data(url, params: dict):
    response = requests.get(url, params=params)
    return response.json()


def create_params(date_str: str):
    params = {"UnitId": "QcbUEzN6E6DL", "animal_opendate": date_str}
    return params


@flow
def flow_adoption_data():
    load_dotenv()

    # request configs
    date = datetime.now() - timedelta(days=1)
    date_str = date.strftime("%Y-%m-%d")
    params = create_params(date_str)
    url = ApiUrls.PetAdoption.value

    # get data
    data = get_data(url, params)

    # GCS upload
    bucket_name = os.getenv("GCS_BUCKET_NAME")
    blob_name = f"raw/{date_str}.parquet"
    data_to_gcs_parquet(data, bucket_name, blob_name)
