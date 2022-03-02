"""
V=4
3πr3


What is the length of a side of the square? 5
The area of the square is: 25.0
What is the length of rectangle? 6
What is the width of the rectangle? 7
The area of the rectangle is: 42.0
What is the radius of the circle? 5
The area of the circle is: 78.5"""
import math
length_square = float(input('What is the length of a side of the square: '))
length_rectangle = float(input('What is the length of the rectangle: '))
width = float(input('What is the width of the rectangle: '))
radius = float(input('What is the radius of the circle: '))

pi = math.pi
area_square = length_square * length_square
area_rectangle = length_rectangle * width
area_circle = pi * radius
volume_cube = length_square
volume_sphere = 4.0/3.0*pi* radius**3


print(f'The area of the square is: {area_square}')
print(f'The area of the rectangle is: {area_rectangle}')
print(f'The area of the circle is: {area_circle}')