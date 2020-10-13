# 简单
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 1.左括号必须用相同类型的右括号闭合。
# 2.左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。

# 通过版
# 分别查找三种括号字符，如果找到就将其从字符串中删除。
# 然后重新查找一遍，直至无法找到为止。
# 如果剩下的字符串是空就返回真值，否则返回假值。
class Solution:
    def isValid(self, s: str) -> bool:
        a = "()"
        b = "[]"
        c = "{}"
        a_bool = b_bool = c_bool = True    # 初始化判断值。
        a_index = b_index = c_index = None

        while a_bool or b_bool or c_bool:
            if a in s:
                a_index = s.find(a)    # 查找是否存在第一种括号。
                s_list = list(s)
                del(s_list[a_index])    # 删除这种括号的左边部分。
                del(s_list[a_index])    # 删除这种括号的右边部分。
                s = "".join(s_list)
                a_bool = b_bool = c_bool = True    # 重置判断值。
                continue
            else:
                a_bool = False    # 如果找不到设置第一种括号的判断值为否。
            if b in s:
                b_index = s.find(b)
                s_list = list(s)
                del(s_list[b_index])
                del(s_list[b_index])
                s = "".join(s_list)
                a_bool = b_bool = c_bool = True
                continue
            else:
                b_bool = False
            if c in s:
                c_index = s.find(c)
                s_list = list(s)
                del(s_list[c_index])
                del(s_list[c_index])
                s = "".join(s_list)
                a_bool = b_bool = c_bool = True
                continue
            else:
                c_bool = False

        if s != "":
            return False
        else:
            return True
test = Solution()
print(test.isValid("(){}}{"))

# 升级版
# 语句更加精炼
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace('[]','').replace('()','').replace('{}','')
        if s == "":
            return True
        else:
            return False
test = Solution()
print(test.isValid("(){}}{"))

# 升级版
# 使用栈的概念进行编程，左边部分视为进栈，遇到右边部分视为出栈。
# 最后栈内还有剩余数据则返回假，否则视为真。
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']    # 如果第一个如栈就是右半部分，则这个问号就起作用。
        for item in s:
            if item in dic:
                stack.append(item)    # 如果是左半部分就进栈。
            elif dic[stack.pop()] != item:    # 如果出栈的对应右半部分不是下一个迭代
                return False    # 则返回假。
        return len(stack) == 1
