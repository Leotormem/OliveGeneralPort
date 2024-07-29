###Pergunta 1: Olhe para o código de exemplo, estude-o cuidadosamente. Escreva uma previsão do que ele fará quando for executado. Sua previsão deve ser adicionada ao código como comentários. Você deve usar os termos-chave executar, produzir e string em sua previsão. 

print("Hello World!")

#Resposta 1: Quando se executar a string ela vai produzir na tela a mensagem "Hello World!"

#Investigar: Use comentários para responder às perguntas de investigação no código de exemplo.

# Qual parte do código de exemplo é a instrução de saída?
## Responda: A funçao de saida é o print()

# Qual parte do código de exemplo é a string?
## Responda: O exemplo de string é o Hello World!

# Qual seria a saída do código print("I love Computing")?
## Responda: A saida serie I love Computing

# O que aconteceria se o código print("I love Comping") fosse executado?
## Responda: a mensagem I love Comping apareceria na tela

# O que aconteceria se o código print("I love Computing" fosse executado?
## Responda: Ocorreria um erro pois falta um parentese no final do codigo

###Pergunta 2: Adapte o código para gerar sua própria mensagem e adicione comentários para mostrar o que ele faz.

print("Bem Vindo ao Curso")

###Pergunta 3: Escreva um programa que produza uma história. A história e a conclusão da história devem sair em várias linhas.

Historia = f"""
Numa pequena vila escondida entre montanhas, vivia um velho carpinteiro chamado Joaquim. Conhecido por suas mãos habilidosas, ele esculpia brinquedos de madeira para as crianças da região. Um dia, ao caminhar pela floresta em busca da madeira perfeita, encontrou uma árvore majestosa que parecia sussurrar segredos do passado, curioso, Joaquim cortou um pequeno galho e, ao esculpi-lo, ele percebeu que cada toque de suas ferramentas revelava uma nova figura de um animal mágico. Um leão, um unicórnio, um dragão. Encantado, ele passou semanas criando uma coleção de criaturas incríveis, que logo começaram a ganhar vida durante a noite."""

Conclusão = f"""
A vila se transformou em um lugar de magia e alegria, com os brinquedos encantados trazendo felicidade a todos. Joaquim, antes um simples carpinteiro, tornou-se o guardião das histórias e sonhos da floresta, e sua lenda foi contada por gerações."""

print (Historia)

print (Conclusão)

#Tarefa de extensão 1: Existe uma maneira de usar uma única instrução de impressão para gerar texto em várias linhas. Crie o programa de história que funciona da mesma forma do que anteriormente, mas usa apenas uma instrução de impressão.

print (Historia + "\n" + Conclusão)

#Tarefa de extensão 2: Existe uma maneira de adicionar um atraso de tempo no código python. Faça alguma pesquisa e crie um programa de história que produza a história e atrase antes de gerar a conclusão.

import time

Historia = f"""
Numa pequena vila escondida entre montanhas, vivia um velho carpinteiro chamado Joaquim. Conhecido por suas mãos habilidosas, ele esculpia brinquedos de madeira para as crianças da região. Um dia, ao caminhar pela floresta em busca da madeira perfeita, encontrou uma árvore majestosa que parecia sussurrar segredos do passado, curioso, Joaquim cortou um pequeno galho e, ao esculpi-lo, ele percebeu que cada toque de suas ferramentas revelava uma nova figura de um animal mágico. Um leão, um unicórnio, um dragão. Encantado, ele passou semanas criando uma coleção de criaturas incríveis, que logo começaram a ganhar vida durante a noite."""

Conclusão = f"""
A vila se transformou em um lugar de magia e alegria, com os brinquedos encantados trazendo felicidade a todos. Joaquim, antes um simples carpinteiro, tornou-se o guardião das histórias e sonhos da floresta, e sua lenda foi contada por gerações."""

print (Historia)
time.sleep(5)
print (Conclusão)

###pergunta 4: Prever e Executar, Olhe para cada exemplo, estude-o cuidadosamente. Escreva uma previsão do que ele fará quando for executado. Sua previsão deve ser adicionada ao código como comentários. Você deve usar os termos-chave variável, atribuir e concatenar em sua previsão

#Prever e executar o exemplo 1

firstName = "Andy"

print(firstName)

# Apos eu atribuir o valor 'Andy' a variavel firstName, eu dou um ordem de saida atraves da função print e isso fará com que o nome Andy seja impresso na tela.

#Prever e executar o exemplo 2

lastName = "Colley"

fullName = firstName + " " + lastName

print(fullName)

# Apos atribuir mais duas variaveis como lastName e outra como fullName faço uma concatenação utilizando o + e com um espaço entre as duas variaveis firstName e lastName, depois peço para a variavel fullName ser impressa na tela para assim formar o nome Andy Collen.

#Prever e executar o exemplo 3

print("Hello " + firstName + ". Your full name is " + fullName + ".")


