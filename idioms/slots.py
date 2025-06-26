#This file was created by Nathan O'Kane on 24/06/24
#Last edited by Nathan O'Kane on 24/06/24

#Below is an example of a python's slots, which allows restriction of a classes attributes
#to just those listed in the slots list


class LogEntry:
    __slots__ = ("timestamp", "level", "message")

    def __init__(self):
        self.timestamp = None
        self.level = None
        self.message = None


newLog = LogEntry()
newLog.timestamp = "09:21"
newLog.level = "INFO"
newLog.message = "Here is a log message"

print(newLog.timestamp)
#This below line will error as the LogEntry class doesn't have a commit message attribute
#newLog.commitMessage = "commit message"