import re
import math
import operator as op
def sqrt(x):
    return(str(float(x)**.5))
def sin(x):
    return(str(math.sin(float(x))))
unary = {"sqrt":sqrt,"sin":sin}
ops = list("/*+-")
funcs = [op.truediv,op.mul,op.add,op.sub]
binary = dict(zip(ops, funcs))
parenFinder = re.compile(r"\(([^\(\)]*)\)")
alpha = r"([A-Za-z]*)"
numeric = r"((-?\d+)(\.\d+)?)"
unaryFinder = re.compile(alpha + r" *" + numeric)
binaryOps = [r"([\*\/])",r"([\+\-])"]
def unaryRun(function, number):
    if function in unary:
        return(unary[function](number))
    else:
        return(function + " " + number)
def binaryRun(number1,op, number2):
    if op in binary:
        number1 = float(number1)
        number2 = float(number2)
        return(str(binary[op](number1,number2)))
    else:
        return(number1 + " " + op + " " + number2)
def evaluate(expression):
        
        #expression = re.sub(r"([A-Za-z]*) *((-?\d+)(\.\d+)?)",lambda x: unaryRun(x[1],x[2]), expression)
    while  re.sub(unaryFinder,lambda x: unaryRun(x[1],x[2]), expression) != expression:
        expression = re.sub(unaryFinder,lambda x: unaryRun(x[1],x[2]), expression)
        if "e" in expression or "j" in expression:
            return("irrational")
    while expression.strip() != re.search(numeric,expression)[1]:
        for order in binaryOps:
            binaryFinder = re.compile(numeric + r" *" + order + r" *" + numeric)
            expression = re.sub(binaryFinder,lambda x: binaryRun(x[1],x[4],x[5]),expression)
        #expression = re.sub(r"([-\d\.]*) *([A-Za-z\+\-\*\\]*) *([-\d\.]*)",lambda x: binaryRun(x[1],x[2],x[3]), expression)
    return(" " + expression + " ")

def resolve_parens(expression):
    while "(" in expression:
        expression = re.sub(parenFinder,lambda x: evaluate(x[1]), expression)
    return(expression)
def calculate(expression):
    expression = resolve_parens(expression)
    
    return(evaluate(expression))
    
print(calculate("3+sqrt(3)/(8+sin(15))"))
    