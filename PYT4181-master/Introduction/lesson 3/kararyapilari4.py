try:
    x = input("ürün adını girin : ").lower()
    reseult = "Gideceğiniz Reyon {}"
    if(x):
        if x == "domates" or x == "patlıcan" or x == "biber":
            reseult = reseult.format("Sebze Reyonu")
        elif x == "şampuan" or x == "parfüm" or x == "deodorant":
            reseult = reseult.format("kozmetik Reyonu")
        elif x == "cep telefonu" or x == "televizyon" or x == "bilgisayar" or x == "kulaklık":
            reseult = reseult.format("Teknoloji Reyonu")
        else:
            reseult = ("Bu ürün Bizde Bulunmamaktadır....")
        print(reseult)
    else:
        print("Ürün Adı Giriniz....")
except Exception as ex:
    print(ex)