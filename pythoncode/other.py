class Calculator:

    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b


if __name__ == "__main__":
    cal = Calculator()
    print(cal.add(1,2))