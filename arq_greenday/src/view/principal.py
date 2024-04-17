import sys 

from greenday import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPixmap
from novo_user import Usuario
from lista_cad import Cad_Control
from preferencia import Preferencia
from lista_prefe import Prefe_Control

class principal(Ui_MainWindow, QMainWindow):


    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.bot_entrar.clicked.connect(self.entrar)
        self.init_components()
        self.controle_cad = Cad_Control()
        self.controle_prefe = Prefe_Control()
        self.cor_sucesso = "background-color: rbg(209, 250, 209);"
        self.cor_erro = "background-color: rbg(250, 185, 185);"
        self.stackedWidget.setCurrentWidget(self.login)

    def entrar(self):
        nome = self.user_login.text()
        senha = self.senha_login.text()
        print(f'Login: {nome}')
        print(f'Senha: {senha}')
        flag_logado = False
        #varrer a lista com um for
        for obj in self.controle_cad.lista_cadastros: 
            print(obj.user)
            print(obj.senha)
            if obj.user == nome and obj.senha == senha:
                self.bot_entrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.main_screen))
                flag_logado = True
        if not flag_logado:
            self.erro.setText(f'ERRO: LOGIN OU SENHA INVALIDOS')
            self.frame.show() 


    def init_components(self): 

        #img
        self.logo.setPixmap(QPixmap('img/logo.png'))

        #ação dos botões pra mudar de pagina
        self.bot_cadastrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.novo_cadastro))
        self.bot_seuperfil.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.perfil))
        self.bot_pref_nots.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pref_nots))
        self.bot_listagem.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.lista_prefe))
        self.bot_nots.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.notificacao))
        self.bot_volt_telalogin.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.login))
        self.bot_sair.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.login))
        self.bot_volt_main.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.main_screen))
        self.bot_volt_mains.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.main_screen))
        self.bot_ir_list2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.lista_prefe))
        self.bot_volt_mainscre.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.main_screen))
        self.bot_volt_mainscree.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.main_screen))

        #botões de ação 
        self.bot_salv_cad.clicked.connect(self.salvar_cad)
        self.bot_salv_prefe.clicked.connect(self.salvar_prefer)
        self.bot_delet_perfil_2.clicked.connect(self.excluir_cadastro)
        self.bot_voltar.clicked.connect(self.excluir_prefe)

        #esconder os frames de mensagens
        self.frame_5.hide()
        self.frame.hide()
        self.frame_msg_perfil.hide()
        self.frame_msg_prefe.hide()
        self.frame_erro_list2.hide()
        self.x_msg.clicked.connect(lambda: self.frame_5.hide())

#cadastro
    def listar_cadastro_tabela(self):
        cont_linhas = 0
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(self.controle_cad.lista_cadastros))
        for cad in self.controle_cad.lista_cadastros:
            self.tableWidget.setItem(cont_linhas, 0, QtWidgets.QTableWidgetItem(cad.email))
            self.tableWidget.setItem(cont_linhas, 1, QtWidgets.QTableWidgetItem(cad.user))
            self.tableWidget.setItem(cont_linhas, 2, QtWidgets.QTableWidgetItem(cad.senha))
            self.tableWidget.setItem(cont_linhas, 3, QtWidgets.QTableWidgetItem(cad.conf_senha))
            self.tableWidget.setItem(cont_linhas, 4, QtWidgets.QTableWidgetItem(cad.perfil))
            cont_linhas += 1

    def salvar_cad(self):
        cad = Usuario()
        cad.email = self.dig_email.text()
        cad.user = self.dig_user.text()
        cad.senha = self.dig_senha.text()
        cad.conf_senha = self.digit_confirma.text()
        cad.perfil = self.usuario_adm.currentText()
        if len(cad.erro_validacao) != 0:
            self.msg_label.setStyleSheet(self.cor_erro)
            self.msg_label.setText(cad.erro_validacao)
            self.frame_5.show()    
        else:
            msg = self.controle_cad.salvar_cad(cad)
            self.erro.setText(msg)
            self.frame.show()
            self.x_erro.clicked.connect(lambda: self.frame.hide())
            self.erro.setStyleSheet(self.cor_sucesso)
            self.stackedWidget.setCurrentWidget(self.login)
            self.listar_cadastro_tabela()
    
    def excluir_cadastro(self):
        indice = self.tableWidget.currentRow()
        msg = self.controle_cad.excluir_cadastro(indice)
        self.msg_erro.setText(msg)
        self.frame_msg_perfil.show()
        self.x_erro_2.clicked.connect(lambda: self.frame_msg_perfil.hide())
        self.msg_erro.setStyleSheet(self.cor_sucesso)
        self.listar_cadastro_tabela()

#preferencia
    def listar_preferencia_tabela(self):
        cont_linhas = 0
        self.tableWidget_2.clearContents()
        self.tableWidget_2.setRowCount(len(self.controle_prefe.lista_prefe))
        for prefe in self.controle_prefe.lista_prefe:
            self.tableWidget_2.setItem(cont_linhas, 0, QtWidgets.QTableWidgetItem(prefe.horario_acordar))
            self.tableWidget_2.setItem(cont_linhas, 1, QtWidgets.QTableWidgetItem(prefe.horario_dormir))
            self.tableWidget_2.setItem(cont_linhas, 2, QtWidgets.QTableWidgetItem(prefe.meio_t))
            self.tableWidget_2.setItem(cont_linhas, 3, QtWidgets.QTableWidgetItem(prefe.tempo_banho))
            self.tableWidget_2.setItem(cont_linhas, 4, QtWidgets.QTableWidgetItem(prefe.uso_sacola))
            cont_linhas += 1


    def salvar_prefer(self):
        prefe = Preferencia()
        prefe.horario_acordar = self.tempo_acorda.text()
        prefe.horario_dormir = self.tempo_dormir.text()
        prefe.meio_t = self.dig_meiotransporte.text()
        prefe.tempo_banho = self.dig_banho.text()
        prefe.uso_sacola = self.opcao_sim_sacola.isChecked()
        if len(prefe.erro_validacao) != 0:
            self.msg_erro_prefe.setStyleSheet(self.cor_erro)
            self.msg_erro_prefe.setText(prefe.erro_validacao)
            self.frame_msg_prefe.show()    
        else:
            msg = self.controle_prefe.salvar_prefer(prefe)
            self.msg_erro_list2.setText(msg)
            self.frame_erro_list2.show()
            self.x_erro_3.clicked.connect(lambda: self.frame_erro_list2.hide())
            self.msg_erro_list2.setStyleSheet(self.cor_sucesso)
            self.stackedWidget.setCurrentWidget(self.lista_prefe)
            self.listar_preferencia_tabela()

    def excluir_prefe(self):
        indice = self.tableWidget_2.currentRow()
        msg = self.controle_prefe.excluir_prefe(indice)
        self.msg_erro_list2.setText(msg)
        self.frame_erro_list2.show()
        self.x_erro_3.clicked.connect(lambda: self.frame_erro_list2.hide())
        self.msg_erro_list2.setStyleSheet(self.cor_sucesso)
        self.listar_preferencia_tabela()



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    principal = principal()
    principal.show()
    qt.exec()
