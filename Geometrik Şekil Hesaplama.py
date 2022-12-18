print("""***********************************

1.Dörtgen


2. Üçgen

**********************************
""")
cevap = input("Hangi Şeklin Tipini İstiyorsun:")

if cevap == "1" :
    print("Kenarların Değerlerini girin:")
    a = int(input("Kenar 1 :"))
    b = int(input("Kenar 2 :"))
    c = int(input("Kenar 3 :"))
    d = int(input("Kenar 4 :"))

    if a==b and a==c and a==d :
        print("Kare")

    elif a == c and b == d :
        print("Dikdörtgen")

    else:
       print("Dörtgen")

if cevap == "2" :
    print("Kenarların Değerlerini girin:")
    x = int(input("Kenar 1 :"))
    y = int(input("Kenar 2 :"))
    z = int(input("Kenar 3 :"))

    if x==y and x==z :
        print("Eşkenar Üçgen")

    elif x==y or x==z :
        print("İkizkenar Üçgen")

    elif abs(y-z)<x<abs(y+z):
        print("Normal Üçgen")

    else:
        print("Üçgen Olma Şartını Sağlamıyor !")









