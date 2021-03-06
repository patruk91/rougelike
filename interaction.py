import inventory.inventory
import data_manager
import hot_cold


def handle_interaction(character, items, char_stats, inv):
    if character == "W":
        loot = items.items.weapons()
        char_stats["ATC"] += loot[1]
        inventory.inventory.add_to_inventory(inv, loot)
    elif character == "F":
        loot = items.items.food()
        if char_stats["HP"] < 100:
            char_stats["HP"] += loot[1]
        if char_stats["HP"] > 100:
            char_stats["HP"] = 100
    elif character == "C":
        loot = items.items.clotches()
        char_stats["DEF"] += loot[1]
        inventory.inventory.add_to_inventory(inv, loot)
    elif character == "&":
        damage = 10
        file_name = "ascii_art/fight_with_mob.txt"
        char_stats = hot_cold.fight(char_stats, damage, file_name)
        if char_stats["HP"] <= 0:
            end_screen = data_manager.load_ascii_art("ascii_art/game_over.txt")
            print(end_screen)
    return inv


def increment_map_iterator(map_iterator, character):
    if character == "D":
        map_iterator += 1
    return map_iterator
