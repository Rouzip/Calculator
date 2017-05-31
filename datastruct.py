from collections import deque
import logging
import re
import math


'''
比较运算符的优先级
返回true 高
false 低
'''


def cmpPri(a: str, b: str)->bool:
    operate = {
        '(': 16,
        's': 16,
        'c': 16,
        't': 16,
        'q': 16,
        'l': 16,
        'i': 16,
        '^': 15,
        '!': 15,
        '*': 12,
        '/': 12,
        '%': 12,
        '+': 11,
        '-': 11,
        '<': 5,
        ',': 1,
        '0': 0
    }
    if a == b and a == '^':
        return True
    if (operate[a] > operate[b]):
        return True
    else:
        return False


'''
将函数转化为单字节运算符
'''


def funToOp(ope: str)->str:
    if ope == 'sin':
        return 's'
    elif ope == 'cos':
        return 'c'
    elif ope == 'tan':
        return 't'
    elif ope == 'sqrt':
        return 'q'
    elif ope == 'log':
        return 'l'
    elif ope == 'mod':
        return '%'
    else:
        return ' '


'''
执行运算操作
读入运算符和操作栈
根据运算符进行运算
'''


def cal(ope: str, Expr: deque):
    a, b, c = None, None, None
    if ope == '+':
        b = Expr.pop()
        a = Expr.pop()
        Expr.append(a+b)
    elif ope == '-':
        b = Expr.pop()
        a = Expr.pop()
        Expr.append(a-b)
    elif ope == '*':
        b = Expr.pop()
        a = Expr.pop()
        Expr.append(a*b)
    elif ope == '/':
        b = int(Expr.pop())
        a = Expr.pop()
        Expr.append(a/b)
    elif ope == '^':
        b = Expr.pop()
        a = Expr.pop()
        Expr.append(math.pow(a, b))
    elif ope == '%':
        b = int(Expr.pop())
        a = Expr.pop()
        Expr.append(a % b)
    elif ope == '!':
        a = Expr.pop()
        Expr.append(math.factorial(int(a)))
    elif ope == '<':
        b = Expr.pop()
        a = Expr.pop()
        Expr.append(a < b)
    elif ope == '>':
        b = Expr.pop()
        a = Expr.pop()
        Expr.append(a > b)
    elif ope == 's':
        a = Expr.pop()
        Expr.append(math.sin(a))
    elif ope == 'c':
        a = Expr.pop()
        Expr.append(math.cos(a))
    elif ope == 't':
        a = Expr.pop()
        Expr.append(math.tan(a))
    elif ope == 'q':
        a = Expr.pop()
        Expr.append(math.sqrt(a))
    elif ope == 'l':
        a = Expr.pop()
        Expr.append(math.log(a))
    else:
        return
    return Expr


'''
将前缀表达式转换为后缀表达式并计算
读入表达式串及寄存器
返回表达式值的计算结果
'''


def getPostfix(expr: str):
    # 记录转换后的表达式
    result = deque()
    # 记录符号
    ops = deque()
    ops.append('0')
    # 记录读入表达式的长度
    length = len(expr)
    isDigit = False
    isFun = False
    isRBracket = False
    # 暂存数字
    dTmp = ''
    # 暂存函数名
    fTmp = ''
    # 正则，匹配数字
    reNum = re.compile(r'[0-9\.]')
    reWord = re.compile(r'[a-z]')
    for i in expr:
        if i == ' ' or i == '\n':
            continue
        # 添加单目负号之前的0，使结果正确
        if (i == '-' and not isDigit and not isRBracket):
            result.append(0)
        # 进行预判断
        isDigit = True if re.search(reNum, i) else False
        isFun = True if re.search(reWord, i) else False
        isRBracket = True if i == ')' else False

        if isDigit:
            dTmp += i
        elif isFun:
            fTmp += i
        else:
            if dTmp:
                result.append(float(dTmp))
            dTmp = ''
            # 处理右括号，将符号全部弹出
            if i == ')':
                while ops[-1] != '(':
                    result = cal(ops[-1], result)
                    ops.pop()
                # 新运算符进栈
                ops.pop()
            # 如果优先级高则直接进栈
            elif cmpPri(i, ops[-1]) or ops[-1] == '(':
                if fTmp:
                    ops.append(funToOp(fTmp))
                    ops.append(i)
                else:
                    ops.append(i)
            # 根据运算符进行运算
            else:
                result = cal(ops[-1], result)
                ops.pop()
                if not cmpPri(i, ops[-1]) and ops[-1] != '(':
                    result = cal(ops[-1], result)
                    ops.pop()
                ops.append(i)
    if dTmp:
        result.append(float(dTmp))
    ops.popleft()
    while ops:
        result = cal(ops[-1], result)
        ops.pop()
    return result[0]

if __name__ == '__main__':
    a = deque('(1+2+3)^(1+2)')
    try:
        print(getPostfix(a))
    except Exception as e:
        logging.exception(e)
