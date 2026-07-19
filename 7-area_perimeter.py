import math

shape = input("Enter Shape (square/circle/triangle): ").lower()

if shape == "square":
    side = float(input("Enter side: "))
    print("Area =", side * side)
    print("Perimeter =", 4 * side)

elif shape == "circle":
    radius = float(input("Enter radius: "))
    print("Area =", round(math.pi * radius * radius, 2))
    print("Circumference =", round(2 * math.pi * radius, 2))

elif shape == "triangle":
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    side3 = float(input("Enter side 3: "))

    print("Area =", 0.5 * base * height)
    print("Perimeter =", side1 + side2 + side3)

else:
    print("Invalid Shape")