#Black Flag

days = int(input())
dailyPlunder = int(input())
expected = float(input())

total = 0



for i in range (1, days + 1):
    total += dailyPlunder
    if i % 3 == 0:
        total += dailyPlunder * 0.5
    if i % 5 == 0:
        total = total * 0.7

if total >= expected:
    print (f"Ahoy! {total:.2f} plunder gained.")
else:
    percentage = ((total / expected) * 100)
    print (f"Collected only {percentage:.2f}% of the plunder.")