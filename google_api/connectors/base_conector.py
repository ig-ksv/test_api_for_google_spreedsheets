from abc import ABC, abstractmethod


class BaseConnector(ABC):
    @abstractmethod
    def connect_to_service(self):
        pass

    @abstractmethod
    def get_values(self):
        pass
