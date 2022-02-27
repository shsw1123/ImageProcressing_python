
H = float(input("Input your Height (m): "))
W = float(input("Input your Body Weight (Kg): "))
BMI = W/H**2
def find_bmi(BMI):
    if BMI >= 40 :
        print("Your BMI is",BMI,"Body shape is Very Fat")
    elif BMI >=35 :
        print("Your BMI is",BMI,"Body shape is Fat level 2")
    elif BMI >= 28.5 :
        print("Your BMI is",BMI,"Body shape is Fat level 1")
    elif BMI >= 23.5 :
        print("Your BMI is",BMI,"Body shape is Overweight")
    elif BMI  >= 18.5 :
        print("Your BMI is",BMI,"Body shape is Normal")
    elif BMI < 18.5 :
        print("Your BMI is",BMI,"Body shape is Underweight")
    else :
        print("Weight or Height Wrong input./n Please try again")



find_bmi(BMI)