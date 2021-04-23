import random
import math

# a programme for a rock, paper, scissors game

def play():
    player_choice = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors:\n")
    player_choice = player_choice.lower()  #just in case user enters a capital letter. Converts to lowercase

    computer = random.choice(['r', 'p', 's']) 

    if player_choice == computer:
        return (0, player_choice, computer)

    if did_win(player_choice, computer):
        return (1, player_choice, computer)
    else:
        return (-1, player_choice, computer)


    def did_win(player, opponent):
        # returns true if the player wins against the opponent 
        # win conditions: r > s, s > p, p > r
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True
        else:
            return False
    

    def play_best_of(n):
        # play against the computer until you win at least half of n games 
        # half of n games =>> ceil(n/2) ==>> winning score
        player_wins = 0    #will count the score
        computer_wins = 0
        winning_score = math.ceil(n/2)
        
        while player_wins < winning_score and computer_wins < winning_score:
            results, player_choice, computer = play()

        # a tie
    if result == 0:
            print('You and the computer have both chosen {}. Its a tie. \n'.format(player_choice))
    
        # you win
    elif result == 1:
            player_wins += 1
            print('You chose {} and the computer chose {}. You won!\n'.format(player_choice, computer))
    else:
            computer_wins += 1
            print('You chose {} and the computer chose {}. You lost.\n'.format(player_choice, computer))

    if player_wins > computer_wins:
        print('You have won the best of {} games!'.format(n))
    else:
        print('Unfortunately, the computer has won the best of {} games. Better luck next time!'.format(n))



    if __name__ == '__main__':
        print(play_best_of(3)) #play to win best of 3 games (i.e >= 2)

    