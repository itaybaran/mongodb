from service.executor import Executor

executor = Executor(config_file_path='service/configuration.yaml')

def root():
    return {"message": "Hello World"}


def read_item(item_id):
    item = executor.mongo.get_doc_by_id(item_id)
    return {"item_id": item_id}


print(root())
print(read_item('U1IT00001'))