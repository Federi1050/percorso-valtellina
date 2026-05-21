# chiede mossa utente
# la manda a Retriver
# -> se json ok
# -> altrimenti errore
# carica su classe apposita: 

from Retriver import Retriver
from OpponentMove import GameState

def play():
    mossa = int(input("inserisci la mossa:\n1 sasso - 2 carta - 3 forbici\n"))
    retr = Retriver()
    risp = None
    if mossa == 1:
        risp = retr.mossa_avversario("rock")
    elif mossa == 2:
        risp = retr.mossa_avversario("paper")
    elif mossa == 3:
        risp = retr.mossa_avversario("scissor")
    else:
        risp = retr.mossa_avversario("ops")

    game = GameState(risp.json())

    # print(game)

    if game.get_is_valido():
        pass
        if game.get_result() == "You Lose":
            pass
            print(
                f"hai giocato {game.get_us().get_name()}, il pc ha giocato {game.get_ai().get_name()}\n"
                f"{game.get_ai().get_name()} batte {game.get_ai().get_beat()}\n"
                f"Hai perso"
            )
        elif game.get_result() == "You Win":
            pass
            print(
                f"hai giocato {game.get_us().get_name()}, il pc ha giocato {game.get_ai().get_name()}\n"
                f"{game.get_us().get_name()} batte {game.get_us().get_beat()}\n"
                f"Hai vinto"
            )
        else:
            pass
            print(
                f"hai giocato {game.get_us().get_name()}, il pc ha giocato {game.get_ai().get_name()}\n"
                f"pareggio"
            )
    else:
        print(risp)

cond = True
while(cond):
    play()

    dom = input("se vuoi smettere di giocare premi 'n' altrimenti premi qualunque altro tasto\n")
    if dom == "n":
        cond = False
