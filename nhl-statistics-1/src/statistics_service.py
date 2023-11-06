from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


class StatisticsService():
    def __init__(self, player_reader):
        reader = player_reader

        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=SortBy.POINTS):
        # metodin käyttämä apufufunktio voidaan määritellä näin

        if sort_by is SortBy.POINTS:
            def sort(player):
                return player.points
        elif sort_by is SortBy.ASSISTS:
            def sort(player):
                return player.assists
        elif sort_by is SortBy.GOALS:
            def sort(player):
                return player.goals

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
