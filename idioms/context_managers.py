from contextlib import contextmanager
from time import perf_counter
import os

#Created on 23/06/25 by Nathan O'Kane
#Last Modified 24/06/25 by Nathan O'Kane


#Basic context manager, which does the same job as the with function for opening files
#Returns a file object and allows you to use any file functions that you would use normally

#----------------------------------------Context Manager #1---------------------------------------#

"""
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

"""
#--------------------------------------Context Manager #2 (using contextlib)------------------------#

#This context manager simply switches the current directory to the supplied directory and then back again,
#Once some action has been performed in the with block
#Here, it writes to a file, in the new context provided

@contextmanager
def change_dir(target_path):
    changed_dir = False
    original_path = os.getcwd()
    os.chdir(target_path)
    try:
        
        yield
    finally:
        if changed_dir:
            os.chdir(original_path)

print("Directory before: ", os.getcwd())
with change_dir("../read-files/"):
    with open("text-from-context-manager.txt", "w") as f:
        f.write("Hello, this was created from the context manager")
    print("In with block it is: ", os.getcwd())

print("And after it is: ", os.getcwd())
    