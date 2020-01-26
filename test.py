keywords = ["fizz", "buzz", "fizzbuzz"]
divisors = [3, 5]

for i in range(1, 16):
    answer = ""
    for divisor in divisors:
        if (i % divisor == 0):
            answer = answer + keywords[divisors.index(divisor)]
    if (answer == ""):
        print(i)
    else:
        print(answer)
