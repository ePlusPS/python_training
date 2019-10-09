import os

def pause():
    input("\nTake a second to review the output.\nPress Enter to continue")
    os.system('cls')

def problem(num):
    if round(num - int(num),1) == 0.1:
        os.system('cls')
    print("Exercise {} ".format(num) + "-"*40)