class Funcionario:
    __name = ''

    def set_name(self, name):
        self.__name = name 
        
    def get_name(self): 
        return self.__name

funcionario = Funcionario()
funcionario2 = Funcionario() 
funcionario2.set_name('Diego')
funcionario.set_name('Jorge')
print(funcionario.get_name(), funcionario2.get_name())