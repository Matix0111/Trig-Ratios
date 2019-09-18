# This program is designed for trig ratios (SOH CAH TOA)
import math
import time

class TrigFunc:

    print("OPTIONS: SOH, CAH, TOA")
    trig_ratio = input("Trig ratio: ")

    def SOH():
        sin_degrees = input("Degrees: ")
        sin_rad = math.sin(math.radians(int(sin_degrees)))
        sin_round = round(sin_rad, 2)
        print("RADIAN: {} ROUNDED: {}".format(sin_rad, sin_round))

        request = input("Exit(E/e) or Continue(C/c): ")
        if request == "E" or request == "e":
            print("EXITING")
            return
        elif request == "C" or request == "c":
            sin_frac = input("Is the Numerator(N/n) or Denominator(D/d) the VARIABLE: ")

            if sin_frac == "N" or sin_frac == "n":
                number = input("Number: ")

                answer = sin_rad * int(number)
                answer_round = round(answer, 2)
                print("Answer: {}".format(answer_round))
            elif sin_frac == "D" or sin_frac == "d":
                print("THIS FUNCTION IS IN PROGRESS")
                timer = 6
                while True:
                    time.sleep(1)
                    timer -= 1

                    print("Exiting in: {}".format(timer))

                    if timer > 0:
                        pass
                    elif timer <= 0:
                        return
                # div_number = input("Number: ")

                # div_answer =

        def CAH():
            pass
        def TOA():
            pass


    if trig_ratio == 'SOH':
        SOH()
    elif trig_ratio == 'CAH':
        CAH()
    elif trig_ratio == 'TOA':
        TOA()

TrigFunc()
