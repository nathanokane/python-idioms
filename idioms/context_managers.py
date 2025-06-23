from contextlib import contextmanager
from time import perf_counter
import os


class ContextManager:
    def __init__(self, name):
        self.fileName = name
        self.fp = None
        self.start_time = None
        self.end_time = None
    
    def __enter__(self):
        self.start_time = perf_counter()
        self.fp = open(self.fileName, "a+")
        self.fp.seek(0) 
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()
        self.end_time = perf_counter()
        self.calc_time()

    def calc_time(self):
        total = self.end_time - self.start_time
        print(f"Total time taken was {total}")



with ContextManager("../read-files/words.txt") as myfile:
    for line in myfile:
        print(line)

    