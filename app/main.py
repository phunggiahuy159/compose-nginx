from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI via Nginx!"}
#test: 
#curl http://localhost
