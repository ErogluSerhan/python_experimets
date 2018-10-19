
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')


list_ = [1,2,3,"Kenan", 5,6,7]

users = {'name':"Kenan", "password":11233, "email":"aa@gmail.com"}

# for user in users:
#     print user["name"], user["password"]


# 0'dan başla 100'e kadar (10 hariç) 2şer 2şer ilerle
print range(0,100,2)

for item in range(10):
    print item

#dictteki key i alıyor
for item in users:
    print item

#items ile alınca key ve value alınabilir
for key, value in users.items():
    print key, value


#in not in
elements = ["table", "apple", "desk", "chair", "orange"]
fruits = ["apple","orange"]
shopping_cart = []

for element in elements:
    if element in fruits:
       print element


# for ve while ile else kullanımı

list_prime = []
for item in range(2,100):
        for number in range(2,item):
            if item%number==0:
                    # print "this number not prime"
                    break
        else:
            list_prime.append(item)
            # print item, "this is a prime number"
print list_prime

# verilen 2 array'de toplamı verilen sayıya eşit olan çiftleri yazdıracak bir fonksiyon tanımlayınız, x=8
arr1 = [-2, 4, -6, 5, 7]
arr2 = [6, 3, 4, 0, 1, 10]
x = 8
list_sayiciftleri = []
for arr1_ in arr1:
    for arr2_ in arr2:
        if x == arr1_+arr2_:
            list_sayiciftleri.append([arr1_,arr2_])
print list_sayiciftleri