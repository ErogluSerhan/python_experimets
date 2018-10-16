
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def deneme_adi():
    print "Hello, World!"

deneme_adi()

# **************************************************************
#ornek bir fonksiyon

def summer(arr1, arr2, x):
    list_sayiciftleri = []
    for arr1_ in arr1:
        for arr2_ in arr2:
            if x == arr1_ + arr2_:
                list_sayiciftleri.append([arr1_, arr2_])
    print list_sayiciftleri

a1 = [-2, 4, -6, 5, 7]
a2 = [6, 3, 4, 0, 1, 10]
x = 8
summer(a1, a2, x)

# **************************************************************
# parametrede default değer kullanırsak, fonksiyn çağırırken o parametre verilmeyebilir

def summer(arr1, arr2, x = 8):
    list_sayiciftleri = []
    for arr1_ in arr1:
        for arr2_ in arr2:
            if x == arr1_ + arr2_:
                list_sayiciftleri.append([arr1_, arr2_])
    print list_sayiciftleri

a1 = [-2, 4, -6, 5, 7]
a2 = [6, 3, 4, 0, 1, 10]
summer(a1, a2)

# **************************************************************
# prametre sayısı belli değil ise '*args' kullanılır

a= [1,2,3]
b=8
print sum(a,b)

def sum(*args):
    total=0
    for number in args:
        total+=number
    print total

sum(1,2,3,4,5,6)

# **************************************************************