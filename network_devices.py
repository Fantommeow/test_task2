class NetworkDevice:
    """Базовый класс для сетевых устройств."""

    def __init__(self, name, ip_address):
        self.name = name
        self.ip_address = ip_address
        self.status = "Inactive"

    def power_on(self):
        """Включает устройство."""
        self.status = "Active"
        print(f"Device {self.name} is powered on.")

    def power_off(self):
        """Выключает устройство."""
        self.status = "Inactive"
        print(f"Device {self.name} is powered off.")

    def get_info(self):
        """Возвращает информацию об устройстве."""
        return f"Device: {self.name}\nIP Address: {self.ip_address}\nStatus: {self.status}"


class Router(NetworkDevice):
    """Класс для маршрутизаторов."""

    def __init__(self, name, ip_address):
        super().__init__(name, ip_address)
        self.routing_table = {}

    def add_route(self, destination, gateway):
        """Добавляет маршрут в таблицу."""
        self.routing_table[destination] = gateway
        print(f"Route added: {destination} -> {gateway}")

    def remove_route(self, destination):
        """Удаляет маршрут из таблицы."""
        if destination in self.routing_table:
            del self.routing_table[destination]
            print(f"Route removed: {destination}")
        else:
            print(f"Route {destination} not found.")

    def get_info(self):
        """Переопределяет метод базового класса, добавляя информацию о таблице маршрутизации."""
        info = super().get_info()
        info += f"\nRouting Table: {self.routing_table}"
        return info


class Switch(NetworkDevice):
    """Класс для коммутаторов."""

    def __init__(self, name, ip_address):
        super().__init__(name, ip_address)
        self.vlan = None

    def create_vlan(self, vlan_id):
        """Создает VLAN."""
        self.vlan = vlan_id
        print(f"VLAN {vlan_id} created.")

    def delete_vlan(self):
        """Удаляет VLAN."""
        if self.vlan is not None:
            self.vlan = None
            print(f"VLAN deleted.")
        else:
            print(f"No VLAN to delete.")

    def get_info(self):
        """Переопределяет метод базового класса, добавляя информацию о VLAN."""
        info = super().get_info()
        if self.vlan is not None:
            info += f"\nVLAN: {self.vlan}"
        return info
