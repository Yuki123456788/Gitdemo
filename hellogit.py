weight = float(input("weight: "))
height = float(input("height: "))/100

while (weight != 0 and height != 0):
    print(f"BMI: {weight/height**2}")
    weight = float(input("weight: "))
    height = float(input("height: "))/100
print("end bmi")
