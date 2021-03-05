from bmi import bmi_cal
from retirement import ret
import retirement

if __name__ == '__main__':
    while True:
        try:
            print("Press 1 to calculate BMI")
            print("Press 2 to calculate Retirement benefit")
            print("Press 0 to exit")
            choice = int(input("My choice is: "))

            if choice == 0:
                break
            elif choice == 1:
                bm = bmi_cal()
                feet = int(input("Height in feet:"))
                feet = float(feet)
                inches = float(input("Height in inches:"))
                weight = float(input("Your weight in pounds:"))
                result = bm.calculate_bmi(feet,inches,weight)
                print(result)
            elif choice == 2:
                age=int(input("What is your current age:"))
                salary = int(input("What is your annual salary:"))
                percent = float(input("What percentage of salary are you going to save:"))
                target = int(input("What is your target savings:"))
                rt = ret()
                res=rt.retirement_cal(age,salary,percent,target)
                print(res)
        except ValueError:
            print("Invalid input. Please try again.")
        