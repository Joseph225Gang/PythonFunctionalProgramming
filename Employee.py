import csv
from dataclasses import dataclass
from tramp import tramp

@dataclass
class Employee:
   id: int
   name: str
   manager: object

with open("d:\\temp\\baby-name.csv") as names:
     reader = csv.reader(names)
     name = lambda: next(reader)[1]
     _= name()

     emps = Employee(1, name(), None)
     for i in range(2, 10):
         emps = Employee(i, nmae(), emps)

     def nth_over(e, over = 0, curr = None):
      if e is None or over == 0:
        yield e if e else curr
      else:
        yield nth_over(e.manager, over - 1, e)

print(tramp(nth_over, emps, 5).name)