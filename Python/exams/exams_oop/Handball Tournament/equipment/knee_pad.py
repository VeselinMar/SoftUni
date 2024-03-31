from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    INCREASE_PERCENT = 0.2

    def __init__(self):
        super().__init__(protection=120, price=15.0)

    def increase_price(self):
        self.price += self.price * self.INCREASE_PERCENT
