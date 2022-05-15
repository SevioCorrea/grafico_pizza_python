import matplotlib.pyplot as plt
import numpy as np

# Valores que serão usados como exemplo
y = np.array([35, 25, 25, 15])

# Itens que receberão os valores
itens_grafico = ['LinkedIn', 'Instagram', 'Facebook', 'Twitter']

# Definir o espaço entre os itens do gráfico
espaço_itens = [0.2, 0.1, 0.1, 0.1]

# Montando o gráfico e executando
plt.pie(y, labels=itens_grafico, explode=espaço_itens, shadow=True)
plt.show()