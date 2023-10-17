class FileManager():
    def __init__(self, path: str, mode: str):
        self.file = open(path, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


print(type({}))
