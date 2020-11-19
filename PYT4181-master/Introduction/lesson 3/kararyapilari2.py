# try:
#     x = int(input("Notunuzu Giriniz : "))
#     if x < 0:
#         print("0'dan küçük not giremezsiniz!!!")
#     elif x > 100:
#         print("100'den Büyük not giremezsiniz!!!")
#     else:
#         print("Notunuz :", x)
# except ValueError as err:
#     print(err)


# try:
#     sayi = int(input("Sayı Giriniz : "))

#     mod = sayi % 2

#     if mod == 0:
#         print("Sayı Çifttir Sayıdır...")
#     else:
#         print("Sayı Tektir...")

# except ValueError as err:
#     print(err)

# try:
#     sifre = input("Şifre Giriniz : ")

#     x = len(sifre)

#     if x >= 8:
#         print("Şifre Onaylandı....")
#     else:
#         print("Daha Uzun Bir Şifre Giriniz..!!!")
# except Exception as ex:
#     print(ex)


# try:
#     username = input("Lüfen Kullanıcı Adınızı Giriniz : ")
#     if username =="admin":
#         password = input("Lütfen şifrenizi giriniz : ")
#         if password == "123":
#             print("Tebrikler Giriş Yaptınız...")
#         else:
#             print("Kullanıcı Adınız Doğru Fakat Şifreniz Yanlış...")
#     else:
#         print("Kullanıcı Adı Hatalı Şifrenizi Kontrol Etmedim...")
# except Exception as ex:
#     print(ex)


# Mantıksal Operatörler

# and sorguya katılan her bir koşulun sağlanması durumu
# or sorguya katılan herhangi bir koşulun sağlanması durumu
# not sorguya olumsuzluk katar, değil ise....


# try:

#     username = "admin"
#     password = "123"

#     x = input("Kullanıcı Adınızı Giriniz : ")
#     y = input("Şifrenizi Giriniz : ")

#     if username == x and password == y:
#         print("Giriş Başarılı...")
#     elif username == x and password != y:
#         print("Hatalı Şifre Girdiniz !!!")
#     elif username != x:
#         print("Kullanıcı Adı Hatalı Şifreyi Kontrol Etmedim..!!!")

# except Exception as ex:
#     print(ex)


try:
    not_ = int(input("Notunuzu Giriniz : "))

    if not_ >= 0 and not_ <= 30:
        print("Notunuz : FF")

    elif not_ > 30 and not_ =< 50:
        print("Notunuz : DD")

    elif not_ > 50 and not_ <= 70:
        print("Notunuz : CC")

    elif not_ > 70 and not_ <= 84:
        print("Notunuz : BB")

    elif not_ > 84 and not_ <= 100:
        print("Notunuz : AA")

    elif not_ < 0 or not_ > 100:
        print("Lütfen 0 İle 100 Arasında Bir Not Giriniz...!!!!")

except Exception as ex:
    print(ex)
