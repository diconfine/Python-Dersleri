try:
    x = int(input("Notunuzu Giriniz: " ))
    result = "Harf Notunuz : {}"
    if x < 0 or x > 100:
        print("Geçersiz Not....")
    else:
        if x <= 30:
            result = result.format("FF")
        elif x <= 50:
            result = result.format("DD")
        elif x <= 70:
            result = result.format("CC")
        elif x <= 84:
            result = result.format("BB")
        else:
            result = result.format("AA")
        
        print(result)
except Exception as ex:
    print(ex)