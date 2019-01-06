

class Player(object):
    _players = {}

    @classmethod
    def get_player(cls, name):
        if name not in cls._players:
            cls._players[name] = cls(name)
        return cls._players[name]

    def __init__(self, name):

        self.name = name
        # Averages for the rounds this player has played
        self.round_averages = [0, 0, 0, 0, 0, 0, 0]
        # Total points for this player of each round
        self.round_totals = [0, 0, 0, 0, 0, 0, 0]
        # Total wins that this player has receded in the rounds
        self.round_wins = [0, 0, 0, 0, 0, 0, 0]
        # Largest score of each round that the player has done
        self.round_high_scores = [0, 0, 0, 0, 0, 0, 0]

        self.total_games_played = 0
        self.total_games_won = 0
        self.total_rounds_won = 0
        # Highest scoring game played by player
        self.high_score_game = 0
        # Lowest scoring game by player
        self.low_score_game = 15000
        # Average score of games played by player
        self.games_score_average = 0
        # Total points incurred by the player
        self.total_games_score = 0

    # Creating a method for updating player scores.
    def update_score(self, score_list, game_winner):
        # Adding a game to the games played
        self.total_games_played += 1
        # Creates a local var for round score.
        game_score = 0

        # Iterates through the list of scores and adds them to total round and re-averages them.
        for score_index in range(len(score_list)):
            self.round_totals[score_index] = self.round_totals[score_index] + score_list[score_index]
            self.round_averages[score_index] = self.round_totals[score_index] / self.total_games_played
            game_score += score_list[score_index]

            # Checks if the round was won if so increments the round won counters.
            if score_list[score_index] == 0:
                self.round_wins[score_index] += 1
                self.total_rounds_won += 1

            # Checks to see if this was the highest scoring round the player has had
            if score_list[score_index] > self.round_high_scores[score_index]:
                self.round_high_scores[score_index] = score_list[score_index]

        # Checks if the game was won by the user, if so increments the games won counter.
        if game_winner == self.name:
            self.total_games_won += 1

        # Handles the total game scores and the average game scores
        self.total_games_score += game_score
        self.games_score_average = self.total_games_score / self.total_games_played

        # Handles the high game score updating
        if game_score > self.high_score_game:
            self.high_score_game = game_score

        # Handles the low score game updating
        if game_score < self.low_score_game:
            self.low_score_game = game_score

    def display_player_score(self):
        print('**************************************************')
        print('SCORES FOR', self.name)
        print('')
        for round_index in range(len(self.round_averages)):
            print('ROUND', round_index,  'AVERAGES: {0:12f}  TOTALS: {1:15d}  HIGHS: {2:12f}'.format(self.round_averages
                             [round_index], self.round_totals[round_index], self.round_high_scores[round_index]))

        print()

        for round_index in range(len(self.round_wins)):
            print('ROUND', round_index, 'WINS: ', self.round_wins[round_index])

        print()

        print('TOTAL ROUNDS WON :', self.total_rounds_won)
        print('GAMES WON        :', self.total_games_won)
        print('GAMES PLAYED     :', self.total_games_played)
        print('GAMES AVERAGE    :', self.games_score_average)
        print('GAMES SCORE TOTAL:', self.total_games_score)
        print('GAME HIGH SCORE  :', self.high_score_game)
        print('GAME LOW SCORE   :', self.low_score_game)
        print()
        print('**************************************************')
        print()
