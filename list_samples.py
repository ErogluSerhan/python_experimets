### LIST ####

list_ornek = ['Tesodev', 2018, 3 ,4]

# liste icinde liste oluyor
biglist = [list_ornek, 2019]
print biglist

# listedeki 3. elemani bas
print list_ornek[3]

# listeye yeni veri ekleme, en sona eklenir. append ile tek eleman atilabilir (cok deger girilirse liste gibi algilar)
list_ornek.append([33,44])
print list_ornek

# birden fazla eleman eklenir. eklenen elemanlar listeye ayri ayri eklenir
list_ornek.extend([66,77])
print list_ornek

# eklenmek istenen eleman, kacinci yere eklenmesi isteniyorsa yazilir. 0. indexe 5'i ekle
list_ornek.insert(0,5)
print list_ornek

# listede 66 elemanini kaldirir
list_ornek.remove([33,44])
print list_ornek

# listede 66 elamani kac kere gecmis
print list_ornek.count(77)

# sirala
list_ornek.sort()
print list_ornek

# ters sirala
list_ornek.sort(reverse=True)
print list_ornek

# listenin siralamasini tersten yap, sort degil, mevcut listeyi tersten siralama
list_ornek.reverse()
print list_ornek