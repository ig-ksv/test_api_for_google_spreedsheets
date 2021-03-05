
from dateutil.parser import parse

from google_api.services.base_service import BaseService
from google_api.daos.base_dao import BaseDao


class GoogleSheetsService(BaseService):
    def __init__(self, service_dao: BaseDao):
        self.service_dao = service_dao

    def get_data_types(self):
        columns = self.service_dao.get_data()

        columns = [(column[0], column[1:]) for column in columns]
        result = {}
        for column in columns:
            if self.is_integer(column[1]):
                result[column[0]] = "Integer"
            elif self.is_float(column[1]):
                result[column[0]] = "Float"
            elif self.is_boolean(column[1]):
                result[column[0]] = "Boolean"
            elif self.is_datetime(column[1]):
                result[column[0]] = "Datetime"
            else:
                result[column[0]] = "String"

        return result

    @staticmethod
    def is_integer(column: list):
        try:
            [int(value) for value in column]
        except ValueError:
            return False
        else:
            return True

    @staticmethod
    def is_float(column: list):
        try:
            [float(value) for value in column]
        except ValueError:
            return False
        else:
            return True

    @staticmethod
    def is_boolean(column: list):
        try:
            result = [value.lower() in ["true", "false"] for value in column]
        except Exception:
            return False
        if all(result):
            return True
        return False

    @staticmethod
    def is_datetime(column: list):
        try:
            [parse(value) for value in column]
        except Exception:
            return False
        else:
            return True
