from google_api.connectors.base_conector import BaseConnector
from google_api.daos.base_dao import BaseDao


class GoogleSheetsDao(BaseDao):
    def __init__(self,
                 connector: BaseConnector,
                 spreadsheet_id: str,
                 spreadsheet_range: str = "A:XX",
                 spreadsheet_dimension: str = "COLUMNS"):
        self.connector = connector
        self.spreadsheet_id = spreadsheet_id
        self.spreadsheet_range = spreadsheet_range
        self.spreadsheet_dimension = spreadsheet_dimension

    def get_data(self):
        values = self.connector.get_values()
        result = values.get(spreadsheetId=self.spreadsheet_id,
                            range=self.spreadsheet_range,
                            majorDimension=self.spreadsheet_dimension).execute()
        return result["values"]
