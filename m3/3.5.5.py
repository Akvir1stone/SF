a = int(input('a'))
b = int(input('b'))
c = int(input('c'))
nums = [a, b, c]
count = 0
for i in nums:
    if i < 45:
        count = count + 1
if count == 1:
    print(True)
else:
    print(False)
