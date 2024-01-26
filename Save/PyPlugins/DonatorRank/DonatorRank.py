# -*- coding: utf-8 -*-
__title__ = 'DonatorRank'
__author__ = 'Coded_Pro'
__version__ = '1.0'
__about__ = "Create VIPs and Donators"
#this is improved version of Donator rank by jakee
import clr
clr.AddReferenceByName("Fougerite")
import System
import Fougerite
import sys
path = Util.GetRootFolder()
sys.path.append(path + "\\Save\\Lib\\")
try:
    import datetime
except ImportError:
    raise ImportError("Missing Extra Libs folder! {DateTime module}")
PSettings = {}
VKIT1 = {}
VKIT2 = {}
DKIT1 = {}
DKIT2 = {}
Vtp = {}
Dtp = {}
UserPerms = {}
blue = "[color #0099FF]"
red = "[color #FF0000]"
red1 = "[color #b30000]"
pink = "[color #CC66FF]"
teal = "[color #00FFFF]"
green = "[color #009900]"
purple = "[color #6600CC]"
white = "[color #FFFFFF]"
yellow = "[color #FFFF00]"     
color1 = "[color #0055ff]"    
abi = "[color #00aaff]"
Sorati1="[color #ff55ff]"
Banafsh1= "[color #aa00ff]"       
Blood = "[color #ffaa00]"
staff = "[color #7CFC00]"
class DonatorRank:
    def On_PluginInit(self):
        Util.ConsoleLog(__title__ + " by " + __author__ + " Version: " + __version__ + " loaded.", False)
        if not Plugin.IniExists("Settings"):
            Plugin.CreateIni("Settings")
            ini = Plugin.GetIni("Settings")
            ini.AddSetting("Settings", "JoinMessages", "true")
            ini.AddSetting("Settings", "LeaveMessages", "true")
            ini.AddSetting("Settings", "ChatPrefix", "true")
            ini.AddSetting("Settings", "OwnerSteamID", "76561197960548575")
            ini.AddSetting("Settings", "HMSteamID", "76561197961063247")         
            ini.AddSetting("Settings", "DevSteamID", "76561197961233431") 
            ini.AddSetting("Settings", "ArmanSteamID", "76561197961251019")   
            ini.AddSetting("Settings", "DeadSteamID", "76561197963861350") 
            ini.AddSetting("Settings", "BloodSteamID", "76561197962357113")       
            ini.AddSetting("Settings", "SwagSteamID", "76561197960497652") 
            ini.AddSetting("Settings", "SajjadSteamID", "76561197962260392") 
            ini.AddSetting("Settings", "OwnerColour", "[color cyan]")
            ini.AddSetting("Settings", "AdminColour", "[color cyan]")
            ini.AddSetting("Settings", "LogTps", "true")
            ini.AddSetting("Settings", "LogBroadcast", "true")
            ini.AddSetting("Settings", ";Below only works with HomeSystem installed", "")
            ini.AddSetting("Settings", "PlayerMaxhomes", "1")
            ini.AddSetting("Settings", "PlayerHomeCooldown", "300")
            ini.AddSetting("Settings", "PlayerHomeTpDelay", "10")
            ini.AddSetting("ModSettings", "ModeratorColour", "[color white]")
            ini.AddSetting("ModSettings", "Maxhomes", "3")
            ini.AddSetting("ModSettings", "HomeCooldown", "300")
            ini.AddSetting("ModSettings", "HomeTpDelay", "10")
            ini.AddSetting("VIPSettings", "VIPColour", "[color white]")
            ini.AddSetting("VIPSettings", "Maxhomes", "2")
            ini.AddSetting("VIPSettings", "HomeCooldown", "200")
            ini.AddSetting("VIPSettings", "HomeTpDelay", "5")
            ini.AddSetting("VIPSettings", "LVL1KitCooldown", "120")
            ini.AddSetting("VIPSettings", "LVL2KitCooldown", "120")
            ini.AddSetting("DonatorSettings", "DonatorColour", "[color white]")
            ini.AddSetting("DonatorSettings", "Maxhomes", "3")
            ini.AddSetting("DonatorSettings", "HomeCooldown", "60")
            ini.AddSetting("DonatorSettings", "HomeTpDelay", "3")
            ini.AddSetting("DonatorSettings", "LVL1KitCooldown", "80")
            ini.AddSetting("DonatorSettings", "LVL2KitCooldown", "80")
            ini.AddSetting("VKIT_Level1", "Inv1", "P250")
            ini.AddSetting("VKIT_Level1", "Qty1", "1")
            ini.AddSetting("VKIT_Level1", "Inv2", "9mm Ammo")
            ini.AddSetting("VKIT_Level1", "Qty2", "50")
            ini.AddSetting("VKIT_Level1", "Inv3", "Leather Helmet")
            ini.AddSetting("VKIT_Level1", "Qty3", "1")
            ini.AddSetting("VKIT_Level1", "Inv4", "Cloth Vest")
            ini.AddSetting("VKIT_Level1", "Qty4", "1")
            ini.AddSetting("VKIT_Level1", "Inv5", "Cloth Pants")
            ini.AddSetting("VKIT_Level1", "Qty5", "1")
            ini.AddSetting("VKIT_Level1", "Inv6", "Leather Boots")
            ini.AddSetting("VKIT_Level1", "Qty6", "1")
            ini.AddSetting("VKIT_Level1", "Inv7", "Large Medkit")
            ini.AddSetting("VKIT_Level1", "Qty7", "3")
            ini.AddSetting("VKIT_Level1", "Inv8", "Small Rations")
            ini.AddSetting("VKIT_Level1", "Qty8", "1")
            ini.AddSetting("VKIT_Level1", "Inv9", "Silencer")
            ini.AddSetting("VKIT_Level1", "Qty9", "1")
            ini.AddSetting("VKIT_Level2", "Inv1", "P250")
            ini.AddSetting("VKIT_Level2", "Qty1", "1")
            ini.AddSetting("VKIT_Level2", "Inv2", "9mm Ammo")
            ini.AddSetting("VKIT_Level2", "Qty2", "50")
            ini.AddSetting("VKIT_Level2", "Inv3", "Leather Helmet")
            ini.AddSetting("VKIT_Level2", "Qty3", "1")
            ini.AddSetting("VKIT_Level2", "Inv4", "Cloth Vest")
            ini.AddSetting("VKIT_Level2", "Qty4", "1")
            ini.AddSetting("VKIT_Level2", "Inv5", "Cloth Pants")
            ini.AddSetting("VKIT_Level2", "Qty5", "1")
            ini.AddSetting("VKIT_Level2", "Inv6", "Leather Boots")
            ini.AddSetting("VKIT_Level2", "Qty6", "1")
            ini.AddSetting("VKIT_Level2", "Inv7", "Large Medkit")
            ini.AddSetting("VKIT_Level2", "Qty7", "3")
            ini.AddSetting("VKIT_Level2", "Inv8", "Small Rations")
            ini.AddSetting("VKIT_Level2", "Qty8", "1")
            ini.AddSetting("VKIT_Level2", "Inv9", "Silencer")
            ini.AddSetting("VKIT_Level2", "Qty9", "1")
            ini.AddSetting("DKIT_Level1", "Inv1", "M4")
            ini.AddSetting("DKIT_Level1", "Qty1", "1")
            ini.AddSetting("DKIT_Level1", "Inv2", "556 Ammo")
            ini.AddSetting("DKIT_Level1", "Qty2", "90")
            ini.AddSetting("DKIT_Level1", "Inv3", "Leather Helmet")
            ini.AddSetting("DKIT_Level1", "Qty3", "1")
            ini.AddSetting("DKIT_Level1", "Inv4", "Leather Vest")
            ini.AddSetting("DKIT_Level1", "Qty4", "1")
            ini.AddSetting("DKIT_Level1", "Inv5", "Leather Pants")
            ini.AddSetting("DKIT_Level1", "Qty5", "1")
            ini.AddSetting("DKIT_Level1", "Inv6", "Leather Boots")
            ini.AddSetting("DKIT_Level1", "Qty6", "1")
            ini.AddSetting("DKIT_Level1", "Inv7", "Silencer")
            ini.AddSetting("DKIT_Level1", "Qty7", "1")
            ini.AddSetting("DKIT_Level1", "Inv8", "Large Medkit")
            ini.AddSetting("DKIT_Level1", "Qty8", "5")
            ini.AddSetting("DKIT_Level1", "Inv9", "Small Rations")
            ini.AddSetting("DKIT_Level1", "Qty9", "10")
            ini.AddSetting("DKIT_Level2", "Inv1", "M4")
            ini.AddSetting("DKIT_Level2", "Qty1", "1")
            ini.AddSetting("DKIT_Level2", "Inv2", "556 Ammo")
            ini.AddSetting("DKIT_Level2", "Qty2", "90")
            ini.AddSetting("DKIT_Level2", "Inv3", "Leather Helmet")
            ini.AddSetting("DKIT_Level2", "Qty3", "1")
            ini.AddSetting("DKIT_Level2", "Inv4", "Leather Vest")
            ini.AddSetting("DKIT_Level2", "Qty4", "1")
            ini.AddSetting("DKIT_Level2", "Inv5", "Leather Pants")
            ini.AddSetting("DKIT_Level2", "Qty5", "1")
            ini.AddSetting("DKIT_Level2", "Inv6", "Leather Boots")
            ini.AddSetting("DKIT_Level2", "Qty6", "1")
            ini.AddSetting("DKIT_Level2", "Inv7", "Silencer")
            ini.AddSetting("DKIT_Level2", "Qty7", "1")
            ini.AddSetting("DKIT_Level2", "Inv8", "Large Medkit")
            ini.AddSetting("DKIT_Level2", "Qty8", "5")
            ini.AddSetting("DKIT_Level2", "Inv9", "Small Rations")
            ini.AddSetting("DKIT_Level2", "Qty9", "10")
            ini.Save()
        if not Plugin.IniExists("TPLocations"):
            Plugin.CreateIni("TPLocations")
            ini = Plugin.GetIni("TPLocations")
            ini.AddSetting("EXAMPLE", ";location name here", "X, Y, Z")
            ini.AddSetting("EXAMPLE", ";ADDING A NEW LOCATION", "Just add the location name plus X/Y/Z location (Add 1 to the Y so players don't glitch into the ground)")
            ini.AddSetting("EXAMPLE", ";COOLDOWNS/DELAYS", "Cooldowns/delays are in seconds")
            ini.AddSetting("EXAMPLE", ";VIP House", "-1000, 450, 200")
            ini.AddSetting("Settings", "VTP Delay", "5")
            ini.AddSetting("Settings", "VTP Cooldown", "30")
            ini.AddSetting("Settings", "DTP Delay", "5")
            ini.AddSetting("Settings", "DTP Cooldown", "30")
            ini.AddSetting("VTP", "Small Rad", "6050, 381, -3620")
            ini.AddSetting("VTP", "Big Rad", "5250, 371, -4850")
            ini.AddSetting("VTP", "Factory Rad", "6300, 361, -4650")
            ini.AddSetting("VTP", "Hanger", "6600, 356, -4400")
            ini.AddSetting("DTP", "Small Rad", "6050, 381, -3620")
            ini.AddSetting("DTP", "Big Rad", "5250, 371, -4850")
            ini.AddSetting("DTP", "Factory Rad", "6300, 361, -4650")
            ini.AddSetting("DTP", "Hanger", "6600, 356, -4400")
            ini.AddSetting("DTP", "Oil Tankers", "6690, 356, -3880")
            ini.AddSetting("DTP", "North Hacker Valley", "5000, 461, -3000")
            ini.AddSetting("DTP", "French Valley", "6056, 385, -4162")
            ini.AddSetting("DTP", "North Next Valley", "4668, 445, -3908")
            ini.Save()
        PSettings.clear()
        VKIT1.clear()
        VKIT2.clear()
        DKIT1.clear()
        DKIT2.clear()
        Vtp.clear()
        Dtp.clear()
        self.UpdatePerms()
        ini = Plugin.GetIni("Settings")
        PSettings["JoinMSG"] = ini.GetBoolSetting("Settings", "JoinMessages")
        PSettings["HMID"] = ini.GetSetting("Settings", "HMSteamID")
        PSettings["LeaveMSG"] = ini.GetBoolSetting("Settings", "LeaveMessages")
        PSettings["ChatPrefix"] = ini.GetBoolSetting("Settings", "ChatPrefix")
        PSettings["OwnerID"] = ini.GetSetting("Settings", "OwnerSteamID")
        PSettings["DevID"] = ini.GetSetting("Settings", "DevSteamID")
        PSettings["ArmanID"] = ini.GetSetting("Settings", "ArmanSteamID")
        PSettings["DeadID"] = ini.GetSetting("Settings", "DeadSteamID")
        PSettings["BloodID"] = ini.GetSetting("Settings", "BloodSteamID")
        PSettings["SwagID"] = ini.GetSetting("Settings", "SwagSteamID")
        PSettings["OwnerColour"] = ini.GetSetting("Settings", "OwnerColour")
        PSettings["AdminColour"] = ini.GetSetting("Settings", "AdminColour")
        PSettings["ModColour"] = ini.GetSetting("ModSettings", "ModeratorColour")
        PSettings["DonatorColour"] = ini.GetSetting("DonatorSettings", "DonatorColour")
        PSettings["VIPColour"] = ini.GetSetting("VIPSettings", "VIPColour")
        PSettings["LogTPS"] = ini.GetBoolSetting("Settings", "LogTps")
        PSettings["LogKicks"] = ini.GetBoolSetting("Settings", "LogKicks")
        PSettings["LogBroadcasts"] = ini.GetBoolSetting("Settings", "LogBroadcast")
        PSettings["PlayerHomesMax"] = self.StrToInt(ini.GetSetting("Settings", "PlayerMaxhomes"), "180")
        PSettings["ModHomesMax"] = ini.GetSetting("ModSettings", "Maxhomes")
        PSettings["DonatorHomesMax"] = ini.GetSetting("DonatorSettings", "Maxhomes")
        PSettings["VIPHomesMax"] = ini.GetSetting("VIPSettings", "Maxhomes")
        PSettings["HomeCoolDown"] = self.StrToInt(ini.GetSetting("Settings", "PlayerHomeCooldown"), "184") * 1000
        PSettings["HomeTpDelay"] = self.StrToInt(ini.GetSetting("Settings", "PlayerHomeTpDelay"), "185")
        PSettings["VHomeCoolDown"] = self.StrToInt(ini.GetSetting("VIPSettings", "HomeCooldown"), "186") * 1000
        PSettings["VHomeTpDelay"] = self.StrToInt(ini.GetSetting("VIPSettings", "HomeTpDelay"), "187")
        PSettings["DHomeCoolDown"] = self.StrToInt(ini.GetSetting("DonatorSettings", "HomeCooldown"), "188") * 1000
        PSettings["DHomeTpDelay"] = self.StrToInt(ini.GetSetting("DonatorSettings", "HomeTpDelay"), "189")
        PSettings["MHomeCoolDown"] = self.StrToInt(ini.GetSetting("ModSettings", "HomeCooldown"), "190") * 1000
        PSettings["MHomeTpDelay"] = self.StrToInt(ini.GetSetting("ModSettings", "HomeTpDelay"), "191")
        PSettings["LVL1DKITCoolDown"] = self.StrToInt(ini.GetSetting("DonatorSettings", "LVL1KitCooldown"), "192") * 1000
        PSettings["LVL1VKITCoolDown"] = self.StrToInt(ini.GetSetting("VIPSettings", "LVL1KitCooldown"), "193") * 1000
        PSettings["LVL2DKITCoolDown"] = self.StrToInt(ini.GetSetting("DonatorSettings", "LVL2KitCooldown"), "194") * 1000
        PSettings["LVL2VKITCoolDown"] = self.StrToInt(ini.GetSetting("VIPSettings", "LVL2KitCooldown"), "195") * 1000
        count = 1
        for key in ini.EnumSection("VKIT_Level1"):
            if "Inv" in key:
                VKIT1[str(count)] = ini.GetSetting("VKIT_Level1", "Inv" + str(count)) + ":" + str(ini.GetSetting("VKIT_Level1", "Qty" + str(count)))
                count += 1
        count = 1
        for key in ini.EnumSection("VKIT_Level2"):
            if "Inv" in key:
                VKIT2[str(count)] = ini.GetSetting("VKIT_Level2", "Inv" + str(count)) + ":" + str(ini.GetSetting("VKIT_Level2", "Qty" + str(count)))
                count += 1
        count = 1
        for key in ini.EnumSection("DKIT_Level1"):
            if "Inv" in key:
                DKIT1[str(count)] = ini.GetSetting("DKIT_Level1", "Inv" + str(count)) + ":" + str(ini.GetSetting("DKIT_Level1", "Qty" + str(count)))
                count += 1
        count = 1
        for key in ini.EnumSection("DKIT_Level2"):
            if "Inv" in key:
                DKIT2[str(count)] = ini.GetSetting("DKIT_Level2", "Inv" + str(count)) + ":" + str(ini.GetSetting("DKIT_Level2", "Qty" + str(count)))
                count += 1
        tp = Plugin.GetIni("TPLocations")
        PSettings["VTPDELAY"] = self.StrToInt(tp.GetSetting("Settings", "VTP Delay"), "217") * 1000
        PSettings["VTPCoolDown"] = self.StrToInt(tp.GetSetting("Settings", "VTP Cooldown"), "218") * 1000
        PSettings["DTPDELAY"] = self.StrToInt(tp.GetSetting("Settings", "DTP Delay"), "219") * 1000
        PSettings["DTPCoolDown"] = self.StrToInt(tp.GetSetting("Settings", "DTP Cooldown"), "220") * 1000
        count = 1
        for key in tp.EnumSection("VTP"):
            Vtp[str(count) + ":" + key] = tp.GetSetting("VTP", key)
            count += 1
        count = 1
        for key in tp.EnumSection("DTP"):
            Dtp[str(count) + ":" + key] = tp.GetSetting("DTP", key)
            count += 1
        
    def On_Command(self, Player, cmd, args):        
        if cmd == "donatorhelp":
            if len(args) == 0:
                rank = self.CheckPerm(Player.SteamID, "Rank")
                if Player.Admin or rank == "VIP" or rank == "Donator" or rank == "Mod":
                    if self.CheckPerm(Player.SteamID, "AddVIPS") or Player.Admin:
                        Player.Message("/vadd [playername] - Add a player as Vip")
                    if self.CheckPerm(Player.SteamID, "AddDonators") or Player.Admin:
                        Player.Message("/dadd [playername] - Add a player as Donator")
                    if self.CheckPerm(Player.SteamID, "AddMods") or Player.Admin:
                        Player.Message("/madd [playername] - Add a player as Mod")
                    if self.CheckPerm(Player.SteamID, "DelVIPS") or Player.Admin:
                        Player.Message("/vdel [playername] - Remove a player as Vip")
                    if self.CheckPerm(Player.SteamID, "DelDonators") or Player.Admin:
                        Player.Message("/ddel [playername] - Remove a player as Donator")
                    if self.CheckPerm(Player.SteamID, "DelMods") or Player.Admin:
                        Player.Message("/mdel [playername] - Remove a player as Mod")
                    if self.CheckPerm(Player.SteamID, "LVL1VKIT") or Player.Admin:
                        Player.Message("/vkit basic - Get the basic VIP kit")
                    if self.CheckPerm(Player.SteamID, "LVL2VKIT") or Player.Admin:
                        Player.Message("/vkit advanced - Get the advanced VIP kit")
                    if self.CheckPerm(Player.SteamID, "LVL1DKIT") or Player.Admin:
                        Player.Message("/dkit basic - Get the basic Donator kit")
                    if self.CheckPerm(Player.SteamID, "LVL2DKIT") or Player.Admin:
                        Player.Message("/dkit advanced - Get the advanced Donator kit")
                    if self.CheckPerm(Player.SteamID, "MODKIT") or Player.Admin:
                        Player.Message("/mkit - Gives you invisible suit + uber items")
                    if self.CheckPerm(Player.SteamID, "VTP") or Player.Admin:
                        Player.Message("/vtp - Teleport to preset locations")
                    if self.CheckPerm(Player.SteamID, "DTP") or Player.Admin:
                        Player.Message("/dtp - Teleport to preset locations")
                    if self.CheckPerm(Player.SteamID, "MTP") or Player.Admin:
                        Player.Message("/mtp [Name] - Teleport to a player")
                        Player.Message("/mtpback - Teleport back to where you were")
                    if self.CheckPerm(Player.SteamID, "UseBroadcast") or Player.Admin:
                        Player.Message("/yell - Tell the server something")
                    if self.CheckPerm(Player.SteamID, "AccessInfo") or Player.Admin:
                        Player.Message("/info [Name] - Get info about a player")
                else:
                    Player.MessageFrom("DonatorRank", "Contact a staff member about becoming a VIP or Donator")
            else:
                Player.Message("Usage: /donatorhelp")
 
        elif cmd == "yell":
            if self.CheckPerm(Player.SteamID, "UseBroadcast") or Player.Admin:
                if args.Length > 0:
                    text = self.argsToText(args)
                    Server.BroadcastFrom("Player Broadcast", text)
                    if PSettings["LogBroadcasts"]:
                        ini = self.getLogIni()
                        date = Plugin.GetDate()
                        time = Plugin.GetTime()
                        ini.AddSetting("BoardCasterLog", date + "|" + time + " || " + Player.Name, Player.SteamID + " said: [" + text + "]")
                        ini.Save()
                    else:
                        return
                else:
                    Player.Message("Usage: /yell [Message]")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "vadd":
            users = self.getUserIni()
            if self.CheckPerm(Player.SteamID, "AddVIPS") or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /vadd [playername]")
                else:
                    vipname = self.CheckV(Player, args)
                    if vipname is not None:
                        if self.isDonator(vipname):
                            Player.Message(vipname.Name + " is a Donator, use /ddel " + vipname.Name)
                        elif self.isMod(vipname):
                            Player.Message(vipname.Name + " is a Moderator, use /mdel " + vipname.Name)
                        elif not self.isVIP(vipname):
                            d = Plugin.GetDate()
                            t = Plugin.GetTime()
                            p = Player.Name
                            users.AddSetting(vipname.SteamID, "UserName", vipname.Name)
                            users.AddSetting(vipname.SteamID, "INFO", "Time: " + t + "||Date: " + d + "||By: " + p)
                            users.AddSetting(vipname.SteamID, "Rank", "VIP")
                            users.AddSetting(vipname.SteamID, "MaxHomes", PSettings["VIPHomesMax"])
                            users.AddSetting(vipname.SteamID, "AddVIPS", "false")
                            users.AddSetting(vipname.SteamID, "AddDonators", "false")
                            users.AddSetting(vipname.SteamID, "AddMods", "false")
                            users.AddSetting(vipname.SteamID, "DelVIPS", "false")
                            users.AddSetting(vipname.SteamID, "DelDonators", "false")
                            users.AddSetting(vipname.SteamID, "DelMods", "false")
                            users.AddSetting(vipname.SteamID, "LVL1VKIT", "true")
                            users.AddSetting(vipname.SteamID, "LVL2VKIT", "true")
                            users.AddSetting(vipname.SteamID, "LVL1DKIT", "false")
                            users.AddSetting(vipname.SteamID, "LVL2DKIT", "false")
                            users.AddSetting(vipname.SteamID, "MODKIT", "false")
                            users.AddSetting(vipname.SteamID, "VTP", "true")
                            users.AddSetting(vipname.SteamID, "DTP", "false")
                            users.AddSetting(vipname.SteamID, "MTP", "false")
                            users.AddSetting(vipname.SteamID, "UseBroadcast", "true")
                            users.AddSetting(vipname.SteamID, "AccessInfo", "false")
                            users.Save()
                            self.UpdatePerms()
                            Server.Broadcast("[color#FFFF00]" + vipname.Name + " [color#FFFFFF]is now a VIP!")
                            vipname.Message("Use /donatorhelp to show the command list available for you.")
                        else:
                            Player.Message(vipname.Name + " is already a VIP.")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "dadd":
            users = self.getUserIni()
            if self.CheckPerm(Player.SteamID, "AddDonators") or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /dadd [playername]")
                else:
                    donname = self.CheckV(Player, args)
                    if donname is not None:
                        if self.isVIP(donname):
                            Player.Message(donname.Name + " is a VIP, use /vdel " + donname.Name)
                        elif self.isMod(donname):
                            Player.Message(donname.Name + " is a Moderator, use /mdel " + donname.Name)
                        elif not self.isDonator(donname):
                            d = Plugin.GetDate()
                            t = Plugin.GetTime()
                            p = Player.Name
                            users.AddSetting(donname.SteamID, "UserName", donname.Name)
                            users.AddSetting(donname.SteamID, "INFO", "Time: " + t + "||Date: " + d + "||By: " + p)
                            users.AddSetting(donname.SteamID, "Rank", "Donator")
                            users.AddSetting(donname.SteamID, "MaxHomes", PSettings["DonatorHomesMax"])
                            users.AddSetting(donname.SteamID, "AddVIPS", "false")
                            users.AddSetting(donname.SteamID, "AddDonators", "false")
                            users.AddSetting(donname.SteamID, "AddMods", "false")
                            users.AddSetting(donname.SteamID, "DelVIPS", "false")
                            users.AddSetting(donname.SteamID, "DelDonators", "false")
                            users.AddSetting(donname.SteamID, "DelMods", "false")
                            users.AddSetting(donname.SteamID, "LVL1VKIT", "false")
                            users.AddSetting(donname.SteamID, "LVL2VKIT", "false")
                            users.AddSetting(donname.SteamID, "LVL1DKIT", "true")
                            users.AddSetting(donname.SteamID, "LVL2DKIT", "true")
                            users.AddSetting(donname.SteamID, "MODKIT", "false")
                            users.AddSetting(donname.SteamID, "VTP", "false")
                            users.AddSetting(donname.SteamID, "DTP", "true")
                            users.AddSetting(donname.SteamID, "MTP", "false")
                            users.AddSetting(donname.SteamID, "UseBroadcast", "true")
                            users.AddSetting(donname.SteamID, "AccessInfo", "false")
                            users.Save()
                            self.UpdatePerms()
                            Server.Broadcast("[color#FFFF00]" + donname.Name + " [color#FFFFFF]is now a Donator!")
                            donname.Message("Use /donatorhelp to show the command list available for you.")
                        else:
                            Player.Message(donname.Name + " is already a Donator")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "madd":
            users = self.getUserIni()
            if self.CheckPerm(Player.SteamID, "AddMods") or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /madd [playername]")
                else:
                    modname = self.CheckV(Player, args)
                    if modname is not None:
                        if self.isVIP(modname):
                            Player.Message(modname.Name + " is a VIP, use /vdel " + modname.Name)
                        elif self.isDonator(modname):
                            Player.Message(modname.Name + " is a Donator, use /ddel " + modname.Name)
                        elif not self.isMod(modname):
                            d = Plugin.GetDate()
                            t = Plugin.GetTime()
                            p = Player.Name
                            users.AddSetting(modname.SteamID, "UserName", modname.Name)
                            users.AddSetting(modname.SteamID, "INFO", "Time: " + t + "||Date: " + d + "||By: " + p)
                            users.AddSetting(modname.SteamID, "Rank", "Mod")
                            users.AddSetting(modname.SteamID, "MaxHomes", PSettings["ModHomesMax"])
                            users.AddSetting(modname.SteamID, "AddVIPS", "true")
                            users.AddSetting(modname.SteamID, "AddDonators", "true")
                            users.AddSetting(modname.SteamID, "AddMods", "false")
                            users.AddSetting(modname.SteamID, "DelVIPS", "true")
                            users.AddSetting(modname.SteamID, "DelDonators", "true")
                            users.AddSetting(modname.SteamID, "DelMods", "false")
                            users.AddSetting(modname.SteamID, "LVL1VKIT", "false")
                            users.AddSetting(modname.SteamID, "LVL2VKIT", "false")
                            users.AddSetting(modname.SteamID, "LVL1DKIT", "false")
                            users.AddSetting(modname.SteamID, "LVL2DKIT", "false")
                            users.AddSetting(modname.SteamID, "MODKIT", "true")
                            users.AddSetting(modname.SteamID, "VTP", "false")
                            users.AddSetting(modname.SteamID, "DTP", "false")
                            users.AddSetting(modname.SteamID, "MTP", "true")
                            users.AddSetting(modname.SteamID, "UseBroadcast", "true")
                            users.AddSetting(modname.SteamID, "AccessInfo", "true")
                            users.Save()
                            self.UpdatePerms()
                            Server.Broadcast("[color#FFFF00]" + modname.Name + " [color#FFFFFF]is now a Moderator!")
                            modname.Message("Use /donatorhelp to show the command list available for you.")
                        else:
                            Player.Message(modname.Name + " is already a Moderator")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "vdel":
            users = self.getUserIni()
            if self.CheckPerm(Player.SteamID, "DelVIPS") or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /vdel [playername]")
                else:
                    vipname = self.CheckV(Player, args)
                    if vipname is not None:
                        if self.isDonator(vipname):
                            Player.Message(vipname.Name + " is a Donator, use /ddel " + vipname.Name)
                        elif self.isMod(vipname):
                            Player.Message(vipname.Name + " is a Moderator, use /mdel " + vipname.Name)
                        else:
                            users.DeleteSetting(vipname.SteamID, "UserName")
                            users.DeleteSetting(vipname.SteamID, "INFO")
                            users.DeleteSetting(vipname.SteamID, "Rank")
                            users.DeleteSetting(vipname.SteamID, "MaxHomes")
                            users.DeleteSetting(vipname.SteamID, "AddVIPS")
                            users.DeleteSetting(vipname.SteamID, "AddDonators")
                            users.DeleteSetting(vipname.SteamID, "AddMods")
                            users.DeleteSetting(vipname.SteamID, "DelVIPS")
                            users.DeleteSetting(vipname.SteamID, "DelDonators")
                            users.DeleteSetting(vipname.SteamID, "DelMods")
                            users.DeleteSetting(vipname.SteamID, "LVL1VKIT")
                            users.DeleteSetting(vipname.SteamID, "LVL2VKIT")
                            users.DeleteSetting(vipname.SteamID, "LVL1DKIT")
                            users.DeleteSetting(vipname.SteamID, "LVL2DKIT")
                            users.DeleteSetting(vipname.SteamID, "MODKIT")
                            users.DeleteSetting(vipname.SteamID, "VTP")
                            users.DeleteSetting(vipname.SteamID, "DTP")
                            users.DeleteSetting(vipname.SteamID, "MTP")
                            users.DeleteSetting(vipname.SteamID, "UseBroadcast")
                            users.DeleteSetting(vipname.SteamID, "AccessInfo")
                            users.Save()
                            self.UpdatePerms()
                            Player.Message(vipname.Name + " is no longer a VIP")
                            vipname.Message("You are not longer a VIP")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "ddel":
            users = self.getUserIni()
            if self.CheckPerm(Player.SteamID, "DelDonators") or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /ddel [playername]")
                else:
                    donname = self.CheckV(Player, args)
                    if donname is not None:
                        if self.isVIP(donname):
                            Player.Message(donname.Name + " is a VIP, use /vdel " + donname.Name)
                        elif self.isMod(donname):
                            Player.Message(donname.Name + " is a Moderator, use /mdel " + donname.Name)
                        else:
                            users.DeleteSetting(donname.SteamID, "UserName")
                            users.DeleteSetting(donname.SteamID, "INFO")
                            users.DeleteSetting(donname.SteamID, "Rank")
                            users.DeleteSetting(donname.SteamID, "MaxHomes")
                            users.DeleteSetting(donname.SteamID, "AddVIPS")
                            users.DeleteSetting(donname.SteamID, "AddDonators")
                            users.DeleteSetting(donname.SteamID, "AddMods")
                            users.DeleteSetting(donname.SteamID, "DelVIPS")
                            users.DeleteSetting(donname.SteamID, "DelDonators")
                            users.DeleteSetting(donname.SteamID, "DelMods")
                            users.DeleteSetting(donname.SteamID, "LVL1VKIT")
                            users.DeleteSetting(donname.SteamID, "LVL2VKIT")
                            users.DeleteSetting(donname.SteamID, "LVL1DKIT")
                            users.DeleteSetting(donname.SteamID, "LVL2DKIT")
                            users.DeleteSetting(donname.SteamID, "MODKIT")
                            users.DeleteSetting(donname.SteamID, "VTP")
                            users.DeleteSetting(donname.SteamID, "DTP")
                            users.DeleteSetting(donname.SteamID, "MTP")
                            users.DeleteSetting(donname.SteamID, "UseBroadcast")
                            users.DeleteSetting(donname.SteamID, "AccessInfo")
                            users.Save()
                            self.UpdatePerms()
                            Player.Message(donname.Name + " is no longer a Donator")
                            donname.Message("you are no longer a Donator")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "mdel":
            users = self.getUserIni()
            if self.CheckPerm(Player.SteamID, "DelMods") or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /mdel [playername]")
                else:
                    modname = self.CheckV(Player, args)
                    if modname is not None:
                        if self.isVIP(modname):
                            Player.Message(modname.Name + " is a VIP, use /vdel " + modname.Name)
                        elif self.isDonator(modname):
                            Player.Message(modname.Name + " is a Donator, use /ddel " + modname.Name)
                        else:
                            users.DeleteSetting(modname.SteamID, "UserName")
                            users.DeleteSetting(modname.SteamID, "INFO")
                            users.DeleteSetting(modname.SteamID, "Rank")
                            users.DeleteSetting(modname.SteamID, "MaxHomes")
                            users.DeleteSetting(modname.SteamID, "AddVIPS")
                            users.DeleteSetting(modname.SteamID, "AddDonators")
                            users.DeleteSetting(modname.SteamID, "AddMods")
                            users.DeleteSetting(modname.SteamID, "DelVIPS")
                            users.DeleteSetting(modname.SteamID, "DelDonators")
                            users.DeleteSetting(modname.SteamID, "DelMods")
                            users.DeleteSetting(modname.SteamID, "LVL1VKIT")
                            users.DeleteSetting(modname.SteamID, "LVL2VKIT")
                            users.DeleteSetting(modname.SteamID, "LVL1DKIT")
                            users.DeleteSetting(modname.SteamID, "LVL2DKIT")
                            users.DeleteSetting(modname.SteamID, "MODKIT")
                            users.DeleteSetting(modname.SteamID, "VTP")
                            users.DeleteSetting(modname.SteamID, "DTP")
                            users.DeleteSetting(modname.SteamID, "MTP")
                            users.DeleteSetting(modname.SteamID, "UseBroadcast")
                            users.DeleteSetting(modname.SteamID, "AccessInfo")
                            users.Save()
                            self.UpdatePerms()
                            Player.Message(modname.Name + " is no longer a Moderator")
                            modname.Message("You are no longer a Moderator")
            else:
                Player.Message("You don't have permission to use this command!")

        elif cmd == "vkit":
            if len(args) == 0:
                if self.CheckPerm(Player.SteamID, "LVL1VKIT") and self.CheckPerm(Player.SteamID, "LVL2VKIT") or Player.Admin:
                    Player.Message("Usage: /vkit [basic / advanced]")
                elif self.CheckPerm(Player.SteamID, "LVL1VKIT"):
                    Player.Message("Usage: /dkit basic")
                elif self.CheckPerm(Player.SteamID, "LVL2VKIT"):
                    Player.Message("Usage: /dkit advanced")
                else:
                    Player.Message("You don't have permission to use this command!")
            elif len(args) == 1:
                if args[0] == "basic":
                    if self.CheckPerm(Player.SteamID, "LVL1VKIT") or Player.Admin:
                        count = len(VKIT1)
                        if Player.Inventory.FreeSlots <= count:
                            Player.Message("You need atleast " + str(count) + " free spaces!")
                        else:
                            waittime = PSettings["LVL1VKITCoolDown"]
                            time = DataStore.Get("LVL1VKitCooldown", Player.SteamID)
                            try:
                                time = int(time)
                            except:
                                time = 0
                            calc = System.Environment.TickCount - time
                            if calc >= 120 or Player.Admin:
                                for key in sorted(VKIT1.keys()):
                                    item = VKIT1[key].split(":")
                                    Player.Inventory.AddItem(item[0], int(item[1]))
                                DataStore.Add("LVL1VKitCooldown", Player.SteamID, System.Environment.TickCount)
                                Player.Notice("You have redeemed kit: VIPKit Basic")
                            else:
                                Player.Message("Time remaining: " + str(datetime.timedelta(0, (waittime / 1000) - (calc / 1000))))
                    else:
                        Player.Message("You don't have permission to use this command!")
                elif args[0] == "advanced":
                    if self.CheckPerm(Player.SteamID, "LVL2VKIT") or Player.Admin:
                        count = len(VKIT2)
                        if Player.Inventory.FreeSlots <= count:
                            Player.Message("You need atleast " + str(count) + " free spaces!")
                        else:
                            waittime = PSettings["LVL2VKITCoolDown"]
                            time = DataStore.Get("LVL2VKitCooldown", Player.SteamID)
                            try:
                                time = int(time)
                            except:
                                time = 0
                            calc = System.Environment.TickCount - time
                            if calc >= waittime or Player.Admin or time == 0:
                                for key in sorted(VKIT2.keys()):
                                    item = VKIT2[key].split(":")
                                    Player.Inventory.AddItem(item[0], int(item[1]))
                                DataStore.Add("LVL2VKitCooldown", Player.SteamID, System.Environment.TickCount)
                                Player.Notice("You have redeemed kit: VIPKit Advanced")
                            else:
                                Player.Message("Time remaining: " + str(datetime.timedelta(0, (waittime / 1000) - (calc / 1000))))
                    else:
                        Player.Message("You don't have permission to use this command!")
 
        elif cmd == "dkit":
            if len(args) == 0:
                if self.CheckPerm(Player.SteamID, "LVL1DKIT") and self.CheckPerm(Player.SteamID, "LVL2DKIT") or Player.Admin:
                    Player.Message("Usage: /dkit [basic / advanced]")
                elif self.CheckPerm(Player.SteamID, "LVL1DKIT"):
                    Player.Message("Usage: /dkit basic")
                elif self.CheckPerm(Player.SteamID, "LVL2DKIT"):
                    Player.Message("Usage: /dkit advanced")
                else:
                    Player.Message("You don't have permission to use this command!")
            elif len(args) == 1:
                if args[0] == "basic":
                    if self.CheckPerm(Player.SteamID, "LVL1DKIT") or Player.Admin:
                        count = len(DKIT1)
                        if Player.Inventory.FreeSlots <= count:
                            Player.Message("You need atleast " + str(count) + " free spaces!")
                        else:
                            waittime = PSettings["LVL1DKITCoolDown"]
                            time = DataStore.Get("LVL1DKitCooldown", Player.SteamID)
                            try:
                                time = int(time)
                            except:
                                time = 0
                            calc = System.Environment.TickCount - int(time)
                            if calc >= waittime or Player.Admin or time == 0:
                                for key in sorted(DKIT1.keys()):
                                    item = DKIT1[key].split(":")
                                    Player.Inventory.AddItem(item[0], int(item[1]))
                                DataStore.Add("LVL1DKitCooldown", Player.SteamID, System.Environment.TickCount)
                                Player.Notice("You have redeemed kit: DonatorKit Basic")
                            else:
                                Player.Message("Time remaining: " + str(datetime.timedelta(0, (waittime / 1000) - (calc / 1000))))
                    else:
                        Player.Message("You don't have permission to use this command!")
                elif args[0] == "advanced":
                    if self.CheckPerm(Player.SteamID, "LVL2DKIT") or Player.Admin:
                        count = len(DKIT2)
                        if Player.Inventory.FreeSlots <= count:
                            Player.Message("You need atleast " + str(count) + " free spaces!")
                        else:
                            waittime = PSettings["LVL2DKITCoolDown"]
                            time = DataStore.Get("LVL2DKitCooldown", Player.SteamID)
                            try:
                                time = int(time)
                            except:
                                time = 0
                            calc = System.Environment.TickCount - time
                            if calc >= waittime or Player.Admin or time == 0:
                                for key in sorted(DKIT2.keys()):
                                    item = DKIT2[key].split(":")
                                    Player.Inventory.AddItem(item[0], int(item[1]))
                                DataStore.Add("LVL2DKitCooldown", Player.SteamID, System.Environment.TickCount)
                                Player.Notice("You have redeemed kit: DonatorKit Advanced")
                            else:
                                Player.Message("Time remaining: " + str(datetime.timedelta(0, (waittime / 1000) - (calc / 1000))))
                    else:
                        Player.Message("You don't have permission to use this command!")
 
        elif cmd == "mkit":
            if self.CheckPerm(Player.SteamID, "MODKIT") or Player.Admin:
                if len(args) == 0:
                    if Player.Inventory.FreeSlots < 4:
                        Player.Message("You need atleast 4 spots free!")
                    else:
                        Player.Inventory.RemoveItem(36)
                        Player.Inventory.RemoveItem(37)
                        Player.Inventory.RemoveItem(38)
                        Player.Inventory.RemoveItem(39)
                        Player.Inventory.AddItemTo("Invisible Helmet", 36, 1)
                        Player.Inventory.AddItemTo("Invisible Vest", 37, 1)
                        Player.Inventory.AddItemTo("Invisible Pants", 38, 1)
                        Player.Inventory.AddItemTo("Invisible Boots", 39, 1)
                        Player.Inventory.AddItem("Uber Hatchet", 1)
                        Player.Inventory.AddItem("Uber Hunting Bow", 1)
                        Player.Inventory.AddItem("Arrow", 20)
                        Player.Inventory.AddItem("Small Rations", 5)
                        Player.Message("You are now invisible!")
                else:
                    Player.Message("Usage: /mkit")
            else:
                Player.Message("You don't have permission to use this command!")

        elif cmd == "vtp":
            if self.CheckPerm(Player.SteamID, "VTP") or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /vtp [Number]")
                    for key in sorted(Vtp.keys()):
                        key = key.split(":")
                        Player.Message(key[0] + ") - " + key[1])
                elif len(args) == 1:
                    waittime = PSettings["VTPCoolDown"]
                    time = DataStore.Get("VTPCooldown", Player.SteamID)
                    try:
                        time = int(time)
                    except:
                        time = 0
                    calc = System.Environment.TickCount - time
                    if 1 >= 0 or Player.Admin:
                        locname = None
                        dictname = None
                        count = 1
                        for key in sorted(Vtp.keys()):
                            cutname = key.split(":")
                            if cutname[0] == args[0]:
                                locname = cutname[1]
                                dictname = key
                            else:
                                count += 1
                        if locname is not None:
                            delay = PSettings["VTPDELAY"]
                            Data = Plugin.CreateDict()
                            Data["Player"] = Player
                            Data["LocationName"] = locname
                            Data["Location"] = Vtp[dictname].split(",")
                            Data["Health"] = Player.Health
                            Data["Type"] = "VTPCooldown"
                            Plugin.CreateParallelTimer("TeleportDelay", int(delay), Data).Start()
                            Player.Message("Teleporting to " + locname + " in " + str(delay / 1000) + " seconds.")
                        else:
                            Player.Message("Usage: /vtp [Number]")
                    else:
                        Player.Message("Time remaining: " + str(datetime.timedelta(0, (waittime / 1000) - (calc / 1000))))
                else:
                    Player.Message("Usage: /vtp [Number]")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "dtp":
            if self.CheckPerm(Player.SteamID, "DTP") or Player.Admin:
                if len(args) == 0:
                    Player.Message("Usage: /dtp [Number]")
                    for key in sorted(Dtp.keys()):
                        key = key.split(":")
                        Player.Message(key[0] + ") - " + key[1])
                elif len(args) == 1:
                    waittime = PSettings["DTPCoolDown"]
                    time = DataStore.Get("DTPCooldown", Player.SteamID)
                    try:
                        time = int(time)
                    except:
                        time = 0
                    calc = System.Environment.TickCount - time
                    if 1 >= 0 or Player.Admin:
                        locname = None
                        dictname = None
                        count = 1
                        for key in sorted(Dtp.keys()):
                            cutname = key.split(":")
                            if cutname[0] == args[0]:
                                locname = cutname[1]
                                dictname = key
                            else:
                                count += 1
                        if locname is not None:
                            delay = PSettings["DTPDELAY"]
                            Data = Plugin.CreateDict()
                            Data["Player"] = Player
                            Data["LocationName"] = locname
                            Data["Location"] = Dtp[dictname].split(",")
                            Data["Health"] = Player.Health
                            Data["Type"] = "DTPCooldown"
                            Plugin.CreateParallelTimer("TeleportDelay", int(delay), Data).Start()
                            Player.Message("Teleporting to " + locname + " in " + str(delay / 1000) + " seconds.")
                        else:
                            Player.Message("Usage: /dtp [Number]")
                    else:
                        Player.Message("Time remaining: " + str(datetime.timedelta(0, (waittime / 1000) - (calc / 1000))))
                else:
                    Player.Message("Usage: /dtp [Number]")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "mtp":
            if self.CheckPerm(Player.SteamID, "MTP") or Player.Admin: 
                if len(args) > 0:
                    targetname = self.CheckV(Player, args)
                    if targetname is not None:
                        if not DataStore.ContainsKey("MODLOCATION", Player.SteamID):
                            DataStore.Add("MODLOCATION", Player.SteamID, Player.Location)
                        targetname.Notice(Player.Name + " has teleported to you!")
                        Player.TeleportTo(targetname, float(1.5), False)
                        Player.Message("Teleported to: " + targetname.Name)
                        Player.Message("To teleport back to where you were, Type /mtpback")
                        if PSettings["LogTPS"] == "true":
                            ini = self.getLogIni()
                            date = Plugin.GetDate()
                            tym = Plugin.GetTime()
                            ini.AddSetting("TPLog", date + "| " + tym + " || " + Player.Name + " Teleported to: " + targetname.Name, targetname.SteamID)
                            ini.Save()
                        else:
                            return
                    else:
                        return
                else:
                    Player.Message("Usage: /mtp [Player Name]")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "mtpback":
            if self.CheckPerm(Player.SteamID, "MTP") or Player.Admin:
                if DataStore.Get("MODLOCATION", Player.SteamID):
                    plocation = DataStore.Get("MODLOCATION", Player.SteamID)
                    Player.TeleportTo(plocation, False)
                    Player.Message("You have been teleported back to your orignal position")
                    DataStore.Remove("MODLOCATION", Player.SteamID)
                else:
                    Player.Message("You have no last locations")
            else:
                Player.Message("You don't have permission to use this command!")
 
        elif cmd == "info":
            if self.CheckPerm(Player.SteamID, "AccessInfo") or Player.Admin:
                if len(args) > 0:
                    target = self.CheckV(Player, args)
                    if target is not None:
                        Player.Message("Info about [color cyan]" + target.Name)
                        Player.Message("IP: [color cyan]" + target.IP)
                        Player.Message("SteamID: [color cyan]" + target.SteamID)
                        Player.Message("Ping: [color cyan]" + str(target.Ping))
                        Player.Message("Health: [color cyan]" + str(target.Health))
                        Player.Message("Time Online: [color cyan]" + str(target.TimeOnline)[:-3] + "[color white] seconds")
                        Player.Message("At home: [color cyan]" + str(target.AtHome))
                        if Server.HasRustPP:
                            RustPP = Server.GetRustPPAPI()
                            Player.Message("Is muted: [color cyan]" + str(RustPP.IsMuted(long(target.SteamID))))
                            Player.Message("Has Godmode: [color cyan]" + str(RustPP.HasGod(long(target.SteamID))))
                        else:
                            return
                    else:
                        return
                else:
                    Player.Message("usage: /info [name]")
            else:
                Player.Message("You don't have permission to use this command!")

    def TeleportDelayCallback(self, timer):
        timer.Kill()
        Data = timer.Args
        Player = Data["Player"]
        if Data["Health"] <= Player.Health:
            locname = Data["LocationName"]
            loc = Data["Location"]
            Player.TeleportTo(float(loc[0]), float(loc[1]), float(loc[2]), False)
            Player.InventoryNotice(locname)
            DataStore.Add(Data["Type"], Player.SteamID, System.Environment.TickCount)
        else:
            Player.Message("You have been hurt, Failed to teleport!")

    def UpdatePerms(self):
        UserPerms.clear()
        users = self.getUserIni()
        usercount = 0
        for steamid in users.Sections:
            usercount += 1
            for setting in users.EnumSection(steamid):
                value = users.GetSetting(steamid, setting)
                if value == "true" or value == "True":
                    UserPerms[steamid + ":" + setting] = True
                elif value == "false" or value == "False":
                    UserPerms[steamid + ":" + setting] = False
                else:
                    UserPerms[steamid + ":" + setting] = value
        Fougerite.Logger.LogWarning("DonatorRank: Found and loaded " + str(usercount) + " VIP/Donator users successfully!")

    def CheckPerm(self, ID, Perm):
        try:
            if UserPerms.has_key(ID + ":" + Perm):
                permission = UserPerms[ID + ":" + Perm]
                return permission
            else:
                return False
        except:
            return False

    def AddData(self, Player):
        try:
            if UserPerms.has_key(Player.SteamID + ":" + "MaxHomes"):
                DataStore.Add("DonatorRank-MaxHomes", Player.SteamID, self.StrToInt(UserPerms[Player.SteamID + ":" + "MaxHomes"], "881"))
            else:
                DataStore.Add("DonatorRank-MaxHomes", Player.SteamID, PSettings["PlayerHomesMax"])
            if Player.SteamID == PSettings["OwnerID"]:
                DataStore.Add("DonatorRank-Cooldown", Player.SteamID, PSettings["MHomeCoolDown"])
                DataStore.Add("DonatorRank-TpDelay", Player.SteamID, PSettings["MHomeTpDelay"])
            elif Player.Admin:
                DataStore.Add("DonatorRank-Cooldown", Player.SteamID, PSettings["MHomeCoolDown"])
                DataStore.Add("DonatorRank-TpDelay", Player.SteamID, PSettings["MHomeTpDelay"])
            elif self.isMod(Player):
                DataStore.Add("DonatorRank-Cooldown", Player.SteamID, PSettings["MHomeCoolDown"])
                DataStore.Add("DonatorRank-TpDelay", Player.SteamID, PSettings["MHomeTpDelay"])
            elif self.isDonator(Player):
                DataStore.Add("DonatorRank-Cooldown", Player.SteamID, PSettings["DHomeCoolDown"])
                DataStore.Add("DonatorRank-TpDelay", Player.SteamID, PSettings["DHomeTpDelay"])
            elif self.isVIP(Player):
                DataStore.Add("DonatorRank-Cooldown", Player.SteamID, PSettings["VHomeCoolDown"])
                DataStore.Add("DonatorRank-TpDelay", Player.SteamID, PSettings["VHomeTpDelay"])
            else:
                DataStore.Add("DonatorRank-Cooldown", Player.SteamID, PSettings["HomeCoolDown"])
                DataStore.Add("DonatorRank-TpDelay", Player.SteamID, PSettings["HomeTpDelay"])
        except:
            DataStore.Add("DonatorRank-MaxHomes", Player.SteamID, PSettings["PlayerHomesMax"])
            DataStore.Add("DonatorRank-Cooldown", Player.SteamID, PSettings["HomeCoolDown"])
            DataStore.Add("DonatorRank-TpDelay", Player.SteamID, PSettings["HomeTpDelay"])

    def DelData(self, Player):
        try:
            DataStore.Remove("DonatorRank-MaxHomes", Player.SteamID)
            DataStore.Remove("DonatorRank-Cooldown", Player.SteamID)
            DataStore.Remove("DonatorRank-TpDelay", Player.SteamID)
            DataStore.Remove("MaxHomes", Player.SteamID)
            DataStore.Remove("MODLOCATION", Player.SteamID)
        except:
            pass

    def On_PlayerConnected(self, Player):
        self.AddData(Player)
        try:
            if PSettings["JoinMSG"]:
                if Player.SteamID == PSettings["OwnerID"]:
                    Server.BroadcastFrom("Owner", Player.Name + " is now Online.")
                elif Player.Admin:
                    Server.BroadcastFrom("WelCome",color1 + "The Player ☾" + abi + Player.Name + color1 + "☽ Has Join The Server.")
                elif self.isMod(Player):
                    Server.BroadcastFrom("WelCome",color1 + "The Player ☾" + abi + Player.Name + color1 + "☽ Has Join The Server.")
                elif self.isDonator(Player):
                    Server.BroadcastFrom("WelCome",color1 + "The Player ☾" + abi + Player.Name + color1 + "☽ Has Join The Server.")
                elif self.isVIP(Player):
                    Server.BroadcastFrom("WelCome",color1 + "The Player ☾" + abi + Player.Name + color1 + "☽ Has Join The Server.")
                else:
                    Server.BroadcastFrom("WelCome",color1 + "The Player ☾" + abi + Player.Name + color1 + "☽ Has Join The Server.")

        except:
            Fougerite.Logger.LogError("DonatorRank: Failed displaying welcome message!")
            pass
 
    def On_PlayerDisconnected(self, Player):
        self.DelData(Player)
        try:
            if PSettings["LeaveMSG"]:
                if Player.SteamID == PSettings["HMID"]:
                    Server.BroadcastFrom("Owner", Player.Name + " is now Offline.")
                elif Player.Admin:
                    Server.Broadcast(color1 + Player.Name + abi + " Has Left The Server")
                elif self.isMod(Player):
                    Server.Broadcast(color1 + Player.Name + abi + " Has Left The Server")
                elif self.isDonator(Player):
                    Server.Broadcast(color1 + Player.Name + abi + " Has Left The Server")
                elif self.isVIP(Player):
                    Server.Broadcast(color1 + Player.Name + abi + " Has Left The Server")
                else:
                    Server.BroadcastFrom("Bye", abi + "The Player ☾" + color1 + Player.Name + abi + "☽ Has Left The Server.")
        except:
            Fougerite.Logger.LogError("DonatorRank: Failed displaying leave message!")
            pass
 
    def On_Chat(self, Player, ChatMessage):
        try:
            muted = False
            if Server.HasRustPP:
                muted = Server.GetRustPPAPI().IsMuted(long(Player.SteamID))
            if PSettings["ChatPrefix"]:
                if PSettings["OwnerID"] == str(Player.SteamID):
                    chatmsg = str(ChatMessage)[1:-1]
                    ocolour = PSettings["OwnerColour"]
                    Server.BroadcastFrom("[Owner]♚" + Player.Name, ocolour + chatmsg)
                    ChatMessage.NewText = "*%"
                    return
                if PSettings["DevID"] == str(Player.SteamID):
                    chatmsg = str(ChatMessage)[1:-1]
                    Server.BroadcastFrom("*Dev* " + Player.Name, pink + chatmsg)
                    ChatMessage.NewText = "*%"
                    return 
                    
        #        if Player.SteamID == "76561197961233431";
         #            chatmsg = str(ChatMessage)[1:-1]              
          #         Server.BroadcastFrom("*Dev* " + Player.Name, Rad +  chatmsg)
          #         ChatMessage.NewText = "*%"
                elif Player.Moderator:
                    chatmsg = str(ChatMessage)[1:-1]
                    Server.BroadcastFrom(Player.Name , staff +"❅ "+ chatmsg)
                    ChatMessage.NewText = "*%"
                elif self.isMod(Player):
                    chatmsg = str(ChatMessage)[1:-1]
                    mcolour = PSettings["ModColour"]
                    Server.BroadcastFrom("[Mad]" + Player.Name, mcolour +"✍ " +  chatmsg)
                    ChatMessage.NewText = "*%"
                elif self.isDonator(Player):
                    if not muted:
                        chatmsg = str(ChatMessage)[1:-1]
                        dcolour = "[color #00aaff]"
                        Server.BroadcastFrom("[Donator]" + Player.Name, dcolour +"🎮 "+ chatmsg)
                        ChatMessage.NewText = "*%"
                    else:
                        return False
                elif self.isVIP(Player):
                    if not muted:
                        chatmsg = str(ChatMessage)[1:-1]
                        vcolour = PSettings["VIPColour"]
                        Server.BroadcastFrom("[VIP]" + Player.Name, vcolour +"➥ "+ chatmsg)
                        ChatMessage.NewText = "*%"
                    else:
                        chatmsg = str(ChatMessage)[1:-1]
                        Server.BroadcastFrom(Player.Name, "➥ "+ chatmsg)
    #                    return False
        except:
            Fougerite.Logger.LogError("DonatorRank: On_Chat Error!")
            pass

    def isMod(self, Player):
        try:
            if self.CheckPerm(Player.SteamID, "Rank") == "Mod":
                return True
            elif Player.Moderator:
                ini = self.getUserIni()
                d = Plugin.GetDate()
                t = Plugin.GetTime()
                ini.AddSetting(modname.SteamID, "UserName", modname.Name)
                ini.AddSetting(modname.SteamID, "INFO", "Time: " + t + "||Date: " + d + "||By: DonatorRank-AutoAdd")
                ini.AddSetting(modname.SteamID, "Rank", "Mod")
                ini.AddSetting(modname.SteamID, "MaxHomes", PSettings["ModHomesMax"])
                ini.AddSetting(modname.SteamID, "AddVIPS", "true")
                ini.AddSetting(modname.SteamID, "AddDonators", "true")
                ini.AddSetting(modname.SteamID, "AddMods", "false")
                ini.AddSetting(modname.SteamID, "DelVIPS", "true")
                ini.AddSetting(modname.SteamID, "DelDonators", "true")
                ini.AddSetting(modname.SteamID, "DelMods", "false")
                ini.AddSetting(modname.SteamID, "LVL1VKIT", "false")
                ini.AddSetting(modname.SteamID, "LVL2VKIT", "false")
                ini.AddSetting(modname.SteamID, "LVL1DKIT", "false")
                ini.AddSetting(modname.SteamID, "LVL2DKIT", "false")
                ini.AddSetting(modname.SteamID, "MODKIT", "true")
                ini.AddSetting(modname.SteamID, "VTP", "false")
                ini.AddSetting(modname.SteamID, "DTP", "false")
                ini.AddSetting(modname.SteamID, "MTP", "true")
                ini.AddSetting(modname.SteamID, "UseBroadcast", "true")
                ini.AddSetting(modname.SteamID, "AccessInfo", "true")
                ini.Save()
                self.UpdatePerms()
                return True
            else:
                return False
        except:
            return False
 
    def isDonator(self, Player):
        try:
            if self.CheckPerm(Player.SteamID, "Rank") == "Donator":
                return True
            else:
                return False
        except:
            return False
 
    def isVIP(self, Player):
        try:
            if self.CheckPerm(Player.SteamID, "Rank") == "VIP":
                return True
            else:
                return False
        except:
            return False
 
    def GetSettingsIni(self):
        if not Plugin.IniExists("Settings"):
            ini = Plugin.CreateIni("Settings")
            ini.Save()
        return Plugin.GetIni("Settings")
 
    def getUserIni(self):
        if not Plugin.IniExists("Users"):
            ini = Plugin.CreateIni("Users")
            ini.Save()
        return Plugin.GetIni("Users")
 
    def getLogIni(self):
        if not Plugin.IniExists("Logs"):
            ini = Plugin.CreateIni("Logs")
            ini.Save()
        return Plugin.GetIni("Logs")
 
    def argsToText(self, args):
        text = str.join(" ", args)
        return text

    def StrToInt(self, string, line):
        try:
            return int(float(str(string)))
        except:
            Fougerite.Logger.LogError("DonatorRank: Error converting string to int [Line: " + line + "]")
 
    #Method provided by Spoock. Converted to Python by DreTaX
    def CheckV(self, Player, args):
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
            for pl in Server.ActivePlayers:
                if nargs in pl.Name.lower():
                    p = pl
                    count += 1
                    continue
        if count == 0:
            Player.Message("Couldn't find " + str.join(" ", args) + "!")
            return None
        elif count == 1 and p is not None:
            return p
        else:
            Player.Message("Found " + str(count) + " players with similar a name. Use a more correct name!")
            return None
 
    #GetPlayerName provided by DreTaX
    def GetPlayerName(self, name):
        try:
            name = name.lower()
            for pl in Server.Players:
                if pl.Name.lower() == name:
                    return pl
            return None
        except:
            return None

    def TrytoGrabID(self, Player):
        try:
            id = Player.SteamID
            return id
        except:
            return None
