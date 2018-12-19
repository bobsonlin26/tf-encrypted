import abc
from typing import List, TypeVar, Generic, Optional


class AbstractTensor(abc.ABC):

    @property
    @abc.abstractproperty
    def factory(self) -> 'AbstractFactory':
        pass

    @property
    @abc.abstractproperty
    def shape(self):
        pass


class AbstractConstant(AbstractTensor):
    pass


class AbstractPlaceholder(AbstractTensor):
    pass


class AbstractVariable(AbstractTensor):
    pass


T = TypeVar('T')
C = TypeVar('C')
V = TypeVar('V')
P = TypeVar('P')


class AbstractFactory(abc.ABC, Generic[T, C, V, P]):

    @property
    @abc.abstractproperty
    def modulus(self) -> int:
        pass

    @property
    @abc.abstractproperty
    def native_type(self):
        pass

    @abc.abstractmethod
    def tensor(self, value) -> T:
        pass

    @abc.abstractmethod
    def constant(self, value) -> C:
        pass

    @abc.abstractmethod
    def variable(self, initial_value) -> V:
        pass

    @abc.abstractmethod
    def placeholder(self, shape) -> P:
        pass

    @abc.abstractmethod
    def sample_uniform(self, shape, minval: Optional[int] = None) -> T:
        pass

    @abc.abstractmethod
    def sample_bounded(self, shape, bitlength: int) -> T:
        pass

    @abc.abstractmethod
    def stack(self, xs: List[T], axis: int = 0) -> T:
        pass

    @abc.abstractmethod
    def concat(self, xs: List[T], axis: int) -> T:
        pass
