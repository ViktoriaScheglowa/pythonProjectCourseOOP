import json
from abc import ABC, abstractmethod


class FileHandler():
    def __init__(self, filename):
        self.filename = filename
        self.open_file = open("./data/" + self.filename, mode="a", encoding="utf-8")

    def write(self, text):
        with self.open_file as file:
            file.write(json.dumps(text, ensure_ascii=False, indent=4))
