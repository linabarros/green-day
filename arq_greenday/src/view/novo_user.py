class Usuario:
    
    def __init__(self, email = None, user = None, senha = None, conf_senha = None, perfil = None) -> None:
        self.user = user
        self.email = email
        self.senha = senha
        self.conf_senha = conf_senha
        self.perfil = perfil
        self.erro_validacao = ''

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if email != None and len(email) != 0:
            self.__email = email
        else:
            self.erro_validacao = f'CAMPO EMAIL OBRIGATÓRIO'

    @property
    def user(self):
        return self.__user
    
    @user.setter
    def user(self, user):
        if user != None and len(user) != 0:
            self.__user = user
        else:
            self.erro_validacao = f'CAMPO NOME DE USUÁRIO OBRIGATÓRIO'
    
    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        if senha != None and len(senha) != 0:
            self.__senha = senha
        else:
            self.erro_validacao = f'CAMPO SENHA OBRIGATÓRIO'

    @property
    def conf_senha(self):
        return self.__conf_senha
    
    @conf_senha.setter
    def conf_senha(self, conf_senha):
        if conf_senha != None and len(conf_senha) != 0:
            self.__conf_senha = conf_senha
        else:
            self.erro_validacao = f'CAMPO CONFIRMAÇÃO DE SENHA OBRIGATÓRIO'
    
    @property
    def perfil(self):
        return self.__perfil
    
    @perfil.setter
    def perfil(self, perfil):
        if perfil != None and perfil != '...':
            self.__perfil = perfil
        else:
            self.erro_validacao = f'CAMPO PERFIL OBRIGATÓRIO'

    def __str__(self) -> str:
        return f'{self.user} \t {self.senha}'
        


