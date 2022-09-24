import time


class Warmer:
    def __init__(self, id, state):
        self.__id = id
        self.__state = state

    def __str__(self):
        return self.__id

    @property
    def id(self):
        return self.__id

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state
        self.get_message()

    def get_message(self):
        if self.__state:
            print(f'Desligando o aquecedor {self}.')
            time.sleep(1)
            print(f'Aquecedor{self} DESLIGADO.')
        else:
            print(f'Ligando o aquecedor {self}')
            time.sleep(1)
            print(f'Aquecedor {self} LIGADO.')
