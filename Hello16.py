from enum import Enum,unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Web = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Mon)

print(Weekday.Tue.value)

for name,member in Weekday.__members__.items():
    print(name,'=>',member)