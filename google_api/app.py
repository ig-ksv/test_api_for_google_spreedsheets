import os

from fastapi import FastAPI
from urllib.parse import urlparse

from google_api.connectors.google_conector import GoogleConnector
from google_api.daos.google_dao import GoogleSheetsDao
from google_api.services.google_service import GoogleSheetsService


app = FastAPI()
api_key = os.environ["GOOGLE_PROJECT_APIKEY"]


@app.get("/")
async def get_company_data(spreadsheet_url: str):
    try:
        url = urlparse(spreadsheet_url)
        spreadsheet_id = url.path.split("/")[-1]
    except Exception:
        return "Url is not valid"
    connector = GoogleConnector(api_key)
    data_dao = GoogleSheetsDao(connector, spreadsheet_id)
    data_service = GoogleSheetsService(data_dao)
    result = data_service.get_data_types()
    return result

