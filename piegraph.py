from pylab import *

produtos = ['Comédia', 'Romance', 'Ação', 'Terror', 'Drama']
quantidade = [9, 15, 12, 6, 20]
cores = ['y', 'c', 'r', 'g', 'b']

pie(quantidade, labels=produtos, colors=cores, autopct='%.1f%%')
title('Gênero de filmes mais assistidos via streaming')
