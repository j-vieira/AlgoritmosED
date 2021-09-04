import copy, numpy

class Veiculo:
    marca = ''
   
    #x = numpy.arange(0, 3, 0.1)
    #y = numpy.sin(x)

    def __init__(self):
        pass
    
    def clone(self):
        return copy.deepcopy(self)

veiculo = Veiculo()
veiculo.marca = 'Toyota'

veiculoClone = veiculo.clone()

print(veiculoClone.marca)

#print(veiculo.marca, veiculoClone.marca)