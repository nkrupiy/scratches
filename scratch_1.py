import unittest

from typing import (
    Any, AnyStr, Callable, Container, ContextManager, Dict, FrozenSet, Generic, Iterable,
    Iterator, List, NoReturn, Optional, overload, Pattern, Sequence, Set, TextIO,
    Tuple, Type, TypeVar, Union
)
import logging
import sys
from types import ModuleType, TracebackType



no_output = 0
def p(t,t1='',t2='',t3='',t4='',t5='',t6='',t7='',t8=''):
    if no_output != 1: print(t,t1,t2,t3,t4,t5,t6,t7,t8)

_T = TypeVar('_T')

p(_T)