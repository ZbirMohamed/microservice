# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

### Heritage , Polymorphisme , Abstract , Encapsulation

class Human:
    def __init__(self,name,age): # Constructeur
        self.name = name
        self.age = age

    def walk(self): #Methodes
        print("I am walking")

    def eat(self):
        print("I am eating")


human1 = Human("Saad",21)
human1.eat()
human1.walk()
print(human1.name)





def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
