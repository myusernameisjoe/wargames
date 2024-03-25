zones_data = [
    {"Zone ID": 1, "Type": "Urban", "Strategic Value": 3, "Resources": 1, "Terrain Difficulty": 2, "Control": "Blue"},
    {"Zone ID": 2, "Type": "Industrial", "Strategic Value": 2, "Resources": 3, "Terrain Difficulty": 1, "Control": "Red"},
    {"Zone ID": 3, "Type": "Rural", "Strategic Value": 1, "Resources": 2, "Terrain Difficulty": 1, "Control": "None"},
    {"Zone ID": 4, "Type": "Mountain", "Strategic Value": 2, "Resources": 1, "Terrain Difficulty": 3, "Control": "None"}
]

faction_forces_data = {
    "Blue": {"Infantry": 100, "Armor": 0, "Air Support": 0, "Special Forces": 0, "Resources": 0},
    "Red": {"Infantry": 150, "Armor": 40, "Air Support": 5, "Special Forces": 10, "Resources": 150}
}

historical_battles_data = [
    {"Battle ID": 1, "Zone ID": 3, "Attacker": "Blue", "Defender": "Red", "Outcome": "Win", "Attacker Losses": 20, "Defender Losses": 30},
    {"Battle ID": 2, "Zone ID": 4, "Attacker": "Red", "Defender": "Blue", "Outcome": "Lose", "Attacker Losses": 50, "Defender Losses": 10},
    {"Battle ID": 3, "Zone ID": 4, "Attacker": "Red", "Defender": "Blue", "Outcome": "Lose", "Attacker Losses": 50, "Defender Losses": 10},
    {"Battle ID": 4, "Zone ID": 2, "Attacker": "Blue", "Defender": "Red", "Outcome": "Win", "Attacker Losses": 10, "Defender Losses": 20},
    {"Battle ID": 5, "Zone ID": 1, "Attacker": "Red", "Defender": "Blue", "Outcome": "Lose", "Attacker Losses": 30, "Defender Losses": 20},
]
