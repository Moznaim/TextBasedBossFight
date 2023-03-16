from Character import Character

class Boss(Character):
    def __init__(self, username):
        super().__init__(username)
        self.setStr(10)
        self.setVit(25)
        self.setInt(5)
        self.setHp(self.getHp()+self.getVit())

    def decimatingSmash(self, character):
        self.new_damage = self.getDamage()+self.getStr()
        character.reduceHp(self.new_damage)
        print(f"{self.getUsername()} performed Decimating Smash! -{self.new_damage}")

    def Recovery(self):
        self.addHp(self.getInt())
        print(f"{self.getUsername()} performed Recovery! +{self.getInt()}")


