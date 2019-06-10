class partyanimal:
    x = 0
    name = ''
    def _init_(self, z):
        self.name = z
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name,'No: ', self.x)
m = partyanimal('musali')
m.party()

f = partyanimal('francis')
f.party()
m.party()
