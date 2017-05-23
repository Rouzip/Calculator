from collections import deque
import logging
# 将中缀表达式改为后缀表达式

# 操作数优先级
operate = {
    '(': 7,
    '*': 6,
    '/': 6,
    '+': 5,
    '-': 5
}


def getPostfix(inputDeque: deque)->deque:
    global operate
    # 使用stack来储存运算符号
    # num用来储存数字
    stack = deque()
    result = deque()

    for i in inputDeque:
        if '0' <= i <= '9':
            result.append(i)
        elif i == '(':
            stack.append(i)
        elif i in operate:
            if not stack or operate[i] >= operate[stack[-1]]:
                stack.append(i)
                continue
            while stack and operate[stack[-1]] >= operate[i]\
                    and stack[-1] != '(':
                result.append(stack.pop())
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
    else:
        while stack:
            result.append(stack.pop())
    return result


# 计算后缀表达式的值
def calculator(inputDeque: deque)->float:
    temp = deque()
    result = deque()
    for i in inputDeque:
        if '0' <= i <= '9':
            result.append(i)
        else:
            try:
                if i == '+':
                    result.append(int(result.pop())+int(result.pop()))
                elif i == '-':
                    result.append(int(result.pop())-int(result.pop()))
                elif i == '*':
                    result.append(int(result.pop())*int(result.pop()))
                elif i == '/':
                    result.append(int(result.pop())/int(result.pop()))
            except Exception as e:
                logging.exception(e)

    return int(result[0])

'''
此函数用来检测输入是否合法，如果不合法返回False
目前想到的只有两个相连的都是运算符
'''


def checkInput(inputDeque)->bool:
    global operate
    if not checkInput:
        return
    for pos, i in enumerate(inputDeque):
        if i+1 < len(inputDeque) \
                and (i in operate and inputDeque[pos+1] in operate):
            return False
    return True


if __name__ == '__main__':
    a = deque('1+2*3+(4*5+6)*7')
    print(getPostfix(a))
    print(calculator(getPostfix(a)))
