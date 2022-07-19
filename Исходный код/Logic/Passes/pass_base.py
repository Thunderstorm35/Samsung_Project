from abc import ABC, abstractmethod
from enum import Enum


class PassBase(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply(self):
        pass


class PassWithParams(PassBase):
    @abstractmethod
    def __init__(self, name):
        super().__init__(name)
        self.params = PassParams()
        self.defineParams()

    @abstractmethod
    def defineParams(self):
        pass


class ParamType(Enum):
    SLIDER = 1
    NUMBER = 2


class PassParam:
    def __init__(self, name, value, min, max, type):
        self._name = name
        self._value = value
        self._min = min
        self._max = max
        self._type = type

    def getName(self):
        return self._name

    def getValue(self):
        return self._value

    def getMin(self):
        return self._min

    def getMax(self):
        return self._max

    def getType(self):
        return self._type

    def setValue(self, value):
        if value >= self._min or value <= self._min:
            self._value = value


class PassParams:
    def __init__(self):
        self._params = dict()

    def addParam(self, name, value, min, max, type):
        self._params[name] = PassParam(name, value, min, max, type)

    def getParam(self, name):
        return self._params[name]

    def getValueByName(self, name):
        return self._params[name].getValue()

    def getParamsList(self):
        return self._params.values()
