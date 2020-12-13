# 추상 클래스
from abc import *

class AbstractGil(metaclass=ABCMeta):
    name = '이름'

    @abstractmethod
    def showName(self):
        print("이름은?")

class Gillog(AbstractGil):

    def __init__(self, name):
        self.name = name
    def showName(self):
        super().showName()
        print(self.name, "입니다.")

gillog = Gillog("gillog")

gillog.showName()