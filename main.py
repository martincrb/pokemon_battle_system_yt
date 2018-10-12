from constants import *
from models.Battle import *
from models.Pokemon import *
#First define pokemons with its stats

pokemon1 = Pokemon("Bulbasaur", 100, 11, 3)
pokemon2 = Pokemon("Charmander", 100, 9, 1)
pokemon1.current_hp = 45
pokemon2.current_hp = 39
#Stats

pokemon1.baseStats = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65
}

pokemon1.ev = {
    HP: 0,
    ATTACK: 0,
    DEFENSE: 0,
    SPATTACK: 0,
    SPDEFENSE: 0,
    SPEED: 0
}

pokemon1.iv = {
    HP: 21,
    ATTACK: 21,
    DEFENSE: 21,
    SPATTACK: 21,
    SPDEFENSE: 21,
    SPEED: 21
}
pokemon1.compute_stats()

pokemon2.baseStats = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65
}

pokemon2.ev = {
    HP: 0,
    ATTACK: 0,
    DEFENSE: 0,
    SPATTACK: 0,
    SPDEFENSE: 0,
    SPEED: 0
}

pokemon2.iv = {
    HP: 21,
    ATTACK: 21,
    DEFENSE: 21,
    SPATTACK: 21,
    SPDEFENSE: 21,
    SPEED: 21
}
pokemon2.compute_stats()
print(pokemon1.stats)
print(pokemon2.stats)
#Attacks
pokemon1.attacks = [Attack("latigo cepa", 11, PHYSICAL, 10, 10, 100)]
pokemon2.attacks = [Attack("scratch", 0, PHYSICAL, 10, 10, 100)]


def ask_command(pokemon):
    command = None
    while not command:
        tmp_command = input("What should "+pokemon.name+" do?").split(" ")
        if len(tmp_command) == 2:
            print(tmp_command)
            try:
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                    command = Command({DO_ATTACK: int(tmp_command[1])})
            except Exception:
                pass
    return command

#Start battle

battle = Battle(pokemon1, pokemon2)

while not battle.is_finished():
    #Main pokemon battle loop
    #First ask for the commands
    command1 = ask_command(pokemon1)
    command2 = ask_command(pokemon2)

    #Generate new turn
    turn = Turn()
    turn.command1 = command1
    turn.command2 = command2

    if turn.can_start():
        # Execute turn
        battle.execute_turn(turn)
        battle.print_current_status()

