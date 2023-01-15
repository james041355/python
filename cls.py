class good:
    def __init__(self,Name,Price):
        self.name = Name
        self.price = Price
class order:
    def __init__(self):
        self.date = '2022-02-02'
        self.name = '富邦'
        self.product = []
    def addProduct(self,good):
        self.product.append(good)
        
Order = order()
newGood = good('劉韶軒',-1)
Order.addProduct(newGood)
print(123)
        
