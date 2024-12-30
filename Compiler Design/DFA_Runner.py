# getting the DFA
final_state = int()
DFA = dict()
# for i in range(100) :
#     state_path = input(f'state q{i} : ')
#     if state_path == 'end':
#         break
    
#     DFA[f'q{i}'] = state_path.split(',')

# final_state = input('final state : ')

# print(f'DFA = {DFA} \nFinal State = {final_state}')

DFA = {
'q0' : ['b0','a1'],
'q1' : ['a2','b0'], 
'q2' : ['a2','b3'],
'q3' : ['b0','a1']
}
final_state = 3

# Check String validity method
def stateExit(state, entery):
    return ''.join([x for x in DFA[f'q{state}'] if entery in x])[1]

def isOk(str):
    current_state = 0
    for i in str:
        print('----------------------')
        print(f'current state = {current_state} | entery = {i} | exit = {stateExit(current_state, i)}')
        current_state = stateExit(current_state, i)
    if int(current_state) == final_state:
        return True
    else :
        return False


# Getting the entery string to DFA machine with repl
def repl():
    while entery := input('enter your string : '):
        if entery == 'end':
            break
        print(isOk(entery))


repl()

