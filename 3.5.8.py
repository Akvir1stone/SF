nums = []
number_of = int(input("how much"))
for i in range(0, number_of):
    nums.append(int(input('num')))
print(len(nums) == len(set(nums)))
