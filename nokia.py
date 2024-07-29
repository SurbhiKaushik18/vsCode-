class Nokia:
    company="Nokia In"
    website="www.nokiaindia.com"
    def contact_details(self,address):
        print("Address: Muzaffarpur ,bihar")
        
  
class Nokia1100(Nokia):

    def __init__(self):
        self.name="Nokia 1100"
        self.year=1998
    def product_details(self):
        print("NAME:",self.name)
        print("Year",self.year)
        print("Company",self.company)
        print("website",self.website)
        super().contact_details()


mobile=Nokia1100()
mobile.product_details()
mobile.contact_details()
