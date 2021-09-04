class Factory(type):
    def __init__(self, *args, **kwargs):
        pass
    '''
    nome = ''
    maquinas = []
    funcionarios = []
    materiais = []
   '''
    def vender(self):
        return self.materiais

class FactoryEletronics(metaclass=Factory):
    pass

print(FactoryEletronics())
#print(Factory().vender())
