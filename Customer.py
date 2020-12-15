

class Customer():
    def __init__(self,customer_name,customer_height,customer_weight):
        self.customer_name = customer_name
        self.customer_height = customer_height
        self.customer_weight=customer_weight
        self.size = None



    def get_name(self):
        return self.customer_name
    def set_name(self,new_name):
        self.customer_name = new_name
    def getH(self):
        return self.customer_height
    def setH(self,new_height):
        self.customer_height=new_height
    def getW(self):
        return self.customer_weight
    def setW(self,new_weight):
        self.customer_weight=new_weight
    def getSize(self):
        return self.size
    def setSize(self,TshirtSize):
        self.size=TshirtSize


    def ShowCustomerInformations(self):
        print("Appropriate Tshirt size for "+self.customer_name+" is "+self.size)




