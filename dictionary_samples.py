
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

users = {1: {'name': 'Jane', 'age': 10},
         2: {'name': 'John', 'age': 22},
         3: {'name': 'Jim', 'age': 25}
         }

print users[1]
print users[2]['name']
print users[3]['age']


# OrderedDict
# verileri girilen siraya gore tutmak için kullanilir

#ornek vardiii


# dictionary clear ile ici bosaltilir
users.clear()
print users

users = {1: {'name': 'Jane', 'age': 10},
         2: {'name': 'John', 'age': 22},
         3: {'name': 'Jim', 'age': 25}
         }

# listeyi kopyalama, ayni yere erferasns vermek yerine yeni bellek alani acip referans ediyor
another_users = users.copy()
print another_users

a = 1
b = 1
c = a

# id bellekteki adresin yerini verir. primitive tipler icin(string, int, float) degiskenlerin degerleri ayni ise ayni alani refere ederler
print id(a)
print id(b)
print id(c)

# değiskenin degeri 1 yerine 2 olunca bellekteki yeri de degisiyor
c = c + 1
print id(c)

# list ve dictionarynin icindeki deger değisse bile referans degismiyor.
a_list = [1, 2]
print id(a_list)
a_list.append(3)
print id(a_list)

# Dictionary Veri Alma .get
dict_ = {"name": "John", "surname": "Doe"}

print dict_.get("age")

# dicionary da aradığınız key va rmı kontrolü için kullanılır
dict_ = {"name": "John", "surname": "Doe"}

print dict_.has_key('surname')
print dict_.has_key('email')

# items
dict_ = {"name": "John", "surname": "Doe"}

print dict_.items()
print dict_.items()[0]
print dict_.items()[0][1]

# dictionary de append yoktur, update var.

#dict_.update{("age":"40")}
print dict_

#dic içindeki key del ile silinir
del dict_["name"]
print dict_