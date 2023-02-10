# Trabalho 2 – Poda alfa-beta em Othello

## Integrantes (Nome / Cartão de Matrícula / Turma)

- Arthur Brackmann Pires / 00326113 / B

- Akim Lee Pizutti / 00302937 / B

- Vitor Vargas / 00302162 / B

## Bibliotecas

- Nenhuma

## Descrição da Função de Avaliação
 Analisando algumas dicas à jogadores iniciantes, notamos a repetição da menção de posições vantajosas. Foi então que decidimos usar como avaliação da posição uma tabela que retém o peso referente a cada posição do tabuleiro de Othello. Após algumas dificuldades que mencionaremos adiante, decidimos pelo uso de uma tabela que, para cada posição, atribuí um peso referente ao seu controle do tabuleiro e à quantos posições cobre.

## Estratégia de Parada
Além de naturalmente pararmos quando não há mais jogadas disponíveis, paramos nossa descida obrigatoriamente quando o algoritmo chega à uma profundidade fixa de MAX_DEPTH (8).


## Eventuais Melhorias
A estratégia de parada pode ser perigosa, pois selecionar um movimento que em 8 jogadas leva a uma posição estratégicamente vantajosa pode não ser o ideal se a peça for tomada na jogada 9. Portanto, seria possível implementar a Quiescence Search para tentar lidar com tais problemas nas tomadas de decisões.

## Decisões de Projeto
 - Decidimos que iríamos usar uma profundidade máxima como estratégia de parada
 - Decidimos usar uma tabela com valores para cada posição do tabuleiro como função de avaliação
 - Usamos o slide que descreve a poda alfa-beta do moodle como base para implementar as funções minimax.
 

## Dificuldades Encontradas
Foi difícil achar algum critério de avaliação decente. Após decidirmos usar uma tabela com pesos para cada posição, o uso da tabela descrita no primeiro artigo das bibliografias citadas 'An Analysis of Heuristic in Othello' retornou resultados insatisfatórios, foi então que encontramos o segundo artigo, o qual melhorou significantemente o algoritmo.

## Bibliografia
'An Analysis of Heuristic in Othello' (https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf)
'Othello/Reversi using Game Theory techniques' (https://play-othello.appspot.com/files/Othello.pdf)
Slide 'Jogos e Busca Competitiva (v2)' do moodle da cadeira