import time


class Warmer:
    def __init__(self, id, name, state):
        self.__id = id
        self.__name = name
        self.__state = state

    def __str__(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state
        self.__get_message()

    def __get_message(self):
        if self.__state:
            print(f'Ligando o aquecedor do {self}')
            time.sleep(1)
            print(f'Aquecedor do {self} LIGADO.')
        else:
            print(f'Desligando o aquecedor do {self}.')
            time.sleep(1)
            print(f'Aquecedor do {self} DESLIGADO.')

    def is_active(self):
        if self.__state:
            return True
        return False
