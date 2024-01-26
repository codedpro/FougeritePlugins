__author__ = 'Coded_Pro'
__version__ = '1.0'


import clr
clr.AddReferenceByPartialName("Fougerite")
import Fougerite

blue = "[color #0099FF]"
red = "[color #FF0000]"
pink = "[color #CC66FF]"
teal = "[color #00FFFF]"
green = "[color #009900]"

class Report:

    def On_PluginInit(self):
        self.IniFile()

    def argsToText(self, args):
        text = str.join(" ", args)
        return text

    def Moderator(self, id):
        if DataStore.ContainsKey("Moderators", id):
            return True
        return False

    def IniFile(self):
        if not Plugin.IniExists("MG_ReportedPlayers"):
            ini = Plugin.CreateIni("MG_ReportedPlayers")
            ini.Save()
        return Plugin.GetIni("MG_ReportedPlayers")

    def GetQuoted(self, array, Reporter):
        text = str.join(" ", array)
        if not '"' in text:
            Reporter.MessageFrom('Manager', 'Usage: /report "PlayerName" "message"')
            Reporter.MessageFrom('Manager', 'Quote signs (") are required.')
            return False
        groups = text.split('"')
        n = len(groups)
        list = []
        for x in xrange(0, n):
            if x % 2 != 0:
                list.append(str(groups[x]))
        return list

    def GetPlayerName(self, namee):
        try:
            name = namee.lower()
            for pl in Server.Players:
                if pl.Name.lower() == name:
                    return pl
            return None
        except:
            return None

    def CheckV(self, Player, args):
        systemname = "Manager"
        count = 0
        if hasattr(args, '__len__') and (not isinstance(args, str)):
            p = self.GetPlayerName(str.join(" ", args))
            if p is not None:
                return p
            for pl in Server.Players:
                for namePart in args:
                    if namePart.lower() in pl.Name.lower():
                        p = pl
                        count += 1
                        continue
        else:
            nargs = str(args).lower()
            p = self.GetPlayerName(nargs)
            if p is not None:
                return p
            for pl in Server.Players:
                if nargs in pl.Name.lower():
                    p = pl
                    count += 1
                    continue
        if count == 0:
            Player.MessageFrom(systemname, "Couldn't find [color#00FF00]" + str.join(" ", args) + "[/color]!")
            return None
        elif count == 1 and p is not None:
            return p
        else:
            Player.MessageFrom(systemname, "Found [color#FF0000]" + str(count) + "[/color] player with similar name. [color#FF0000] Use more correct name!")
            return None

    def SaveReportToIni(self, Reporter, ReportedName, Text):
        ini = self.IniFile()
        enum = ini.EnumSection("Reports")
        length = len(enum)
        if length == 0:
            lastreportnumber = 0
        else:
            lastreportnumber = int(enum[length - 1])
        ini.AddSetting("Reports", str(lastreportnumber + 1), "Reporter: " + Reporter.Name + " | Reported:  " + ReportedName + "  | Reason: " + Text)
        ini.Save()

    def On_Command(self, Reporter, cmd, args):
        ini = self.IniFile()
        enum = ini.EnumSection("Reports")
        length = len(enum)
        if cmd == "report":
            if len(args) == 0:
                Reporter.MessageFrom("Report", '/report "Name" "Reason" - Quote signs (") are required.')
                if Reporter.Admin or self.Moderator(Reporter.SteamID):
                    Reporter.MessageFrom("Report", "/report list - List Reports")
                    Reporter.MessageFrom("Report", "/report view - View report.")
                    Reporter.MessageFrom("Report", "/report delete - Mark and Delete report.")
                    Reporter.MessageFrom("Report", "/report deleteall - Delete all")
            else:
                if args[0] == "help":
                    Reporter.MessageFrom("Report", green + "Get420Reported++ " + __version__ + " Made by " + __author__)
                    Reporter.MessageFrom("Report", '/report "Name" "Reason" - Quote signs (") are required.')
                    if Reporter.Admin or self.Moderator(Reporter.SteamID):
                        Reporter.MessageFrom("Report", "/report list - List Reports")
                        Reporter.MessageFrom("Report", "/report view - View report.")
                        Reporter.MessageFrom("Report", "/report delete - Mark and Delete report.")
                        Reporter.MessageFrom("Report", "/report deleteall - Delete all")
                elif args[0] == "list":
                    if not Reporter.Admin and not self.Moderator(Reporter.SteamID):
                        return
                    Reporter.MessageFrom("Report", green + "There are (" + teal + str(length) + green + ") reports atm.")
                    for key in enum:
                        Reporter.MessageFrom("Report", "Ticket: " + key)
                elif args[0] == "view":
                    if not Reporter.Admin and not self.Moderator(Reporter.SteamID):
                        return
                    # cmd args[0] args[1]
                    # /report view id
                    if len(args) == 1:
                        Reporter.MessageFrom("Report", red + "Usage: /report view id")
                        return
                    id = args[1]
                    if not id.isdigit():
                        Reporter.MessageFrom("Report", red + "ID must be a number.")
                        return
                    if not ini.GetSetting("Reports", id) and ini.GetSetting("Reports", id) is None:
                        Reporter.MessageFrom("Report", red + "This report doesn't exist!")
                        return
                    Reason = ini.GetSetting("Reports", id)
                    Reporter.MessageFrom("Report", red + "You are viewing Ticket ID: " + id)
                    Reporter.MessageFrom("Report", green + "Case: " + teal + Reason)
                elif args[0] == "delete":
                    if not Reporter.Admin and not self.Moderator(Reporter.SteamID):
                        return
                    if len(args) == 1:
                        Reporter.MessageFrom("Report", red + "Usage: /report delete id")
                        return
                    id = args[1]
                    if not id.isdigit():
                        Reporter.MessageFrom("Report", red + "ID must be a number.")
                        return
                    ini.DeleteSetting("Reports", id)
                    Reporter.MessageFrom("Report", red + "Case:" + id + " deleted.")
                    ini.Save()
                elif args[0] == "deleteall":
                    if not Reporter.Admin and not self.Moderator(Reporter.SteamID):
                        return
                    for key in enum:
                        ini.DeleteSetting("Reports", key)
                    Reporter.MessageFrom("Report", red + "All cases deleted.")
                    ini.Save()
                else:
                    if len(args) <= 1:
                        Reporter.MessageFrom('Report', 'Usage: /report "PlayerName" "message"')
                        Reporter.MessageFrom('Report', 'Quote signs (") are required.')
                        return
                    array = self.GetQuoted(args, Reporter)
                    if not array:
                        return
                    Reported = self.CheckV(Reporter, array[0])
                    if Reported is None:
                        return
                    self.HandleReport(Reporter, Reported, array[1])

    def HandleReport(self, Reporter, Reported, Message):
        if len(Message) > 47:
            Reporter.MessageFrom("Report", red + "Too long reason. Write It shorter.")
            return
        for player in Server.Players:
            if player.Admin or player.Moderator:
                player.MessageFrom("Report", red + "New report submitted!")
                player.MessageFrom("Report", red + "Check it with the /report view command.")
        Plugin.Log("ReportLogs", "Reporter: " + Reporter.Name + " | " + Reporter.SteamID + " | Reported: " + Reported.Name +
            " | " + Reported.SteamID + " |  Reason: " + Message)
        self.SaveReportToIni(Reporter, Reported.Name, Message)
        Reporter.MessageFrom("Report", red + "Report submitted.")
