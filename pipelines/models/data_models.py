from pydantic.dataclasses import dataclass


@dataclass
class AnimalAdoptionData:
    """
    - animal_id: 動物的流水編號
    - animal_subid: 動物的區域編號
    - animal_area_pkid: 動物所屬縣市代碼
    - animal_shelter_pkid: 動物所屬收容所代碼
    - animal_place: 動物的實際所在地
    - animal_kind: 動物的類型
    - animal_sex: 動物性別
    - animal_bodytype: 動物體型 [SMALL | MEDIUM | BIG]
    - animal_colour: 動物毛色
    - animal_age: 動物年紀
    - animal_sterilization: 是否絕育
    - animal_bacterin: 是否施打狂犬病疫苗
    - animal_foundplace: 動物尋獲地
    - animal_title: 動物網頁標題
    - animal_status: 動物狀態 [NONE | OPEN | ADOPTED | OTHER | DEAD]
    - animal_remark: 資料備註
    - animal_caption: 其他說明
    - animal_opendate: 開放認養時間(起)
    - animal_closeddate: 開放認養時間(迄)
    - animal_update: 動物資料異動時間
    - animal_createtime: 動物資料建立時間
    - shelter_name: 動物所屬收容所名稱
    - album_file: 圖片名稱
    - album_update: 資料更新時間
    - cDate: 資料建立時間
    - shelter_address: 地址
    - shelter_tel: 聯絡電話
    - top: 取得前幾筆
    - Page: 頁碼 (Y)
    """

    animal_id: str
    animal_subid: str
    animal_area_pkid: str
    animal_shelter_pkid: str
    animal_place: str
    animal_kind: str
    animal_sex: str
    animal_bodytype: str
    animal_colour: str
    animal_age: str
    animal_sterilization: str
    animal_bacterin: str
    animal_foundplace: str
    animal_title: str
    animal_status: str
    animal_remark: str
    animal_caption: str
    animal_opendate: str
    animal_closeddate: str
    animal_update: str
    animal_createtime: str
    shelter_name: str
    album_file: str
    album_update: str
    cDate: str
    shelter_address: str
    shelter_tel: str
    top: str
    Page: str
