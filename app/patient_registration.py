from fastapi import FastAPI


app = FastAPI()



@app.get("/home")
def yoyo():
    return " welcome  back to fastapi"