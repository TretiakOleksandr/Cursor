from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, name, coordinate, team):
        self.name = name
        self.coordinate = coordinate
        self.team = team

    @property
    def display_name(self):
        return f'{self.name} ({self.team}) - {self.coordinate}'

    @classmethod
    def create_from_dict(cls, dict_:dict):
        return cls(name=dict_.get('FNAME'), coordinate=dict_.get('FCOORDINATE'), team=dict_.get('FTEAM'))

    @abstractmethod
    def check_cell(self):
        pass

class Horse(Figure):
    def check_cell(self):
        pass

class Pawn(Figure):
    def check_cell(self):
        pass