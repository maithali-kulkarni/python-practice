from dataclasses import dataclass

@dataclass
class Student:
    Name: str
    Age : int
    Course: str

    def compare(self, Name2):
        if self.Name== Name2:
            # print(self.Name)
            # print(Name2)
            print(True)
        print(False)
obj = Student("Damu",23,"IT")
obj.compare("Damu")