# Usando mais uma vez o + para fazer uma concatenação para a mensagem ser impressa na mesma linha, peço para o programa, atravez das variaveis ja definidas imprimir a mensagem 'Hello Andy. Your full name is Andy Colley.

###pergunta 5: Tarefa - Investigar, Use comentários para responder às perguntas de investigação no código de exemplo.

### Exemplo código 1

fName = "Mr"

lName = "Colley"


print(fName)

#Identifique uma variável no código

# Resposta: fname

#Identifique uma string no código

# Resposta: Mr

# A linha 4 foi alterada para lName = "Thorpe". Como isso afeta a saída?

#Resposta: Não ira afetar em nada por a função print esta pedindo a saida do fName

# A linha 3 foi alterada para fName = "Mrs". Como isso afeta a saída?

# Resposta: afetara pois na saida ao inves de ser impresso o Mr vai ser impresso o Mrs

### Exemplo código 2

num1 = 20

num2 = 5

total1 = num1 + 15

total2 = num2 * 2

total3 = num1 - num2

print(total3)

# O que será gerado pelo programa?

# Responda: A saida da função sera a subtração da variavel num1 e num2 dando assim o resultado na tela que sera igual a 15.

### Exemplo código 3

name1 = "Ross" 

name2 = "Monica" 

name3 = "Joey" 

name4 = "Rachel" 

name5 = "Chandler" 

print(name1 + " e " + name4) 

print(name3) 

name3 = "Phoebe" 

# Quantas variáveis são usadas no programa?

# Responda: 6

# Qual seria o impacto de mudar print(name1, " e ", name4) para print(name1, " e ", name5) ?

# Responda: O impacto seria que em vez da saida ser Ross e Rachel será Ross e Chandler

# Qual é o propósito do símbolo '+' em print(name1 + " e " + name4) 

# Responda: O proposito é fazer uma concatenação e a saida ser toda na mesma linha.

# A linha print(name3) é adicionada ao final do código. Explique o que ele fará.

# Responda: Ela da a saida para ser impresso na tela o valor da funçao name3 que é Joey.

###Pergunta 6: Adapte o código para gerar o que está sendo pedido nos comentários. Complemente com comentários para deixar seu código bastante claro.

# Atribuição de Variável - Modificar

# Você pode combinar variáveis com strings em uma saída

name1 = "Axl"

name2 = "Slash"

#Adicione mais 2 variáveis para armazenar 'Duff' e 'Izzy'

name1 = "Axl"

name2 = "Slash"

name3 = "Duff"

name4 = "Izzy"

#Esta linha usa concatenação para juntar as variáveis com a string 'and' para formar uma frase.

#Complete a linha para gerar todas as variáveis

print(name1 + " and " + name2 + " and " + nome3 +  " and " + nome4)

###Pergunta 7: Atribua seu nome e sua comida favorita a 2 variáveis separadas com nomes adequados. Emita o conteúdo das variáveis em 2 linhas separadas.

#Emita o conteúdo das variáveis em 2 linhas separadas.

# Atribuição de Variáveis

# Atribua seu nome e sua comida favorita a 2 variáveis separadas com nomes adequados.

############# SIMPLES ###################

# Mostra o conteúdo das variáveis em 2 linhas separadas

nome = "Leonardo"

comida = "Sushi"

print(nome)

print(comida)

#Tarefa de extensão 1: Emita duas frases (não apenas o conteúdo das variáveis). O primeiro com seu nome, o segundo com sua comida favorita.

############# MÉDIO ####################

# Saída de duas frases não apenas o conteúdo das variáveis). O primeiro com seu nome, o segundo com sua comida favorita.

print("Meu nome é" + " " + nome)

print("Minha comida favorita é" + " " + comida)

#Tarefa de extensão 2: Emita ambas as informações como parte da mesma frase. Certifique-se de ter espaços e pontuação nos lugares corretos.

############# COMPLEXO ###################

# Emita ambas as informações como parte da mesma frase.

# Certifique-se de ter espaços e pontuação nos lugares corretos.

print("Ola, meu nome é " + nome + " " + "e minha comida favorita é " + comida + ".")

###Pergunta 8: #No código main.py no Replit, são mostradas algumas linhas para manipulação de números em horas. Adicione os comentários apropriados para deixar o código mais inteligível.

#O código foi gerado inicialmente por causa desse enunciado:

#Você está enchendo uma piscina e tem duas mangueiras. A mangueira verde enche em 1,5 horas e a mangueira azul em 1,2 horas. Você deseja acelerar o processo usando as duas mangueiras. Quanto tempo levará usando as duas mangueiras, em minutos?

#Por fim, preveja qual vai ser o valor da variável time, escrevendo a resposta como comentário

time_green = 1.5

time_blue = 1.2

#A primeira coisa feita foi atribuir variaveis a cada mangueira e designar um valor

minutes_green = 60 * time_green

minutes_blue = 60 * time_blue

#Apos isso, foi designado mais duas variaveis para tranformar o tempo que cada mangueira enche de horas para minutos.

