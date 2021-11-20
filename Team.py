problem = int(input())
count = 0
for i in range(0, problem):
    x = input()
    if x.count('1') >= 2:
        count += 1
print(count)