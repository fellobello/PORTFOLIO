#Define races with Ability Score modifiers
races = {
    "Human": [{"Subrace": "Human", "Ability Score Modifiers": {"Strength": 1, "Dexterity": 1, "Constitution": 1, "Intelligence": 1, "Wisdom": 1, "Charisma": 1}}],
    "Elf": [
        {"Subrace": "Plain Elf", "Ability Score Modifiers": {"Strength": 0, "Dexterity": 2, "Constitution": 0, "Intelligence": 0, "Wisdom": 0, "Charisma": 0}}, 
        {"Subrace": "High Elf", "Ability Score Modifiers": {"Strength": 0, "Dexterity": 2, "Constitution": 0, "Intelligence": 1, "Wisdom": 0, "Charisma": 0}},
        {"Subrace": "Wood Elf", "Ability Score Modifiers": {"Strength": 0, "Dexterity": 2, "Constitution": 0, "Intelligence": 0, "Wisdom": 1, "Charisma": 0}},
        {"Subrace": "Drow", "Ability Score Modifiers": {"Strength": 0, "Dexterity": 2, "Constitution": 0, "Intelligence": 0, "Wisdom": 0, "Charisma": 1}}
    ],
    "Dwarf": [
        {"Subrace": "Plain Dwarf", "Ability Score Modifiers": {"Strength": 0, "Dexterity": 0, "Constitution": 2, "Intelligence": 0, "Wisdom": 0, "Charisma": 0}}, 
        {"Subrace": "Hill Dwarf", "Ability Score Modifiers": {"Strength": 0, "Dexterity": 0, "Constitution": 2, "Intelligence": 0, "Wisdom": 1, "Charisma": 0}},
        {"Subrace": "Mountain Dwarf", "Ability Score Modifiers": {"Strength": 2, "Dexterity": 0, "Constitution": 2, "Intelligence": 0, "Wisdom": 0, "Charisma": 0}}
    ],
    "Halfling": [
        {"Subrace": "Plain Halfling", "Ability Score Modifiers": {"Strength": 0, "Dexterity": 2, "Constitution": 0, "Intelligence": 0, "Wisdom": 0, "Charisma": 0}}, 
        {"Subrace": "Lightfoot Halfling", "Ability Score Modifiers": {"Strength": 0, "Dexterity": 2, "Constitution": 0, "Intelligence": 0, "Wisdom": 0, "Charisma": 1}},
        {"Subrace": "Stout Halfling", "Ability Score Modifiers": {"Strength": 0, "Dexterity": 2, "Constitution": 1, "Intelligence": 0, "Wisdom": 0, "Charisma": 0}}
    ],
    "Dragonborn": [{"Subrace": "Dragonborn", "Ability Score Modifiers": {"Strength": 2, "Dexterity": 0, "Constitution": 0, "Intelligence": 0, "Wisdom": 0, "Charisma": 1}}],
    "Gnome": [
        {"Subrace": "Plain Gnome", "Ability Score Modifiers": {"Strength": 0, "Dexterity": 0, "Constitution": 1, "Intelligence": 2, "Wisdom": 0, "Charisma": 0}}, 
        {"Subrace": "Rock Gnome", "Ability Score Modifiers": {"Strength": 0, "Dexterity": 0, "Constitution": 1, "Intelligence": 2, "Wisdom": 0, "Charisma": 0}},
        {"Subrace": "Deep Gnome", "Ability Score Modifiers": {"Strength": 0, "Dexterity": 1, "Constitution": 0, "Intelligence": 2, "Wisdom": 0, "Charisma": 0}}
    ],
    "Half-Elf": [{"Subrace": "Half-Elf", "Ability Score Modifiers": {"Strength": 0, "Dexterity": 0, "Constitution": 0, "Intelligence": 0, "Wisdom": 0, "Charisma": 2}}],
    "Half-Orc": [{"Subrace": "Half-Orc", "Ability Score Modifiers": {"Strength": 2, "Dexterity": 0, "Constitution": 1, "Intelligence": 0, "Wisdom": 0, "Charisma": 0}}]
}

#Define Classes and Subclasses
classes = {
    "Barbarian": [],
    "Bard": [],
    "Cleric": ["Life Domain", "Light Domain", "Nature Domain", "Tempest Domain", "Trickery Domain", "War Domain"],
    "Druid": ["Circle of the Land", "Circle of the Moon"],
    "Fighter": ["Champion", "Battle Master", "Eldritch Knight"],
    "Monk": ["Way of the Open Hand", "Way of Shadow", "Way of the Four Elements"],
    "Paladin": ["Oath of Devotion", "Oath of the Ancients", "Oath of Vengeance"],
    "Ranger": ["Hunter", "Beast Master"],
    "Rogue": ["Thief", "Assassin", "Arcane Trickster"],
    "Sorcerer": [],
    "Warlock": ["The Archfey", "The Fiend", "The Great Old One"],
    "Wizard": ["School of Evocation", "School of Abjuration", "School of Conjuration", "School of Divination", "School of Enchantment", "School of Illusion", "School of Necromancy", "School of Transmutation"]
}

def display_classes(classes):
    for class_name, subclasses in classes.items():
        print(f"{class_name}:")
        for subclass in subclasses:
            print(f"  {subclass}")

#display_classes(classes)
#display_classes(races) 

character = {
    "Race": "",
    "Class": "",
    "Ability Scores": {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    },
    "Skills": {},
    "Feats": [],
    "Background": "",
    "Alignment": "",
    "Appearance": {
        "Gender": "",
        "Age": 0,
        "Height": 0,
        "Weight": 0,
        "Physical Characteristics": ""
    },
    "Personality": "",
    "Name": "",
    "Backstory": "",
    "Goals": "",
    "Flaws": "",
    "Relationships": {},
    "Inventory": {},
    "Currency": {},
    "Reputation": ""
}

"""def print_character(character):
  print(f"Race: {character['Race']}")
  print(f"Class: {character['Class']}")
  print("Ability Scores:")
  for key, value in character['Ability Scores'].items():
    print(f"  {key}: {value}")
  print("Skills:")
  for key, value in character['Skills'].items():
    print(f"  {key}: {value}")
  print(f"Feats: {', '.join(character['Feats'])}")
  print(f"Background: {character['Background']}")
  print(f"Alignment: {character['Alignment']}")
  print("Appearance:")
  for key, value in character['Appearance'].items():
    print(f"  {key}: {value}")
  print(f"Personality: {character['Personality']}")
  print(f"Name: {character['Name']}")
  print(f"Backstory: {character['Backstory']}")
  print(f"Goals: {character['Goals']}")
  print(f"Flaws: {character['Flaws']}")
  print("Relationships:")
  for key, value in character['Relationships'].items():
    print(f"  {key}: {', '.join(value)}")
  print("Inventory:")
  for key, value in character['Inventory'].items():
    print(f"  {key}: {', '.join(value)}")
  print("Currency:")
  for key, value in character['Currency'].items():
    print(f"  {key}: {value}")
  print(f"Reputation: {character['Reputation']}")"""