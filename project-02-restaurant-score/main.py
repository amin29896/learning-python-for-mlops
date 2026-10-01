from needed_modules import *
from pathlib import Path
import asyncio
async def main():
    try:

        p=Path("data")
        if p.exists()==False:
            raise FileNotFoundError 
        json_files=list(p.glob("*.json"))
        if len(json_files)==0:
            raise DataFileEmptyError 
        tasks=list(asyncio.create_task(process(path)) for path in json_files)
        results=await asyncio.gather(*tasks)
        success=0
        failed=0
        total_time=0.0
        tot_score=0.0
        for r in results:
            if r.status=="SUCCESS":
                success+=1
                print(f"SUCCESS {r.filename} , ID: {r.request_id}, Prediction : {r.prediction}, EXECUTION TIME : {r.execution_time}")
                tot_score+=r.prediction["score"]
            else:
                failed+=1
            total_time+=r.execution_time
        print("-"*50)
        print(f"SUMMARY:{success} succeeded and {failed} failed , AVG TIME : {round(total_time/len(results),4)}, GLOBAL SCORE : {round(tot_score/success,4)} ")
    except FileNotFoundError:
        print("data file not found")
    except DataFileEmptyError:
        print("your data file is empty")
asyncio.run(main())
