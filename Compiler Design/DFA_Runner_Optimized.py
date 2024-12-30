# Get the DFA
final_state = input("Enter the final state: ").strip()  # Getting the final state first
DFA = {}

# Input DFA transitions until 'end' is encountered
for i in range(100):
    state_path = input(f'Enter transitions for state q{i} (or type "end" to stop): ').strip()
    if state_path.lower() == 'end':
        break
    DFA[f'q{i}'] = state_path.split(',')

print(f'DFA = {DFA} \nFinal State = {final_state}')

# test values
# DFA = {'q0': ['a1', 'b0'], 'q1': ['a2', 'b0'], 'q2': ['a2', 'b3'], 'q3': ['a1', 'b0']} 


# Check transition for a given state and symbol
def state_exit(state, entry):
    # Return the next state for a given entry symbol
    for transition in DFA[f'q{state}']:
        if entry in transition:
            return transition[1]  # Assumes transition format is like ('a', 'q1')
    return None  # If no valid transition found


def is_ok(input_string):
    current_state = 0
    for symbol in input_string:
        print('----------------------')
        print(f'Current state = {current_state} | Input = {symbol} | Next state = {state_exit(current_state, symbol)}')
        next_state = state_exit(current_state, symbol)
        if next_state is None:
            print("Invalid transition encountered.")
            return False
        current_state = int(next_state)  # Update state based on the next state
    return int(current_state) == int(final_state)  # Compare final state with the current state


# Input string processing loop (REPL)
def repl():
    while True:
        input_string = input('Enter your string (or "end" to stop): ').strip()
        if input_string.lower() == 'end':
            break
        print(is_ok(input_string))  # Check if the DFA accepts the string

# Run the REPL (read-eval-print loop)
repl()
