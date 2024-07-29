class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    def __gt__(self,new):
        if self.price>new.price:
            print(self.price,"is greater.")
        else:
            print(new.price,"is grater")
o1=order("Ice-cream",97)
print(o1.price)
new=order("Ice-cream",98)
print(new.price)
new2=o1>new
new2