
def balance_parenthesis(s1):
    l1 = list(s1)
    lstack = []
    i = 0
    while (i < len(s1)):
        c = l1[i]
        if (c == '[' or c == '(' or c == '{'):
            lstack.append(c)
        elif c == ']':
            if not lstack or lstack.pop() != '[':
                return False
        elif c == ')':
            if not lstack or lstack.pop() != '(':
                return False
        elif c == '}':
            if not lstack or lstack.pop() != '{':
                return False
        i += 1
    return not lstack

##print(balance_parenthesis(s1 = "aasd()[]"))
print(balance_parenthesis(s1 = "asdasd]"))








