try:
    # connection open
    # db c(read) r(ead) u(pdate) d(elete) işlemleri
    # connection close
    sayi = int(input("lütfen sayı gir : "))
    print("tebrik ederim, IQ 160")
except:
    #işlemler sırasında hata meydena gelirse napcaz?
   print("Vazgeçtim")
finally:
    #connection close
    print("senden bişey olmayacağı zaten belliydi =) ")

# Her iki durumdada yapılması gereken bir işleminiz varsa bunu finally içine yazmanız tekrarını engelleyecektir.
# finally işlemi her koşulda çalışacaktır....