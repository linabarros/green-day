class Preferencia:
    
    def __init__(self, horario_acordar = None, horario_dormir = None, meio_t = None, tempo_banho = None, uso_sacola = None, uso_celular = None) -> None:
        self.horario_acordar = horario_acordar
        self.horario_dormir = horario_dormir
        self.meio_t = meio_t
        self.tempo_banho = tempo_banho
        self.uso_sacola = uso_sacola
        self.uso_celular = uso_celular
        self.erro_validacao = ''

    @property
    def horario_acordar(self):
        return self.__horario_acordar
    
    @horario_acordar.setter
    def horario_acordar(self, horario_acordar):
        if horario_acordar != '' or horario_acordar != '00:00' :
            self.__horario_acordar = horario_acordar
        else:
            self.erro_validacao = f'CAMPO "HORÁRIO DE ACORDAR" OBRIGATÓRIO'
        
        
    @property
    def horario_dormir(self):
        return self.__horario_dormir
    
    @horario_dormir.setter
    def horario_dormir(self, horario_dormir):
        if horario_dormir != '' or horario_dormir != '00:00':
             self.__horario_dormir = horario_dormir
        else:
            self.erro_validacao = f'CAMPO "HORÁRIO DE DORMIR" OBRIGATÓRIO'
        
    @property
    def meio_t(self):
        return self.__meio_t
    
    @meio_t.setter
    def meio_t(self, meio_t):
        if meio_t != None and len(meio_t) != 0:
            self.__meio_t = meio_t
        else:
            self.erro_validacao = f'CAMPO "MEIO DE TRANSPORTE" OBRIGATÓRIO'

    @property
    def tempo_banho(self):
        return self.__tempo_banho
    
    @tempo_banho.setter
    def tempo_banho(self, tempo_banho):
        if tempo_banho != None and len(tempo_banho) != 0:
            self.__tempo_banho = tempo_banho
        else:
            self.erro_validacao = f'CAMPO "MÉDIA DE TEMPO NO BANHO" OBRIGATÓRIO'
    
    @property
    def uso_sacola(self) -> bool:
        return self.__uso_sacola
    
    @uso_sacola.setter
    def uso_sacola(self, uso_sacola:bool):
        if uso_sacola != '':
            self.__uso_sacola = uso_sacola
        else:
            self.erro_validacao = f'CAMPO "USO DE SACOLA PLÁSTICA É ALTO" OBRIGATÓRIO'


    def __str__(self) -> str:
        return f'{self.horario_dormir} \t {self.horario_dormir}'
        


