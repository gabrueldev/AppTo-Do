# App To-Do

![CI](https://github.com/gabrueldev/AppTo-Do/actions/workflows/actions.yml/badge.svg)

### Já pensou em anotar suas tarefas e ser lembrado delas?

API REST de lista de tarefas em que o próprio app manda **emails de lembrete** para o usuário, para a lista não esfriar e os afazeres não se acumularem. As tarefas terão prazo e poderão ser diárias, mensais ou de qualquer categoria que o usuário criar.

## Status

| Parte | Situação |
|---|---|
| Autenticação com JWT (cadastro, login, edição e exclusão de conta) | ✅ Pronto e testado |
| CRUD de tarefas com prazo e categoria | 🚧 Em desenvolvimento |
| Lembretes por email com Redis + Celery | 📋 Planejado |
| Front-end simples em HTML + CSS consumindo a API | 📋 Planejado |

## Rotas disponíveis

```
POST   /api/user/cadaster/            → cria a conta
POST   /api/user/login/               → devolve access e refresh token (JWT)
PATCH  /api/user/edit/<username>/     → edita a conta (só o próprio dono)
DELETE /api/user/delete/<username>/   → apaga a conta (só o próprio dono)
```

Editar e apagar a conta usa uma permissão própria (`IsOwner`): mesmo logado, um usuário não consegue alterar a conta de outro. Os testes cobrem esse caso.

## Tecnologias

+ Python 3.12
+ Django + Django REST Framework
+ JSON Web Token (SimpleJWT + dj-rest-auth)
+ SQLite em desenvolvimento
+ Pytest | Testes Automatizados
+ CI com GitHub Actions

## Rodando o projeto

    pip install -r app/requirements.txt
    python manage.py migrate
    python manage.py runserver

## Testes

    pytest

Os testes rodam a cada push pelo GitHub Actions.
