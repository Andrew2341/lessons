#import database

class Player:

    def __init__(self, player_id):
        self.player_id = player_id
        self.name = None
        self.gold = None

    def get_data(self):
        # Заммнить на данныь из базы данных
        players = {
            1:{"name":"admin", "lvl":1, "exp":200, "gold":100},
            2:{"name":"tester", "lvl":99, "exp":300, "gold":200}
        }

        if self.player_id in players.keys():
            self.set_data(players[self.player_id])


    def set_data(self, players_data):
        self.name = players_data["name"]
        self.gold = players_data["gold"]
