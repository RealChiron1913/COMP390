import itertools

# 生成1到10的数字列表
num = 10
for i in range(0, num):
    numbers = list(range(0, i + 1))

# 使用permutations函数生成所有排列组合
    all_permutations = list(itertools.permutations(numbers))
# 遍历并打印所有排列组合
    for perm in all_permutations:
        nums = []
        for num in perm:
            nums.append(num)
        print(nums)