# Bear the brunt | Aguenta o tranco
This is an educational project to talk about performance tests.
This project contains other branches that follow the script of the main presentation.
The presentation slides can be found [here](https://speakerdeck.com/labcodes/sua-aplicacao-web-aguenta-o-tranco)

the branching order from the presentation:
1. como-a-gente-usa
2. que-tal-tentar-salvar-alguma-coisa
3. vixe-faltou-autenticar
4. se-tivesse-mais-de-um-usuario
5. erro-pra-mim-e-sucesso
6. bora-ajustar-essas-tarefas
7. coisinhas-interessantes

## How to run the performance tests
1. Run the app
2. Run the following command on cmd
```
locust
```
## How to run the app
### Create and activate a virtual environment
```
virtualenv env
source env/bin/activate
```

### Install the requiremnts
```
pip install -r requirements.txt
```

### create an .env file
```
SECRET_KEY=this-is-not-a-secret
DEBUG=False
```

### Create a user
```
from django.contrib.auth.models import User
User.objects.create_user(username='foo', email='foo@bar.com', password='bar')
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Login
### Method: POST
>```
>localhost:8000/api/token/
>```
### Body (**raw**)

```json
{
    "username": "username",
    "password": "password"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: List Meals
### Method: GET
>```
>localhost:8000/api/meals/
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Create Meal
### Method: POST
>```
>localhost:8000/api/meals/
>```
### Body (**raw**)

```json
{
    "sku": "meal123",
    "slug": "soup",
    "title": "Grandma Soup",
    "description": "My Favorite Grandma Soup",
    "category": "mains",
    "start_date": "2022-07-31",
    "end_date": "2030-07-31"
}
```

### 🔑 Authentication bearer

|Param|value|Type|
|---|---|---|
|token|{{access_token}}|string|
