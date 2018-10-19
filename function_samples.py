
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

def sum(*args):
    total = 0
    for number in args:
        # bu da olur if type(number) is int or type(number) is float:
        if type(number) == int or type(number) == float:
            total += number
    print total


# **************************************************************
# prametre sayısı belli değil ise '**kwargs' kullanılır, parametre çiftleri(key-value) olarak değişlenler alınır

def card(**kwargs):
    print kwargs

card(name="kenan", surname="Kurt", email="aa@gmail.com")

# **************************************************************
# fonksiyon return

def calculate(r):
    return 2*3.14*r

a=calculate(3)
print a


# **************************************************************
# fonksiyon return eder gerekirse birden fazla parametre ile return eder

def calculate(r):
    area= 3.14*r**2
    l = 2*3.14*r
    return area, l

a, b = calculate(3)
print a, b


def calculate(r):
    area= 3.14*r**2
    l = 2*3.14*r
    return [area, l]

a = calculate(3)
print a

# **************************************************************

