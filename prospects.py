import requests

class ProspectsAPI:
    __current = 'ohl'
    __leagues = {
        'ohl': {
            'code': 'ohl',
            'season_ids': [68],
            'key': '2976319eb44abe94'
        },
        'whl': {
            'code': 'whl',
            'season_ids': [270],
            'key': '41b145a848f4bd67'
        },
        'qmjhl': {
            'code': 'lhjmq',
            'season_ids': [193],
            'key': 'f322673b6bcae299'
        },
    }

    @classmethod
    def __url(cls):
        data = cls.__leagues[cls.__current]

        return f"https://lscluster.hockeytech.com/feed/?client_code={data['code']}&key={data['key']}"

    @classmethod
    def set_league(cls, league):
        if league in cls.__leagues:
            cls.__current = league

    @classmethod
    def teams(cls):
        response = requests.get(f'{cls.__url()()}&feed=modulekit&view=teamsbyseason')

        if response.status_code == 200:
            return response.json()['SiteKit']['Teamsbyseason']

        return []

    @classmethod
    def player(cls, player_id):
        return {
            'profile': ProspectsAPI.player_profile(player_id),
            'game_by_game': ProspectsAPI.player_game_by_game_stats(player_id),
            'stats': ProspectsAPI.player_stats(player_id)
        }

    @classmethod
    def player_profile(cls, player_id):
        response = requests.get(f'{cls.__url()}&feed=modulekit&view=player&category=profile&player_id={player_id}')

        if response.status_code == 200:
            return response.json()['SiteKit']['Player']

        return {}

    @classmethod
    def player_game_by_game_stats(cls, player_id):
        response = requests.get(f'{cls.__url()}&feed=modulekit&view=player&category=gamebygame&player_id={player_id}')

        if response.status_code == 200:
            return response.json()['SiteKit']['Player']

        return {}

    @classmethod
    def player_stats(cls, player_id):
        response = requests.get(f'{cls.__url()}&feed=modulekit&view=player&category=seasonstats&player_id={player_id}')

        if response.status_code == 200:
            return response.json()['SiteKit']['Player']

        return {}

    @classmethod
    def schedule(cls):
        response = requests.get(f'{cls.__url()}&feed=modulekit&view=schedule')

        if response.status_code == 200:
            return response.json()['SiteKit']['Schedule']

        return []

    @classmethod
    def game(cls, game_id):
        return {
            'summary': ProspectsAPI.game_summary(game_id),
            'pbp': ProspectsAPI.game_play_by_play(game_id)
        }

    @classmethod
    def game_summary(cls, game_id):
        response = requests.get(f'{cls.__url()}&feed=gc&game_id={game_id}&tab=gamesummary')

        if response.status_code == 200:
            return response.json()['GC']['Gamesummary']

        return {}

    @classmethod
    def game_play_by_play(cls, game_id):
        response = requests.get(f'{cls.__url()}&feed=gc&game_id={game_id}&tab=pxpverbose')

        if response.status_code == 200:
            return response.json()['GC']['Pxpverbose']

        return []

if __name__ == '__main__':
    import code; code.interact(local=dict(globals(), **locals()))
