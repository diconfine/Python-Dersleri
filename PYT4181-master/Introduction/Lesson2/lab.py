# örnek 1) dışarıdan alınan 2 sayının toplamıyla farkının bölümünden kalanı kaçtır

sayi1 = float(input("Lütfen 1. sayıyı giriniz : "))
sayi2 = float(input("Lütfen 2. sayıyı giriniz : "))
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
mod = toplam % fark

print(mod)


# örnek 2) dışarıdan girilen bir sayının 10 eksiğinin 20 fazlasının ikiye bölümünden kalan kaçtır


sayi = int(input("Lütfen sayı girini : "))
# 1)
sayi = sayi - 10
sayi = sayi + 20
sayi = sayi % 2
print("İşlem sonucu :", sayi)


sayi = ((sayi - 10) + 20) % 2
print(sayi)


# örnek 3) dışarıdan girilen iki sayının karelerinin toplamı ile karelerinin farkı toplamı kaçtır.


s1 = int(input("lütfen 1. sayıyı giriniz : "))
s2 = int(input("lütfen 2. sayıyı giriniz : "))

kare1 = s1**2
kare2 = s2**2

toplam = kare1 + kare2
fark = kare1 - kare2
print("İşlem sonucu :", (toplam + fark))


# örnek 4) Vize notu %30, final notu %70'ini alıp not ortalamasını hesaplayıp kullanıcıya aldığı not'u gösteriniz


not_vize = float(input("Lütfen vize notuzunu giriniz : "))
not_final = float(input("Lütfen final notuzunu giriniz : "))


_not = (not_vize * 0.30) + (not_final * 0.70)
print("Not ortalamanız :", _not)


# örnek 5) Kullanıcı ilk olarak adını, 2 olarak ise soyismini girsin, işlem sonunda kullanıcıya   isim.soyisim@hotmail.com şeklimnde mail adersini teslim ediniz.


firstname = input("lütfen adınızı giriniz : ")
lastname = input("lütfen soyadınızı giriniz : ")

mail = firstname + "." + lastname + "@hotmail.com"
print(mail)
# {} => placeholder (yer tutucu)
mail = "{}.{}@hotmail.com".format(firstname, lastname)
# isim.soyisim@hotmail.com
print(mail)
mail = f"{firstname}.{lastname}@hotmail.com"
print(mail)
