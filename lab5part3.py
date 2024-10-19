# JOHNATHAN SULLIVAN BMI CALCULATOR (LAB 5)
#This program allows you to calculate the BMI of an individual and displays whether the person has optimal weight

#Named Constants are listed below
#Enter the users height in inches below
Height=float(input('Enter your height using inches:'))
#Enter the users weight in lbs below
Weight=float(input('Enter your weight using lbs:'))
#BMI FORMULA BELOW
BMI= Weight * 703/Height**2
if BMI<18.5:
    print('Underweight')
elif BMI>25:
    print('Overweight')
elif BMI>= 18 and BMI<=25:
    print('Optimal Weight')



