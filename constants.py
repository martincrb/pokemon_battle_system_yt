
#Pokemon stats
HP = "HP"
ATTACK = "Attack"
DEFENSE = "Defense"
SPATTACK = "SpAttack"
SPDEFENSE = "SpDefense"
SPEED = "Speed"


#Commands
DO_ATTACK = "attack"
DO_ATTACK_SELECTION = "selected_attack"

#Attack categories
PHYSICAL = "physical"
SPECIAL = "special"
NATURES = [
    "Hardy",
    "Lonely",
    "Brave",
    "Adamant",
    "Naughty",
    "Bold",
    "Docile",
    "Relaxed",
    "Impish",
    "Lax",
    "Timid",
    "Hasty",
    "Serious",
    "Jolly",
    "Naive",
    "Modest",
    "Mild",
    "Quiet",
    "Bashful",
    "Rash",
    "Calm",
    "Gentle",
    "Sassy",
    "Careful",
    "Quirky"
]
NATURE_MATRIX = [
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},
    {HP: 1, ATTACK: 1.1, DEFENSE: 0.9, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},
    {HP: 1, ATTACK: 1.1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 0.9},
    {HP: 1, ATTACK: 1.1, DEFENSE: 1, SPATTACK: 0.9, SPDEFENSE: 1, SPEED: 1},
    {HP: 1, ATTACK: 1.1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 0.9, SPEED: 1},
    {HP: 1, ATTACK: 0.9, DEFENSE: 1.1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},
    {HP: 1, ATTACK: 1, DEFENSE: 1.1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 0.9},
    {HP: 1, ATTACK: 1, DEFENSE: 1.1, SPATTACK: 0.9, SPDEFENSE: 1, SPEED: 1},
    {HP: 1, ATTACK: 1, DEFENSE: 1.1, SPATTACK: 1, SPDEFENSE: 0.9, SPEED: 1},
    {HP: 1, ATTACK: 0.9, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1.1},
    {HP: 1, ATTACK: 1, DEFENSE: 0.9, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1.1},
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 0.9, SPDEFENSE: 1, SPEED: 1.1},
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 0.9, SPEED: 1.1},
    {HP: 1, ATTACK: 0.9, DEFENSE: 1, SPATTACK: 1.1, SPDEFENSE: 1, SPEED: 1},
    {HP: 1, ATTACK: 1, DEFENSE: 0.9, SPATTACK: 1.1, SPDEFENSE: 1, SPEED: 1},
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1.1, SPDEFENSE: 1, SPEED: 0.9},
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1.1, SPDEFENSE: 0.9, SPEED: 1},
    {HP: 1, ATTACK: 0.9, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1.1, SPEED: 1},
    {HP: 1, ATTACK: 1, DEFENSE: 0.9, SPATTACK: 1, SPDEFENSE: 1.1, SPEED: 1},
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1.1, SPEED: 0.9},
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 0.9, SPDEFENSE: 1.1, SPEED: 1},
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},
]
TYPES = [
    "Normal",
    "Fighting",
    "Flying",
    "Poison",
    "Ground",
    "Rock",
    "Bug",
    "Ghost",
    "Steel",
    "Fire",
    "Water",
    "Grass",
    "Electric",
    "Psychic",
    "Ice",
    "Dragon",
    "Dark",
    "Fairy"
    ]

TYPE_CHART = [
    [1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,2,1,1,.5,.5,1,1,1,1,1,1,2,1,1,.5,2],
    [1,.5,1,1,0,2,.5,1,1,1,1,.5,2,1,2,1,1,1],
    [1,.5,1,.5,2,1,.5,1,1,1,1,.5,1,2,1,1,1,.5],
    [1,1,1,.5,1,.5,1,1,1,1,2,2,0,1,2,1,1,1],
    [.5,2,.5,.5,2,1,1,1,2,.5,2,2,1,1,1,1,1,1],
    [1,.5,2,1,.5,2,1,1,1,2,1,.5,1,1,1,1,1,1],
    [0,0,1,.5,1,1,.5,2,1,1,1,1,1,1,1,1,2,1],
    [.5,2,.5,0,2,.5,.5,1,.5,2,1,.5,1,.5,.5,.5,1,.5],
    [1,1,1,1,2,2,.5,1,.5,.5,2,.5,1,1,.5,1,1,.5],
    [1,1,1,1,1,1,1,1,.5,.5,.5,2,2,1,.5,1,1,1],
    [1,1,2,2,.5,1,2,1,1,2,.5,.5,.5,1,2,1,1,1],
    [1,1,.5,1,2,1,1,1,.5,1,1,1,.5,1,1,1,1,1],
    [1,.5,1,1,1,1,2,2,1,1,1,1,1,.5,1,1,2,1],
    [1,2,1,1,1,2,1,1,2,2,1,1,1,1,.5,1,1,1],
    [1,1,1,1,1,1,1,1,1,.5,.5,.5,.5,1,2,2,1,2],
    [1,2,1,1,1,1,2,.5,1,1,1,1,1,0,1,1,.5,2],
    [1,.5,1,2,1,1,.5,1,2,1,1,1,1,1,1,0,.5,1]
    ]