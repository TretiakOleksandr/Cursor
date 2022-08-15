class VacuumCleaner:
    trash_tank_volume = 0
    water_tank_volume = 0
    def __init__(self, water_tank_level,trash_tank_level,power_level,id_):
        self.water_tank_level = water_tank_level
        self.trash_tank_level = trash_tank_level
        self.power_level = power_level
        self.id_ = id_
    @property
    def info(self):
        return f"{self.id_}; power - {self.power_level}%; " \
               f"water tank - {self.water_tank_level/self.water_tank_volume * 100}%; " \
               f"trash tank - {self.trash_tank_level/self.trash_tank_volume * 100}"
