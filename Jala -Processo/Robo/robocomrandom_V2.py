import random

class Part():
    def __init__(self, name: str, attack_level=0, defense_level=0, energy_consumption=0):
        self.name = name
        self.attack_level = attack_level
        self.defense_level = defense_level
        self.energy_consumption = energy_consumption

    def get_status_dict(self):
        formatted_name = self.name.replace(" ", "_").lower()
        return {
            "{}_name".format(formatted_name): self.name.upper(),
            "{}_status".format(formatted_name): self.is_available(),
            "{}_attack".format(formatted_name): self.attack_level,
            "{}_defense".format(formatted_name): self.defense_level,
            "{}_energy_consump".format(formatted_name): self.energy_consumption,
        }

    def reduce_defense(self, attack_level):
        self.defense_level -= attack_level
        if self.defense_level <= 0:
            self.defense_level = 0
            
    def is_available(self):
        return self.defense_level <= 0


class Robot:
    def __init__(self, name, color_code):
        self.name = name
        self.color_code = color_code
        self.energy = 100
        self.parts = [
            Part("Head", attack_level=5, defense_level=10, energy_consumption=5),
            Part("Weapon", attack_level=15, defense_level=0, energy_consumption=10),
            Part("Left Arm", attack_level=3, defense_level=20, energy_consumption=10),
            Part("Right Arm", attack_level=6, defense_level=20, energy_consumption=10),
            Part("Left Leg", attack_level=4, defense_level=20, energy_consumption=15),
            Part("Right Leg", attack_level=8, defense_level=20, energy_consumption=15),
        ]

    def print_status(self):
        print(self.color_code)
        str_robot = robot_art.format(**self.get_part_status())
        self.greet()
        self.print_energy()
        print(str_robot)
        print(colors["White"]) 

    def greet(self):
        print(f"Hello, my name is {self.name}")

    def print_energy(self):
        print(f"We have {self.energy} percent energy left")

    def get_part_status(self):
        part_status = {}
        for part in self.parts:
            status_dict = part.get_status_dict()
            part_status.update(status_dict)
        return part_status

    def is_there_available_part(self):
        for part in self.parts:
            if part.is_available():
                return True
        return False

    def is_on(self):
        return self.energy >= 0

    def attack(self, enemy_robot, part_to_use, part_to_attack):
        damage = random.randint(1, 90)
        enemy_robot.energy -= damage 
        enemy_robot.parts[part_to_attack].reduce_defense(damage)
        self.energy -= self.parts[part_to_use].energy_consumption
        print(f"{self.name} causou {damage} de dano a {enemy_robot.name}.")
        self.energy = max(0, self.energy)

    
def get_part_status(self):
    part_status = {}
    for part in self.parts:
        status_dict = part.get_status_dict()
        part_status.update(status_dict)
    return part_status

def play():
    playing = True
    print("Welcome to the game!")
    print("Datas for player 1: ")
    robot_one = build_robot(colors, 1)
    print("Datas for player 2: ")
    robot_two = build_robot(colors, 2)
    current_robot = robot_one
    enemy_robot = robot_two
    rount = 0

    while playing:
        if rount % 2 == 0:
            current_robot = robot_one
            enemy_robot = robot_two
        else:
            current_robot = robot_two
            enemy_robot = robot_one
        current_robot.print_status()

        def get_valid_integer_input(prompt):
            while True:
                try:
                    value = int(input(prompt))
                    if value <= 5:
                        return value
                    else:
                        print("O número precisa ser entre 0 e 5")
                except ValueError:
                    print("Valor invalido, tente usar apenas números")

        part_to_use = get_valid_integer_input(f"{current_robot.name}, Qual parte devo usar para atacar? Escolha o número da parte do inimigo: ")
        part_to_attack = get_valid_integer_input(f"{current_robot.name}, Qual parte do inimigo devemos atacar? Escolha o número da parte do inimigo para atacar: ")
        enemy_robot.print_status()
        current_robot.attack(enemy_robot, part_to_use, part_to_attack)
        rount += 1
        if not enemy_robot.is_on() or enemy_robot.is_there_available_part() == False:
            playing = False
            print("Congratulations, you won")

    if robot_one.energy > robot_two.energy:
        print(f"{robot_one.name} wins with {robot_one.energy} energy!")
    elif robot_two.energy > robot_one.energy:
        print(f"{robot_two.name} wins with {robot_two.energy} energy!")
 
        

def choose_color(colors, robot_name):
    available_colors = colors
    print("Available colors: ")
    for key, value in available_colors.items():
        print(value, key)
    print(colors["White"])
    print(f"{robot_name}, choose a color:")
    while True:
        chosen_color = input("Choose a color: ").capitalize()
        if chosen_color in available_colors:
            color_code = available_colors[chosen_color]
            return color_code
        else:
            print(f"{chosen_color} é invalido, Escolha uma cor que estaja na lista")

def build_robot(colors, robot_number):
    robot_name = input(f"Robot {robot_number}° name: ")
    color_code = choose_color(colors, robot_name)
    robot = Robot(robot_name, color_code)
    robot.print_status()
    return robot

robot_art = r"""
      0: {head_name}
      Is available: {head_status}
      Attack: {head_attack}                              
      Defense: {head_defense}
      Energy consumption: {head_energy_consump}
              ^
              |                  |1: {weapon_name}
              |                  |Is available: {weapon_status}
     ____     |    ____          |Attack: {weapon_attack}
    |oooo|  ____  |oooo| ------> |Defense: {weapon_defense}
    |oooo| '    ' |oooo|         |Energy consumption: {weapon_energy_consump}
    |oooo|/\_||_/\|oooo|          
    `----' / __ \  `----'           |2: {left_arm_name}
   '/  |#|/\/__\/\|#|  \'           |Is available: {left_arm_status}
   /  \|#|| |/\| ||#|/  \           |Attack: {left_arm_attack}
  / \_/|_|| |/\| ||_|\_/ \          |Defense: {left_arm_defense}
 |_\/    O\=----=/O    \/_|         |Energy consumption: {left_arm_energy_consump}
 <_>      |=\__/=|      <_> ------> |
 <_>      |------|      <_>         |3: {right_arm_name}
 | |   ___|======|___   | |         |Is available: {right_arm_status}
// \\ / |O|======|O| \  //\\        |Attack: {right_arm_attack}
|  |  | |O+------+O| |  |  |        |Defense: {right_arm_defense}
|\/|  \_+/        \+_/  |\/|        |Energy consumption: {right_arm_energy_consump}
\__/  _|||        |||_  \__/        
      | ||        || |          |4: {left_leg_name} 
     [==|]        [|==]         |Is available: {left_leg_status}
     [===]        [===]         |Attack: {left_leg_attack}
      >_<          >_<          |Defense: {left_leg_defense}
     || ||        || ||         |Energy consumption: {left_leg_energy_consump}
     || ||        || || ------> |
     || ||        || ||         |5: {right_leg_name}
   __|\_/|__    __|\_/|__       |Is available: {right_leg_status}
  /___n_n___\  /___n_n___\      |Attack: {right_leg_attack}
                                |Defense: {right_leg_defense}
                                |Energy consumption: {right_leg_energy_consump}

"""

colors = {
    "Black": '\x1b[90m',
    "Blue": '\x1b[94m',
    "Cyan": '\x1b[96m',
    "Green": '\x1b[92m',
    "Magenta": '\x1b[95m',
    "Red": '\x1b[91m',
    "White": '\x1b[97m',
    "Yellow": '\x1b[93m',
}

play()
