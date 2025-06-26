from dataclasses import dataclass

#This file was created by Nathan O'Kane on 26/06/25
#Last edited by Nathan O'Kane on 26/06/25

#Below is an example of the dataclass, which is a more efficient way of structuring classes
#This is more intuative than the standard way and matches object oriented languages more closely

@dataclass(frozen=True)
class LogEntry:
    timestamp : str
    message : str
    level : str = "info"


log1 = LogEntry(timestamp="09:31",message="WARNING: variable not initialized")
print(repr(log1))

log2 = LogEntry(timestamp="14:12", message="INFO: DATA step ran at this line")
print(log1==log2)

#The frozen keyword means that the following would result in an error, as it means the values are immutable.
#log1.message = "Error"


