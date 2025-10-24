class kaushik:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"The age of {self.name} Kaushik is {self.age}")

m1 = kaushik("Namish",20)
m2 = kaushik("Yajat",16)

m1.display()
m2.display()