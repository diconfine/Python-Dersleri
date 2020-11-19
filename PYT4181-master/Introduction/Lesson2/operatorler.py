# Aritmetik operatorler

# +, -, /, *, %

sayi1 = 120
sayi2 = 50

toplam = sayi1 + sayi2
print("işlem sonucu" + " "*50 + ": " + str(toplam))
# işlem sonucu                                                  : 170


number1 = input("Lütfen 1. sayıyı giriniz : ")
print(type(number1))   # <class 'str'>
number1 = int(number1)  # <class 'int'>

print(type(number1))


s1 = int(input("Lütfen 1. sayıyı giriniz : "))
s2 = int(input("Lütfen 2. sayıyı giriniz : "))

toplam = s1 + s2
fark = s1 - s2
carpim = s1 * s2
kuvvet = s1 ** s2
bolum = s1 / s2
mod = s1 % s2

result = "Toplama İşlemi Sonucu : " + str(toplam)+"\nÇıkartma İşlemi Sonucu : " + str(fark) + "\nÇarpma İşlemi Sonucu : " + str(
    carpim)+"\nKuvvet İşlemi Sonucu : "+str(kuvvet)+"\nBölme İşlemi Sonucu : "+str(bolum)+"\nMod İşlemi Sonucu : " + str(mod)

print(result)
