# Avalia_JogoDeForca

APS 7 - Álgebra Linear e Teoria da Informação - 2023.1

## Integrantes do grupo
* [Isabelle da Silva Santos](https://github.com/isabelleatt)
* [Livia Tanaka](https://github.com/liviatanaka)

## Introdução

O projeto "Avalia Jogo de Forca" é uma APS (Atividade Prática Supervisionada) desenvolvido para a disciplina de Álgebra Linear e Teoria da Informação, ministrada pelo professor Tiago Fernandes Tavares.
Esse projeto tem como objetivo projetar e avaliar um jogador de forca, executando um número grande de jogos diferentes e reportando a probabilidade de seu algoritmo vencer o jogo.

## Resolução do problema

Para conseguir implementar um jogador automático de forca que ganha o máximo de vezes possível com apenas 5 vidas, foi necessário implementar um jogador inteligente que utiliza o conceito de probabilidade para escolher a letra que mais se repete no vocabulário, e assim, aumentar as chances de acertar a palavra.

Para isso, seguimos os seguintes passos:

1. Criação do dataframe:

    Para a criação do dataframe, utilizamos a biblioteca pandas para ler o arquivo `br-sem-acentos.txt` e transformar o conteúdo desse arquivo em um dataframe. O aquivo `frequencia1.csv` informa quais letras aparecem em cada palavra.

1. Implementação do jogo de forca

    Para a implementação do jogo de forca, utilizamos a classe `JogoDeForca` que foi disponibilizada pelo professor. Além disso, essa classe possui os seguintes métodos: `novo_jogo`, `tentar_letra` e `tentar_palavra`. O método `novo_jogo` cria um novo jogo com uma palavra aleatória e 5 vidas. O método `tentar_letra` valida o chute passado como parâmetro e o mesmo ocorre com o método `tentar_palavra`.

1. Criação de um jogador

    a. Inicia a rodada filtrando as palavras com o número de letras igual ao da palavra misteriosa;
    b. Escolhe a letra de acordo com o método selecionado. Os dois métodos são:
        * `letra_mais_frequente`: Probabilidade da letra na lista de palavras, ou seja, seleciona a letra que mais aparece nas palavras, de modo que, contabiliza o número de ocorrências de cada letra em cada palavras;  
        * `letra_mais_palavras`: Probabilidade da letra aparecer na palavra, ou seja, seleciona a letra que aparece em um maior número de palavras, independente do número de ocorrências da letra em uma mesma palavra;
    c. Chuta a letra escolhida;
    d. Filtra a lista de palavras de acordo com o resultado do chute;
        * Caso a letra apareça na palavra, o jogador chuta considerando as suas posições na palavra;
        * Caso ela não apareça, o jogador filtra tirando as palavras que tenham tal letra;
    e. O jogador volta para o passo `b` até ele encontrar a palavra, ou até ele perder todas as vidas;
        * Caso ele chegue na última vida e não tenha informações suficientes para acertar a palavra, ele chuta uma plavra com base na lista de palavras possíveis.

## Conclusão

Com a implementação do jogador inteligente, conseguimos aumentar as chances de acertar a palavra secreta, pois, ao utilizar a entropia para escolher a letra que mais se repete no vocabulário, conseguimos diminuir o número de palavras possíveis que a palavra secreta pode ser.

### Relacionando com a teoria

É possível relaciona a estratégia que utilizamos para encontrar a palavra com o código de Hufmann, pois, assim como o código utiliza a probabilidade das letras para construir a árvore,


ao utilizar a frequencia para escolher a letra que mais se repete no vocabulário, conseguimos diminuir o número de palavras possíveis que a palavra secreta pode ser, assim como o ``código de Hufmann, que utiliza a entropia para diminuir o número de bits necessários para representar uma palavra. Pois, assim como o código utiliza a probabilidade das letras para construir a árvore,


* Bibliotecas utilizadas
    
        * pandas
        * numpy
        * random
        * math
