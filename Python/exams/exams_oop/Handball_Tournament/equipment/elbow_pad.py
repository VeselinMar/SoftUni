from Python.exams.exams_oop.Handball_Tournament.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    INCREASE_PERCENT = 0.1

    def __init__(self):
        super().__init__(protection=90, price=25.0)

    def increase_price(self):
        self.price += self.price * self.INCREASE_PERCENT
        