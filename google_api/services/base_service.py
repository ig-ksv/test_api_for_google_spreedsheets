from abc import ABC, abstractmethod


class BaseService(ABC):
    @abstractmethod
    def get_data_types(self):
        pass
