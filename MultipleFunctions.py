class multiplefunctions():
    def OddEven():
        num=int(input("Enter the number:"))
        if((num%2)==0):
            print("Even number")
            message="Even Number"
        else:
            print("Odd Number")
            message="Odd Number"
        return message        
    def BMICal():
        num=int(input("Enter the BMI Intex:"))
        if(num<18.5):
            print("Under wieght")
            weight="Under wieght"
        elif(num<=24.9):
            print("Normal weight")
            weight="Normal weight"
        elif(num<29.9):
            print("Overweight")
            weight="Overweight"
        else:
            print("Very Overweight")
            weight="Very Overweight"
        return weight