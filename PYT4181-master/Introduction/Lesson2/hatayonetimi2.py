try:
    sayi1 = int(input("Lütfen 1. sayıyı giriniz : "))
    sayi2 = int(input("Lütfen 2. sayıyı giriniz : "))

    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    bolum = sayi1 / sayi2
    mod = sayi1 % sayi2

    print(
        f"Sayıların Toplamı : {toplam}\nSayıların Farkı : {fark}\nSayıların Bölümü : {bolum}\nSayıların Çarpımı : {carpim}\nSayıların Modu : {mod}")

except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except OverflowError:
    print("OverflowError")
except MemoryError:
    print("MemoryError")
except:
    print("genel hata yakalama alanı")


 