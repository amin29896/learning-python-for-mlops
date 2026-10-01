import asyncio
import json
import time
from pathlib import Path
from . import *
async def process(filepath:Path) -> predictionresult:
    try:

        start_time=time.perf_counter()
        await asyncio.sleep(0.1)
        raw_text=filepath.read_text(encoding="utf-8").lower()
        data=json.loads(raw_text)
        payload_text=data["payload"]["feeling"]
        if "happy" in payload_text:
            pred_data={"label":"positive","score":0.90}
        elif "worried" in payload_text:
            pred_data={"label":"negative","score":0.40}
        elif "broken" in payload_text:
            pred_data={"label":"negative","score":0.20}
        elif "excited" in payload_text:
            pred_data={"label":"positive","score":1}
        else:
            pred_data={"label":"neutral","score":0.50}

        return(predictionresult(filepath.name,"SUCCESS",data["id"],pred_data,execution_time=round(time.perf_counter()-start_time,4)))
    except FileNotFoundError:
        print("file not found ")
        return(predictionresult(None,"FAILURE",None,None,execution_time=round(time.perf_counter()-start_time,4)))
    except json.JSONDecodeError:
        print(f"check the syntax of {filepath.name}")
        return(predictionresult(filepath.name,"FAILURE",None,None,execution_time=round(time.perf_counter()-start_time,4)))
    except Exception:
        return(predictionresult(None,"FAILURE",None,None,execution_time=round(time.perf_counter()-start_time,4)))
    

