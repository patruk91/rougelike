import movement
import interaction
import hot_cold
import items.items
import data_manager
import common
import ui
import os



HERO_BEGIN_POSITION = [[1, 20], [1, 13], [1, 20], [1, 16]]
HERO_END_POSITION = [[2, 20], [2, 13], [2, 20], [2, 16]]
LEVELS_NAME = ['levels/level1.txt', 'levels/level2.txt', 'levels/level3.txt', 'levels/level4.txt']


def engine_work(char_stats, inv, map_iterator):
    get_char = ""
    hero_coordinates = HERO_BEGIN_POSITION[map_iterator]
    level_map = data_manager.get_maps_from_file(LEVELS_NAME[map_iterator])
    level_map = movement.place_new_hero_position(level_map, hero_coordinates)
    ui.display_level_map(level_map, char_stats, inv)
    game_won = True
    while get_char != "q" and game_won:
        get_char = movement.get_char_in_terminal()
        os.system('clear')
        new_hero_coordinates = movement.handle_coordinates(get_char, hero_coordinates, LEVELS_NAME[map_iterator])
        if common.check_if_item_interaction(new_hero_coordinates, level_map):
            character = common.get_character_at_position(level_map, new_hero_coordinates)
            map_iterator = interaction.increment_map_iterator(map_iterator, character)
            if map_iterator < 4 and character == "D":
                level_map = data_manager.get_maps_from_file(LEVELS_NAME[map_iterator])
                hero_coordinates = HERO_BEGIN_POSITION[map_iterator]

            game_won = handle_game_won_boss(char_stats, character, game_won, map_iterator)
            char_stats = interaction.handle_interaction(character, map_iterator, items, char_stats, inv)


            if game_won != False:
                level_map = movement.update_map(get_char, level_map, new_hero_coordinates, hero_coordinates)
                ui.display_level_map(level_map, char_stats, inv)

        else:
            level_map = movement.update_map(get_char, level_map, hero_coordinates, new_hero_coordinates)
            ui.display_level_map(level_map, char_stats, inv)
            hero_coordinates = new_hero_coordinates


def handle_game_won_boss(char_stats, character, game_won, map_iterator):
    if character == "D" and map_iterator == 4:

        damage = 15
        char_stats = hot_cold.fight(char_stats, damage)
        if char_stats["HP"] > 0:
            end_screen = data_manager.load_ascii_art("ascii_art/win.txt")
            print(end_screen)
            game_won = False

        else:
            end_screen = data_manager.load_ascii_art("ascii_art/game_over.txt")
            print(end_screen)
            game_won = False
    return game_won
