import random
class Unit:
    def __init__(self) -> None:
        self.max_health = 100
        self.current_health = self.max_health
        self.attack = 10
        self.armor = 0
        self.current_armor = self.armor
        self.agility = 10
        self.estus = 3
    def get_damage(self, attack) -> None:
        self.current_health -= attack

    def make_damage(self, other) -> None:
        other.get_damage(self.attack)


class Player(Unit):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.money = 0
        self.exp_for_level = 10
        self.current_exp = 0

    def level_up(self, experience) -> None:
        self.current_exp += experience
        if self.current_exp >= self.exp_for_level:
            # Если опыта набралось нужное кол-во для поднятия уровня, то поднимаем уровень и кол-во exp для нового уровня
            self.current_exp = self.current_exp - self.exp_for_level
            self.level += 1
            self.exp_for_level = self.level * 10


class Enemy(Unit):
    money_after_death = 10
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.money = 10


class Knight(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.exp_after_death = 20
        self.agility = self.agility * 1.5
        self.max_health = self.max_health * 0.7

    knight_ascii = r'''
                   _.--.    .--._
                 ."  ."      ".  ".
                ;  ."    /\    ".  ;
                ;  '._,-/  \-,_.`  ;
                \  ,`  / /\ \  `,  /
                 \/    \/  \/    \/
                 ,=_    \/\/    _=,
                 |  "_   \/   _"  |
                 |_   '"-..-"'   _|
                 | "-.        .-" |
                 |    "\    /"    |
                 |      |  |      |
         ___     |      |  |      |     ___
     _,-",  ",   '_     |  |     _'   ,"  ,"-,_
   _(  \  \   \"=--"-.  |  |  .-"--="/   /  /  )_
 ,"  \  \  \   \      "-'--'-"      /   /  /  /  ".
!     \  \  \   \                  /   /  /  /     !
!      \  \  \   \                /   /  /  /      !
'''

class Skeleton(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.exp_after_death = 15
        self.max_health = self.max_health * 1.3
        self.agility = self.agility * 0.4

    skeleton_ascii = r'''
                              _.--""-._
  .                         ."         ".
 / \    ,^.         /(     Y             |      )\
/   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
|        :|    `>   '.     l_..-------.._l      .'
|      __l;__ .'      "-.__.||_.-'v'-._||`"----"
 \  .-' | |  `              l._       _.'
  \/    | |                   l`^^'^^'j
        | |                _   \_____/     _
        j |               l `--__)-'(__.--' |
        | |               | /`---``-----'"1 |  ,-----.
        | |               )/  `--' '---'   \'-'  ___  `-.
        | |              //  `-'  '`----'  /  ,-'   I`.  \
      _ L |_            //  `-.-.'`-----' /  /  |   |  `. \
     '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
      `._;/7(-.......'  /        ) (     |  |            | |
      `._;l _'--------_/        )-'/     :  |___.    _._./ ;
        | |                 .__ )-'\  __  \  \  I   1   / /
        `-'                /   `-\-(-'   \ \  `.|   | ,' /
                           \__  `-'    __/  `-. `---'',-'
                              )-._.-- (        `-----'
    '''

class Demon(Enemy):
    def __init__(self) -> None:
        super().__init__()
        self.exp_after_death = 15
        self.attack = self.attack * 1.3
        self.armor = self.armor * 0.7

    demon_ascii = r'''
 *                       *
    *                 *
   )       (\___/)     (
* /(       \ (. .)     )\ *
  # )      c\   >'    ( #
   '         )-_/      '
 \\|,    ____| |__    ,|//
   \ )  (  `  ~   )  ( /
    #\ / /| . ' .) \ /#
    | \ / )   , / \ / |
     \,/ ;;,,;,;   \,/
      _,#;,;;,;,
     /,i;;;,,;#,;
    //  %;;,;,;;,;
   ((    ;#;,;%;;,,
  _//     ;,;; ,#;,
 /_)      #,;    ))
         //      \|_
         \|_      |#\
          |#\      -"
'''


class Seller(Unit):
    pass
    # TODO: Добавить продавца

def battle(player, enemy):  # Атака | Блок | Эстус
    status = 1
    player_condition = True  # True = Life; False - Death
    while player.current_health > 0 and enemy.current_health > 0:
        status += 1

        if status % 2 == 0:  # Мой ход
            player_solution = int(input("Твой ход: "))
            if player_solution == 1:  # Атака
                dice = random.randint(1, 20)
                if 1 <= dice <= 15:
                    enemy.get_damage(player.attack)
                elif 16 <= dice <= 20:
                    enemy.get_damage(2 * player.attack)

                if enemy.current_health <= 0:  # Смерть врага
                    player.level_up(enemy.exp_after_death)
                    player.money += enemy.money_after_death
                    print(f"Победил игрок")
            if player_solution == 2:  # Блок
                player.current_armor += 5
                # TODO: добавить взаимодействие с броней и сделать броню на определенное количество ходов

            if player_solution == 3:  # Эстус
                difference_in_health = player.max_health - player.current_health
                if difference_in_health >= 10 and player.estus > 0:
                    player.current_health += 10
                    player.estus -= 1
                if difference_in_health < 10 and player.estus > 0:
                    player.current_health += difference_in_health
                    player.estus -= 1

            if player_solution == 4:  # Способность
                pass
                # TODO: добавить действия связанные с механикой героя


        if status % 2 != 0:  # Ход врага
            enemy_solution = random.randint(1, 4)

            if enemy_solution == 1:  # Атака
                dice = random.randint(1, 20)
                if 1 <= dice <= 15:
                    player.get_damage(enemy.attack)
                if 16 <= dice <= 20:
                    player.get_damage(2 * enemy.attack)
                if player.current_health <= 0:
                    player_condition = False
                    print(f"Победил враг")
                    return player_condition

            if enemy_solution == 2:  # Блок
                enemy.current_armor += 5
                # TODO: добавить взаимодействие с броней и сделать броню на определенное количество ходов

            if enemy_solution == 3:  # Способность
                pass
                # TODO: добавить действия связанные с механикой героя

me = Player()
enemy = Demon()
battle(me, enemy)