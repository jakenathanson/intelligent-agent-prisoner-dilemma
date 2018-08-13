from gamesimulator.action import Action
from gamesimulator.player import Player

A, B = Action.A, Action.B

# replace instances of 'Template' with your strategy name (this can be whatever you'd like)
class Template(Player):
    """A player who only ever defects.

    Name:
    WUSTL Key (not ID #):
    """

    name = 'Template'


    @staticmethod
    def strategy(opponent: Player) -> Action:
        # right now this code will always choose action B
        return B