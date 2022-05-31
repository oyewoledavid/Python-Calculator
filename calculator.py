#This calculator is built to take in input and return the result depending on the operator the user inputs
#The functions named start and rerun are to make the programme repeat as many times as the user wants
#The programme is not 100% error proof, i will get better as i progress.

#Written and tested with VScode.



def start():
    first_number = float(input("Enter First Number: "))
    operator = input("Enter an Operator: ")
    second_number = float(input("Enter second Number: "))

    if operator == "+":
        print('{} + {}'.format(first_number, second_number))
        print(first_number + second_number)
    elif operator == "*":
        print('{} * {} = '.format(first_number, second_number))
        print(first_number * second_number)
    elif operator == "-":
        print('{} - {} = '.format(first_number, second_number))
        print(first_number - second_number)
    elif operator == "/":
        print('{} / {} = '.format(first_number, second_number))
        print(first_number / second_number)
    elif operator == "%":
        print('{} % {} = '.format(first_number, second_number))
        print(first_number % second_number)
    else:
        print("Enter a valid Number and operator")
    rerun()
def rerun():
    repeat = input("Are you done? enter YES or NO: ")
    if repeat.upper() == 'NO':
        start()
    elif repeat.upper() == 'YES':
        print("Thank You. GOODBYE!!!")
    else:
        rerun()
start()