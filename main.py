import pandas as pd
import os
import matplotlib.pyplot as plt


os.system('cls')

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_1.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science/refs/heads/main/base-de-dados-challenge-1/loja_4.csv"

class Loja():
    '''
        Classe para análise de dados de uma loja a partir de um arquivo CSV

        Atributos:
            dados (DataFrame): DataFrame carregado a partir do CSV com as informações da loja.
            nome: String com um nome para designar a loja

        Métodos:
            faturamento() -> float:
            Retorna o faturamento total da empresa.

            satisfacao() -> float:
                Retorna a média da avaliação das compras.

            frete() -> float:
                Retorna o valor médio do frete.

            populares(i: int) -> dict:
                Retorna as i categorias de produto mais vendidas.

            maisVendidos(i: int) -> dict:
                Retorna os i produtos mais vendidos.

            menosVendidos(i: int) -> dict:
                Retorna os i produtos menos vendidos.

        '''
    
    def __init__(self,path : str, nome : str):
        """
        Inicializa a classe Loja carregando os dados de um arquivo CSV.

        Args:
            path (str): Caminho ou URL para o arquivo CSV.
            nome (str): Nome para identificar a loja
        """
        self.dados = pd.read_csv(path)
        self.nome = nome

    def faturamento(self) -> float: 
        """
        Calcula o faturamento total da empresa com base na coluna 'Preço'.

        Returns:
            float: Faturamento total, arredondado para 2 casas decimais.
        """
        return float(round(self.dados['Preço'].sum(),2))
    
    def satisfacao(self) -> float:
        """
            Calcula a média de satisfação dos clientes com base na coluna
            'Avaliação da compra'.

            Returns:
                float: Média das avaliações, arredondada para 2 casas decimais.
        """
        return float(round(self.dados['Avaliação da compra'].sum()/len(self.dados['Avaliação da compra']),2))
    
    def frete(self) -> float:
        """
        Calcula o valor médio do frete com base na coluna 'Frete'.

        Returns:
            float: Frete médio, arredondado para 2 casas decimais.
        """

        return float(round(self.dados['Frete'].sum()/len(self.dados['Frete']),2))
    
    def populares(self,i: int = 5) -> dict:
        """
        Retorna as i categorias de produto mais vendidas.

        Args:
            i (int, optional): Número de categorias a retornar. Padrão é 5.

        Returns:
            dict: Dicionário com categorias e respectivas quantidades.
        """

        return {categoria: qtd for categoria, qtd in self.dados['Categoria do Produto'].value_counts().head(i).items()}
    
    def maisVendidos(self,i: int = 5) -> dict:
        """
    Retorna os i produto mais vendidos.

    Args:
        i (int, optional): Número de categorias a retornar. Padrão é 5.

    Returns:
        dict: Dicionário com categorias e respectivas quantidades.
    """
        return {item:qtd for item, qtd in self.dados['Produto'].value_counts().head(i).items()}
    
    def menosVendidos(self,i: int = 5) -> dict:
        """
            Retorna os i produto menos vendidos.

            Args:
                i (int, optional): Número de categorias a retornar. Padrão é 5.

            Returns:
                dict: Dicionário com categorias e respectivas quantidades.
        """
        return {item:qtd for item, qtd in self.dados['Produto'].value_counts().tail(i).items()}
    
    def analise(self,i:int = 5) -> None:
        """
            Exibe no console um resumo com estatísticas da loja.

            Mostra:
            - Faturamento total
            - Média de satisfação
            - Frete médio
            - As i categorias de produto mais populares
            - Os i produtos mais vendidos
            - Os i produtos menos vendidos

            Args:
                i (int, optional): Número de itens/categorias a exibir em cada análise.
                    Padrão é 5.

            Returns:
                None: A função apenas imprime as informações no console.
            """
        
        print(f"Faturamento Total - R${"{:,.2f}".format(self.faturamento())}")
        print("-"*40)
        print(f"Média de Satisfação - {self.satisfacao()}")
        print("-"*40)
        print(f"Frete Médio - R${self.frete()}")
        print()
        print("Itens Mais Populares")
        print()
        print(self.dados['Categoria do Produto'].value_counts().head(i))
        print()
        print("-"*40)
        print("Mais vendidos")
        print(self.dados['Produto'].value_counts().head(i))
        print("."*40)
        print("Menos vendidos")
        print(self.dados['Produto'].value_counts(ascending=True).head(i))
        print("="*40)
                     
loja1 = Loja(url, "Loja 1")
loja2 = Loja(url2, "Loja 2")
loja3 = Loja(url3, "Loja 3")
loja4 = Loja(url4, "Loja 4")

lojas = [loja1, loja2, loja3, loja4]

'''
#Faturamento por loja

plt.bar([x.nome for x in lojas], [x.faturamento() for x in lojas], color = 'skyblue')
plt.title("Faturamento total por loja")
plt.xlabel('Loja')
plt.ylabel('Total')
plt.show()'''

#Principais categorias por loja
'''
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
axs = axs.flatten()

for i, loja in enumerate(lojas):
    dados = loja.populares()  
    axs[i].pie(
        dados.values(),
        labels=dados.keys(),
        autopct='%1.1f%%',
        startangle=90
    )
    axs[i].set_title(f"Loja {i + 1}")
    axs[i].axis('equal') 

plt.tight_layout()
plt.show()
'''
#Histograma para verificar as avaliações por loja
''' 
fig, axs = plt.subplots(2,2, figsize=(10,8))
axs = axs.flatten()

for i, loja in enumerate(lojas):
    dados = loja.dados['Avaliação da compra']
    axs[i].hist(dados,bins=10,edgecolor = 'black')
    axs[i].set_title(f"Loja{i+1}")
    
plt.tight_layout()
plt.show()'''






    





