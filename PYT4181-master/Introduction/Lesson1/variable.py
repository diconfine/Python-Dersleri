# yorum satırı. bu alanda yazdıklarınız derlenmez.

print("Hello World!")
print('Welcome to python')
print(""" Bilge Adam Python Dersleri """)
print(''' Bilge Adam Beşiktaş Yazılım Dersleri ''')


# degisken tanimlama kurallari
# 1) degisken, ismi sayi ile baslayamaz
# 2) degisken, 2 veya fazla kelimeden olusamaz, olusacak ise, ornk
#  benim_kullaniciAdim = "kahramanmaraslimustafa"
# 3) degisken tanimlamasi yapilirken, kesinlikle tanimli kelimeler kullanilamaz
# 4) degisken adinda lutfen rica ediyorum, turkce karakter kullanmayiniz.


# NOT : dosya eklerken lütfen sayı ile başlamasın, tanımlı kelime olmasın....


# python
# degiskenAdi = degiskenDegeri
# veri tipini otomatik olarak kendisi belirler, veri tipi ataması yapılmaz.
username = "admin"

# C#
# veriTipi degiskenAdi = degiskenDegeri
# string username = "admin"


# javascript
# var, let, const => var username = "admin" | username = "admin"

# global alan değişken tanımlama
firstname = "murat"
lastname = "vuranok"
phone = "+901234567890"
mail = "murat.vuranok@bilgeadam.com"

# yukarıda tanımlanan veri tipleri string(metinsel) değerlerdir.


# aşşağıdaki tanımladığımız değişken türü int(sayısal) veri tipidir.
# sayısal verip tipleri => int, float
age = 99


# elinizdeki değerin veri tipini bilmiyorsanız,
# <class 'int'>  type => içerisine verdiğiniz parametrenin(değerin) size veri tipini teslim eder.
print(type(age))

weight = 99.1
print(type(weight))  # <class 'float'>


# yazdığnız kodları düzenlemek için Ctrl(cmd) + shift + f


print(firstname)
print(lastname)
print(mail)
print(age)

# murat vuranok murat.vuranok@bilgeadam.com 99
# NOT :  , ile ayrırısanız,default olarak arala bir boşluk atacaktır.
print(firstname, lastname, mail, age)


# murat - vuranok - murat.vuranok@bilgeadam.com - 99
print(firstname, lastname, mail, age, sep=" - ")


# + operatörü ile birleştiriyorsanız, aralara boşluk eklemek için, haricen " " eklemeniz gerekir.
# print(firstname + " " + lastname + " - " + mail + age) hatalı kullanım (şimdilik...)


# + operatörü  => metinsel değerlerde bağlaç görevini görür, 2 veya birden fazla metni birleştirir.
# + operatörü  => sayısal değerlerde ise, toplama işelemi görür


fullname = firstname + " " + lastname
print(fullname)
print("personelin adı :", fullname)
print("personelin adı : " + fullname)

# mantıksal veri tipi : boolean
result = True
print(result)
result = False
print(result)


result = 10 > 5
print("İşlem sonucu :", result)

# İşlem sonucu : True


print(type(result))  # <class 'bool'>

# \n   => bir alt satıra geç, paragraf başı, yeni satır
print((fullname + "\n") * 5)


# Bilge
# Adam
# Yazılım
# Dersleri

print("Bilge\nAdam\nYazılım\nDersleri ")


print("""
Bilge
Adam
Yazılım
Dersleri
""")


print("""
------------------------ Telefon Rehberi ------------------------
#                                                               #
#                                                               #
#                                                               #
#                                                               #
#                                                               #
#                                                               #
#                                                               #
------------------------ Telefon Rehberi ------------------------
""")


help(print) 