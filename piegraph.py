from pylab import *

genero = ['Comédia', 'Romance', 'Ação', 'Terror', 'Drama']
percentual = [9, 15, 12, 6, 20]
cores = ['y', 'c', 'r', 'g', 'b']

pie(percentual, labels=genero, colors=cores, autopct='%.1f%%')
title('Gênero de filmes mais assistidos via streaming')
