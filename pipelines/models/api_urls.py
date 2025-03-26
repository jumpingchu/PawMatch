from enum import Enum, unique


@unique
class ApiUrls(Enum):
    PetAdoption = "https://data.moa.gov.tw/Service/OpenData/TransService.aspx"
