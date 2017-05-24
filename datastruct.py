from collections import deque
import logging
import re



# 操作数优先级
operate = {
    '(': 7,
    '^': 5,
    '!': 5,
    '*': 2,
    '/': 2,
    '%': 2,
    '+': 1,
    '-': 1
}

# 需要去掉左括号，所以我又开了一个运算符字典
suboperate = {
    '^': 5,
    '!': 5,
    '*': 2,
    '/': 2,
    '%': 2,
    '+': 1,
    '-': 1,
    '.': 0
}

'''
进行初步的检测
此函数用来检测输入是否合法，如果不合法返回False
目前想到的只有两个相连的都是运算符
'''


def checkInput(inputDeque)->bool:
    global operate
    global suboperate
    # 左右两括号的数量
    left, right = 0, 0
    if not inputDeque:
        return False
    # 检测是否有两个相连的算术运算符，如果有则说明输入有错误
    for pos, i in enumerate(inputDeque):
        if pos+1 < len(inputDeque) \
                and (i in suboperate and inputDeque[pos+1] in suboperate):
            return False
    # 对于括号的数目进行检测匹配
    for i in inputDeque:
        if i == '(':
            left += 1
        elif i == ')':
            right += 1
    if left != right:
        return False
    return True


# 将中缀表达式改为后缀表达式
def getPostfix(inputDeque: deque)->deque:
    global operate
    # 使用stack来储存运算符号
    # num用来储存数字
    if not checkInput(inputDeque):
        raise Exception
    stack = deque()
    result = deque()
    temp = []
    try:
        for i in inputDeque:
            # 如果有数字，那么则进入缓存，在下一个运算符前压入结果栈(finally有对末尾的数字进行处理)
            if '0' <= i <= '9' or i == '.':
                temp.append(i)
                continue
            result.append(''.join(temp))
            temp.clear()
            # 对于(直接进栈
            if i == '(':
                stack.append(i)
            elif i in operate:
                # 如果运算符栈空或操作符优先级大于栈顶优先级入栈
                if not stack or operate[i] > operate[stack[-1]]:
                    stack.append(i)
                    continue
                # 如果运算符栈非空，且栈顶的操作符优先级大于当前运算符的优先级，将栈中运算符弹出，
                # 直到运算符优先级小于当前操作符优先级，但是遇到左括号无条件终止弹出
                while stack and operate[stack[-1]] >= operate[i]\
                        and stack[-1] != '(':
                    result.append(stack.pop())
                stack.append(i)
            # 遇到右括号，首先对操作符栈中匹配是否有左括号，然后将栈中左括号前的操作符弹出，删除左括号
            elif i == ')':
                if not '(' in stack:
                    raise print('您输入的括号无法匹配')
                while stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
        else:
            # 结尾temp缓存数字处理，并将操作符栈中的操作符依次弹出
            if temp:
                result.append(''.join(temp))
            while stack:
                result.append(stack.pop())
    except Exception as e:
        logging.exception(e)
    finally:
        return result


# 计算后缀表达式的值
# 返回的值只可以在一定范围之内，可以考虑大数如何办，还有高精度小数
def calculator(inputDeque: deque):
    temp = deque()
    result = deque()
    reWord = re.compile(r'[0-9]')
    for i in inputDeque:
        num = re.search(reWord, i)
        '''
        现在这里没有什么好的方法将单位数字转化为多位数字
        现在的想法是使用正则来匹配出数字，确定需要进栈的是什么
        初步看了一下正则的原理，感觉很难？
        '''
        if num:
            # 做数字转换，不在计算的时候进行类型转换，进栈就转化为数字
            result.append(int(i)) if not '.' in i else result.append(float(i))
        else:
            if i == '+':
                result.append(result.pop()+result.pop())
            elif i == '-':
                a, b = result.pop(), result.pop()
                a, b = b, a
                result.append(a-b)
            elif i == '*':
                result.append(result.pop()*result.pop())
            elif i == '/':
                a, b = result.pop(), result.pop()
                a, b = b, a
                if b == 0:
                    raise ZeroDivisionError
                result.append(a/b)
            elif i == '%':
                a, b = result.pop(), result.pop()
                a, b = b, a
                if b == 0:
                    raise ZeroDivisionError
                result.append(a % b)
    return result[0]


if __name__ == '__main__':
    a = deque('(((6+6)*6+3)*2+6)*2')
    try:
        print(getPostfix(a))
        print(calculator(getPostfix(a)))
    except Exception as e:
        logging.exception(e)
    
