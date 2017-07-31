import turtle
import math

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("orange")
    #draw_square()
    draw_triangles()
    #draw_initial()
    window.exitonclick()


def draw_triangles():
    triangle_handle = turtle.Turtle()    
    points = [[-200,-100],[0,200],[200,-100]]
    sierpinski_trialngle(points, 2, triangle_handle)
    
def getmidpoint(p1, p2):
    return ((p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski_trialngle(points, degree, triangle_handle):
    draw_triangle(points, triangle_handle)
    if (degree > 0):
        sierpinski_trialngle([points[0],
                                        getmidpoint(points[0], points[1]),
                                        getmidpoint(points[0], points[2])],
                              degree - 1, triangle_handle)

        sierpinski_trialngle([points[1],
                                        getmidpoint(points[1], points[0]),
                                        getmidpoint(points[1], points[2])],
                              degree - 1, triangle_handle)
                             
        sierpinski_trialngle([points[2],
                                        getmidpoint(points[2], points[0]),
                                        getmidpoint(points[2], points[1])],
                              degree - 1, triangle_handle)

def draw_triangle(points, triangle_handle):    
    triangle_handle.penup()
    triangle_handle.goto(points[0][0], points[0][1])
    triangle_handle.pendown()
    triangle_handle.goto(points[1][0], points[1][1])
    triangle_handle.goto(points[2][0], points[2][1])
    triangle_handle.goto(points[0][0], points[0][1])
    
def draw_square():
    square_handle = turtle.Turtle()
    square_handle.shape("turtle")
    square_handle.speed(10)
    sides = 0
    degrees = 0

    while (degrees <= 360):
        square_handle.setheading(degrees)
        while (sides < 4):
            square_handle.forward(100)
            square_handle.right(90)
            sides += 1
        degrees += 10
        sides = 0

def draw_circle():
    circle_handle = turtle.Turtle()
    circle_handle.shape("turtle")
    circle_handle.circle(50, None, None)
        

def draw_initial():
    handle = turtle.Turtle()    
    handle.speed(10)

    handle.right(180)
    handle.forward(100)
    handle.left(90)
    handle.forward(50)
    handle.left(90)
    handle.forward(100)
    handle.right(90)
    handle.forward(50)
    handle.right(90)
    handle.forward(100)

    handle.penup()
    handle.right(180)
    handle.forward(150)
    handle.pendown()
    handle.left(90)
    handle.forward(100)
    length = math.sqrt((100** 2 + 50 ** 2))
    print(length)
    handle.right(150)
    handle.forward(length)
    handle.left(120)
    handle.forward(length)
    handle.right(150)
    handle.forward(100)
    
    
        
draw_shapes()
