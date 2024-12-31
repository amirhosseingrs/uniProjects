# getting the grammar
none_finishers = input('enter none-finishers like(A,B,C) : ').split(',')
Grammar = dict()
for i in none_finishers : 
    Grammar[i] = input(f'Expression of the {i} like(Aa|b|epsilon) : ').split('|')
print(f'Grammar = {Grammar}')


# check the left recursion of the Grammar
LRR = ''
Names = [x for x in "ZYXWVUTSRQPONMLKJIHGFEDCBA" if x not in none_finishers]
def isLRecursion(none_finisher, exprs) :
    return next((x for x in exprs if x[0] == none_finisher), None)
for i in Grammar:
    none_finisher = i
    exprs = Grammar[i]
    isRec = isLRecursion(none_finisher, exprs)
    if isRec != None :
        name = Names.pop()
        alpha = isRec[1:]
        betha = [x + f' {name}' for x in exprs if none_finisher not in x]
        # print(f'alpha = {alpha} and betha = {betha}')
        # print(f'{none_finisher} -> {"|".join(betha)} \n{name} -> {alpha} {name} |  ε')
        LRR += f'{none_finisher} -> {"|".join(betha)} \n{name} -> {alpha} {name} |  ε\n'
    else : 
        LRR += f'{none_finisher} -> {"|".join(exprs)}\n'
print(f'Left Recursions Handler: \n{LRR}')







# check for the Left Factoring of the Grammar 
Commons = dict()
def Add_Common(common, exprs, bethas) :
    Commons[common] = {'exprs' : exprs, 'bethas' : bethas}

def check_commons(str1, str2):
    res = str()
    for i, x in enumerate(str1):
        if x == str2[i] and len(str2)-1 > i :
            res += x
        else :
            # res += x
            break
    return res

first_expr = next(iter(Grammar.values()))
while first_expr != '':
    common = str()
    checkee = first_expr[0]
    for i in range(1, len(first_expr)):
        print(f'commons for {checkee} and {first_expr[i]} = {check_commons(checkee, first_expr[i])}')


    break