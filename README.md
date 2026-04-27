# Gerador de Senhas Seguras (Web)

Aplicacao web simples para gerar senhas seguras e aleatorias com base em criterios definidos pelo usuario.

## Descricao

O projeto implementa um gerador de senhas com foco em seguranca e simplicidade. O usuario escolhe tamanho e tipos de caracteres, e a aplicacao garante pelo menos um caractere de cada tipo selecionado.

## Tecnologias

- Python 3.12+
- Flask
- Pytest
- HTML + CSS

## Requisitos

- Python 3.12+
- Ambiente virtual ativo

## Instalacao

```bash
pip install -r requirements.txt
```

## Uso

```bash
python app.py
```

Acesse no navegador: `http://127.0.0.1:5000`

## Testes

```bash
pytest
```

## Funcionalidades do MVP

- Definir tamanho da senha
- Incluir/excluir maiusculas, minusculas, numeros e simbolos
- Garantir ao menos 1 caractere por tipo selecionado
- Geracao criptograficamente segura com `secrets`

## Secao de IA

A IA foi utilizada para apoiar:

- Geracao inicial da estrutura do projeto
- Criacao e refinamento de testes automatizados
- Melhorias de documentacao (README)

## Limitacoes

- Nao armazena historico de senhas
- Nao possui autenticacao de usuarios
- Nao possui API publica
- Nao possui indicador de forca da senha (futuro)
