# myfood

## Create and activate a virtual environment
```
virtualenv env
source env/bin/activate
```

## Install the requiremnts
```
pip install -r requirements.txt
```

## create an .env file
```
SECRET_KEY=this-is-not-a-secret
DEBUG=False
```


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


