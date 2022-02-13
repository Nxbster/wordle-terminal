from termcolor import colored

def yellow_case(target, guess):

    output = ""

    for n in range(0, 5):
        if guess[n] == target[n]:
            output = output + colored(guess[n], 'white', 'on_green')
        elif guess[n] != target[n]:
            if guess[n] in target:
                output = output + colored(guess[n], 'white', 'on_yellow')
            else:
                output = output + colored(guess[n], 'white', 'on_red')
    
    print(output)
