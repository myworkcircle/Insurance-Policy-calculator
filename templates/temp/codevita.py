
x = int(input())
s = input()
y = int(input())
result = []
while(y>0):
    t = int(input())
    cut = t-2
    char = s[t-1]
    new = s[:cut]
    counter = new.count(char)
    print(counter)
    result.append(counter)
    y=-1
for i in range(0,y):
    print(result[i])