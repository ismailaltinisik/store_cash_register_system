import turtle
class product():
    def __init__(self, name, price, quantity, barcode):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.barcode = barcode

    def __str__(self):
        return f"{self.quantity} {self.name}:{self.price}₺"

#Products
milk = product("milk", 13, "1l", "stü1015")
yogurt = product("yogurt", 15, "5kg", "stü2030")

#class to receive products supplied by the user
while True:
    request = input("Enter products.press q to exit: ")
    if request == "q":
        break
    elif request == "milk" or request == "stü1015":
        print(milk)
        Products.append(milk)
    elif request == "yogurt" or request == "stü2030":
        print(yogurt)
        Products.append(yogurt)
    else:
        print("The product you entered does not exist")

print("\n".join([f"{product.name}: {product.price}₺" for product in Products]))
print(f"\033[1mTotal:\033[0m {sum([product.price for product in Products])}₺")


turtle.mainloop()





