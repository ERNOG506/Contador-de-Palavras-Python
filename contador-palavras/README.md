# Contador de Palavras

Programa em Python que conta quantas palavras existem em uma frase digitada pelo
usuario ou em um arquivo de texto.

Este projeto foi desenvolvido com uma estrutura organizada para portfolio,
seguindo boas praticas simples do ecossistema Python.

## Funcionalidades

- Contar palavras de uma frase digitada pelo usuario
- Contar palavras de um arquivo `.txt`
- Ignorar pontuacoes soltas na contagem
- Validar entradas vazias
- Exibir mensagens claras no terminal
- Testes automatizados com `unittest`

## Tecnologias

- Python 3.10+
- Regex
- `pathlib`
- `unittest`

## Estrutura do projeto

```txt
contador-palavras/
├── main.py
├── README.md
├── .gitignore
├── requirements.txt
├── LICENSE
├── exemplos/
│   └── texto_exemplo.txt
├── src/
│   └── contador_palavras/
│       ├── __init__.py
│       ├── cli.py
│       └── counter.py
└── tests/
    ├── __init__.py
    └── test_counter.py
```

## Como executar

Entre na pasta do projeto:

```powershell
cd "C:\Users\nogue\Documents\Codex\projetos\contador-palavras"
```

Execute o programa:

```powershell
py main.py
```

## Exemplo de uso

Entrada:

```txt
Bem, e so mais um dia para eu ser um profissional em programacao.
```

Saida:

```txt
Legal! Voce acabou de me dizer no que pensou usando 13 palavras!
```

## Como contar palavras de um arquivo

No menu, escolha a opcao `2` e informe o caminho de um arquivo de texto.

Exemplo:

```powershell
C:\Users\nogue\Documents\Codex\projetos\contador-palavras\exemplos\texto_exemplo.txt
```

## Como rodar os testes

```powershell
py -m unittest discover -s tests
```

## Objetivo do projeto

Este projeto demonstra:

- manipulacao de strings;
- leitura de arquivos;
- uso de expressoes regulares;
- separacao de responsabilidades;
- organizacao de projeto Python;
- testes automatizados.
