from contextlib import contextmanager
from time import perf_counter
import os


#Basic context manager, which does the same job as the with function for opening files
#Returns a file object and allows you to use any file functions that you would use normally

#


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
        #Could be modified to handle exceptions, via checking the value of exc_type, which stores exception type
        #like so 'if exc_type is ZeroDivisionError return true' for example, this will skip the error

    def calc_time(self):
        total = self.end_time - self.start_time
        print(f"Total time taken was {total}")



with ContextManager("../read-files/words.txt") as myfile:
    lines=myfile.read()

    