
import turtle 

screen = turtle.Screen() 
screen.setup(800,600)

circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fastest')
circle.up()

square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed('fastest')
square.up()

circle.goto(0,280)
circle.stamp()

k = 0 
for i in range(1,17):
	y = 30*1
	for j in range(i-k): 
		x =30*j 
		square.goto(x,-y+280)
		square.stamp()
		square.goto(-x,-y+280)
		square.stamp()

	if i % 4 == 0: 
		x = 30*(j+1)
		circle.color('red')
		circle.goto(-x,-y+280)
		circle.stamp()
		circle.goto(x,-y+280)
		circle.stamp()
		k += 2 

	if i%4 == 2: 
		x =  30*(j+1)
		square.color('yellow')
		square.goto(-x,-y+280)
		square.stamp()
		square.goto(-x,-y+280)
		square.stamp()

turtle.exitonclick()
