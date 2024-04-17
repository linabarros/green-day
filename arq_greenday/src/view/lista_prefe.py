class Prefe_Control:

    def __init__(self) -> None:
        self.lista_prefe = None
         
    def salvar_prefer(self, prefe):
        self.lista_prefe.append(prefe)
        return 'PREFERÊNCIA SALVA COM SUCESSO!'
    
    @property
    def lista_prefe(self):
        return self.__lista_prefe
    
    @lista_prefe.setter
    def lista_prefe (self, lista):
        self.__lista_prefe = []

    def excluir_prefe(self, indice):
        del self.lista_prefe[indice]
        return 'PREFERÊNCIA EXCLUIDA COM SUCESSO!'
