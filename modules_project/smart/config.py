import os 
from dotenv import load_dotenv
load_dotenv()
class config:
    MAX_VALUE : int=int(os.environ.get("MAX_INPUT_VALUE",100000))
    PRECISION : int=int(os.environ.get("CALC_PRECISION",2))
