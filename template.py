from gamesimulator.action import Action
from gamesimulator.player import Player
import itertools
from functools import lru_cache

A, B = Action.A, Action.B

# replace instances of 'Template' with your strategy name (this can be whatever you'd like)
class jakenathanson(Player):
    """A player who only ever defects.

    Name:
    WUSTL Key (not ID #):
    """

    name = 'jakenathanson'


    @staticmethod
    def strategy(opponent: Player) -> Action:
        # right now this code will always choose action B
        #print(opponent.history)
        def detect_cycle(history, min_size=1, max_size=12, offset=0):
            """Detects cycles in the sequence history.

            Mainly used by hunter strategies.

            Parameters
            ----------
            history: sequence of A and B
                The sequence to look for cycles within
            min_size: int, 1
                The minimum length of the cycle
            max_size: int, 12
            offset: int, 0
                The amount of history to skip initially
            """
            history_tail = history[offset:]
            new_max_size = min(len(history_tail) // 2, max_size)
            for i in range(min_size, new_max_size + 1):
                has_cycle = True
                cycle = tuple(history_tail[:i])
                for j, elem in enumerate(history_tail):
                    if elem != cycle[j % len(cycle)]:
                        has_cycle = False
                        break
                if has_cycle:
                    return cycle
            return None
        #print (len(opponent.history))



        #default to defect
        move = A
        #looking for cycles
        if(detect_cycle(opponent.history, min_size=3, max_size=12, offset=4) != None):
                dcycle = detect_cycle(opponent.history, min_size=3, max_size=15, offset=4)
                lcycle = len(dcycle)
                lhistory= len(opponent.history)
                position = ((lhistory-4) % (lcycle))
                count = 0
                #lets see if this is a cycle of A's bc then this is either tit for tat or grudge
                for x in range(lcycle):
                    if(dcycle[x]==A):
                        count +=1
                if (count==lcycle): #Grudge or tit for tat is in effect lets be nice
                    move = A
                    #print("grudge detected")
                     #Return B
                elif(detect_cycle(opponent.history, min_size=3, max_size=15, offset=4) != None):
                    #print("predicted")
                    #print(len(opponent.history))
                    #print(dcycle)
                    #print(opponent.history[position-1])

                    if(opponent.history[position-1]==A):
                        move = B
                    if(opponent.history[position-1]==B):
                        move = B
                    #move = B
        # lets determine probablitiy that this is a random player
        else:
            a = 0
            b = 0
            if(len(opponent.history)>15):
                move = B


                # for x in range(len(opponent.history)):
                #     if(opponent.history[x]==A):
                #         a +=1
                #     else:
                #         b +=1
                # # I set threshold at 15% difference after 20 because
                # if(abs(1-abs(a/b))<.35):
                #     move = B
                #     print("prob")







                #detect random



                #detectedat = len(opponent.history)
                #detected = True
        #looking for grudge

        #if(opponent)




        #print(detect_cycle(opponent.history, min_size=1, max_size=12, offset=4))
        #print (len(opponent.history))
        return move
