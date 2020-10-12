# 简单
# 编写一个函数来查找字符串数组中的最长公共前缀，如果不存在公共前缀，返回空字符串 ""。
# 如果参数是空，就返回空字符串 ""。

# 通过版
# 将每个字符串的每个字母提取出来组成一个新列表。
# 如果列表中的元素都一样，那就输出这个字母。
# 如果一旦出现不一样就暂停输出。
class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            strs.sort(key = lambda item : len(item))    # 对原始列表进行排序。
            sum = 0
            for x in range(len(strs[0])):    # 第一个字符的字母长度。
                one_letter_list = []    #设置一个空的新列表用来存放字母。
                for y in strs:
                    one_letter_list.append(y[x])    # 将字母逐个添加至列表。
                if one_letter_list.count(one_letter_list[0]) == len(strs):
                    sum += 1    # 计算有几个列表符合要求。
                else:
                    break    # 遇到不符合的情况在第一时间跳出循环。
            return strs[0][:sum]
test = Solution()
print(test.longestCommonPrefix(["cir","car"]))

# 改进版
# 求出列表中的最小字符串与最大字符串。
# 只要它们的某一位字母一样，就代表所有的字符串该位上的字母都一样。
# 如果不一样就输出最小字符串的切片。
# 如果都一样就输出最小的字符串。
class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if not strs: return ""    # 如果是空列表就返回空字符串。
        str0 = min(strs)
        str1 = max(strs)
        for i in range(len(str0)):
            if str0[i] != str1[i]:    # 遍历各位上的字母，使两者进行比较。
                return str0[:i]    # 如果不同就返回切片。
        return str0    # 如果相同就返回最小字符串本身。
test = Solution()
print(test.longestCommonPrefix(["cir","car"]))

# 改进版
# 使用zip（0函数将各位字母组成元组。
# 再使用set()函数统计元组中重复的元素，如果等于1那么说明元组中的元素都是一样的。
# 最后把这个元素添加到切片结果中。
class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ''
        for item in zip(*strs):    # 使用zip()函数将列表作为参数传入。
            if len(set(item)) == 1:
                result += item[0]
            else:
                break
        return result
test = Solution()
print(test.longestCommonPrefix(["cir","car"]))
