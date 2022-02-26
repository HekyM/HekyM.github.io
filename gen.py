import json
from copy import deepcopy


heroes = {
    "Shadow": {
        "Annabelle": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Onkirimaru": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Eloise": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Tix": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Ithaqua": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Gustin": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Horus": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Jahra": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Kamath": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": False,
        },
        "Corpsedemon": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": False,
        },
        "Blood Blade": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Walter": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Field": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Kharma": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Aidan": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Baade": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Lutz": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Dominator": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Glen": {
            "class": "Priest",
            "stars": [4, 5, 6, 9],
            "elite": False,
            "imprint": False,
        },
        "Bonecarver": {
            "class": "Assassin",
            "stars": [4, 5, 6, 9],
            "elite": False,
            "imprint": False,
        },
        "Deathsworn": {
            "class": "Mage",
            "stars": [4, 5, 6, 9],
            "elite": False,
            "imprint": False,
        },
        "Lamb": {
            "class": "Ranger",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Bone General": {
            "class": "Warrior",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Nightmare Knight": {
            "class": "Warrior",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Gbagbo": {
            "class": "Ranger",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Grumpy Corpse": {
            "class": "Warrior",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
    },
    "Fortress": {
        "Holmes Young": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Saja": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Fiona": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Inosuke": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Sherlock": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "UniMax-3000": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Penny": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Xia": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Valentino": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Sigmund": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": False,
        },
        "Flame Strike": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Emily": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Ormus": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "OD-01": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Miki": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Mirage": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Bleecker": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Iceblink": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Honor Guard": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Kristian": {
            "class": "Warrior",
            "stars": [4, 5, 6, 9],
            "elite": False,
            "imprint": False,
        },
        "Roy": {
            "class": "Assassin",
            "stars": [4, 5, 6, 9],
            "elite": False,
            "imprint": False,
        },
        "Sierra": {
            "class": "Mage",
            "class-supplement": "Priest",
            "stars": [4, 5, 6, 9],
            "elite": False,
            "imprint": False,
        },
        "Iron Bambi": {
            "class": "Warrior",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "LM-02": {
            "class": "Ranger",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Liquor": {
            "class": "Ranger",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Storm Huddle": {
            "class": "Warrior",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Time Mage": {
            "class": "Mage",
            "class-supplement": "Priest",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
    },
    "Abyss": {
        "Natasha": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Waldeck": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Morax": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Ignis": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Delacium": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Nakia": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Cthugha": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "King Barton": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Kroos": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": False,
        },
        "Skerei": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": False,
        },
        "Barea": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Dantalian": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Karim": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Gusta": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Fat Mu": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Lord Balrog": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Queen": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Margaret": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Destroyer": {
            "class": "Mage",
            "stars": [4, 5, 6, 9],
            "elite": False,
            "imprint": False,
        },
        "Aleria": {
            "class": "Mage",
            "stars": [4, 5, 6, 9],
            "elite": False,
            "imprint": False,
        },
        "Norma": {
            "class": "Priest",
            "stars": [4, 5, 6, 9],
            "elite": False,
            "imprint": False,
        },
        "Immolatus": {
            "class": "Warrior",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Lemegeton": {
            "class": "Warrior",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Akasha": {
            "class": "Assassin",
            "class-supplement": "Ranger",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Tanner": {
            "class": "Warrior",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Rogge": {
            "class": "Priest",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
    },
    "Forest": {
        "Xiahou": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Gloria": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Flora": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Rogan": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Elyvia": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Garuda": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Oberon": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Valkyrie": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Heart Watcher": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": False,
        },
        "Vesa": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": False,
        },
        "Eddga": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Rosa": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Malassa": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Groo": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Starlight": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Faceless": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Dragon Slayer": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Demon Hunter": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "The Grey-eyed": {
            "class": "Assassin",
            "stars": [4, 5, 6, 9],
            "elite": False,
            "imprint": False,
        },
        "Zekkis": {
            "class": "Priest",
            "class-supplement": "Mage",
            "stars": [4, 5, 6, 9],
            "elite": False,
            "imprint": False,
        },
        "Thale": {
            "class": "Priest",
            "class-supplement": "Mage",
            "stars": [4, 5, 6, 9],
            "elite": False,
            "imprint": False,
        },
        "Kargath": {
            "class": "Warrior",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Headstriker": {
            "class": "Assassin",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Ent Elder": {
            "class": "Priest",
            "class-supplement": "Mage",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Chief": {
            "class": "Warrior",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Wind Walker": {
            "class": "Ranger",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
    },
    "Dark": {
        "Phorcys": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Drake": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Carrie": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Amen-Ra": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Aspen": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Mihm": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Amuvor": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Das Moge": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Sleepless": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Dark Arthindol": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Dark Spirit": {
            "class": "Mage",
            "stars": [4, 5, 6, 9],
            "elite": False,
            "imprint": False,
        },
        "Logan": {
            "class": "Mage",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Darkness Fanella": {
            "class": "Mage",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
    },
    "Light": {
        "Eos": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Andrea": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Tussilago": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Russell": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Tara": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Aida": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Belrain": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Faith Blade": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Michelle": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": True,
        },
        "Asmodel": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Gerke": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": False,
            "imprint": False,
        },
        "Divine Spirit": {
            "class": "Mage",
            "stars": [4, 5, 6, 9],
            "elite": False,
            "imprint": False,
        },
        "Fegan": {
            "class": "Warrior",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
        "Disciple": {
            "class": "Priest",
            "stars": [4, 5],
            "elite": False,
            "imprint": False,
        },
    },
    "Transcendence": {
        "The Sun Devourer - Eos": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Lord of Fear - Aspen": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Fairy Queen - Vesa": {
            "class": "Priest",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Star Wing - Jahra": {
            "class": "Mage",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Asmodel the Dauntless": {
            "class": "Warrior",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Scarlet Queen - Halora": {
            "class": "Ranger",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
        "Sword Flash - Xia": {
            "class": "Assassin",
            "stars": [5, 6, 9, 10],
            "elite": True,
            "imprint": True,
        },
    }
}

