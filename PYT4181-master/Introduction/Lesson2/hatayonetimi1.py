# Programcı hataları (Error)

sayi = 1
# Program kusurları
# İstisnai hatalar
# Mantıksal hatalar

# phone_number = int(
#     input("lütfen telefon numaranızı başında 0 olmadan giriniz"))
# print("Tebrikler!")



try:
    phone_number = int(
    input("lütfen telefon numaranızı başında 0 olmadan giriniz : "))
    print("Tebrikler!")
except:
    print("sadece sayısal veri girmek ne kadar zor olabilir?")