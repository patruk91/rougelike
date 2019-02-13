import data_manager
import ui
import common
import character_creation.character_creation as char_cr
import os
import engine
import interaction
import hot_cold




def menu():
    HERO_BEGIN_POSITION = [[1, 20], [1, 13], [1, 20], [1, 16]]
    HERO_END_POSITION = [[2, 20], [2, 13], [2, 20], [2, 16]]
    LEVELS_NAME = ['levels/level1.txt', 'levels/level2.txt', 'levels/level3.txt', 'levels/level4.txt']
    map_iterator = 0
    os.system('clear')
    while True:
        print(data_manager.load_asci_art("asci_art/menu_art.txt"))
        answer = ui.menu_option()
        if common.validate_string_input(answer, condition=["1", "2", "3", "4"]):
            if answer == "1":
                char_stats = char_cr.create_character(5, {}, True)
                inv = {}
                os.system('clear')

                # start engine module
                get_char = ""
                hero_coordinates = HERO_BEGIN_POSITION[map_iterator]
                level_map = data_manager.get_maps_from_file(LEVELS_NAME[map_iterator])
                level_map = engine.place_new_hero_position(level_map, hero_coordinates)
                ui.display_level_map(level_map)
                game_won = True
                while get_char != "q" and game_won:
                    get_char = engine.get_char_in_terminal()
                    os.system('clear')
                    new_hero_coordinates = engine.handle_coordinates(get_char, hero_coordinates, LEVELS_NAME[map_iterator])
                    if common.check_if_item_interaction(new_hero_coordinates, level_map):
                        character = common.get_character_at_position(level_map, new_hero_coordinates)
                        map_iterator = interaction.handle_interaction(character, map_iterator)

                        if character == "D":
                            if map_iterator < 4:
                                level_map = data_manager.get_maps_from_file(LEVELS_NAME[map_iterator])
                                hero_coordinates = HERO_BEGIN_POSITION[map_iterator]
                            else:
                                damage = 15
                                char_stats = hot_cold.fight(char_stats, damage)
                                if char_stats["HP"] > 0:
                                    end_screen = data_manager.load_asci_art("asci_art/win.txt")
                                    print(end_screen)
                                    game_won = False

                                else:
                                    end_screen = data_manager.load_asci_art("asci_art/game_over.txt")
                                    print(end_screen)
                                    game_won = False

                        if game_won != False:
                            level_map = engine.update_map(get_char, level_map, new_hero_coordinates, hero_coordinates)
                            ui.display_level_map(level_map)

                    else:
                        level_map = engine.update_map(get_char, level_map, hero_coordinates, new_hero_coordinates)
                        ui.display_level_map(level_map)
                        hero_coordinates = new_hero_coordinates

            elif answer == "2":
                pass
            elif answer == "3":
                pass
            elif answer == "4":
                exit()


def main():
    menu()

if __name__ == "__main__":
    main()
