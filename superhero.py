class Superhero:
    def __init__(self, name, alias, origin, powers):
        self.name = name
        self.alias = alias
        self.origin = origin
        self.powers = powers 

    def show_powers(self):
        print(f"\n{self.alias}'s Powers:")
        for power in self.powers:
            print(f" {power}")

    def activate_power(self, power):
        if power in self.powers:
            print(f"{self.alias} activates {power} ")
        else:
            print(f"{power} is not one of {self.alias}'s powers.")

    def teleport(self, location):
        if "Teleportation" in self.powers:
            print(f"{self.alias} teleports to {location} ")
        else:
            print(f"{self.alias} does not have the Teleportation power.")

    def pause_time(self):
        if "Chrono Pause" in self.powers:
            print(f"{self.alias} activates Chrono Pause ... Time stands still.")
        else:
            print(f"{self.alias} cannot pause time.")

class TechSuperhero(Superhero):
    def hack_digital_world(self):
        if "Digital Phasing" in self.powers:
            print(f"{self.alias} enters the digital world through Digital Phasing ")
        else:
            print(f"{self.alias} does not have Digital Phasing ability.")

astria = TechSuperhero(
    name="Ahenda Olwal",
    alias="Astria",
    origin="Mombasa, Kenya",
    powers=[
        "Teleportation", 
        "Telepathy", 
        "Digital Phasing", 
        "Invisibility Cloak", 
        "Chrono Pause", 
        "Kinetic Recall"
    ]
)

print("Welcome to the World of Astria!")
print(f"Real Name: {astria.name}")
print(f"Alias: {astria.alias}")
print(f"Origin: {astria.origin}")

astria.show_powers()
astria.activate_power("Telepathy")
astria.teleport("Greece")
astria.pause_time()
astria.hack_digital_world()
