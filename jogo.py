import random

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()} \nVida: {self.get_vida()} \nNível: {self.get_nivel()}"
    
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0
            
    def ataque_normal(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4) 
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
    
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
           
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()} \n"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8 )
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} com habilidade especial {self.get_habilidade()} e causou {dano} de dano!")
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
        
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()} \n"

class Jogo:
    """ Classe Orquestradora do jogo    """

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Superman", vida=100, nivel=10, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Lex Luthor", vida=100, nivel=10, tipo="Humano")

    
    def iniciar_batalha(self):
        print("Batalha iniciada!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("Detalhes dos Personagens: ")
            print("Heroi:")
            print(self.heroi.exibir_detalhes())
            print("Inimigo:")
            print(self.inimigo.exibir_detalhes())
            input("Pressione Enter para atacar!")
            escolha = input("Escolha (1 - ataque Normal, 2 - Ataque Especial 3 - Passar a vez): ")
            if escolha == "1":
                self.heroi.ataque_normal(self.inimigo)
                self.heroi.exibir_detalhes()

            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
                self.heroi.exibir_detalhes()

            elif escolha == "3":
                print("Você passou a vez!")
            else:
                print("Opção inválida. Tente novamente!")
            print("....")
            if self.inimigo.get_vida() > 0:
                self.inimigo.ataque_normal(self.heroi)
                self.inimigo.exibir_detalhes()
            input("Pressione Enter para continuar!")
        if self.heroi.get_vida() > 0:
            print("\nParabens, você venceu a batalha !")
        else:
            print("Você foi derrotado hahaha!")
# Criar instancias da classe Jogo
jogo = Jogo()
jogo.iniciar_batalha()
        