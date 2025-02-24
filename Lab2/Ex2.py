def detect(text):
    state = "q0"
    transitions = {
        "q0": {"c": "q1"},
        "q1": {"a": "q2", "c": "q1"},
        "q2": {"t": "q3", "c": "q1"},
    }

    for char in text.lower():
        state = transitions.get(state, {}).get(char, "q0")
        if state == "q3":
            return True
    return False

text = "My Cat is Tom"
print(detect(text))
