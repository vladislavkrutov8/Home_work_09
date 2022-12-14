def left_digit(user_expression, pos):
    pos -= 1
    digit = ''
    while pos>= 0  and not user_expression[pos] in ['+', '-', '*', '/', '(', ')']:
        digit = user_expression[pos] + digit
        pos -= 1
    if user_expression[pos] == '-':
        digit = '-' + digit
    return digit

def right_digit(user_expression, pos):
    pos += 1
    digit = ''
    while pos <= len(user_expression)-1 and not user_expression[pos] in ['+', '-', '*', '/', '(', ')']:
        digit = digit + user_expression[pos]
        pos += 1
    return digit

def div_operation(user_expression):
    if '/' in user_expression:
        pos = user_expression.index("/")
        b = left_digit(user_expression, pos)
        f = right_digit(user_expression, pos)
        result = float(left_digit(user_expression, pos))/float(right_digit(user_expression, pos))
        user_expression = user_expression[:pos-len(b)] + str(result) + user_expression[pos+1+len(f):]
    return user_expression


def mult_operation(user_expression):
    if '*' in user_expression:
        pos = user_expression.index("*")
        b = left_digit(user_expression, pos)
        f = right_digit(user_expression, pos)
        result = float(left_digit(user_expression, pos))*float(right_digit(user_expression, pos))
        user_expression = user_expression[:pos-len(b)] + str(result) + user_expression[pos+1+len(f):]
    return user_expression


def sum_operation(user_expression):
    if '+' in user_expression:
        pos = user_expression.index("+")
        b = left_digit(user_expression, pos)
        f = right_digit(user_expression, pos)
        result = float(left_digit(user_expression, pos))+float(right_digit(user_expression, pos))
        user_expression = user_expression[:pos-len(b)] + str(result) + user_expression[pos+1+len(f):]
    return user_expression


def dif_operation(user_expression):
    if '-' in user_expression:
        pos = user_expression[1:].index("-")+1
        b = left_digit(user_expression, pos)
        f = right_digit(user_expression, pos)
        result = float(left_digit(user_expression, pos))-float(right_digit(user_expression, pos))
        user_expression = user_expression[:pos-len(b)] + str(result) + user_expression[pos+1+len(f):]
    return user_expression


def eval_simple_expression(simple_expression):
    while '/' in simple_expression:
        simple_expression = div_operation(simple_expression)
    while '*' in simple_expression:
        simple_expression = mult_operation(simple_expression)
    while '+' in simple_expression:
        simple_expression = sum_operation(simple_expression)
    while '-' in simple_expression[1:]:
        simple_expression = dif_operation(simple_expression)
    return simple_expression

def eval_bracket_expression(user_expression):
    left_pos = 0
    right_pos = 0
    for i in range(len(user_expression)):
        if user_expression[i] == '(':
            left_pos = i
        if user_expression[i] == ')':
            right_pos = i
            if left_pos == 0:
                left_part = ''
            else:
                left_part = user_expression[:left_pos]
            if right_pos == len(user_expression)-1:
                right_part = ''
            else:
                right_part = user_expression[right_pos+1:]

            user_expression = left_part + eval_simple_expression(user_expression[left_pos+1:right_pos]) + right_part
            return user_expression
    return user_expression


def staples(user_expression):
    count_s=0
    for i in range(len(user_expression)):
        if user_expression[i] == '(':
            count_s += 1
        if user_expression[i] == ')':
            count_s -= 1
        if count_s<0:
            return count_s
    return count_s

# try:
#     user_expression = input("?????????????? ?????????????????? ?????? ???????????????????? ????????????????: ").replace(' ', '')
#     if staples(user_expression) == 0:
#         while '(' in user_expression:
#             user_expression = eval_bracket_expression(user_expression)
#         user_expression = eval_simple_expression(user_expression)
#         print("??????????????????: ", round(float(user_expression),5))
#     else:
#         print('???????????? ?? ???????????????????? ????????????')

# except Exception as err:
#     print('???????????????? ????????????: ', str(err.args))

def calc(user_expression):
    if staples(user_expression) == 0:
        while '(' in user_expression:
            user_expression = eval_bracket_expression(user_expression)
        user_expression = eval_simple_expression(user_expression)
        return str(round(float(user_expression),5))
    else:
        return '???????????? ???????????????????? ???????????? '