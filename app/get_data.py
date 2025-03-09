import pandas as pd
import requests
from models import ApiUrls


def get_data(url):
    response = requests.get(url)
    return response.json()


data = get_data(ApiUrls.PetAdoptionUrl)

df = pd.DataFrame(data)
