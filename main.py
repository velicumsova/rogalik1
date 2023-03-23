import console
from game_animations import ChooseHero

if __name__ == '__main__':
    # Объект main_console - единственный способ вывода в консоль. Он должен передоваться во все другие объекты
    main_console = console.Console()

    hero_class = ChooseHero(main_console).choice_hero()
    # код игры ... (Создание объектов и вызов их методов. Только высокоуровневые функции)




