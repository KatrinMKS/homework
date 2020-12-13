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
            elif self.wizard.spell > spell:
                self.wizard = wizard(spell, magic_wand)
        def get(self):
            if self.wizard is None:
                return None
            return self.wizard.magic_wand
