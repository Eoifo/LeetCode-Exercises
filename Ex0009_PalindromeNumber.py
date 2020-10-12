# 简单
# 判断一个整数是否是回文数。
# 回文数是指正序和倒序读都是一样的整数。
# 进阶要求：你能不将整数转为字符串来解决这个问题吗？

# 通过版
# 将数字转换为字符形式，然后与其反转进行比较。
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        if string_x == string_x[::-1]:    # 原字符串与其反转形式进行比较。
            return True
        else:
            return False
test = Solution()
print(test.isPalindrome(101))

# 改进版
# 通过不断的除以10来确定整数的位数，然后分别对比第一位与最后一位的数字。
class Solution:
    def isPalindrome(self, x: int) -> bool:
        mod_list = []
        while x != 0:
            mod = x % 10
            mod_list.append(mod)    # 不断的除以10，并将结果添加到列表中。
            x //= 10
        print(mod_list)
        if mod_list == list(reversed(mod_list)):    # 将列表反转后与原列表进行比较。
            return True
        else:
            return False
test = Solution()
print(test.isPalindrome(121))
