nome = "Olivia Rogéria"
idade = 21
musica = "God 4 u"
profissao = "Cantora"
altura = 1.65
print(nome, "é uma grande", profissao, "com apenas",
      idade, "criou um grande sucesso \n da geração teen",
      musica, "informação inutil ela tem", altura, "de altura")

import random
piadas = [
    "Porque o menino estava falando ao telefone deitado?\nR.: Para não cair a ligação.",
    "Qual é a fórmula da água benta?\nR.: H Deus O!",
    "O diretor da empresa pergunta ao novo funcionário:\n- O conailista já disse qual é a sua tarefa?\n- Sim. Acordá-lo quando eu perceber que o senhor está a chegar.",
    "Qual é o alimento mais sagrado que existe?\nR.: O amém doím.",
    "Por que o policia não usa sabão?\nR.: Porque ele prefere deter gente.",
    "Qual é o café favorito do desenvolvedor?\nR.: Java.",
    "Qual a cidade brasileira que não tem táxi?\nR.: Uberlnândia",
    "O que o HTML disse ao CSS?\nR.: “Eu gosto do seu estilo!”",
    "Como o Batman faz para entrar na Bat-caverna?\nR.: Ele bat-palma.",
    "Por que a mulher do Hulk se divorciou dele? ?\nR.: Porque ela queria um homem mais maduro."
]

print("Quer escutar uma piada? 1-sim 2-nao")
pi = input()
op = int(pi)
while(op == 1):
    if(op == 1):
        piada = random.choice(piadas)
        print(piada)
        pii = input()
        op = int(pii)
    elif(op == 2):
        print("Você não tem senso de humor >:|")


