# ctrl + k + c    => seçili alanı yorum satırına alır
# ctrl + k + u    => seçili alanı yorum satırından alır
# alt + shift + f => kodları düzenler
# alt + z         => woordwrap (ekran sonunda satırı alta alır)


# Convert  : elinizdeki değeri farklı değerlere (veri tiplerine) çevirmek için kullanılır.

# int()   : tam sayı veri tipine çevirir
# str()   : string (metinsel) veri tipine çevirir
# float() : ondalıklı sayısal değere çevirir
# chr()   : verdiğiniz sayısal değerin, metinsel değerini teslim eder.
# ord()   : verdiğiniz karakterin, ascii (sayısal) değerini teslim eder.

sayi1 = "123"  # metinsel bir değişken
sayi2 = "123"

print(sayi1 + sayi2)  # 123123

# + operatörü, metinsel değerlerde bağlaç görevini görür.

# Kullanıcıdan (dışarıdan) değer almak için, input() metodu kullanılır.

sayi1 = input("Lütfen 1. sayıyı giriniz : ")
sayi2 = input("Lütfen 2. sayıyı giriniz : ")

print(sayi1)
print(type(sayi1))

# sayı1 ve sayı2 değeri string olduğundan, bu değeri yan yana yazdıracaktır.
print(sayi1 + sayi2)


toplam = float(sayi1) + float(sayi2)
print("İşlem sonucu :", toplam)


result = int(sayi1) + int(sayi2)

print(result)


print(chr(65), ord('A'))  
print(chr(90), ord('Z')) 
print(chr(97), ord('a'))  
print(chr(122), ord('z'))  
