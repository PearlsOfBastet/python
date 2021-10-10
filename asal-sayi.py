print("***** Programdan exit ile çıkabilirsiniz. *****")
sayi = int(input("Bir sayı giriniz :"))
x = 1
count = 0
# while (sayi != "exit") :
for i in range(x,sayi+1):
    if sayi % i == 0:
        print(f"Girilen sayı {i} sayısına tam bölünüyor.")
        count +=1
    else:
        continue
x +=1
if count == 2:
    print(f"{sayi} sayısı asal bir sayıdır.")
else:
    print(f"{sayi} sayısı asal bir sayı değildir.")


