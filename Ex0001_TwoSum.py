# 简单
# 给定一个整数数组 nums 和一个目标值 target。
# 请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

# 通过版
# 思路核心是使用“None”值进行占位，以避免序号的错乱。
nums = [3, 3]
target = int(input("Enter the target:"))
index_list = []
for num in nums:
    difference = target - num
    nums[nums.index(num)] = None    # 把当前数用“None”值进行占位，避免序号的错乱。
    if difference in nums and len(index_list) == 0:
        index_list.append(nums.index(None))
        index_list.append(nums.index(difference))
    else:
        nums[nums.index(None)] = num    # 如果不符合要求，则重新将“None”值复原为当前数。
print(index_list)

# 改进版
# 传统的思路是用target减去第一个数，判断其差会不会在之后的列表中出现。
# 改进版的思路是用target减去一个数，判断其差会不会在之前的列表中出现，这样就避免了减数序号的错乱。
# 从效果上来说这和传统思路是一致的。
def twoSum1(nums, target):
    lens = len(nums)
    j = -1
    for i in range(1, lens):    # 使用range()直接形成减数的序号。
        temp = nums[:i]    # 形成之前的列表切片。
        if (target - nums[i]) in temp:
            j = temp.index(target - nums[i])    # 返回差的序号。
            break
    if j >= 0:
        return [j, i]
nums = [3, 3]
target = 6
print(twoSum1(nums, target))

# 改进版
# 使用enumerate()函数将序列转换成字典。
def twoSum2(nums, target):
    hashmap={}
    for ind, num in enumerate(nums):
        hashmap[num] = ind    # 形成初始字典。
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)    # 寻找差在字典中对应的值。
        if j is not None and i != j:
            return [i, j]    # 这里只返回遍历过程中的第一个结果。
nums = [3, 2, 4]
target = 6
print(twoSum2(nums, target))
