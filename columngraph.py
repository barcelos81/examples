from pylab import *

tempo = [15, 10, 7, 22]
x = [1, 2, 3, 4]

barh(x, tempo)
yticks(x, ('Cenário 1', 'Cenário 2', 'Cenário 3', 'Cenário 4'))

xlabel('Tempo (em min)')
ylabel('Cenários de teste')
title('Tempos de execução de testes')
