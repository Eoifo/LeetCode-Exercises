# 简单
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

# 通过版
# 计算特殊情况出现的次数，没出现一次，就减去对应特殊情况数值的2倍。
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_letter_to_int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        keywords = ("IV", "IX", "XL", "XC", "CD", "CM")
        count_list = []    # 建立一个空列表，以存放特殊情况出现的次数。
        for keyword in keywords:
            count_list.append(s.count(keyword))    # 将特殊情况出现的次数存入列表。

        s_list = list(s)
        sum_temp = 0
        for letter in s_list:
            sum_temp += roman_letter_to_int[letter]    # 将每个字符对应的值全部加起来。

        result = sum_temp \
        - (count_list[0] + count_list[1]) * 2 \
        - (count_list[2] + count_list[3]) * 20 \
        - (count_list[4] + count_list[5]) * 200 \
        # 而特殊情况的出现导致上一步加的过程出现了重复,所以要减去相应数值的2倍来修正。
        return result
test = Solution()
print(test.romanToInt("MCMXCIV"))

# 改进版
# 如果前一个字符代表的数值小于后一个字符代表的数值，
# 那么就在求和中减去前一个字符对应的数值。
# 如果前一个字符代表的数值大于后一个字符代表的数值，
# 那么就在求和中加上前一个字符对应的数值。
class Solution:
    def romanToInt(self, s: str) -> int:
        Roman2Int = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        Int = 0
        n = len(s)
        for index in range(n - 1):    # 遍历除最后一个字符以外的所有字符。
            if Roman2Int[s[index]] < Roman2Int[s[index + 1]]:
                Int -= Roman2Int[s[index]]    # 如果小于，那么减去。
            else:
                Int += Roman2Int[s[index]]    # 如果大于，那么加上。

        return Int + Roman2Int[s[-1]]    # 让求和的结果加上最后一个字符对应的值。
test = Solution()
print(test.romanToInt("MCMXCIV"))
