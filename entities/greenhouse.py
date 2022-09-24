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

    @temperature.setter
    def temperature(self, temperature):
        self.__temperature = temperature

    @humidity.setter
    def humidity(self, humidity):
        self.__humidity = humidity