leveling = {
    "5": {
        "lvl": 100,
        "self:4": 2,
        "self:5": 1, # get 5* or build from 4+3*
        "4": 6,
        "3": 4,
        "stone": 1800,
        "spirit": 2600000,
        "gold": 5600000,
    },
    "6": {
        "lvl": 140,
        "self:5": 1,
        "5": 4,
        "stone": 2000,
        "spirit": 12000000,
        "gold": 14000000,
    },
    "7": {
        "lvl": 160,
        "self:5": 0,
        "5": 4,
        "stone": 2000,
        "spirit": 9100000,
        "gold": 9700000,
    },
    "8": {
        "lvl": 180,
        "self:5": 0,
        "5": 3,
        "6": 1,
        "stone": 3000,
        "spirit": 10400000,
        "gold": 10600000,
    },
    "9": {
        "lvl": 200,
        "self:5": 1,
        "5": 2,
        "6": 1,
        "stone": 4000,
        "spirit": 12400000,
        "gold": 11800000,
    },
    "10": {
        "lvl": 250,
        "self:5": 2,
        "6": 1,
        "9": 1,
        "stone": 10000,
        "spirit": 77000000,
        "gold": 39000000,
    },
    "E1": {
        "lvl": 260,
        "self:5": 1,
        "9": 1,
        "10": 0,
        "stone": 10000,
        "spirit": 32000000,
        "gold": 11100000,
    },
    "E2": {
        "lvl": 270,
        "self:5": 1,
        "9": 1,
        "10": 0,
        "stone": 10000,
        "spirit": 41000000,
        "gold": 14000000,
    },
    "E3": {
        "lvl": 290,
        "self:5": 0,
        "9": 0,
        "10": 1,
        "stone": 15000,
        "spirit": 104000000,
        "gold": 35000000,
    },
    "E4": {
        "lvl": 310,
        "self:5": 1,
        "9": 0,
        "10": 1,
        "stone": 15000,
        "spirit": 137000000,
        "gold": 46000000,
    },
    "E5": {
        "lvl": 330,
        "self:5": 1,
        "9": 0,
        "10": 1,
        "stone": 20000,
        "spirit": 209000000,
        "gold": 70000000,
        "stellar": 0,
    },
    "V1": {
        "lvl": 330,
        "10": 1,
        "stellar": 138630,
    },
    "V2": {
        "lvl": 330,
        "10": 1,
        "stellar": 587610,
    },
    "V3": {
        "lvl": 330,
        "10": 1,
        "stellar": 1458390,
    },
    "V4": {
        "lvl": 330,
        "10": 1,
        "stellar": 2750070,
    },
    "+5": {
        "lvl": 335,
        "spirit": 64300000,
        "gold": 21600000,
    },
    "+10": {
        "lvl": 340,
        "spirit": 69100000,
        "gold": 23200000,
    },
    "+15": {
        "lvl": 345,
        "spirit": 73900000,
        "gold": 24800000,
    },
    "+20": {
        "lvl": 350,
        "spirit": 78700000,
        "gold": 26500000,
    },
}

