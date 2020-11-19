try:
    sayi1 = int(input("Sayı Giriniz : "))
    sayi2 = int(input("Sayı Giriniz : "))
    sonuc = sayi1 / sayi2

except ValueError as error:
    print(ValueError)

else:
    try:
        print(sayi1/sayi2)
        print("işlem sonu")
    except ZeroDivisionError as err:
        print(err)

# alt + shift + aşşağı ok => duplicate line (Yani Satırı alt Satırla yer değiştirir.)
