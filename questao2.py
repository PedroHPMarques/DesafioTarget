def fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return numero == b or numero == 0
