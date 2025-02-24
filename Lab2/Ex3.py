class AutomatVerificare:
    def __init__(self):
        self.finalState = "q3"
        self.transitions = {
            "q0": {"a": "q1"},
            "q1": {"b": "q2"},
            "q2": {"c": "q3"},
            "q3": {"a": "q3", "b": "q3", "c": "q3", "d": "q3"}
        }

    def Cuvant(self, cuvant):
        state = "q0"
        for char in cuvant:
            if char not in "abcd":
                return False
            state = self.transitions.get(state, {}).get(char, "q0")
        return state == self.finalState

automat = AutomatVerificare()
cuvinte = ["abc", "aaabbc", "abcabc"]

for cuvant in cuvinte:
    print(f"{cuvant} - {automat.Cuvant(cuvant)}")