class allfunctions():
        def Subfields():
            print("Sub-fields in AI are:")
            list = [
                "Machine Learning",
                "Neural Networks",
                "Vision",
                "Robotics",
                "Speech Processing",
                "Natural Language Processing"]
            for field in list:
                print(field)    
            
        def OddEven():
            num=int(input("Enter a number:"))
            if((num%2)==0):
                num1=num
                print(num1,"is Even Number")

        def Elegibile():
            gender=input("Your Gender:")
            age=int(input("Your age:"))
            if gender=="male":
               if(age>=21):
                   print("Eligible")
               else:
                   print("Not Eligible")              
            if gender=="female":
               if(age>=18):
                   print("Eligible")
               else:
                   print("Not Eligible")
                   
        def Percentage():
            mark1=int(input("Subject1="))
            mark2=int(input("Subject2="))
            mark3=int(input("Subject3="))
            mark4=int(input("Subject4="))
            mark5=int(input("Subject5="))
            total=mark1+mark2+mark3+mark4+mark5
            print("total=",total)
            totalsubnum=[mark1,mark2,mark3,mark4,mark5]
            percent=total/len(totalsubnum)
            print("Percentage:",percent)

        def triangle():
            num1=int(input("Height:"))
            num2=int(input("Breadth"))
            print("Area formula:(Height*Breadth)/2")
            Area=num1*num2/2
            print("Area of triangle:",Area)
            num3=int(input("Height1:"))
            num4=int(input("Height2:"))
            num5=int(input("Breadth:"))
            print("Perimeter formula: Height1+Height2+Breadth")
            Perimeter=num3+num4+num5
            print("Perimeter of triangle:",Perimeter)

    
        