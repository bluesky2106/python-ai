from abc import ABC, abstractmethod


class PersistentStorage(ABC):
    @abstractmethod
    def add_data(self):
        pass

    @abstractmethod
    def get_all_data(self):
        pass
