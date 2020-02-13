import turtle

n = 80

turtle.up()  # lift the pen
turtle.speed(11)  # turn it up to 11!

turtle.seth(310)
for j in range(n):
    # carefully calculated (absolutely not trial and error)
    turtle.goto(-1000 + (20 * j), 200 + (20 * j))
    for i in range(n):
        x = i + (n * j)
        if x % 3 == 0 and x % 5 == 0:
            turtle.write("FizzBuzz", False)
            turtle.forward(40)
        elif x % 3 == 0:
            turtle.write("Fizz", False)
            turtle.forward(40)
        elif x % 5 == 0:
            turtle.write("Buzz", False)
            turtle.forward(40)
        else:
            turtle.write(x, False)
            turtle.forward(40)


turtle.exitonclick()
