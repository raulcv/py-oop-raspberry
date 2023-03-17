from packages.shapes import Paper, Rectangle, Oval, Triangle
""""
paper = Paper()

rect1 = Rectangle()

rect1.set_color("Blue")
rect1.set_height(100)
rect1.set_width(200)

rect1.draw()

rect2 = Rectangle()
rect2.set_x(100)
rect2.set_y(100)
rect2.set_color("green")
rect2.set_height(150)
rect2.set_width(50)

rect2.draw()

paper.display()
"""
paper = Paper()
oval = Oval()
oval.set_color("black")
oval.set_x(150)
oval.set_y(10)
oval.set_width(50)
oval.set_height(50)
oval.draw()

tri = Triangle(100, 200, 175, 60, 250, 200)
tri.set_color("orange")
tri.draw()

rect1 = Rectangle()
rect1.set_x(120)
rect1.set_y(200)
rect1.set_color("green")
rect1.set_height(150)
rect1.set_width(30)
rect1.draw()

rect2 = Rectangle()
rect2.set_x(200)
rect2.set_y(200)
rect2.set_color("green")
rect2.set_height(150)
rect2.set_width(30)
rect2.draw()

paper.display()