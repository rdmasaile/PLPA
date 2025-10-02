class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")

    def apply_discount(self, percentage):
        discount_amount = self.price * (percentage / 100)
        self.price -= discount_amount
        print(f"New price after {percentage}% discount: ${self.price:.2f}")

# add inheritance
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, price, android_version):
        super().__init__(brand, model, price)
        self.android_version = android_version

    def display_info(self):
        super().display_info()
        print(f"Android Version: {self.android_version}")

class iPhone(Smartphone):
    def __init__(self, brand, model, price, ios_version):
        super().__init__(brand, model, price)
        self.ios_version = ios_version

    def display_info(self):
        super().display_info()
        print(f"iOS Version: {self.ios_version}")

# Example usage
android_phone = AndroidPhone("Samsung", "Galaxy S21", 799, "11")
android_phone.display_info()
android_phone.apply_discount(10)

iphone = iPhone("Apple", "iPhone 13", 999, "15")
iphone.display_info()
iphone.apply_discount(5)