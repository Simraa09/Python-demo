num = 2
while num <= 100:
    i = 2
    prime = True
    while i < num:
        if num % i == 0:
            prime = False
            break
        i += 1
    if prime:
        print(num)
    num += 1