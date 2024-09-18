from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    with open("data/hello.txt", "r") as f:
        return {"message": f.read()}
