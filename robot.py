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

 

class Part():
    """
    Clase que representa una parte de un robot.
    """

 

    def __init__ (self, name: str, attack_level=0, defense_level=0, energy_consumption=0):
        """
        Inicializa una parte del robot con un nombre, nivel de ataque, nivel de defensa y consumo de energía.
        """
        self.name = name  # Asigna el nombre a la parte del robot
        self.attack_level = attack_level  # Asigna el nivel de ataque a la parte del robot
        self.defense_level = defense_level  # Asigna el nivel de defensa a la parte del robot
        self.energy_consumption = energy_consumption  # Asigna el consumo de energía a la parte del robot

 

    def get_status_dict(self):
        """
        Devuelve un diccionario con el estado de la parte del robot.
        """
        formatted_name = self.name.replace(" ", "_").lower()  # Formatea el nombre de la parte para su uso en el diccionario
        return {
            "{}_name".format(formatted_name): self.name.upper(),
            "{}_status".format(formatted_name): self.is_available(),
            "{}_attack".format(formatted_name): self.attack_level,
            "{}_defense".format(formatted_name): self.defense_level,
            "{}_energy_consump".format(formatted_name): self.energy_consumption,
        }  # Retorna un diccionario con el estado de la parte, incluyendo su nombre, estado de disponibilidad, nivel de ataque, nivel de defensa y consumo de energía

 

    def is_available(self):
        """
        Verifica si la parte del robot está disponible (tiene nivel de defensa mayor que cero).
        """
        return not self.defense_level <= 0  # Retorna True si el nivel de defensa de la parte es mayor que cero, lo que indica que está disponible

 

colors = {
    "Black": '\x1b[90m',
    "Blue": '\x1b[94m',
    "Cyan": '\x1b[96m',
    "Green": '\x1b[92m',
    "Magneta": '\x1b[95m',
    "Red": '\x1b[91m',
    "White": '\x1b[97m',
    "Yellow": '\x1b[93m',    
}


import random
import itertools

