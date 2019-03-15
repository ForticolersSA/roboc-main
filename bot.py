


class Bot:


    def __init__(self, x=0, y=0,name=""):
        self.x = x
        self.y = y
        self.name = name
        self.datas = (x,y,name)

    def __repr__(self):
        name_var = f"'{self.name}'" if self.name!="" else ""
        return f"<Bot{name_var} : {self.datas}>"

    def set_position(self,pos):
        self.x = pos[0]
        self.y = pos[1]
    def get_datas(self):
        return self.datas
