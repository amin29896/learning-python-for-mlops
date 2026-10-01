from dataclasses import dataclass,field,InitVar
from datetime import datetime 
@dataclass
class config:
    model_name:str
    _batch_size:int
    api_key: InitVar[str]
    created_at:str=field(default_factory=lambda:datetime.now().isoformat())
    tags:list=field(default_factory=list)
    masked_api:str=""
    def __post_init__(self,key):
        if len(key) >4 :
            self.masked_api="*"*(len(key)-4)+key[-4:]
        else :
            self.masked_api="****"
    @property
    def batch_size(self) -> int:
        return(self._batch_size)
    @batch_size.setter
    def batch_size(self,value:int):
        if not isinstance(value,int) or value<=0:
            raise ValueError("batch size must be a positive integer")
        self._batch_size=value

        


