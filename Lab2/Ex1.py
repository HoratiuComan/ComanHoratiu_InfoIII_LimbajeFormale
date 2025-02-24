def AutomatFinit(input_string):
    state = 'q0'
    final_states = {'q3'}
    transitions = { 'q0': {'0': 'q1', '1': 'q2'},
                    'q1': {'0': 'q3', '1': 'q0'},
                    'q2': {'0': 'q1', '1': 'q3'} }

    for symbol in input_string:

        if symbol not in {'0', '1'}:
            return False

        state = transitions.get(state, {}).get(symbol)
        if state is None:
            return False

    return state in final_states

print(AutomatFinit("101"))