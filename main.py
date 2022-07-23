import characters as chars
import enemies as bad
import stats
import math

def char_create():
    print("Welcome to the game, please enter your name:")
    chars.list_o_chars["HERO"]["name"] = input()
    print("here are your base stats:", chars.list_o_chars["HERO"])
    print("You have 10 points to upgrade your stats")
    print("You can upgrade your HP, MP, ATK, DEF, SPD")
    print("all points upgrade the stat by 1, except HP and MP")
    print("HP increases by 2 per 1 stat spend and MP increases by .5 per 1 stat spend")
    points = 10
    while points > 0:
        print("You have", points, "points left")
        print("What stat would you like to upgrade?")
        print(chars.list_o_chars["HERO"])
        stat = input()
        stat = stat.upper()
        if stat == "HP":
            chars.list_o_chars["HERO"]["hp"] += 2
            points -= 1
        elif stat == "MP":
            chars.list_o_chars["HERO"]["mp"] += .5
            points -= 1
        elif stat == "ATK":
            chars.list_o_chars["HERO"]["atk"] += 1
            points -= 1
        elif stat == "DEF":
            chars.list_o_chars["HERO"]["def"] += 1
            points -= 1
        elif stat == "SPD":
            chars.list_o_chars["HERO"]["spd"] += 1
            points -= 1
        else:
            print("Invalid stat")
    print("Here are your current stats: ", chars.list_o_chars["HERO"])

enemy = stats.list_o_stats["Enemy"]
current_foe = bad.list_o_enemies["Orc"]

def hero_prep():
    stats.list_o_stats["HERO"]["hp"] = chars.list_o_chars["HERO"]["hp"]
    stats.list_o_stats["HERO"]["mp"] = chars.list_o_chars["HERO"]["mp"]
    stats.list_o_stats["HERO"]["damage"] = chars.list_o_chars["HERO"]["atk"] * 2
    stats.list_o_stats["HERO"]["damage"] = round(stats.list_o_stats["HERO"]["damage"])
    stats.list_o_stats["HERO"]["defense"] = chars.list_o_chars["HERO"]["def"] * 0.75
    stats.list_o_stats["HERO"]["defense"] += chars.list_o_chars["HERO"]["def"] / 2
    stats.list_o_stats["HERO"]["defense"] = math.floor(stats.list_o_stats["HERO"]["defense"])
    stats.list_o_stats["HERO"]["go"] = chars.list_o_chars["HERO"]["spd"]
    stats.list_o_stats["HERO"]["dodge"] = chars.list_o_chars["HERO"]["spd"] / 100
    stats.list_o_stats["HERO"]["crit"] = chars.list_o_chars["HERO"]["spd"] / 100

def enemy_prep():
    enemy["hp"] = current_foe["hp"]
    enemy["mp"] = current_foe["mp"]
    enemy["damage"] = current_foe["atk"] * 2
    enemy["damage"] = round(enemy["damage"])
    enemy["defense"] = current_foe["def"] * 0.75
    enemy["defense"] += current_foe["def"] / 2
    enemy["defense"] = math.floor(enemy["defense"])
    enemy["go"] = current_foe["spd"]
    enemy["dodge"] = current_foe["spd"] / 100
    enemy["crit"] = current_foe["spd"] / 100



# char_create()
hero_prep()
enemy_prep()
print("\n")


def combat():
    global fighting
    fighting = True
    global hero_attack_damage
    hero_attack_damage = stats.list_o_stats["HERO"]["damage"] - enemy["defense"]
    global enemy_attack_damage
    enemy_attack_damage = enemy["damage"] - stats.list_o_stats["HERO"]["defense"]
    while fighting:
        if enemy_attack_damage < 0:
            enemy_attack_damage = 1
        if hero_attack_damage < 0:
            hero_attack_damage = 1
        if stats.list_o_stats["HERO"]["hp"] <= 0:
            print("You have died")
            fighting = False
            break
        elif enemy["hp"] <= 0:
            print(f"You have defeated the {current_foe['name']}")
            print("The enemy has", enemy["hp"], "HP left")
            fighting = False
            break
        else:
            if stats.list_o_stats["HERO"]["go"] >= enemy["go"]:
                print("You attack first")
                enemy["hp"] -= hero_attack_damage
                print("You did", hero_attack_damage, "damage")
                if enemy["hp"] <= 0:
                    print("The enemy has", enemy["hp"], "HP left")
                    print(f"You have defeated the {current_foe['name']}")
                    fighting = False
                    break
                else:
                    print("The enemy attacks")
                    stats.list_o_stats["HERO"]["hp"] -= enemy_attack_damage
                    print("The enemy did", enemy_attack_damage, "damage")
                    print("You have", stats.list_o_stats["HERO"]["hp"], "HP left")
                    if stats.list_o_stats["HERO"]["hp"] <= 0:
                        print("You have died")
                        fighting = False
                        break
            else:
                print("The enemy attacks first")
                stats.list_o_stats["HERO"]["hp"] -= enemy_attack_damage
                print("The enemy did", enemy_attack_damage, "damage")
                print("You have", stats.list_o_stats["HERO"]["hp"], "HP left")
                if stats.list_o_stats["HERO"]["hp"] <= 0:
                    print("You have died")
                    fighting = False
                    break
                else:
                    print("You attack")
                    enemy["hp"] -= hero_attack_damage
                    print("You did", hero_attack_damage, "damage")
                    if enemy["hp"] <= 0:
                        print("The enemy has", enemy["hp"], "HP left")
                        print(f"You have defeated the {current_foe['name']}")
                        fighting = False
                        break



combat()
print("\n")
current_foe = bad.list_o_enemies["Goblin"]
enemy_prep()
combat()

print("\n")
current_foe = bad.list_o_enemies["Troll"]
enemy_prep()
combat()

print("\n")
current_foe = bad.list_o_enemies["Skeleton"]
enemy_prep()
combat()