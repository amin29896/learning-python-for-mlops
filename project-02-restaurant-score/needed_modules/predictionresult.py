from dataclasses import dataclass,field
from typing import Optional
from datetime import datetime
@dataclass
class predictionresult:
    filename:Optional[str]
    status:str
    request_id:Optional[str]
    prediction:Optional[dict[str,any]]
    execution_time:float
    created_at:str=field(default_factory=lambda:datetime.now().isoformat())
    error_message:Optional[str]=None

