# -*- coding:utf-8 -*-
from __future__ import division
import random
import string
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# **************************************************************
# string.split() count prametresi verildiği zaman o sayı kadar böl demek

text = 'lorem ipsum dolo, ssdflkwr, sadasdd.'

strng_array = text.split(',')
strng_array_2 = text.split(',', 1)
strng_array_3 = text.split('ip')

print strng_array
print strng_array_2
print strng_array_3


# **************************************************************
# string.strip(),  text içindeki / ve 0 karakterlerini temizliyor

text = '//0lorem ipsum dolo, ssdflkwr, sadasdd.00/'
clean_text = text.strip('/0')

print text
print clean_text


# **************************************************************
# strip trim gibi boşlukları alıyor

def excel_space_trimmer(strn):
    words = strn.split(" ")
    clean_words = []
    for word in words:
        if word != "":
            clean_words.append(word.strip(" "))
    print words
    print clean_words
    print " ".join(clean_words)

def excel_space_trimmer_short_version(strn):
    print " ".join([word for word in strn.split(" ") if word != ""])

excel_space_trimmer("hello  world")
excel_space_trimmer_short_version("hello  world")

# **************************************************************
# other string manipulations

text = 'lorASDAS iASDasdasdo, ssdflkwr, sadasdd.'
text_lower = text.lower()

print text_lower
print text.islower()
print text_lower.islower()
print text.capitalize()
print text.startswith("l") #string istenen karakterle/karakterlerle başlıyor mu kontrlü
print text.count('i')
print text.replace('lor','LOR') #lor gördüğü yere LOR çakıyor
print text.lower().replace('a','Q')
print '{}. Gün, {} işleri yapılır'.format(1,'Temizlik'.lower())
print '-'.join(['green' ,'orange', 'blue'])


# **************************************************************

def pwd_generator(char_number, difficulty_level):

    if difficulty_level == "1":
        pwd_ = string.ascii_letters
    elif difficulty_level == "2":
        pwd_ = string.ascii_letters + string.digits
    elif difficulty_level == "3":
        pwd_ = string.ascii_letters + string.digits + string.punctuation
    else:
        pwd_ = string.ascii_letters

    password = ''.join(random.choice(pwd_) for i in range(int(char_number)))
    return password

print "Şifre Kaç Karakter Olsun?"
v_char_number = raw_input();

print "Hangi Zorluk Seviyesnde Olsun? 1,2,3 "
v_difficulty_level = raw_input();

v_password = pwd_generator(v_char_number, v_difficulty_level)
print v_password


#hocanın çözümü buraya yapıştırılacak!!!!!!!!!!!!!!!!!!!!!!!!!!!!


#1:harfler, 2:sayı+harf, 3: sayı+harf+noktalama







