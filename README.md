# Introdução

O projeto é baseado no desafio da plataforma Dio que pede o seguinte:

```

Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal

Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"

```

O algoritmo de pontuação será o Elo Rating System:

1. **Cálculo inicial**: Cada jogador começa com um rating de base, muitas vezes 1200, que se ajusta com base em vitórias, derrotas ou empates contra outros jogadores.
2. **Ajuste de Rating**: Após cada jogo, o rating de um jogador é ajustado com base no resultado e no rating do adversário. Se um jogador com um rating mais baixo vence um jogador com um rating mais alto, o ganhador receberá mais pontos do que se vencesse um jogador com um rating mais baixo.
3. **Fórmula**: A fórmula básica para ajustar o rating é:  

$$
Novo Rating = Rating Antigo + K(Resultado - Expectativa)  
$$

onde:  

   - K é um fator constante (geralmente 32, 24 ou 16),
   - Resultado é 1 para uma vitória, 0,5 para um empate e 0 para uma derrota,
   - Expectativa  é calculada pela fórmula:  

$$
Expectativa = \frac{1}{1 + 10^{((Rating do Adversário - Rating Antigo)/400)}}
$$
