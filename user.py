class Users:
    def __init__(self, name, cc, years):
        self.name = name
        self.cc = cc
        self.years = years

    def toDBCollection(self):
        return{
            'name': self.name,
            'cc': self.cc,
            'years': self.years
        }
