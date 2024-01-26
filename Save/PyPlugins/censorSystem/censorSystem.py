__title__ = 'censorSystem'
__author__ = 'Coded_Pro'
__version__ = '1.0'

import clr
clr.AddReferenceByPartialName("Fougerite")
import Fougerite

class censorSystem:
    def On_PlayerConnected(self, Player):
        Player.SendCommand("censor.nudity False")

    def On_Command(self, Player, cmd, args):
        if cmd == "dodol" or cmd == "dick" :
            if len(args) == 0:
                Player.MessageFrom("censorSystem", "[color yellow]Bezan: /dodol - /dick on/off")
            elif len(args) == 1:
                if args[0] == "on":
                    Player.SendCommand("censor.nudity False")
                    Player.MessageFrom("censorSystem", "[color lime]Alan Mitoni Dodol/dick Bebini :)")
                elif args[0] == "off":
                    Player.SendCommand("censor.nudity True")
                    Player.MessageFrom("censorSystem", "[color lime]Alan Dige Nemitoni Dodol Bebini :)")
                else:
                    Player.MessageFrom("censorSystem", "[color yellow]Bezan: /dodol-/dick on/off")
            elif len(args) > 1:
                Player.MessageFrom("censorSystem", "[color yellow]Bezan: /dodol-/dick on/off")
