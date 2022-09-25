class GreenHouse:
    def __init__(self, client_id, name, temperature, humidity):
        self.__client_id = client_id
        self.__name = name
        self.__temperature = temperature
        self.__humidity = humidity

    def __str__(self):
        return self.__name

    @property
    def client_id(self):
        return self.__client_id

    @property
    def name(self):
        return self.__name

    @property
    def temperature(self):
        return self.__temperature

    @property
    def humidity(self):
        return self.__humidity

    def raise_temperature(self):
        self.__temperature += 1

    def drop_temperature(self):
        self.__temperature -= 1

    def raise_humidity(self):
        self.__humidity += 1

    def drop_humidity(self):
        self.__humidity -= 1

