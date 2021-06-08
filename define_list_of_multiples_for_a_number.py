divisible = int(input("Which integer's multiple numbers do you want to get? Enter an integer: "))
until = int(input("Until which number do you want to get a list of multiples for the integers defined? Enter an integer:  "))

for number in range(until+1):
    if number % divisible  == 0:
        print(number)