rate_hose_green = 1 / minutes_green

rate_hose_blue = 1 / minutes_blue

#apos isso foi definido uma varivel para o tempo que cada mangueira demora para encher uma piscina

rate_host_combined = rate_hose_green + rate_hose_blue

# aqui foi definido a soma do tempo de enchimento

time = 1 / rate_host_combined

#simplicando o valor para o enchimento de uma piscina

# Escreva neste comentário qual será o valor de time no final da execução do código

# Resposta: 40 minutos

###pergunta 9: código foi gerado inicialmente por causa desse enunciado: Você está enchendo uma piscina e tem duas mangueiras. A mangueira verde enche em 1,5 horas e a mangueira azul em 1,2 horas. Você deseja acelerar o processo usando as duas mangueiras. Quanto tempo levará usando as duas mangueiras, em minutos?

#Modifique o código para o caso de serem usadas duas mangueiras verdes iguais para encher a piscina. Imprima o valor do tempo levado usando a função print().

time_green = 1.5

time_blue = 1.2

minutes_green = 60 * time_green

minutes_blue = 60 * time_blue

rate_hose_green = 1 / minutes_green

rate_hose_blue = 1 / minutes_blue

rate_host_combined = 2*rate_hose_green

time = 1 / rate_host_combined

print(time)

###pergunta 10: Escreva um código que funcione de acordo com o enunciado

#Você está enchendo uma piscina e tem 3 mangueiras. A mangueira vermelha enche em 2 horas, a mangueira azul leva 1,2 hora e a mangueira amarela em 1 hora. Você deseja acelerar o processo usando as três mangueiras. Quanto tempo levará usando todas as mangueiras, em minutos?

time_red = 2

time_blue = 1.2

time_yellow = 1

minutes_red = 60 * time_red

minutes_blue = 60 * time_blue

minutes_yellow = 60 * time_yellow

rate_hose_red = 1 / minutes_red

rate_hose_blue = 1 / minutes_blue

rate_hose_yellow = 1 / minutes_yellow

rate_host_combined = rate_hose_red + rate_hose_blue + rate_hose_yellow

time = 1 / rate_host_combined

print(time)

###Pergunta11: Escreva um código que funcione de acordo com o enunciado. Faça um programa que somará dois números e mostrará a média desses números como resultado.

a = [335, 245] 

soma = sum(a)

media = soma / len(a)

print (media)

###pergunta 12: Escreva um código que funcione de acordo com o enunciado. Faça um programa que calcule a área de um triângulo. Onde você informará a base e a altura. 

#Fórmula: A = (b x h) / 2

#Onde: A = Área

#b = base

#h = altura

b = int (input("Digite o valor da base "))
h = int (input("Digite o valor da altura "))

A = (b * h) / 2

print(A)

###Pergunta 13: Escreva um código que funcione de acordo com o enunciado. Faça um programa que calcule a área de um retângulo. Onde você informará o comprimento e a largura. 

#Fórmula: A = c x l 

#Onde: A2 = Área

#c = comprimento

#l = largura

c = int (input("Entre com o comprimento"))
l = int (input("Entre com a largura"))

A2 = c * l 

print(A2)

###Pergunta 14: Escreva um código que funcione de acordo com o enunciado. Faça um programa que calcule o volume de um paralelepípedo. Onde você informará o comprimento, a largura e a altura. 

#Fórmula: V = c x l x h

#Onde: V = Volume

#c2 = comprimento

#l2 = largura

#h2 = altura

c2 = int(input("Entre com o comprimento "))
l2 = int(input("entre com a largura "))
h2 = int(input("Entre com a altura "))

 V = c2 * l2 * h2

print(V)

###Pergunta 15: Escreva um código que funcione de acordo com o enunciado

#Três amigos saíram juntos para o cinema. O amigo 1 levou R$100,00. O amigo 2 levou 2 vezes e meia o valor do amigo 1. E o amigo 3 levou a metade do valor somado dos outros dois amigos. Faça um programa que calcule o valor total que os três amigos levaram para o cinema.

Amigo1 = 100
Amigo2 = (2.5 * Amigo1)
Amigo3 = (Amigo1 + Amigo2) / 2

Total = Amigo1 + Amigo2 + Amigo3

print("R$" , Total)

###Pergunta 16: Escreva um código que funcione de acordo com o enunciado.
#Quatro amigas foram ao shopping comprar roupas. A amiga 1 levou R$240,00. A amiga 2 levou dois terços (2/3) do valor da amiga 1. A amiga 3 levou 3 vezes o valor da amiga 2. A amiga 4 levou o valor somado das amigas 2 e 3. Faça um programa que calcule o valor total que as quatro amigas levaram para o shopping. 

Amiga1 = 240
Amiga2 = (2/3 * Amiga1)
Amiga3 = (3 * Amiga2)
Amiga4 = (Amiga2 + Amiga3)

Total2 = Amiga1 + Amiga2 + Amiga3 + Amiga4

print(Total2)