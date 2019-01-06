from LPR_ADD_GAME import lpr_add_game
import csv
import os
from LPR_ADD_PLAYER import lpr_add_player
from LPR_PLAYER_CLASS import Player
from LPR_VIEW_GAMES import lpr_view_game
print('WELCOME TO LIVER POOL RUMMY SCORE KEEPER, TO EXIT TYPE -Q at any point')


user_selection = ''
games_list = []
if os.path.isfile('GAME_SCORES.csv')== True:
    with open('GAME_SCORES.csv') as file:
        for row in csv.DictReader(file, skipinitialspace=True):
            game_dict = {}
            for k, v in row.items():
                if v != '':
                    game_dict[k] = v
            games_list.append(game_dict)
    for game in games_list:
        for key in game:
            if key != 'winner':
                csv_player_scores = [int(x) for x in game[key].replace('[', '').replace(']', '').split(',')]
                Player.get_player(key).update_score(csv_player_scores, game['winner'])

else:
    print('====================================================')
    print('COULD NOT LOAD PLAYER GAMES LIST FILE GAME_SCORE.CSV')
    print('====================================================')
# Start up, load scores into classes, load games into list

while user_selection != '-Q':
    print('MAIN LPR MENU: ')
    print('ADD NEW GAME -N')
    print('ADD PLAYER   -P')
    print('EXIT         -Q')
    print('PLAYER SCORE -S')
    print('GAME SCORES  -G')

    # Adding a new game.
    user_selection = input('WHAT WOULD YOU LIKE TO DO : ').upper()
    if user_selection == '-N':
        new_game_dic = lpr_add_game()
        if new_game_dic != 0:
            games_list.append(new_game_dic)
            for key in new_game_dic.keys():
                if key != 'winner':
                    Player._players[key].update_score(new_game_dic[key], new_game_dic['winner'])

    elif user_selection == '-S':
        print('WHAT PLAYER WOULD YOU LIKE TO PRINT: ')
        user_selection_test = True
        while user_selection_test:
            user_score_selection = input().upper()
            if user_score_selection in Player._players:
                user_selection_test = False
                Player._players[user_score_selection].display_player_score()
            elif user_score_selection == '-Q':
                user_selection_test = False
            else:
                print('USER NOT IN LIST, TRY AGAIN: ')
    # Adding a new player
    elif user_selection == '-P':
        lpr_add_player()

    # Viewing games in the games list
    elif user_selection == '-G':
        lpr_view_game(games_list)

print('EXITING, PLEASE DO NOT SHUT DOWN.')
# Quitting , save to txt file.
with open('GAME_SCORES.csv', 'w') as csvfile:
    fields = ['winner']
    for key in Player._players.keys():
        fields.append(key)

    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    for game_index in range(len(games_list)):
        writer.writerow(games_list[game_index])
