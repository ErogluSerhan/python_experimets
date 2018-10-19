# -*- coding:utf-8 -*-
from __future__ import division
import csv
import pprint
import sys
reload(sys)
sys.setdefaultencoding('utf8')


with open("train.csv") as f:
    data = csv.reader(f)
    export_data = []
    for line in data:
        export_data.append(line)
print len(export_data)
print export_data[0]
print export_data[1]


# ****************************************************
with open("train.csv") as f:
    data = csv.DictReader(f, delimiter=";")
    export_data = []
    for line in data:
        export_data.append(line)
print len(export_data)
print export_data[0]
print export_data[1]

for item in export_data:
    print item["marital"], item["housing"]

# ****************************************************

with open("Titanic.csv") as f:
    data = csv.DictReader(f, quoting=csv.QUOTE_NONNUMERIC) #sayı olmayanları tırnağa al sayı olanları bırak
    export_data = []
    for line in data:
        export_data.append(line)

for item in export_data:
    print item["Age"]

filtered_data = filter(lambda x: x["Age"] > 0, export_data)
filtered_data_male = filter(lambda x: x["Age"] > 0 and x["Sex"] == "male", export_data)

agelist = []
for item in filtered_data:
    agelist.append(item["Age"])

agelist_sex = []
for item in filtered_data_male:
    agelist_sex.append(item["Age"])


print agelist

print sum(agelist)/len(agelist) #yaş ortalaması
print sum(agelist_sex)/len(agelist_sex) #erkek yaş ortalaması

print pprint.pprint(filtered_data)  #pretty print

print filtered_data

f = open("data.csv", "wb")
writer = csv.DictWriter(f, filtered_data[1].keys(), quoting=csv.QUOTE_NONNUMERIC)
writer.writeheader()
writer.writerows(filtered_data)
f.close()

# ****************************************************
#sort etme
with open("Titanic.csv") as f:
    data = csv.DictReader(f, quoting=csv.QUOTE_NONNUMERIC) #sayı olmayanları tırnağa al sayı olanları bırak
    export_data = []
    for line in data:
        export_data.append(line)

filtered_data = filter(lambda x: x["Survived"] > 0 and x["Sex"] == "Female", export_data)
sorted_data = sorted(filtered_data, key=lambda x:x["Age"])

print sorted_data

def converter(x):
    x[""]= int(x[""])
    return x

pprint.pprint(map(converter, filtered_data))