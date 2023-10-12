import datetime
import time
import os

one = """
  |
  |"""

two = """
 _
 _|
|_ """

three = """
 _
 _|
 _|
"""

four = """
|_|
  |
"""

five = """
 _
|_
 _|
"""

six = """
 _
|_
|_|
"""

seven = """
 _
 _|
  |
"""

eight = """
 _
|_|
|_|
"""

nine = """
 _
|_|
 _|
"""

zero = """
 _
| |
|_|"""
# y = str(x)
# print(type(x))
# z = str(datetime.datetime.now())
# print("__\t__")
# print(y[0:4])

# pr 

# print(one, end="")
# print(two, end="")
# print(three, end="")
# print(four, end="")

dict = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}

while True:
    x = datetime.datetime.now()
    y = x.strftime("%H:%M:%S %p")
    curr_time = str(y)
    print(curr_time)
    time.sleep(1)
    if curr_time[0] == "1":
        print(one,end="")

    for a in dict:
        if a[1.value] == curr_time[0]:
            print(a)

        if a == curr_time[1]:
            print(a)

        if a == curr_time[3]:
            print(a)

        if a == curr_time[4]:
            print(a)
   
    # os.system('CLS')
    


