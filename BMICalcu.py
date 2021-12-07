import math

weight_unit = True
weight_kg = float()
weight_lb = float()
age = int()
name = str()
height_cm = float()
height_in = float()

print("Hello welcome to wayne's BMI Calculator!")
print("What is your name? ")
name = input()
print("Alrighty then! " + name + ", lets get started! ")

print("Select weight unit, kg or lb?")
print("True for kg False for lb")
weight_unit = input()

if weight_unit:
    weight_kg = float(input("Input weight: "))
    age = int(input("Input age: "))
    height_cm = float(input("Input height in cm: "))
    result = result = weight_kg/((height_cm/100)**2)
    print(f"Your BMI is: {result}")
if result <= 18.4:
    print("You are underweight.")
elif result <= 24.9:
    print("You are healthy.")
elif result <= 29.9:
    print("You are over weight.")
elif result <= 34.9:
    print("You are severely over weight.")
elif result <= 39.9:
    print("You are obese.")
else:
    print("You are severely obese.")
