# Base class for all characters
class Character:
    def __init__(self, name, hitPoints, strength, defence):
        # Each character has a name, health points (hitPoints), strength, and defence
        self.name = name
        self.hitPoints = hitPoints
        self.strength = strength
        self.defence = defence
    
    def take_damage(self, damage):
        # Calculate the damage by reducing it based on defence, but always at least 1 damage
        actual_damage = max(damage - self.defence, 1)
        self.hitPoints -= actual_damage
        print(f"{self.name} takes {actual_damage} damage. Remaining HP: {self.hitPoints}")
    
    def is_alive(self):
        # Check if the character is still alive
        return self.hitPoints > 0
    
    def do_action(self):
        # This method will be different for each character, so it should be defined in subclasses
        raise NotImplementedError("Subclasses must implement this method")

# Warrior class, a type of character that gains rage and can perform heavy attacks
class Warrior(Character):
    def __init__(self, name):
        # Set default attributes for Warrior (more health, more strength)
        super().__init__(name, hitPoints=120, strength=20, defence=15)
        self.ragePoints = 0  # Warriors build up rage over time
    
    def heavy_swing(self):
        # A stronger attack that uses rage
        return self.strength * 2  # Heavy swing does double damage
    
    def do_action(self):
        # If the warrior has enough rage, perform a strong attack, otherwise a normal one
        if self.ragePoints >= 15:
            self.ragePoints -= 15
            print(f"{self.name} performs a Heavy Swing!")
            return self.heavy_swing()
        else:
            self.ragePoints += 5  # Gain rage if no heavy swing is performed
            print(f"{self.name} performs a normal attack!")
            return self.strength

# Mage class, a character that uses magic (mana) to cast fireballs
class Mage(Character):
    def __init__(self, name):
        # Set default attributes for Mage (less health, uses mana for spells)
        super().__init__(name, hitPoints=100, strength=10, defence=5)
        self.manaPoints = 50  # Mana for casting spells
        self.fireballDamage = 30  # Fireball does more damage than normal attacks
    
    def do_action(self):
        # If the mage has enough mana, cast a fireball, otherwise use a normal attack
        if self.manaPoints >= 10:
            self.manaPoints -= 10
            print(f"{self.name} casts a Fireball!")
            return self.fireballDamage
        else:
            print(f"{self.name} performs a normal attack!")
            return self.strength

# Paladin class, a mix of warrior and healer, can heal themselves in battle
class Paladin(Warrior):
    def __init__(self, name):
        # Inherits from Warrior but also has healing abilities
        super().__init__(name)
        self.healAmount = 25  # Paladins can heal themselves
    
    def do_action(self):
        # If health is low, heal instead of attacking
        if self.hitPoints <= 30 and self.ragePoints >= 10:
            self.ragePoints -= 10
            self.hitPoints += self.healAmount
            print(f"{self.name} heals for {self.healAmount} HP!")
            return 0  # Healing doesn't cause damage
        else:
            return super().do_action()

# Function to simulate a battle between Paladin and Mage
def battle_simulation():
    paladin = Paladin("Sir Lancelot")
    mage = Mage("Merlin")
    
    # Keep the battle going while both are alive
    while paladin.is_alive() and mage.is_alive():
        # Paladin attacks Mage
        mage_damage = paladin.do_action()
        mage.take_damage(mage_damage)
        if not mage.is_alive():
            print("Mage is defeated!")
            break
        
        # Mage attacks Paladin
        paladin_damage = mage.do_action()
        paladin.take_damage(paladin_damage)
        if not paladin.is_alive():
            print("Paladin is defeated!")
            break

# Run the battle simulation
battle_simulation()
