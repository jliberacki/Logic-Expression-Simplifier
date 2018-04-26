import string

variables = string.ascii_letters+'0'+'1'
operators = {'~': 4,'&': 3, '>': 3, '^': 2, '=': 2, '|': 1, '(':0,')':None}


def is_logic(expr):
    #checks if the expr is correct
    next_char=variables+'('+'~'
    bracket_control=0
    operators_str=''.join(operators.keys())
    for x in expr:
        if x in next_char:
            if x=='(':
                bracket_control+=1
                next_char=variables+'('+'~'
            elif x==')':
                if(bracket_control < 1): return False
                else:
                    next_char=operators_str
                    bracket_control-=1
            elif x in variables:
                next_char=operators_str
            elif x=='~':
                next_char=variables+'('+'~'
            elif x in operators_str:
                next_char=variables+'('
        else: return False
    return True

def convert_to_rpn(string):
    stack=[]
    output=[]
    for char in string:
        if char not in operators.keys():
            output.append(char)
        elif char == ')':
            x = stack.pop()
            while(x!='('):
                output.append(x)
                x = stack.pop()
        elif operators.get(char)==0:
            stack.append(char)
        elif stack and operators.get(char) > operators.get(stack[-1]):
            stack.append(char)
        else:
            while(stack and operators.get(char) < operators.get(stack[-1])):
                x = stack.pop()
                if x != '(':
                    output.append(x)
            stack.append(char)
    while stack:
        output.append(stack.pop())
    return output

def evaluete_expresion(rpn):
    stack=[]
    for char in rpn:
        if(char not in operators):
            stack.append(char)
        elif char is '~':
            stack.append(not bool(int(stack.pop())))
        else:
            x = bool(int(stack.pop()))
            y = bool(int(stack.pop()))
            if char is '=':
                stack.append(x == y)
            elif char is '^':
                stack.append(x != y)
            elif char is '&':
                stack.append(x and y)
            elif char is '|':
                stack.append(x or y)
            elif char is '>':
                stack.append(x or not y)
    return stack.pop()    
 

def add_one(bin_num):
    #add one to binary number in list
    length=len(bin_num)
    for i in range(length):
        if bin_num[length-i-1]==0:
            bin_num[length-i-1]=1
            return bin_num
        else:
            bin_num[length-i-1]=0

def all_true_evaluations(expr, variables):
    bin_num = [0 for i in variables]
    output = []
    for i in range(0, 2 ** len(variables)):
        tmp = expr[:]
        for var, value in zip(variables, bin_num):
            tmp = list(map(lambda c: value if c is var else c, tmp ))
        if evaluete_expresion(tmp) == True:
            output.append(bin_num[:])
        bin_num = add_one(bin_num)
    return output


def remove_duplicates(list):
    output = []
    seen = []
    for value in list:
        if value not in seen:
            output.append(value)
            seen.append(value)
    return output

def bin_to_dec(bin_num):
    #convert binary number in list to decimal value
    bin_num = [str(i) for i in bin_num]
    num_str=''.join(bin_num)
    return int(num_str,2)