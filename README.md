# Trabalho 2 – Poda alfa-beta em Othello

## Integrantes (Nome / Cartão de Matrícula / Turma)

- Arthur Brackmann Pires / 00326113 / B

- Akim Lee Pizutti / 00302937 / B

- Vitor Vargas / 00302162 / B

## Bibliotecas

- deepcopy

## Descrição da Função de Avaliação
O critério de avaliação foi feito com base nas regras introdutórias do Othello, onde cada posição do tabuleiro possui uma prioridade estratégica. 

Se durante nossa rodada tivermos, por exemplo, duas jogadas válidas, uma em um dos cantos do tabuleiro e outra em uma posição mais central do tabuleiro, iremos fazer a jogada no canto, pois os cantos do tabuleiro possuem maior vantagem estratégica ao longo do jogo.

Com base nisto, pesquisamos na internet alguma referência para esta implementação e encontramos o artigo mencionado na seção acima, que consta com uma matriz de valores preenchida conforme estas prioridade determinadas para as posições do tabuleiro.

Utilizando esta matriz de pesos a cada rodada, o algoritmo de poda alfa beta utiliza estes pesos para as comparações, recebendo uma jogada [linha,coluna] e procurando na matriz de pesos qual a sua prioridade.

## Estratégia de Parada
Utilizamos uma simples busca limitada à profundidade 6. Esta profundidade foi escolhida pois não afeta a eficiência do algoritmo, enquanto também permite uma boa previsão de movimentos. Profundidades acima de 6 não melhoraram considerávelmente as chances de vitória do jogador, e também afetaram negativamente a performance do algoritmo.

## Eventuais Melhorias
A estratégia de parada pode ser perigosa, pois selecionar um movimento que em 8 jogadas leva a uma posição estratégicamente vantajosa pode não ser o ideal se a peça for tomada na jogada 9. Portanto, seria possível implementar a Quiescence Search para tentar lidar com tais problemas nas tomadas de decisões.

## Decisões de Projeto
Seguimos a implementação usual do algoritmo de poda alfa beta, apenas adaptando-o aos elementos do cenário de jogo e a estratégia de parada. Estas adaptações foram:
- Teste de profundidade máxima
    - Se chegamos na profundidade máxima, o algoritmo deve parar
- Teste de expansão de nodos
    - Expande o nodo caso não possua filhos
- Teste de jogadas possíveis
    - Se o algoritmo ainda não chegou na profundidade máxima mas não possui mais jogadas possíveis a serem analisadas, o algoritmo encerra

## Dificuldades Encontradas
Foi difícil achar algum critério de avaliação decente. Após decidirmos usar uma tabela com pesos para cada posição, o uso da tabela descrita no primeiro artigo das bibliografias citadas 'Othello/Reversi using Game Theory techniques', retornou resultados insatisfatórios, foi então que encontramos o segundo artigo, o qual melhorou significantemente o algoritmo.

## Bibliografia
'Othello/Reversi using Game Theory techniques' (https://play-othello.appspot.com/files/Othello.pdf)
'An Analysis of Heuristic in Othello' (https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf)