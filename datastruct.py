from collections import deque
import logging
import re

# 将中缀表达式改为后缀表达式

# 操作数优先级
operate = {
    '(': 7,
    '*': 6,
    '/': 6,
    '+': 5,
    '-': 5
}

suboperate = {
    '*': 6,
    '/': 6,
    '+': 5,
    '-': 5
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
            if '0' <= i <= '9':
                temp.append(i)
                continue
            result.append(''.join(temp))
            temp.clear()
            if i == '(':
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
                if not '(' in stack:
                    raise print('您输入的括号无法匹配')
                while stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()
        else:
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
def calculator(inputDeque: deque)->float:
    temp = deque()
    result = deque()
    reWord = re.compile(r'[0-9]')
    '''
    编译错误？
    类型错误，从上一个函数之中返回的是生成器
    '''
    for i in inputDeque:
        num = re.search(reWord, i)
        '''
        现在这里没有什么好的方法将单位数字转化为多位数字
        现在的想法是使用正则来匹配出数字，确定需要进栈的是什么
        初步看了一下正则的原理，感觉很难？
        '''
        if num:
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


if __name__ == '__main__':
    a = deque('11+2*3+(4*5+6)*7')
    print(getPostfix(a))
    print(calculator(getPostfix(a)))
