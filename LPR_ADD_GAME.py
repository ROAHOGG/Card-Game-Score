"""
This file, liverpool rummy add game, will take games of liverpool rummy and add them to the text document for storage
and analysis this file is called from liverpool rummy control.

if completed all the way through returns a dictiary with keys as players in game and values as a list of scores starting
from 0 to 6 as the rounds

if exit midway through form filling will return a int 0 to signify exiting before completion.
"""


def lpr_add_game(player_list):
    # Start out by asking how many players are playing
    print('-------------------------------------------------------------')
    print(' ADDING NEW GAME, TYPE -Q TO STOP ADDING NEW GAME AT ANY TIME')
    print('-------------------------------------------------------------')

    # Sets up a test for if the number of players the user inputs is valid
    user_input_test = True
    while user_input_test:
        # Asks how many players have played
        number_of_players = input('How many players in game? ').upper()
        # If -Q is typed will quit program
        if number_of_players == '-Q':
            print('-----------------------------------------------------')
            print('             STOPPED ADDING NEW GAME')
            print('-----------------------------------------------------')
            return 0
        else:
            # Trys to convert the user input to intiger
            try:
                number_of_players = int(number_of_players)
            except ValueError:
                # If it cant it will ask for a number rather than misc char
                user_input_test = True
                print('Please enter a number, ', end='')
                # Checks to see that more than one player playing
            else:

                if number_of_players <= 1:
                    print('Cant have a solo game, ', end='')
                else:
                    # Ends the loop if everything is good.
                    user_input_test = False
    # Setting up a list of who is playing this game
    player_in_game_list = []
    # Cycle through how many players there are checking if they are players in the system
    for player in range(1, number_of_players + 1):
        player_name_input_test = True
        while player_name_input_test:
            # Getting the user input as to who the players are
            print('Who is player number', player, ': ', end='')
            player_name_input = input().upper()
            # Exiting if the user inputs -Q
            if player_name_input == '-Q':
                print('-----------------------------------------------------')
                print('             STOPPED ADDING NEW GAME')
                print('-----------------------------------------------------')
                return 0
            # Checking the player against the master database fed in the parameters of the function
            elif player_name_input in player_list:
                # Checks if the player is already in the game
                if player_name_input in player_in_game_list:
                    # If player is in master list and in game, allows the user to try again
                    print('Player in game, Try again. ', end='')
                    player_name_input_test = True

                else:
                    # If the use is in the master list and not in the game then this adds them to the game
                    player_in_game_list.append(player_name_input)
                    player_name_input_test = False

            else:
                # If the player is not in the master list
                print('Player not in database, Try again. ', end='')
                player_name_input_test = True

    # Create an empty dictionary to hold scores of the game
    player_score_dictionary = {}
    # For every player in game ask all scores for each stage of the game
    for player in player_in_game_list:
        # create a var to hold if the score was imputed correctly
        correct_score_answer = True
        while correct_score_answer:
            # Adds person to dict and if player is in dict wipes scores for reentry if scores were imputed incorrectly
            player_score_dictionary[player] = []
            print('SCORES FOR PLAYER : ', player)
            for stage in range(1, 8):
                # Create a test for if a number was imputed
                score_input_test = True
                while score_input_test:
                    print('What was', player, '\'s score in round', stage, ': ', end='')
                    score = input().upper()
                    if score == '-Q':
                        print('-----------------------------------------------------')
                        print('             STOPPED ADDING NEW GAME')
                        print('-----------------------------------------------------')
                        return 0
                    else:
                        try:
                            score = int(score)
                        except ValueError:
                            score_input_test = True
                            print('Please enter a number, ', end="")
                        else:
                            player_score_dictionary[player].append(score)
                            score_input_test = False
            print('ARE THESE SCORES FOR', player, 'CORRECT:   Y/N')
            for stage in range(0, 7):
                print('ROUND', stage + 1, ':', player_score_dictionary[player][stage])

            final_score_check = True
            while final_score_check:
                print('ARE THESE SCORES FOR', player, 'CORRECT:   Y/N : ', end='')
                score_answer = input().upper()
                if score_answer == 'Y':
                    correct_score_answer = False
                    final_score_check = False
                elif score_answer == '-Q':
                    print('-----------------------------------------------------')
                    print('             STOPPED ADDING NEW GAME')
                    print('-----------------------------------------------------')
                    return 0
                elif score_answer == 'N':
                    correct_score_answer = True
                    final_score_check = False
                else:
                    print('PLEASE INPUT A VALID RESPONSE ', end='')



    winning_score = 1500
    winner = ''
    # Makes a final entry to the dictionary holding scores with a key of winner showing who won the game.
    for player,  score_list in player_score_dictionary.items():
        total_score = 0
        # Takes the scores of each player and totals them out
        for score in score_list:
            total_score += score
        # Checks if the curent score being totald is less than the lowest others, if it is set the player as 'winner'
        if winning_score > total_score:
            winning_score = total_score
            winner = player
    # Adds the 'winner' key to the dictionary and sets the value as the winner of the game.
    player_score_dictionary['winner'] = winner
    return player_score_dictionary



