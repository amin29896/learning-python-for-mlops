from . import *
from .config import config
from .exceptions import limitexception
def add(a:float,b:float) -> float:
    if a>config.MAX_VALUE or b>config.MAX_VALUE:
        raise limitexception
    return round(a+b,config.PRECISION)
def mul(a:float,b:float) -> float:
    if a>config.MAX_VALUE or b>config.MAX_VALUE:
        raise limitexception
    return round(a*b,config.PRECISION)
def subs(a:float,b:float) -> float:
    if a>config.MAX_VALUE or b>config.MAX_VALUE:
        raise limitexception
    return round(a-b,config.PRECISION)
def div(a:float,b:float) -> float:
    if a>config.MAX_VALUE or b>config.MAX_VALUE:
        raise limitexception
    if(b==0):
        raise ZeroDivisionError
    return round(a/b,config.PRECISION)
