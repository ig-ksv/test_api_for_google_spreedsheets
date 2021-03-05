from abc import ABC, abstractmethod
from googleapiclient.discovery import build

from google_api.connectors.base_conector import BaseConnector


class GoogleConnector(BaseConnector):
    def __init__(self, api_key: str):
        self.service = self.connect_to_service(api_key)

    @staticmethod
    def connect_to_service(api_key):
        return build('sheets', 'v4', developerKey=api_key)

    def get_values(self):
        sheet = self.service.spreadsheets()
        return sheet.values()
