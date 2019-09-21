# This program is designed for trig ratios (SOH CAH TOA)
import math # Importing math module for advanced functions(sin, cos, tan)

class TrigFunc: # Making a class for the whole script

    print("OPTIONS: SOH, CAH, TOA") # Displaying options
    trig_ratio = input("Trig ratio: ") # Getting user input for ratio type

    def SOH(): # Sin function
        sin_degrees = input("Degrees: ") # Getting input for degrees
        sin_rad = math.sin(math.radians(int(sin_degrees))) # Turning the degrees to radian
        sin_round = round(sin_rad, 2) # Rounding the radian to 2 decimal places
        print("RADIAN: {} ROUNDED: {}".format(sin_rad, sin_round)) # Printing radian and ROUNDED radian

        request = input("Exit(E/e) or Continue(C/c)? ") # Getting input for continuation or exiting
        if request == "E" or request == "e": # If the user wants to exit
            print("EXITING") # Print exiting
            return # Break out of loop (exits the prog)
        elif request == "C" or request == "c": # If the user wants to contine
            sin_frac = input("Is the Numerator(N/n) or Denominator(D/d) the VARIABLE? ") # Getting input for variable being the numerator or denominator

            if sin_frac == "N" or sin_frac == "n": # If the variable is the numerator
                number = input("Number: ") # Getting input for the number

                answer = sin_rad * int(number) # Multiplying the radian by the number
                answer_round = round(answer, 2) # Rounding the answer to 2 decimal places
                print("Answer: {}".format(answer_round)) # Prints ROUNDED answer
            elif sin_frac == "D" or sin_frac == "d": # If the number is the denominator
                div_number = input("Number: ") # Getting input for the number

                div_answer = int(div_number) / math.sin(math.radians(int(sin_degrees))) # Dividing the number by the sin of the degrees
                div_rounded_answer = round(div_answer, 2) # Rounds the answer to 2 decimal places

                print("Answer: {}".format(div_rounded_answer)) # Prints ROUNDED answer

    def CAH(): # Cos function
        cos_deg = input("Degrees: ") # Getting input for degrees
        cos_rad = math.cos(math.radians(int(cos_deg))) # Turning the degrees to radian
        cos_round = round(cos_rad, 2) # Rounding the answer to 2 decimal places
        print("RADIAN: {} ROUNDED: {}".format(cos_rad, cos_round)) # Printing radian and ROUNDED radian

        request_cos = input("Exit(E/e) or Continue(C/c)? ") # Getting user input for continuation or exiting
        if request_cos == 'E' or request_cos == 'e': # If the user wants to exit
            print("EXITING") # Print exiting
            return # Break out of loop(exits the prog)
        elif request_cos == 'C' or request_cos == "c": # If the user wants to continue
            cos_frac = input("Is the Numerator(N/n) or Denominator(D/d) the VARIABLE? ") # Getting input for variable being the numerator or denominator

            if cos_frac == "N" or cos_frac == 'n': # If the variable is the numerator
                cos_number = input("Number: ") # Getting input for the number

                cos_answer = cos_rad * int(cos_number) # Multiplying radian by the number
                cos_answer_round = round(cos_answer, 2) # Rounding the answer to 2 decimal places
                print("Answer: {}".format(cos_answer_round)) # Prints the ROUNDED answer

            elif cos_frac == "D" or cos_frac == "d": # If the variable is the denominator
                div_cos = input("Number: ") # Getting input for the number

                div_cos_answer = div_cos / math.cos(math.radians(int(cos_deg))) # Dividing the number by the cos of the degrees
                div_rounded_cos_answer = round(div_cos_answer, 2) # Rounding the answer to 2 decimal places
                print("Answer: {}".format(div_rounded_cos_answer)) # Prints ROUNDED answer

    def TOA(): # Tan function
        toa_deg = input("Degrees: ") # Getting put for degrees
        toa_rad = math.tan(math.radians(int(toa_deg))) # Turing the degrees to radian
        toa_rounded = round(toa_rad, 2) # Rounding the answer to 2 decimal places
        print("RADIAN: {} ROUNDED: {}".format(toa_rad, toa_rounded)) # Printing the radian and ROUNDED radian

        request_toa = input("Exit(E/e) or Continue(C/c)? ") # Getting input for continuation or exiting
        if request_toa == "E" or request_toa == "e": # If the user wants to exit
            print("EXITING") # Print exiting
            return # Break out of Loop (exits the prog)
        elif request_toa == "C" or request_toa == "c": # If the user wants to contine
            toa_frac = input("Is the Numerator(N/n) or Denominator(D/d) the VARIABLE? ") # Getting input for variable being the numerator or denominator

            if toa_frac == "N" or toa_frac == "n": # If the variable is the numerator
                toa_number = input("Number: ") # Getting input for number

                toa_answer = toa_rad * int(toa_number) # Multiplying the radian by the number
                toa_answer_round = round(toa_answer, 2) # Rounding the answer to 2 decimal places
                print("Answer: {}".format(toa_answer_round)) # Prints ROUNDED answer

            elif toa_frac == "D" or toa_frac == "d": # If the variable is the denominator
                div_toa = input("Number: ") # Getting input for number

                div_toa_answer = div_toa / math.tan(math.radians(int(toa_deg))) # Dividing the number by the tan of the degrees
                div_rounded_toa_answer = round(div_toa_answer, 2) # Rounding the answer to 2 decimal places
                print("Answer: {}".format(div_rounded_toa_answer)) # Prints ROUNDED answer

    if trig_ratio == 'SOH': # If the ratio type is SOH
        SOH() # Call the SOH function
    elif trig_ratio == 'CAH': # If the ratio type is CAH
        CAH() # Call the CAH function
    elif trig_ratio == 'TOA': # If the ratio type is TOA
        TOA() # Call the TOA function
    else: # If the ratio type is anything but the available options
        print("This is an invalid option, please relaunch program") # Notify of invalid option

TrigFunc() # Call the WHOLE class
