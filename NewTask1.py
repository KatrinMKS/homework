class wizard:
    def __init__(self, spell, magic_wand=None):
        self.spell = spell
        self.magic_wand = magic_wand

class Wizards_Container:
    def __init__(self):
        self.wizard = None

    def put(self, spell, magic_wand):
        if self.wizard is None:
            self.wizard = wizard(spell, magic_wand)
        else: 
            self.wizard = wizard(spell, magic_wand)
    def get(self):
        if self.wizard is None:
            return None
        return self.wizard.magic_wand
        
        
c1= Wizards_Container()
print (c1.get())
c1.put(1, 'Welcome to')  
print(c1.get())
c1.put(2, 'Hogwarts')
print(c1.get())
