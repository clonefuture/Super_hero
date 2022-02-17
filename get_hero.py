import requests
from pprint import pprint


class Superhero:
    def __init__(self, token):
        self.token = token

    def compare_intelligence(self, super_heroes_lst, power_stat):
        s_heroes = {}
        for heroes in super_heroes_lst:
            uris = f'https://superheroapi.com/api/{token}/search/{heroes}'
            resp = requests.get(uris)
            id_hero = resp.json()['results'][0]['id']
            name = resp.json()['results'][0]['name']
            pwr_stats = resp.json()['results'][0]['powerstats'][power_stat]
            s_heroes[name] = int(pwr_stats)
        max_val = max(s_heroes.values())
        max_intell = {k: v for k, v in s_heroes.items() if v == max_val}
        return print(f'Самый умный - {"".join(max_intell.keys())}')


if __name__ == '__main__':

    super_heroes_lst = ['Hulk', 'Captain America', 'Thanos']
    power_stat = 'intelligence'
    token = '2619421814940190'
    connect = Superhero(token)
    connect.compare_intelligence(super_heroes_lst, power_stat)