import turtle  # 🐢🐢

n = 80


turtle.up()
turtle.speed(11)

turtle.seth(310)

for j in range(n):
    turtle.goto(-600 + (20 * j), 100 * (20 * j))
    for i in range(n):
        x = i + (n*j)
        if x % 3 == 0 and x % 5 == 0:
            turtle.write("fizzbuzz", False)
        else:
            turtle.write(x, False)

turtle.exitonclick()
