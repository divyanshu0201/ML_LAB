class calculator:
    def _add(self):
        print("Enter the two numbers :")
        x=int(input("Enter 1st number :"))
        y=int(input("Enter 2nd number : "))
        z=x+y
        print(str(z))
    def _subtract(self):
        print("Enter the two numbers :")
        x=int(input("Enter 1st number :"))
        y=int(input("Enter 2nd number : "))
        z=x-y
        print(str(z))
    def _multiply(self):
        print("Enter the two numbers :")
        x=int(input("Enter 1st number :"))
        y=int(input("Enter 2nd number : "))
        z=x*y
        print(str(z))
    def _division(self):
        print("Enter the two numbers :")
        x=int(input("Enter 1st number :"))
        y=int(input("Enter 2nd number : "))
        z=x//y
        print(str(z))
    def _operations(self):
        print("Enter 1 for addition")
        print("Enter 2 for subtraction")
        print("Enter 3 for multiplication")
        print("Enter 4 for division")
        i=int(input("Enter :"))
        if i==1:
            self._add()
        if i==2:
            self._subtract()
        if i==3:
            self._multiply()
        else:
            self._division()
calculator1 = calculator()
calculator1._operations()