class Robot():
    """
    Clase que representa un robot.
    """

    def __init__ (self, name, color_code):
        """
        Inicializa un robot con un nombre y un código de color.
        """
        self.name = name  # Asigna el nombre al robot
        self.color_code = color_code  # Asigna el código de color al robot
        self.energy = 100  # Inicializa la energía del robot en 100
        self.parts = [
            Part("Head", attack_level=5, defense_level=25, energy_consumption=5),
            Part("Weapon", attack_level=15, defense_level=25, energy_consumption=10),
            Part("Left_Arm", attack_level=6, defense_level=25, energy_consumption=10),
            Part("Right_Arm", attack_level=3, defense_level=25, energy_consumption=10),
            Part("Left_Leg", attack_level=8, defense_level=25, energy_consumption=15),
            Part("Right_Leg", attack_level=4, defense_level=25, energy_consumption=15),
        ]  # Crea una lista de partes del robot con sus respectivos niveles de ataque, defensa y consumo de energía
        self.inventory = {}

    def greet(self):
        """
        Saluda al robot.
        """
        print("Hello, my name is", self.name)

    def print_energy(self):
        """
        Imprime la energía actual del robot.
        """
        print("We have", self.energy, "percent energy left")

    def attack(self, enemy_robot, part_to_use, part_to_attack):
        """
        Realiza un ataque a otro robot utilizando una parte propia y atacando una parte del robot enemigo.
        """
        enemy_part = enemy_robot.parts[part_to_attack]
        attack_level = self.parts[part_to_use].attack_level
        # Calcula el daño al robot enemigo
        enemy_part.defense_level -= attack_level
        # Desprende partes dependiendo del lugar atacado
        if enemy_part.name == "Head":
            num_items = random.randint(1, 5)
            self.add_to_inventory("synthovisor cortex", num_items, attack_bonus=5)
        elif enemy_part.name == "Left_Arm" or enemy_part.name == "Right_Arm":
            num_items = random.randint(1, 5)
            self.add_to_inventory("cyber module", num_items, defense_bonus=5)
        elif enemy_part.name == "Left_Leg" or enemy_part.name == "Right_Leg":
            num_items = random.randint(1, 5)
            self.add_to_inventory("elemental piece", num_items, defense_bonus=100)
        elif enemy_part.name == "Weapon":
            num_items = random.randint(1, 5)
            self.add_to_inventory("electro arrows", num_items, attack_bonus=10)

        self.energy -= self.parts[part_to_use].energy_consumption

    def add_to_inventory(self, item_name, quantity, attack_bonus=None, defense_bonus=None):
        """
        Agrega elementos al inventario del robot.
        """
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity

        if attack_bonus is not None:
            self.inventory[item_name + "_attack_bonus"] = attack_bonus
            
        if defense_bonus is not None:
            self.inventory[item_name + "_defense_bonus"] = defense_bonus
            
        print("You have obtained a robot piece: {} - {}".format(item_name, self.get_item_description(item_name)))

    def get_item_description(self, item_name):
        """
        Devuelve una descripción del ítem basado en su nombre.
        """
        if item_name == "synthovisor cortex":
            return "A synthetic visual enhancement device that provides a +5 attack bonus."
        elif item_name == "cyber module":
            return "An advanced cybernetic module that provides a +5 defense bonus."
        elif item_name == "elemental piece":
            return "A mysterious elemental piece that grants impenetrable defense for one turn."
        elif item_name == "electro arrows":
            return "Electrically charged arrows that provide a +10 attack bonus for one turn."
        else:
            return "Unknown robot piece."

    def is_on(self):
        """
        Verifica si el robot está encendido (tiene energía mayor o igual a cero).
        """
        return self.energy >= 0

    def is_there_available_parts(self):
        """
        Verifica si hay partes disponibles en el robot.
        """
        for part in self.parts:
            if part.is_available():
                return True
        return False

    def fuse_power(self):
        """
        Combina ítems del inventario con una parte del robot para aplicar un bonus.
        """
        print("Inventory items:")
        # Verificar si el inventario está vacío
        if not self.inventory:
            print("No hay objetos para combinar")
            return
        # Mostrar los ítems y su cantidad en el inventario
        for item, quantity in self.inventory.items():
            print("{} - Quantity: {}".format(item, quantity))
        item_to_fuse = input("Choose an item to fuse (type 'done' to finish): ")
        parts_to_boost = []
        # Iterar hasta que se introduzca 'done' para finalizar la fusión de ítems
        while item_to_fuse != "done":
            part_to_boost = input("Choose a part to boost (1-6): ")
            part_to_boost = int(part_to_boost)
            parts_to_boost.append(part_to_boost)
            # Llamar al método apply_bonus para aplicar los bonus a la parte del robot seleccionada
            self.apply_bonus(item_to_fuse, part_to_boost)
            item_to_fuse = input("Choose another item to fuse (type 'done' to finish): ")
        # Mostrar el diccionario actualizado de las partes del robot
        print("Diccionario de las partes del robot:")

    def apply_bonus(self, item_to_fuse, part_to_boost):
        """
        Aplica el bonus de un ítem a una parte del robot.
        Parámetros:
        - item_to_fuse: El nombre del ítem que se va a fusionar.
        - part_to_boost: El número de la parte del robot a la que se va a aplicar el bonus.
        """
        item_name = item_to_fuse.replace("_attack_bonus", "").replace("_defense_bonus", "")
        # Verificar si el ítem está en el inventario del robot
        if item_name in self.inventory:
            if "{}_attack_bonus".format(item_name) in self.inventory:
                # Obtener el bonus de ataque del ítem
                attack_bonus = self.inventory["{}_attack_bonus".format(item_name)]
                # Aumentar el nivel de ataque de la parte seleccionada
                self.parts[part_to_boost - 1].attack_level += attack_bonus
            if "{}_defense_bonus".format(item_name) in self.inventory:
                # Obtener el bonus de defensa del ítem
                defense_bonus = self.inventory["{}_defense_bonus".format(item_name)]
                # Aumentar el nivel de defensa de la parte seleccionada
                self.parts[part_to_boost - 1].defense_level += defense_bonus
            # Descontar el ítem del inventario
            self.inventory[item_to_fuse] -= 1
            # Imprimir un mensaje de confirmación
            print("Applied bonus from item '{}' to part '{}'".format(item_name, self.parts[part_to_boost - 1].name))

    def print_status(self):
        """
        Imprime el estado actual del robot, incluyendo su nombre, energía y partes.
        """
        print(self.color_code)  # Imprime el código de color del robot
        str_robot = robot_art.format(**self.get_part_status())  # Obtiene el estado de las partes del robot en forma de diccionario y lo formatea en una cadena
        self.greet()  # Saluda al robot
        self.print_energy()  # Imprime la energía del robot
        print(str_robot)  # Imprime la representación visual del robot
        print(colors["White"])  # Restablece el color de la consola a blanco

    def get_part_status(self):
        """
        Devuelve un diccionario con el estado de todas las partes del robot.
        """
        part_status = {}  # Diccionario para almacenar el estado de las partes del robot
        for part in self.parts:  # Itera sobre todas las partes del robot
            status_dict = part.get_status_dict()  # Obtiene el estado de una parte en forma de diccionario
            part_status.update(status_dict)  # Agrega el estado de la parte al diccionario general
        return part_status

