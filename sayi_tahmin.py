import random
sayi = random.randint(1,100)
x = 0
hak = int(input("Kaç hak istersiniz :"))

while hak > x:
    tahmin = int(input("1 ile 100 arasında bir sayı giriniz  :"))

    if sayi == tahmin:
        print(f"tebrikler {sayi} sayısını buldunuz.")
    else:
        if sayi > tahmin:
            print("Üzgünüm bilemediniz daha büyük bir tahmin yapınız.")
        else:
            print("Üzgünüm bilemediniz daha küçük bir tahmin yapınız.")
    hak -=1
print(f"Üzgünüz {sayi} sayısını bulamadınız tekrar bekleriz.")

