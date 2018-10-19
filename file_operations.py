# -*- coding:utf-8 -*-
from __future__ import division
import sys
reload(sys)
sys.setdefaultencoding('utf8')

f = open("file_ops_.txt", "r")
a = f.read()
f.close()

print a

#****************************************************

f = open("bag_of_words", "r")
f_out = f.read().lower()
f.close()

stratejik = ["organization", "direction", "decision", "choice", "vision", "risk"]
taksiktel = ["control", "objective", "finance", "marketing"]
operasyonel = ["execution", "operation", "production", "solution"]

# python way
dict_ = {"stratejik": sum([f_out.count(word) for word in stratejik]), "taktiksel": sum([f_out.count(word) for word in taksiktel]), "operasyonel" : sum([f_out.count(word) for word in operasyonel])}
print max(dict_, key=lambda x: dict_[x])

# uzundan kısa yol
# i = sum([f_out.count(word) for word in stratejik])
# y = sum([f_out.count(word) for word in taksiktel])
# z = sum([f_out.count(word) for word in operasyonel])

# uzun yol
# i = 0
# y= 0
# z = 0
# for word in stratejik:
#     i = f_out.count(word) + i
#
# for word in taksiktel:
#     y = f_out.count(word) + y
#
# for word in operasyonel:
#     z = f_out.count(word) + z
# print i, y, z
# print max(i, y, z)

#****************************************************
