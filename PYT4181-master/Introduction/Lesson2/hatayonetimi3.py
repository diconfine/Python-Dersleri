try:
    sayi = int(input("Lütfen sayısal değer giriniz : "))
    print("Afferin sana, iyi iş başardın!!!")
    # sayi = sayi / 0
    print("İşlem sonu!!!")


except ZeroDivisionError as ex:
    print("LOG Mesajı :", ex)


except ValueError as hata:
    print("Lütfen Tekrar Deneyiniz!!!")
    print("LOG Mesajı :", hata)


except Exception as hata:  # en genel hata yakalayıcı, en sonda olmalıdır.
    print("İşlem Hatası")  # Kullanıcının göreceği hata
    print("LOG Mesajı :", hata)  # loglama yapacağımız hata mesajı
