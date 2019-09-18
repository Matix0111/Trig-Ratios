# This program is designed for trig ratios (SOH CAH TOA)
import math

class TrigFunc:
    print("OPTIONS: SOH, CAH, TOA")
    trig_ratio = input("Trig ratio: ")

    if trig_ratio == 'SOH':
        SOH()
    elif trig_ratio == 'CAH':
        CAH()
    elif trig_ratio == 'TOA':
        TOA()

    def SOH():
        sin_degrees = input("Degrees: ")
        sin_rad = math.sin(math.radians(sin_degrees))
        sin_round = round(sin_round, 2)
        print("Degrees: {} ROUNDED: {}".format(sin_rad, sin_round)

        c_or_e = input("Exit(E/e) or Continue(C/c): ")
        if c_or_e == "E" or c_or_e == "e":
            print("EXITING")
            return
        elif c_or_e == "C" or c_or_e == "c":
            sin_frac = input("Is the Numerator(N/n) or Denominator(D/d) the variable: ")

            if sin_frac == "N" or sin_frac == "n":
                pass
            elif sin_frac == "D" or sin_frac == "d":
                pass

    def CAH():
        pass
    def TOA():
        pass
