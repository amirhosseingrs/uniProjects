# getting the grammar
# none_finishers = input('enter none-finishers like(A,B,C) : ').split(',')
# Grammar = dict()
# for i in none_finishers : 
#     Grammar[i] = input(f'Expression of the {i} like(Aa|b|epsilon) : ').split('|')
# print(f'Grammar = {Grammar}')
Grammar = {'A': ['sdfA', 'sdfB', 'sdA', 'sA', 'efB', 'efaA'], 'B': ['f']}
none_finishers = ['A','B']
###########################################################################################################
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






# #############################################################################################################
# check for the Left Factoring of the Grammar 
Commons = dict()
def Add_Common(common, exprs, bethas) :
    Commons[common] = {'exprs' : exprs, 'bethas' : bethas}

def check_commons(str1, str2):
    res = ''
    if str1 == '' or str2 == '' : return res
    for i, x in enumerate(str1):
        if x == str2[i] and len(str2)-1 > i :
            res += x
        else :
            # res += x
            break
    return res




first_expr = next(iter(Grammar.values()))
while len([x for x in first_expr if x != '']) != 0:
    # find commons and saving
    for i in range(len(first_expr)) :
        exprs = [i]
        checkee = first_expr[i]
        common = checkee
        # print(f'checkee = {checkee}')
        if checkee == '' : continue
        # print(f' j list = {first_expr[]}')
        for j in range(len(first_expr)):
            checker = first_expr[j]
            if checker == '' : continue
            # print(f'checker = {checker} and j = {j}')
            check_common = check_commons(checkee, checker)
            if len(check_common) > 1 : 
                if len(check_common) < len(common) : 
                    common = check_common
                exprs.append(j)
            # print(f'checkee : {checkee} |  checker : {checker} = {check_common}')
        # print(f'common found = {common}    exprs = {exprs}')
        
        # caculate bethas
        bethas = [f[len(common):] for f in [x for i,x in enumerate(first_expr) if i in exprs]]
        # print(f'bethas = {bethas}')

        # savings the informations into Commons dictionary
        Add_Common(common, exprs, bethas)
        # make all the exprs equal to ''
        for i in exprs : 
            first_expr[i] = ''
        # print(f'first_expr = {first_expr}')
# print(Commons)
# printing the Result of LeftFactoring
factors = dict()
res = 'A -> '
for i in Commons.items():
    bethas = i[1]['bethas']
    # print(i[0])
    if bethas != ['']:
        name = Names.pop()
        res += i[0] + name + '|'
        factors[name] = bethas
    else : 
        res += i[0] + '|'
print(f'\nLeft Factoring : \n{res[:-1]}')
for i in factors.items():
    bethas = '|'.join(i[1])
    print(f'{i[0]} -> {bethas}')
        
    
############################################################################################################
