class Temperature:
    celcius = 30
    @classmethod
    def Conversion(cls):
        farahenheit = (cls.celcius * 9/5) + 32
        return farahenheit
    
obj = Temperature()
print(obj.Conversion())

class Temperature1:
    celcius = 30
    @staticmethod
    def Conversion():
        farahenheit = (Temperature1.celcius * 9/5) + 32
        return farahenheit
    
obj1 = Temperature1()
print(obj1.Conversion())
