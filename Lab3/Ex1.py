class AutomatFinit:
    def __init__(self):
        self.stare = "q0"
        self.bautura_selectata = None
        self.nume_bautura = {"C": "Cafea", "T": "Ceai", "A": "Cappuccino", "H": "Ciocolată caldă"}

    def tranzitie(self, simbol):
        tranzitii = {
            ("q0", "C"): "q1",
            ("q0", "T"): "q2",
            ("q0", "A"): "q3",
            ("q0", "H"): "q4",
            ("q1", "OK"): "q0",
            ("q2", "OK"): "q0",
            ("q3", "OK"): "q0",
            ("q4", "OK"): "q0"
        }

        if (self.stare, simbol) in tranzitii:
            if self.stare == "q0" and simbol in self.nume_bautura:
                self.bautura_selectata = simbol

            self.stare = tranzitii[(self.stare, simbol)]

            if simbol == "OK" and self.bautura_selectata:
                print(f"A fost selectată băutura: {self.nume_bautura[self.bautura_selectata]}")
                self.bautura_selectata = None
        else:
            print("Tranziție invalidă!")

    def ruleaza(self):
        while True:
            print(f"Starea curentă: {self.stare}")
            simbol = input("Introduceți simbol (C, T, A, H, OK")

            if simbol == "exit":
                break

            self.tranzitie(simbol)
        print("Automatul s-a oprit.")


if __name__ == "__main__":
    automat = AutomatFinit()
    automat.ruleaza()
