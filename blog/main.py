from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def show():
    return {'message':'welcom to my home page'}
