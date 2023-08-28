print("Welcome to the Body Mass Index Calculator, or for short BMI! ")

height = input("Enter your height in m:\n")
weight = input("Enter your weight in kg:\n")


height_2 = float(height)
weight_2 = float(weight)


bmi = int(weight_2 / height_2**2)

print(f"Your BMI is: 1.75{bmi}")
