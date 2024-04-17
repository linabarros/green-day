class Cad_Control:
    def __init__(self) -> None:
        self.lista_cadastros = None
         
    def salvar_cad(self, cad):
        self.lista_cadastros.append(cad)
        return 'CADASTRO SALVO COM SUCESSO!'
    
    @property
    def lista_cadastros(self):
        return self.__lista_cadastros
    
    @lista_cadastros.setter
    def lista_cadastros (self, lista):
        self.__lista_cadastros = []

    def excluir_cadastro(self, indice):
        del self.lista_cadastros[indice]
        return 'CADASTRO EXCLUIDO COM SUCESSO!'
