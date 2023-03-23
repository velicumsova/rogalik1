import curses

from console import Console


class Hero:
    def __init__(self):
        # assci_art не больше 50 символов в ширену и 40 в высоту
        self.assci_art = ''
        self.description = ''
        self.class_name = 'Нет'

    def get_assci_art_size(self):
        A = self.assci_art.split('\n')
        if len(A) == 0:
            return 0, 0
        x = 0
        for i in A:
            x = max(len(i), x)
        y = len(A)
        return x, y


class HeroWarrior(Hero):
    def __init__(self):
        super().__init__()
        self.assci_art = r'''       .---.
      /_____\
      ( '.' )
       \_-_/_
    .-"`'V'//-.
   / ,   |// , \
  / /|Ll //Ll|\ \
 / / |__//   | \_\
 \ \/---|[]==| / /
  \/\__/ |   \/\/
   |/_   | Ll_\|
     |`^"""^`|
     |   |   |
     |   |   |
     |   |   |
     |   |   |
     L___l___J
      |_ | _|
     (___|___)'''
        self.description = "Воин - сила и мощь. Отличный выбор."
        self.class_name = 'Warrior'


class HeroJester(Hero):
    def __init__(self):
        super().__init__()
        self.assci_art = r'''          ___
         /\  \
        /  \/ \
   ___  \   O /  ___
  /    \ \   / /    \
 /   __ -    -  __   \
/___/ | (0)  (0)| \___\
O  ___|    ^    |___  O
 /     \  ===  /    \
/   /\  \_____/ /\   \
\_ / /          \ \_ /
O   /   /\   /\  \  O
     \ /  \ /  \ /
      O    O    O
'''
        self.description = "Клоун - ловкость и скорость. Хороший выбор?"
        self.class_name = 'Jester'


class HeroTank(Hero):
    def __init__(self):
        super().__init__()
        self.assci_art = r"""      /.--.\
      |====|
      |`::`|
  .-;`\..../`;_.-^-._
 /  |...::..|`   :   `|
|   /'''::''|   .:.   |
;--'\   ::  |..:::::..|
<__> >._::_.| ':::::' |
|  |/   ^^  |   ':'   |
\::/|       \    :    /
|||\|        \   :   /
''' |___/\___|`-.:.-`
     \_ || _/    `
     <_ >< _>
     |  ||  |
     |  ||  |
    _\.:||:./_
   /____/\____\
"""
        self.description = "Без комментариев. Лучший выбор."
        self.class_name = 'Tank'


class ChooseHero:
    def __init__(self, console_: Console):
        self.console = console_

        self.classes = [HeroWarrior(), HeroJester(), HeroTank()]
        if len(self.classes) != 3:
            raise Exception(f'Должно быть ровно 3 класса на выбор')

    def draw(self, selected_hero):
        self.console.clear()
        self.console.write_border(0, 0, 150, 49)
        for i in range(len(self.classes)):
            assci_x_size, assci_y_size = self.classes[i].get_assci_art_size()
            start_position_x = (self.console.max_width // 3) * i \
                               + ((self.console.max_width // 3 - assci_x_size) // 2)

            start_position_y = (40 - assci_y_size) // 2

            self.console.write_object_by_long_string(start_position_x, start_position_y, self.classes[i].assci_art)
            if selected_hero == i:
                self.console.write_border(start_position_x-1, start_position_y-1, assci_x_size+2, assci_y_size+2)

                self.console.write_line((self.console.max_width-len(self.classes[i].description))//2,
                                        40, self.classes[i].description)

    def choice_hero(self):
        selected = 0
        self.draw(selected)
        while True:
            key = self.console.get_char()

            if key == curses.KEY_LEFT:
                selected -= 1
            elif key == curses.KEY_RIGHT:
                selected += 1
            elif key == 10:
                return self.classes[selected].class_name
            else:
                continue

            selected = max(selected, 0)
            selected = min(2, selected)
            self.draw(selected)








