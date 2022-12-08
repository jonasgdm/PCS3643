# PCS3643 - Laboratório de Engenharia de Software I
#### Jonas Gomes de Morais - 10893805
#### Pedro Vitor Bacic - 11806934

## Link do site na nuvem - jonasgm.pythonanywhere.com
#### Usuários:
- operador
- funcionario
- torre
- gerente
- piloto

## Atividades das demais aulas
A documentação desenvolvida nas atividades das aulas está presente na pasta [`\Docs`](https://github.com/jonasgdm/PCS3643/tree/main/Docs) deste repositório.

## Atividade da aula 5
Nesta aula, foi inicializada uma aplicação com o framework Django, incluindo seu versionamento com o presente repositório na plataforma GitHub.

### Pré-requisitos

Os pré-requisitos para executar o projeto são ter instalados Python e o framework Django.

### Passo a passo

#### 1. Clonando o repositório

Execute o seguinte comando na pasta onde deseja clonar o repositório:

```
git clone https://github.com/jonasgdm/PCS3643.git
```

#### 2. Inicializando ambiente virtual
Estando na raiz do projeto (`...\MyProj\`), executar o comando:

```
python -m venv env
```

Para windows:
```
.\env\Scripts\Activate.ps1
```

Para linux ou mac:
```
source env/bin/activate
```

#### 3. Executando aplicação
Para executar a aplicação, insira o seguinte comando no terminal:

```
python manage.py runserver
```

Após isso, podemos acessar a aplicação em um navegador, por exemplo, na URL [http://localhost:8000/FIRST](http://localhost:8000/FIRST).

Para mais detalhes, consultar a referência [\[2\]](#Referências).

### Atividade da aula 6
Nesta aula, foi iniciado o desenvolvimento do banco de dados, criando os modelos para as classes e inicializando o banco com as migrações. Além disso foram feitos testes para esses modelos, verificando o seu funcionamento adequado.

Para atualizar os modelos no banco de dados após quaisquer modificações, execute os seguintes comandos:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Para rodar os testes, execute o seguinte comando:

```
python manage.py test
```

### Atividade das aulas 8 e 9
Os testes de  de unidade podem ser rodados pelo mesmo comando da Aula 6:

```
python manage.py test
```

Já o conteudo implementado pode ser acessado pela lista [abaixo](#Templates), o conteúdo pode ser acessado diretamente pelos links. 

### Atividade da aula 14

## Templates
Pelas telas iniciais, abaixo, é possivel acessar as aplicações:

- `http://localhost:8000/inicio-operador` - Tela inicial para Operador de Voos

- `http://localhost:8000/inicio-monitoracao/` - Tela inicial para Piloto, Funcionário da COmpanhia Aérea e Funcionário da Torre de Controle

- `http://localhost:8000/inicio-gerente/` - Tela inicial para Gerente

A seguir tem-se a lista das telas implementadas:

- `http://localhost:8000/crud` - Tela do CRUD

- `http://localhost:8000/crud/create` - Tela de criar cadastro de Voo 

- `http://localhost:8000/crud/read` - Tela de ver dados do Voo (lista)

- `http://localhost:8000/crud/read/idVOO` - Tela de ver dados do Voo (especifico para cada código de voo existente substituido em idVOO)

- `http://localhost:8000/crud/update/` - Tela de autalizar dados do Voo (lista)

- `http://localhost:8000/crud/update/idVOO` - Tela de autalizar dados do Voo (especifico para cada código de voo existente substituido em idVOO)

- `http://localhost:8000/crud/delete/` - Tela de deletar cadastro do Voo (lista)

- `http://localhost:8000/crud/delete/idVOO` - Tela de deletar cadastro do Voo (especifico para cada código de voo existente substituido em idVOO)

- `http://localhost:8000/relatorio/` - Tela de selecionar os tipos de Relatório

- `http://localhost:8000/relatorio/partidas/` - Tela do relatório pelas partidas

- `http://localhost:8000/relatorio/chegadas/` - Tela do relatório pelas chegadas

- `http://localhost:8000/relatorio/partidas-gerado/intervaloSolicitado/` - Tela do relatório gerado (especifico para cada intervalo solicitado substituido em intervaloSolicitado)

- `http://localhost:8000/relatorio/chegadas-gerado/intervaloSolicitado/` - Tela do relatório gerado (especifico para cada intervalo solicitado substituido em intervaloSolicitado)

- `http://localhost:8000/painel-monitoracao/` - Tela do Painel de Monitoração

- `http://localhost:8000/monitoracao-status/` - Tela de Monitoração de Status

- `http://localhost:8000/monitoracao-status/update/idVOO/` - Tela da Atualização de Status (especifico para cada código de voo existente substituido em idVOO)

## Projeto da disciplina
O projeto consiste em um sistema de monitoramento de voos, com funcionalidades como o cadastro e atualização de dados sobre os voos, o monitoramento em tempo real dos mesmos e a geração de relatórios detalhados sobre as viagens [\[1\]](#Referências).

## Referências
1. HIRAMA, Kechi. [PCS 3643 Enunciado Monitoramento de Voos de Aviões](https://edisciplinas.usp.br/pluginfile.php/7309402/mod_resource/content/1/PCS%203643%20Enunciado%20Monitoramento%20de%20Voos%20de%20Avi%C3%B5es%20v1.pdf). versão 1, 2022.
2. FARFÁN, Carlos; CHAVEZ, Michelet D. C.; HIRAMA, Kechi. [Aula 5 Django - Primeiros Passos](https://edisciplinas.usp.br/mod/folder/view.php?id=4478284). versão 4, 2022.
