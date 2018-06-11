from LPR_PLAYER_CLASS import Player


def lpr_add_player(player_dictionary):
    players = player_dictionary.keys()
    player_creation_test = True

    print('--------------------------------------------------------------')
    print('ADDING NEW PLAYER, TYPE -Q TO STOP ADDING NEW GAME AT ANY TIME')
    print('--------------------------------------------------------------')

    while player_creation_test:
        new_player = input('Who is the new player: ').upper()

        if new_player == '-Q':
            return 0

        elif new_player in players:
            print('Sorry, player exists ')
            player_creation_test = True

        else:
            print('Is the name correct \"', new_player, '\" Y for yes, any key for no : ',  end='')
            player_creation_test_final = input().upper()
            if player_creation_test_final == 'Y':
                player_dictionary[new_player] = Player(new_player)
                return player_dictionary
            if player_creation_test_final == '-Q':
                return 0
