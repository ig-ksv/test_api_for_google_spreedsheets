from abc import ABC, abstractmethod


class BaseDao(ABC):
    @abstractmethod
    def get_data(self):
        pass
