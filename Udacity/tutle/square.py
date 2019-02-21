import turtle

# def draw_sqr(name):
window = turtle.Screen()
window.bgcolor('red')
# window.exitonclick()

def draw_sqr(name):	
	for i in range(4):
		name.forward(100)
		name.right(90)

def draw_tri(name):	
	name.speed(0.01)
	# for i in range(3):
	name.right(120)
	name.forward(100)
	name.right(240)
	name.forward(100)
	name.right(240)
	name.forward(100)


	

brad = turtle.Turtle()
draw_tri(brad)
for k in range(36):
	draw_tri(brad)
	brad.right(10)
window.exitonclick()



