shape = input("Enter shape type: ")
breadth_cm = float(input("Enter breadth: "))
height_cm = float(input("Enter height: "))

def parameters(breadth_cm, height_cm):
    perimeter = 2*(breadth_cm + height_cm)
    area_of_triangle = 0.5*(0.5*breadth_cm)*height_cm
    if shape == "rectangle":
        return "The perimeter of the shape is " + str(perimeter) + "cm"
    elif shape == "triangle":
        return "The area of the triangle is " + str(area_of_triangle) + "cm^2"
    else:
        print("operation is invalid!")
p1 = parameters(breadth_cm, height_cm)
print (p1)
input()