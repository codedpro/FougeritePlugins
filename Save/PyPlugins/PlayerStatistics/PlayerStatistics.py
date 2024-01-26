__author__ = 'Coded_Pro'
__version__ = '1.0'
clr.AddReferenceByPartialName("Fougerite")

import clr
import Fougerite
import json
from System import TimeSpan

DATA_FILE = "player_statistics.json"

player_statistics = {}


class PlayerStatistics:

    def On_PluginInit(self):
        self.load_player_statistics()

    def On_PlayerConnected(self, player, login):
        player_id = player.SteamID
        if player_id not in player_statistics:
            player_statistics[player_id] = {
                "kills": 0,
                "deaths": 0,
                "playtime": 0,
                "distance_traveled": 0.0,
                "airdrops_looted": 0,
                "airdrops_called": 0,
                "c4_used": 0,
                "entities_killed": {} 
            }
        self.save_player_statistics()

    def On_PlayerDisconnected(self, player):
        self.save_player_statistics()

    def On_PlayerKilled(self, death_event):
        if death_event.AttackerIsPlayer and death_event.VictimIsPlayer:
            attacker_id = death_event.Attacker.SteamID
            victim_id = death_event.Victim.SteamID

            player_statistics[attacker_id]["kills"] += 1
            player_statistics[victim_id]["deaths"] += 1

            self.save_player_statistics()

    def On_PlayerSpawned(self, player, spawn_event):
        player_id = player.SteamID

        player_statistics[player_id]["playtime"] += 1

        self.save_player_statistics()

    def On_PlayerMove(self, player, move_event):
        player_id = player.SteamID

        distance_traveled = move_event.Distance
        player_statistics[player_id]["distance_traveled"] += distance_traveled

    def On_AirdropLoot(self, airdrop_event):
        player_id = airdrop_event.Looter.SteamID
        player_statistics[player_id]["airdrops_looted"] += 1

    def On_AirdropCalled(self, airdrop_event):
        player_id = airdrop_event.Caller.SteamID
        player_statistics[player_id]["airdrops_called"] += 1

    def On_PlacedStructure(self, placement_event):
        if placement_event.Structure == "C4":
            player_id = placement_event.Builder.SteamID
            player_statistics[player_id]["c4_used"] += 1

    def On_EntityHurt(self, hurt_event):
        if hurt_event.AttackerIsPlayer and hurt_event.VictimIsNPC:
            attacker_id = hurt_event.Attacker.SteamID
            entity_type = hurt_event.Victim.Name

            entity_kills = player_statistics[attacker_id]["entities_killed"]
            entity_kills[entity_type] = entity_kills.get(entity_type, 0) + 1

            self.save_player_statistics()

    def load_player_statistics(self):
        global player_statistics
        try:
            with open(DATA_FILE, "r") as file:
                player_statistics = json.load(file)
        except (IOError, ValueError):
            player_statistics = {}

    def save_player_statistics(self):
        try:
            with open(DATA_FILE, "w") as file:
                json.dump(player_statistics, file, indent=4)
        except IOError:
            console.log("Error saving player statistics to file")


player_stats_instance = PlayerStatistics()
