def isempty(st):
    if len(st)==0:
        return True
    return False
    
def EvaluateExpression(exp):
    st = []
    
    for i in exp.split():
        if i.isdigit():
            st.append(int(i))
        else:
            op2 = st.pop()
            op1 = st.pop()
            # print("op1: ",op1,"op2: ",op2)
            if i == '+':
                res = op1 + op2
            elif i == '-':
                res = op1 - op2
            elif i == '*':
                res = op1 * op2
            elif i == '/':
                res = op1 / op2
            elif i == '**':
                res = op1 ** op2
            st.append(res)
            # print("res: ",res)
    return st.pop()
            
print(float(EvaluateExpression(input())))