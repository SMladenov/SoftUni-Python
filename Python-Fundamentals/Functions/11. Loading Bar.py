#Loading Bar

def percentage (number):
    times = number // 10
    if times == 10:
        return f"100% Complete!\n[{'%' * times}]"
    elif 1 <= times <= 9:
        return f"{number}% [{'%' * times}{'.' * (10 - times)}]\nStill loading..."
    elif times == 0:
        return f"{number}% [{10 * '.'}]\nStill loading..."

number = int(input())

print (f"{percentage(number)}")
