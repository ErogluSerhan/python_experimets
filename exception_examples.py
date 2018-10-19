# -*- coding:utf-8 -*-
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

a = raw_input("Enter a number: ")

# *********************************************************

try:
    a = int(a)
    print a/5
except:
    print "Not possible"

print a


# *********************************************************

try:
    a = int(a)
    print a/5
except ValueError:
    print "Value Error"
except ZeroDivisionError:
    print "Zero Division Error"

print a


# *********************************************************

try:
    a = int(a)
    print a/5
except ValueError as e:
    f = open("system.log", "ab")
    f.write(str(e) + str(time.time()) +"\n")
except ZeroDivisionError as e:
    f = open("system.log", "ab")
    f.write(str(e) + "\n")
except Exception as e:
    f = open("system.log", "ab")
    f.write(str(e) + "\n")

f.close()

print a


# *********************************************************

def logger(e):
    with open("system.log","ab") as f:
        a = time.localtime()
        datetime_ = time.strftime("%Y/%m/%d %H:%M:%S", a)
        f.write(datetime_ + " || " + str(e) + "\n")

try:
    a = int(a)
    print a / 5
except ValueError as e:
    logger(e)
    raise Exception("x library does not expect such a value")
except ZeroDivisionError as e:
    logger(e)
except Exception as e:
    logger(e)


# *********************************************************


