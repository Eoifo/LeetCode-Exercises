# 简单
# 给出一个32位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 假设我们的环境只能存储得下32位的有符号整数，如果反转后整数溢出那么就返回0。

# 通过版
# 先判断正数是否小于零，把负号在反转后加入。
# 再判断反转后是否溢出，确定是否按要求返回零值。
class Solution:
    def reverse(self, x: int) -> int:
        abs_x = abs(x)
        list_x = list(str(abs_x))
        list_x.reverse()
        result = int("".join(list_x))

        if x < 0:
            result = -1 * result

        if result in range(-2**31, 2**31):
            return result
        else:
            return 0
test = Solution()
print(test.reverse(-120))

# 改进版
# 先判断正数是否小于零，把负号在反转后加入。
# 再判断反转后是否溢出，确定是否按要求返回零值。
class Solution:
    def reverse(self, x: int) -> int:
        abs_x = abs(x)
        result = int(str(abs_x)[::-1])    # 使用了字符串的切片功能，从而避免了转换为列表的步骤。

        if x < 0:
            result = -1 * result

        if result in range(-2**31, 2**31):
            return result
        else:
            return 0
test = Solution()
print(test.reverse(-120))