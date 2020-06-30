import psycopg2
import time

from prospects import ProspectsAPI
from utils import Utils

class ProspectDatabase:

    def __init__(self, user = 'vaism', dbname = "prospects"):
        self.user = user
        self.dbname = dbname
        self.conn = None
        self.cursor = None
        self.create_connection()

    def create_connection(self):
        try:
            self.conn = psycopg2.connect(
                database = self.dbname,
                user = self.user,
            )

            self.cursor = self.conn.cursor()
        except Error as e:
            print(error)

    def seed_data(self):
        self._seed_teams()
        self._seed_game_stats()
        self._seed_players()

    def _seed_teams(self):
        teams = ProspectsAPI.teams()

        for team in teams:
            self.cursor.execute(
                """
                    INSERT into team (team_id, name, city, code, team_logo_url)
                    VALUES (%s, %s, %s, %s, %s);
                """,
                (team['id'], team['name'], team['city'], team['code'], team['team_logo_url'])
            )

        self.conn.commit()

    def _seed_game_stats(self):
        games = ProspectsAPI.schedule()

        for game in games:
            data = ProspectsAPI.game(game['game_id'])

            pbp, game = data['pbp'], data['summary']

            if not pbp:
                continue

            away_players = game['visitor_team_lineup']['players']
            home_players = game['home_team_lineup']['players']

            for index, players in enumerate([away_players, home_players]):
                team_code = game['home']['code'] if index else game['visitor']['code']

                print(f"Adding {game['game_date']} - {game['home']['name']} vs {game['visitor']['name']}")

                for player in players:
                    self.cursor.execute(
                        """
                            INSERT into player_game_by_game_stats (
                                player_id, first_name, last_name, date, goals, assists, points, plus_minus,
                                pim, shots, shots_on_net, faceoffs_won, faceoffs_lost, team, position
                            )
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                        """,
                        (
                            player['player_id'],
                            player['first_name'],
                            player['last_name'],
                            game['game_date_iso_8601'],
                            player['goals'],
                            player['assists'],
                            player['goals'] + player['assists'],
                            player['plusminus'],
                            player['pim'],
                            player['shots'],
                            player['shots_on'],
                            player['faceoff_wins'],
                            int(player['faceoff_attempts']) - int(player['faceoff_wins']),
                            team_code,
                            player['position_str']
                        )
                    )

            self.conn.commit()

    def _seed_players(self):
        self.cursor.execute("SELECT DISTINCT player_id FROM player_game_by_game_stats")

        for player_id in Utils.flatten(self.cursor.fetchall()):
            player = ProspectsAPI.player_profile(player_id)

            if player.get('error'):
                print(f"Error: {player_id} - {player.get('error')}")
                continue

            print(f"Adding player {player['first_name']} {player['last_name']} ({player_id})")

            self.cursor.execute(
                """
                    INSERT into player (
                        player_id, name, first_name, last_name, country, height, birthdate, active, rookie, shoots,
                        weight, position, player_img_url
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """,
                (
                    player_id,
                    f"{player['first_name']} {player['last_name']}",
                    player['first_name'],
                    player['last_name'],
                    player['homecntry'],
                    player['height'][:4],
                    player['birthdate'],
                    player.get('active', '0'),
                    player.get('rookie', '0'),
                    player['shoots'],
                    player['weight'],
                    player['position'],
                    player['primary_image']
                )
            )

            self.conn.commit()

if __name__ == '__main__':
    database = ProspectDatabase()
    database.seed_data()
