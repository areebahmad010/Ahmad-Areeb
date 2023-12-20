user_input = []
x = 0
c = 0
s = 0
j = 0
low = pow(10, 9)
while x != - 1:
    x = int(input("Enter number to add to the sequence: "))
    user_input.append(x)
for i in range(0, len(user_input)-1):
    s += user_input[i]
    c += 1
    if user_input[i] < low:
        low = user_input[i]
c = i + 1
mean = s/c
print(f"Count = ", c, " sum = ", s, " min = ", low, " mean = ", mean)
# it looks like I learned how to use git today
