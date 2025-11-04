#Perfect Number

def isPerfect (number):
    listDivisors = []
    for i in range (1, number):
        if number % i == 0:
            listDivisors.append(i)
    if sum(listDivisors) == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

number = int(input())

print (f"{isPerfect(number)}")
