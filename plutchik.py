import turtle

# Source: https://www.geeksforgeeks.org/draw-a-flower-using-turtle-in-python/

turtle.setpos(0,0)

# Top Petal
turtle.left (135)
turtle.fillcolor ("gray")
turtle.begin_fill()
turtle.circle (-200,90)
turtle.right (90)
turtle.circle (-200,90)
turtle.end_fill()

# Bottom Petal
turtle.left (90)
turtle.fillcolor ("blue")
turtle.begin_fill()
turtle.circle (-200,90)
turtle.right (90)
turtle.circle (-200,90)
turtle.end_fill()

# Left Petal
turtle.fillcolor ("yellow")
turtle.begin_fill()
turtle.circle (-200,90)
turtle.right (90)
turtle.circle (-200,90)
turtle.end_fill()

# Right Petal
turtle.left(90)
turtle.fillcolor ("orange")
turtle.begin_fill()
turtle.circle (-200,90)
turtle.right (90)
turtle.circle (-200,90)
turtle.end_fill()

turtle.penup()

# Writing words in right petal
turtle.setheading(0)
turtle.forward(100)
turtle.write("Anticipation/Hope")
turtle.backward(100)

# Writing words in top petal
turtle.left(90)
turtle.forward(100)
turtle.write("Like")
turtle.backward(100)

# Writing words in left petal
turtle.left(90)
turtle.forward(150)
turtle.write("Joy/Happiness")
turtle.backward(150)

# Writing words in top petal
turtle.left(90)
turtle.forward(100)
turtle.write("Sadness")
turtle.backward(100)

turtle.done()