import console
from game_animations import ChooseHero, DrawLevel

if __name__ == '__main__':
    # Объект main_console - единственный способ вывода в консоль. Он должен передоваться во все другие объекты
    main_console = console.Console()
    lever_drawer = DrawLevel(main_console)

    # Выбор класса персонажа
    hero_class = ChooseHero(main_console).choice_hero()

    for i in range(1, 100):
        lever_drawer.draw_level_screen(i)
        main_console.clear_buffer()
        main_console.get_char()




