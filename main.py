from fastapi import FastAPI
from service.executor import Executor


app = FastAPI()
executor = Executor(config_file_path='service/configuration.yaml')


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_name}")
async def read_item(item_name):
    item = executor.mongo.get_doc_by_id(item_name)
    return {"item": item}