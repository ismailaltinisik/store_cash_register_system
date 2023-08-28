#product class
class ürün():
    def __init__(self, adı, fiyatı, miktarı, barkodu):
        self.adı = adı
        self.fiyatı = fiyatı
        self.barkodu = barkodu
        self.miktarı = miktarı

    def __str__(self):
        return f"{self.miktarı} {self.adı}:{self.fiyatı}₺"
#Products
süt = ürün("süt", 13, "1l", "stü1015")
yoğurt = ürün("yoğurt", 15, "5kg", "stü2030")
#class to receive products supplied by the user
ürünler = []

while True:
    istek = input("ürün giriniz.çıkmak için q tuşuna basınız: ")
    if istek == "q":
        break
    elif istek == "süt" or istek == "stü1015":
        print(süt)
        ürünler.append(süt)
    elif istek == "yoğurt" or istek == "stü2030":
        print(yoğurt)
        ürünler.append(yoğurt)
    else:
        print("girdiğiniz ürün bulunmuyor")

print("\n".join([f"{ürün.adı}: {ürün.fiyatı}₺" for ürün in ürünler]))
print(f"\033[1mToplam:\033[0m {sum([ürün.fiyatı for ürün in ürünler])}₺")







