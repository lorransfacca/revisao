class Pessoa:
    def __init__(self,nome,idade,genero,endereco,telefone,email):
        self.nome = nome 
        self.idade = idade
        self.genero = genero
        self.endereco = endereco
        self.telefone = telefone
        self.email = email    

class Paciente(Pessoa):
    def __init__(self,nome,idade,genero,endereco,telefone,email,sanguineo,sintoma):
        super().__init__(nome,idade,genero,endereco,telefone,email)
        self.sanguineo = sanguineo
        self.sintoma = sintoma

    def imprimir_sintoma(self):
        return print('Sintomas: ' + self.sintoma)

    def imprimir_dados(self):
        print('Nome: ' + self.nome)
        print('Idade: ' + self.idade)
        print('Genero: ' + self.genero)
        print('Sanguineo: ' + self.sanguineo)
        print('Endereco: ' + self.endereco)
        print('Telefone: ' + self.telefone)
        print('Email: ' + self.email)

class Medico(Pessoa):
    def __init__(self,nome,idade,genero,endereco,telefone,email,crm, atuacao):
        super().__init__(nome,idade,genero,endereco,telefone,email)
        self.crm = crm
        self.atuacao = atuacao

    def imprimir_dados(self):
        print('Nome: ' + self.nome)
        print('Idade: ' + self.idade)
        print('Genero: ' + self.genero)
        print('Endereco: ' + self.endereco)
        print('Telefone: ' + self.telefone)
        print('Email: ' + self.email)
        print('Atuacao: ' + self.atuacao)


    def imprimir_crm(self):
        return print( 'CRM: '+ self.crm)

print('______PACIENTE______')
paciente = Paciente('Marcia','23', 'Feminino', 'Itaquera','11 32418901', 'marciahacker@gmail.com', 'A-', 'Gripe')
paciente.imprimir_dados()     
paciente.imprimir_sintoma()

print('______MEDICO______')
medico = Medico('Dr° Fernando','45', 'Masculino', 'Itaquera', '11 987532659', 'drfernando@gmail.com', '45016','clinico geral')
medico.imprimir_dados()     
medico.imprimir_crm()