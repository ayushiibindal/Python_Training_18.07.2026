import math

shape = input("Enter Shape (cube/cylinder/cone/cuboid): ").lower()

if shape == "cube":

    side = float(input("Enter side of cube: "))

    surface_area = 6 * side * side
    volume = side ** 3

    print(f"\n----- Cube -----")
    print(f"Surface Area = {surface_area}")
    print(f"Volume = {volume}")

elif shape == "cylinder":

    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))

    surface_area = 2 * math.pi * radius * (radius + height)
    volume = math.pi * radius * radius * height

    print(f"\n----- Cylinder -----")
    print(f"Surface Area = {round(surface_area, 2)}")
    print(f"Volume = {round(volume, 2)}")

elif shape == "cone":

    radius = float(input("Enter radius: "))
    height = float(input("Enter height: "))

    slant_height = math.sqrt(radius ** 2 + height ** 2)

    surface_area = math.pi * radius * (radius + slant_height)
    volume = (1 / 3) * math.pi * radius * radius * height

    print(f"\n----- Cone -----")
    print(f"Surface Area = {round(surface_area, 2)}")
    print(f"Volume = {round(volume, 2)}")

elif shape == "cuboid":

    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    height = float(input("Enter height: "))

    surface_area = 2 * (length * breadth + breadth * height + height * length)
    volume = length * breadth * height

    print(f"\n----- Cuboid -----")
    print(f"Surface Area = {surface_area}")
    print(f"Volume = {volume}")

else:
    print(f"\nInvalid Shape! Please enter cube, cylinder, cone or cuboid.")