def play():
    """
    Función principal del juego. Controla la lógica del juego.
    """
    playing = True  # Variable que indica si el juego está en curso
    print("Welcome to the game")
    robot_one = Robot("Jarvis", colors["Green"])  # Crear el primer robot con nombre "Jarvis" y color verde
    robot_two = Robot("Friday", colors["Blue"])  # Crear el segundo robot con nombre "Friday" y color azul
    rount = 0  # Contador para llevar la cuenta de los turnos
    while playing:
        if rount % 2 == 0:  # Si el contador de turnos es par, es el turno del primer robot
            current_robot = robot_one  # Establecer el primer robot como el robot actual
            enemy_robot = robot_two  # Establecer el segundo robot como el robot enemigo
        else:  # Si el contador de turnos es impar, es el turno del segundo robot
            current_robot = robot_two  # Establecer el segundo robot como el robot actual
            enemy_robot = robot_one  # Establecer el primer robot como el robot enemigo
        current_robot.print_status()  # Imprimir el estado del robot actual
        print("Inventory:")
        current_robot.fuse_power()  # Combina ítems del inventario con partes del robot para aplicar bonificaciones
        current_robot.print_status()  # Imprimir el estado del robot actual
        print("What part should I use to attack?")
        part_to_use = input("Choose a number part: ")  # Solicitar al usuario que elija una parte del robot para atacar
        part_to_use = int(part_to_use)  # Convertir la entrada del usuario a un número entero
        enemy_robot.print_status()  # Imprimir el estado del robot enemigo
        print("Which part of the enemy should we attack?")
        part_to_attack = input("Choose an enemy part to attack: ")  # Solicitar al usuario que elija una parte del robot enemigo para atacar
        part_to_attack = int(part_to_attack)  # Convertir la entrada del usuario a un número entero

        current_robot.attack(enemy_robot, part_to_use, part_to_attack)  # El robot actual ataca al robot enemigo utilizando las partes seleccionadas
        
        rount += 1  # Incrementar el contador de turnos

        if not enemy_robot.is_on() or enemy_robot.is_there_available_parts() == False:
            # Si el robot enemigo no tiene energía o no tiene partes disponibles, el juego termina
            playing = False  # Cambiar el estado del juego a False para salir del bucle
            print("Congratulations! You won")  # Imprimir un mensaje de felicitación
            print(current_robot.name)  # Imprimir el robot actual

play()