# hero: 140x140 (25)
# shard: 158x158 (25)

def img_hero_shard(faction, data):
    if faction in ['Dark', 'Light', 'Transcendence']:
        _faction = faction
    else:
        _faction = 'Any'

    if data['elite']:
        _type = 'Elite'
        
    else:
        _type = 'Normal'

    if 4 in data['stars']:
        _stars = 4
        _faction = 'Any'
    else:
        _stars = 5

    return f'{_faction} {_type} {_stars}&#9733;'

def img_hero(faction, name, stars, data):
    if stars in data['stars']:
        # _name = name.lower().replace(' ', '_')
        return f'{name} {stars}&#9733;'
    else:
        return None

def img_imprint(data):
    if data['imprint']:
        return 'Stars V4'
    else:
        return None


def fusion_hero(faction, name, data):
    return {
        'faction': faction,
        'name': name,
        'source-img': img_hero_shard(faction, data),
        **{
            f'stars-{stars}-img': img_hero(faction, name, stars, data)
            for stars in [4, 5, 6, 9, 10]
        },
        'imprint-img': img_imprint(data),
        'class': data['class'],
    }


def generate_leveling():
    rows = []
    for key, data in leveling.items():
        rows.append({
            "stars": key,
            "lvl": data.get('lvl', 0),
            "self": data.get('self:5', 0),
            "5": data.get('5', 0),
            "6": data.get('6', 0),
            "9": data.get('9', 0),
            "10": data.get('10', 0),
            "stone": data.get('stone', 0),
            "spirit": data.get('spirit', 0),
            "gold": data.get('gold', 0),
            "stellar": data.get('stellar', 0),
        })
    
    return rows

def generate_total_leveling():
    per_lvl_rows = generate_leveling()
    rows = []
    row = {
        "stars": "",
        "lvl": 0,
        "self": 0,
        "5": 0,
        "6": 0,
        "9": 0,
        "10": 0,
        "stone": 0,
        "spirit": 0,
        "gold": 0,
        "stellar": 0,
    }
    for per_lvl_row in per_lvl_rows:
        for key, value in per_lvl_row.items():
            if key == 'stars':
                row[key] = value
            else:
                row[key] += value

        rows.append(deepcopy(row))

    return rows


def generate():
    def generate_fusion_heroes(faction):
        faction_heroes = heroes[faction]
        rows = []

        for name, data in faction_heroes.items():
            rows.append(fusion_hero(faction, name, data))
        return rows

    def generate_shelter_heroes(faction):
        faction_heroes = heroes[faction]
        row = {hero_class:[] for hero_class in ['Warrior', 'Assassin', 'Ranger', 'Mage', 'Priest']}
        for name, data in faction_heroes.items():
            if 4 in data['stars']:
                img = img_hero(faction, name, 4, data)
                row[data['class']].append(img)
                if "class-supplement" in data:
                    row[data['class-supplement']].append(img)
                row['faction'] = faction
        return [row]

    fusion_heroes_filename = 'data/fusion_heroes.v1.json'
    shelter_heroes_filename = 'data/shelter_heroes.v1.json'
    lvl_filename = 'data/lvl.v1.json'

    fusion_heroes = []
    for faction in heroes.keys():
        fusion_heroes.extend(generate_fusion_heroes(faction))

    with open(fusion_heroes_filename, 'w') as outfile:
        json.dump(fusion_heroes, outfile)

    shelter_heroes = []
    for faction in ['Shadow', 'Fortress', 'Abyss', 'Forest']:
        shelter_heroes.extend(generate_shelter_heroes(faction))

    with open(shelter_heroes_filename, 'w') as outfile:
        json.dump(shelter_heroes, outfile)

    with open(lvl_filename, 'w') as outfile:
        json.dump(generate_leveling(), outfile)

    # with open('data/lvl-total.json', 'w') as outfile:
    #     json.dump(generate_total_leveling(), outfile)

    import re
    with open ('index.html', 'r' ) as f:
        content = f.read()

    content = re.sub('data\/fusion_heroes\.v[0-9]+\.json', fusion_heroes_filename, content, flags = re.M)
    content = re.sub('data\/shelter_heroes\.v[0-9]+\.json', shelter_heroes_filename, content, flags = re.M)
    content = re.sub('data\/lvl\.v[0-9]+\.json', lvl_filename, content, flags = re.M)

    with open ('index.html', 'w' ) as f:
        f.write(content)

    return

generate()