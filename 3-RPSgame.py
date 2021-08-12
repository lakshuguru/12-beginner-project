
import random as rd
def play():
    user=input("rock-'r', paper-'p', scissor-'s'")
    computer=rd.choice(['r', 'p', 's'])

    if user==computer:
        return 'It\'s tie'

    if iswin(user, computer):
        return 'you won'

    return "you lost"  

def iswin(player,opponent):
            if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
                return True

print(play())

                
