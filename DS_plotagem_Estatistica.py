#python
#Isso aqui é a caixa de pandora, caderninho de anotações(bagunçado).
#Tudo feito no colab, estudo de conceitos.

#*************************************APLICANDO_ESTATISTICA_COM_PYTHON************************************************************

massa = [200,200,200,200,200,200,200,200,200,200,251,251,251,251,251,251,251,251,251,251,251,251,251,251,
         253,253,253,253,253,253,253,253,253,253,253,253,253,253,253,257,257,257,257,257,257,257,257,257,
         257,257,257,260,260,260,260,260,260,260,260]
import numpy
#desvio padrão
x= numpy.std(massa)
print(f'O desvio padrão é igual à: {x:.2f}')
#media
m = numpy.mean(massa)
print(f'A média é igual à {m:.2f} Kg')
#variância
v = numpy.var(massa)
print(f'A variância é igual à: {v:.2f} Kg²')

#**************************************************************PLOTAGEM_DE_GRAFICOS_E_COISITAS_MAS**************************************

#Distribuição de dados
import numpy
ex = numpy.random.uniform(0.0, 5.0, 250)
print(ex)

import matplotlib.pyplot as plt
plt.hist(ex, 5)
plt.show()

import numpy
import matplotlib.pyplot as plt
a = numpy.random.uniform(0.0, 5.0, 100000)
plt.hist(a, 100)
plt.show()

import numpy
import matplotlib.pyplot as plt
a = numpy.random.normal(5.0, 1.0, 100000)
plt.hist(a, 100)
plt.show()

import matplotlib.pyplot as plt
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

import numpy
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(f'{r:.3f}')

#*********************************************************LIVRO-DATA-SCIENCE************************************************************

from collections import Counter
import matplotlib.pyplot as plt
"""import numpy
numero_de_amigos = numpy.random.uniform(0, 100, 250)
print(numero_de_amigos)"""
numero_de_amigos = [21,46,3,35,67,95,53,72,58,10,26,25,25,2,5,25,2,5,2,5,52,55,25,34,90,33,38,20,56,2,47,15]
numero_de_amigos = Counter(numero_de_amigos)
xs = range(101)
ys = [numero_de_amigos[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histograma do número de amigos")
plt.xlabel("N° de amigos")
plt.ylabel("N° de pessoas")
plt.show()

#*********************************************************LIST**************************************************************************

names =  ['Lucas', 'Alice', 'Thiago', 'João', 'Cássia']
for i, name in enumerate(names):
  print(f" Seja bem-vindo(a) {name}")
import random
my_best_friend = random.choice(names)
print(f"Você foi escolhido(a) {my_best_friend}")

#**********************************************************JSON*************************************************************************

import json
# Abrir o arquivo json.json
with open("json.json") as file:
    # Carregar seu conteúdo e torná-lo um novo dicionário
    data = json.load(file)

    # Excluir o par chave-valor "client" de cada pedido
    #for order in data["dados"]:
       # del order["_time"]

# Abrir (ou criar) um arquivo orders_new.json
# e armazenar a nova versão dos dados.
#with open("orders_new.json", 'w') as file:
    #json.dump(data, file)
print(json.dumps(data, indent=4,   sort_keys=True , separators=(". ", " = ")))

#*********************************************************LIST****************************************************************************

import pandas as pd
frutas = ['Banana','Maracujá','Lima','Coco', 'Manga']
cores = [ 'Amarelo','Amarelo','Verde','Verde','Rossa']
nomes = ['Lucas', 'Bianca', 'luan', 'kaique','Tina']
df = pd.DataFrame({
    'frutas': frutas,
    'cores': cores,
    'nomes':nomes,
})
df

#**************************************************DICT_AND_LIST************************************************************************

nome = str(input('Qual o seu nome? '))
print('É um prazer te conhecer,{}'.format(nome))
print(f'É um prazer te conhecer, {nome}')
for i in range(10):
  print(i)
notas = {
    'Português' : 8,
    'Matemática'  : 8,
    'Geografia' : 9
}
for chave, valor in notas.items():
  print(f"{chave}:{valor}")
frutas = ['Banana','Pera','Uva']
for indice, valor in enumerate(frutas):
  print(f'Índice = {indice} | Valor = {valor}')

#*****************************************************************COLORS*****************************************************************

print("____\033[31mO\033[m\033[33ml\033[m\033[32má\033[m \033[34mM\033[m\033[35mu\033[m\033[30mn\033[m\033[37md\033[m\033[7;30mo\033[m____")
nome = str(input("Digite o seu nome: "))
idade = int(input("Quantos anos você tem? "))
print("Olá,", nome,",é um prazer conhecer você!!! ")
if idade < 18:
  print("\033[31mVocê ainda é jovem para estar aqui; vaza, meu chapa.\033[m")
else:
  print("\033[32mAcesso liberado, meu chapa.\033[m")


#********************************************************************CSV******************************************************************

from csv import reader
opened_file = open('/content/arquivo1.csv')
read_file = reader(opened_file)
arquivo1 = tuple(read_file)
arquivo1 = arquivo1[0:]
print(arquivo1)
#import matplotlib
#matplotlib.pyplot.plot(arquivo1)
#matplotlib.pyplot.show(arquivo1)


#***************************************************************DIO**********************************************************************

print('---QUAL MÊS CORRESPONDE AO NÚMERO?---')
while(1):
  print('Digite um número de 1 a 12 .')
  n = int(input())
  if n < 1 or n > 12:
    print('digite um valor válido!')
  mes = ['','janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
  print(mes[n].upper())


#************************************************************CSV**********************************************************************

import pandas as pd
df = pd.read_csv('data.csv')
#df1 = pd.DataFrame(df)
print(df1.to_string())
#df = df[refugos1mld.csv].str.split(';')
#print(df)


