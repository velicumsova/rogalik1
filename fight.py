class Unit:
    def __init__(self):
        self.max_health = 100
        self.current_health = self.max_health
        self.attack = 10
        self.armor = 0
        self.current_armor = 0
        self.agility = 10

    def get_damage(self, attack):
        self.current_health -= attack

    def make_damage(self, other):
        other.get_damage(self.attack)


class Player(Unit):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.money = 0
        self.level_exp = 10
        self.current_exp = 0

    def level_up(self, experience):
        self.current_exp += experience
        self.level_exp = self.level_exp * 10


class Enemy(Unit):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.money = 10


class Knight(Enemy):
    def __init__(self):
        super().__init__()
        self.agility = self.agility * 1.3
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
    def __init__(self):
        super().__init__()
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
    def __init__(self):
        super().__init__()
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