from abc import ABCMeta, abstractmethod


class GameElement(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def calculate_rules(self):
        pass

    @abstractmethod
    def process_events(self, events):
        pass
