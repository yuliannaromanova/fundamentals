for i in range(1, 151):
    print(i)

for x in range(5, 1001, 5):
    print(x)

for x in range(1, 101):
    print(x)
    if x % 5 == 0:
        print("Coding")
    if x % 10 == 0:
        print("Coding Dojo")

sum = 0
x = 1
while x <=500000:
    if x % 2 != 0:
        sum = sum + x
        print(sum)

for x in range(2018, 0, -4):
    print(x)

lowNum = 2
highNum = 55
mult = 4
for x in range(lowNum, highNum):
    if x % mult == 0:
        print(x)