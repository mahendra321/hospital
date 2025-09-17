from fastapi import FastAPI


app = FastAPI()



@app.get("/home")
def yoyo():
    return " welcome  back to fastapi"
@app.get("/test")
def testing():
    return "yoyo this a test!!!!!!!!!!!!!"