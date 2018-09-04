'''area od triangle,square and circle'''
def Area (radius):
    PI = 3.14159
    area =float (PI*radius *radius)
    return area
def Area_triangle(h,b):
    areat=float(h*b)*0.5
    return areat
def Area_square(a):
    areas=float(a*a)
    return areas;

radius = int(input("enter the radius of the circle:"))
h=float(input("enter the height of the triangle:"))
b=float(input("enter the base of the triangle:"))
a=float(input("enter the side of the squre:"))

print("area of the circle:",Area(radius))
print("area of the triangle:",Area_triangle(h,b))
print("area of the square:",Area_square(a))             

