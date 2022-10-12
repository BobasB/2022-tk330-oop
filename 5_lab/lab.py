class Rocket():
    def __init__(self, name:str, mass, size) -> None:
        assert name.isascii(), "Назва ракети має містити символи ASCII"
        assert mass >= 0 and size >= 0, "Маса та Розмір Ракети не може бути меншою за 0!"
        #Так працює але так не роблять
        #if not size > 0:
        #    raise AssertionError("Розмір Ракети не може бути меншою за 0!")
        
        self.name = name
        self.mass = mass
        self.size = size
    
    @property
    def info(self):
        return f"Ракета {self.name} має масу {self.mass} кг та розмір {self.size} м."
    
    def convert_to_pounds(self):
        return self.mass * 2.20462262
    
    def convert_to_feet(self):
        return self.size * 3.2808399

    @property
    def info_in_en(self):
        return f"Ракета {self.name} має масу {self.convert_to_pounds()} фунтів та розмір {self.convert_to_feet()} футів."


#r = Rocket("Falcon 9", 549054, 70)
#print(r.info)
#print(r.info_in_en)
#r2 = Rocket("Atlas V", 546700, 58.3)
#print(r2.info)