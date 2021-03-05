import pytest

from unittest.mock import MagicMock

from google_api.services.google_service import GoogleSheetsService


test_cols = {"range": "Sheet1!A1:Z999",
             "majorDimension": "COLUMNS",
             "values": [["Batsman", "65756", "65756", "65756", "65756", "3676", "3676"],
                        ["Batsman_Name", "Mohammed Shami", "Bhuvneshwar", "Shami",
                         "Bhuvneshwar Kumar", "MS Dhoni", "MS Dhoni"],
                        ["Isball", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE", "TRUE"],
                        ["Over", "49.6", "49.6", "49.5", "49.4", "49.3", "49.2"],
                        ["Timestamp", "2019-07-02 13:18:47", "2019-07-02 13:17:28", "2019-07-02 13:16:03",
                         "2019-07-02 13:15:17", "2019-07-02 13:13:39", "2019-07-02 13:12:47"]
                        ]}


class TestGoogleApiService:

    def test_get_data_types(self):
        test_dao = MagicMock()
        test_dao.get_data.return_value = test_cols.copy()["values"]
        service = GoogleSheetsService(test_dao)
        result = service.get_data_types()

        assert result["Batsman"] == "Integer"
        assert result["Batsman_Name"] == "String"
        assert result["Isball"] == "Boolean"
        assert result["Over"] == "Float"
        assert result["Timestamp"] == "Datetime"



