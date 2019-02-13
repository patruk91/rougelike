

def handle_interaction(character, map_iterator):
    damage = 10
    if character == "W":
        pass
    #     loot = items.items.weapons()
    #     char_stats["ATC"] += loot[1]
    #     inventory.inventory.add_to_inventory(inv, loot)
    #     del inv[loot[1]]
    # elif character == "F":
    #     loot = items.items.food()
    #     if char_stats["HP"] < 100:
    #         char_stats["HP"] += loot[1]
    #     if char_stats["HP"] > 100:
    #         char_stats["HP"] = 100
    # elif character == "C":
    #     loot = items.items.clotches()
    #     char_stats["DEF"] += loot[1]
    # elif character == "&":
    #     char_stats = hot_cold.fight(char_stats, damage)
    #     if char_stats["HP"] <= 0:
    #         end_screen = data_manager.load_asci_art("asci_art/game_over.txt")
    #         print(end_screen)
    elif character == "D":
        map_iterator += 1
    return map_iterator
