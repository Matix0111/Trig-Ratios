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
            sin_frac = input("Is the Numerator(N/n) or Denominator(D/d) the VARIABLE? ")

            if sin_frac == "N" or sin_frac == "n":
                number = input("Number: ")

                answer = sin_rad * int(number)
                answer_round = round(answer, 2)
                print("Answer: {}".format(answer_round))
            elif sin_frac == "D" or sin_frac == "d":
                div_number = input("Number: ")

                div_answer = int(div_number) / math.sin(math.radians(int(sin_degrees)))

                print(div_answer)

    def CAH():
        cos_deg = input("Degrees: ")
        cos_rad = math.cos(math.radians(int(cos_deg)))
        cos_round = round(cos_rad, 2)
        print("RADIAN: {} ROUNDED: {}".format(cos_rad, cos_round))

        request_cos = input("Exit(E/e) or Continue(C/c): ")
        if request_cos == 'E' or request_cos == 'e':
            print("EXITING")
            return
        elif request_cos == 'C' or request_cos == "c":
            cos_frac = input("Is the Numerator(N/n) or Denominator(D/d) the VARIABLE? ")

            if cos_frac == "N" or cos_frac == 'n':
                cos_number = input("Number: ")

                cos_answer = cos_rad * int(cos_number)
                cos_answer_round = round(cos_answer, 2)
                print("Answer: {}".format(cos_answer_round))

            elif cos_frac == "D" or cos_frac == "d":
                div_cos = input("Number: ")

                div_cos_answer = div_cos / math.cos(math.radians(int(cos_deg)))
                print("Answer: {}".format(div_cos_answer))
    def TOA():
        pass


    if trig_ratio == 'SOH':
        SOH()
    elif trig_ratio == 'CAH':
        CAH()
    elif trig_ratio == 'TOA':
        TOA()
    else:
        print("This is an invalid option, please relaunch program")

TrigFunc()
