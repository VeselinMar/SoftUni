class RCAConnection:
    def connect_to_device_via_rca_cable(self, device):
        pass


class EthernetCableConnection:
    def connect_to_device_via_ethernet_cable(self, device):
        pass


class HDMICableConnection:
    def connect_to_device_via_hdmi_cable(self, device):
        pass


class EntertainmentDevice:

    def __init__(self, name: str, id_: int, power: int = 0):
        self.name = name
        self.id = id_
        self.power = power

    def connect_device_to_power_outlet(self, device):
        pass


class Television(EntertainmentDevice, RCAConnection, HDMICableConnection):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(EntertainmentDevice, HDMICableConnection):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(EntertainmentDevice, HDMICableConnection, EthernetCableConnection):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EntertainmentDevice, EthernetCableConnection):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
