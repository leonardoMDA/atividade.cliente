class Cliente:
    def __init__(self, nome, idade, sexo, email, telefone, endereco):
        self.nome = nome  
        self.idade = idade
        self.sexo = sexo
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def apresentar_cadastro(self):
        print("Cadastro efetuado com sucesso!")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Sexo: {self.sexo}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

    def __str__(self):
        return f'{self.nome} - {self.idade} - {self.sexo} - {self.email} - {self.telefone} - {self.endereco}'

cliente = Cliente(
    nome="joão da silva", 
    idade=30, 
    sexo="Masculino", 
    email="joao@email.com", 
    telefone="123456789", 
    endereco="Rua A, 123"
)
cliente.apresentar_cadastro()