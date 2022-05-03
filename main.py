import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("arqExcel.csv", delimiter=";")
print("\nExibe a tabela inteira")
print(dataframe)

print("\nExibe os dois últimos registros")
print(dataframe.tail(2))

print("\nExibe dois produtos e seus respectivos valores")
print([dataframe.head(2)[["produto","valor"]]])

print("\nLista todos os tipos de produtos sem repetição")
print(dataframe["tipo"].unique())

print("\nLista a quantidade de valores agrupados para cada tipo")
print(dataframe["tipo"].value_counts())

print("\nDe todos os dados o (dataFrame mais externo), e realiza um filtro no campo do tipo somente Bebida")
print(dataframe[dataframe["tipo"]=="Bebida"])

print("\nDe todos os dados (dataFrame mais externo), faça um filtro no campo tipo somente por Bebida das quais a quantidade seja menor que 15")
print(dataframe[(dataframe["tipo"]=="Bebida") & (dataframe["qtd"]<15)])

print("\nPlota um grafico passando os 6 primeiros produtos, com seus nomes e valores ")
plt.xlabel("valor")
plt.ylabel("produto")
plt.bar(dataframe.head(6)["produto"],dataframe.head(6)["valor"],color='#993399')
plt.show()