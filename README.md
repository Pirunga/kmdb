Description
KMDb's API with creation, list and authentication of users (user, crítico and admin), creation, filter, delete and list of movie(s), creation and update of review and comments.

Dev
Luiz Almeida - All

Tecnologias
Black, Django, and Django Rest Framework

Instalação
To create .venv use command:

```
    python -m venv .venv
```

To active the venv use command:

```
    source .venv/bin/activate
```

To install all tecnologies use command:

```
    pip install -r requirements.txt
```

To create the tables use command:

```
    ./manage.py makemigrations
```

To configurate the tables use command:

```
    ./manage.py migrate
```

To start the server localy use command:

```
    ./manage.py runserver
```

Rotas

ROOT - "/api".

"/accounts/" ["POST"] - To creater a user.

Usuário - It will have is_staff and is_superuser as False
Crítico - It will is_staff as True and is_superuser as False
Admin - It will is_staff and is_superuser as True

Usuário:

```
    Body request:
        {
            "username": "user",
            "password": "1234",
            "first_name": "John",
            "last_name": "Wick",
            "is_superuser": false,
            "is_staff": false
        }

    Status: 201_CREATED
    Response:
        {
            "id": 1,
            "username": "user",
            "first_name": "John",
            "last_name": "Wick",
            "is_superuser": false,
            "is_staff": false,
        }
```

Crítico:

```
    Body request:
        {
            "username": "critic",
            "password": "1234",
            "first_name": "Jacques",
            "last_name": "Aumont",
            "is_superuser": false,
            "is_staff": true
        }

    Status: 201_CREATED
    Response:
        {
            "id": 2,
            "username": "critic",
            "first_name": "Jacques",
            "last_name": "Aumont",
            "is_superuser": false,
            "is_staff": true,
        }
```

Administrador:

```
    Body request:
        {
            "username": "admin",
            "password": "1234",
            "first_name": "Jeff",
            "last_name": "Bezos",
            "is_superuser": true,
            "is_staff": true
        }

    Status: 201_CREATED
    Response:
        {
            "id": 3,
            "username": "admin",
            "first_name": "Jeff",
            "last_name": "Bezos",
            "is_superuser": true,
            "is_staff": true,
        }
```

Existed user's:

```
    Status: 400_BAD_REQUEST
    Response:
        {
            "username": [
                "A user with that username already exists."
            ]
        }
```

"/login/" ["POST"] - To Authenticate user.

```
    Body Request:
        {
            "username": "critic",
            "password": "1234"
        }

    Status: 200_OK
    Response:
        {
            "token": "dfd384673e9127213de6116ca33257ce4aa203cf"
        }
```

"/movies/" ["POST"] - To create a movie, must be logged as admin.

```
    Header -> Authorization: Token <admin-token>
    Body Request:
        {
            "title": "O Poderoso Chefão",
            "duration": "175m",
            "genres": [
                {"name": "Crime"},
                {"name": "Drama"}
                ],
            "launch": "1972-09-10",
            "classification": 14,
            "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' de Nova York que está feliz, pois Connie (Talia Shire), sua filha,se casou com Carlo (Gianni Russo). Por ser seu padrinho Vito foi procurar o líder da banda e ofereceu 10 mil dólares para deixar Johnny sair, mas teve o pedido recusado."
        }

    Status: 201_CREATED
    Response:
        {
            "id": 1,
            "title": "O Poderoso Chefão",
            "duration": "175m",
            "genres": [
                {
                "id": 1,
                "name": "Crime"
                },
                {
                "id": 2,
                "name": "Drama"
                }
            ],
            "launch": "1972-09-10",
            "classification": 14,
            "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' de Nova York que está feliz, pois Connie (Talia Shire), sua filha,se casou com Carlo (Gianni Russo). Por ser seu padrinho Vito foi procurar o líder da banda e ofereceu 10 mil dólares para deixar Johnny sair, mas teve o pedido recusado.",
            "criticism_set": [],
            "comment_set": []
        }
```

"/movies/" ["GET"] - To list all movies.

```
    Status: 200_OK
    Response:
        [
            {
                "id": 1,
                "title": "O Poderoso Chefão",
                "duration": "175m",
                "genres": [
                {
                    "id": 1,
                    "name": "Crime"
                },
                {
                    "id": 2,
                    "name": "Drama"
                }
                ],
                "launch": "1972-09-10",
                "classification": 14,
                "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' de Nova York que está feliz, pois Connie (Talia Shire), sua filha,se casou com Carlo (Gianni Russo). Por ser seu padrinho Vito foi procurar o líder da banda e ofereceu 10 mil dólares para deixar Johnny sair, mas teve o pedido recusado.",
                "criticism_set": [],
                "comment_set": []
            },
            {
                "id": 2,
                "title": "Um Sonho de Liberdade",
                "duration": "142m",
                "genres": [
                {
                    "id": 2,
                    "name": "Drama"
                },
                {
                    "id": 3,
                    "name": "Ficção científica"
                }
                ],
                "launch": "1994-10-14",
                "classification": 16,
                "synopsis": "Andy Dufresne é condenado a duas prisões perpétuas consecutivas pelas mortes de sua esposa e de seu amante. Porém, só Andy sabe que ele não cometeu os crimes. No presídio, durante dezenove anos, ele faz amizade com Red, sofre as brutalidades da vida na cadeia, se adapta, ajuda os carcereiros, etc."
                "criticism_set": [],
                "comment_set": []
            }
        ]
```

"/movies/" ["GET"] - To list all movies with the specifications passed in body request, title field is required.

```
    Body Request:
        {
            "title": "liberdade"
        }


    Status: 200_OK
    Response:
        [
            {
                "id": 2,
                "title": "Um Sonho de Liberdade",
                "duration": "142m",
                "genres": [
                {
                    "id": 2,
                    "name": "Drama"
                },
                {
                    "id": 3,
                    "name": "Ficção científica"
                }
                ],
                "launch": "1994-10-14",
                "classification": 16,
                "synopsis": "Andy Dufresne é condenado a duas prisões perpétuas consecutivas pelas mortes de sua esposa e de seu amante. Porém, só Andy sabe que ele não cometeu os crimes. No presídio, durante dezenove anos, ele faz amizade com Red, sofre as brutalidades da vida na cadeia, se adapta, ajuda os carcereiros",
                "criticism_set": [],
                "comment_set": []
            },
            {
                "id": 3,
                "title": "Em busca da liberdade",
                "duration": "175m",
                "genres": [
                {
                    "id": 2,
                    "name": "Drama"
                },
                {
                    "id": 4,
                    "name": "Obra de época"
                }
                ],
                "launch": "2018-02-22",
                "classification": 14,
                "synopsis": "Representando a Grã-Bretanha,  corredor Eric Liddell (Joseph Fiennes) ganha uma medalha de ouro nas Olimpíadas de Paris em 1924.  Ele decide ir até a China para trabalhar como missionário e acaba encontrando um país em guerra. Com a invasão japonesa no território chinês durante a Segunda Guerra Mundial, Liddell acaba em um campo de concentração.",
                "criticism_set": [],
                "comment_set": []
            }
        ]
```

"/movies/<int:movie_id>/" ["GET"] - To list a specific movie.

```
    Status: 200_OK
    Response:
        {
            "id": 1,
            "title": "O Poderoso Chefão",
            "duration": "175m",
            "genres": [
            {
                "id": 1,
                "name": "Crime"
            },
            {
                "id": 2,
                "name": "Drama"
            }
            ],
            "launch": "1972-09-10",
            "classification": 14,
            "synopsis": "Don Vito Corleone (Marlon Brando) é o chefe de uma 'família' de Nova York que está feliz, pois Connie (Talia Shire), sua filhase casou com Carlo (Gianni Russo). Por ser seu padrinho Vito foi procurar o líder da banda e ofereceu 10 mil dólares para deixar Johnnysair, mas teve o pedido recusado.",
            "criticism_set": [],
            "comment_set": []
        }
```

"/movies/<int:movie_id>/" ["DELETE"] - To delete a specific movie, must be logged as admin.

```
    Header -> Authorization: Token <admin-token>
    Status: 204_NO_CONTENT
    No Response
```

"/movies/<int:movie_id>/review/" ["POST"] - To create a critical's review in a specific movie, must be logged as critic.

```
    Header -> Authorization: Token <critical-token>
    Body Request:
        {
            "stars": 7,
            "review": "Nomadland podia ter dado muito errado. Podia ser dramático demais, monótono demais ou opaco demais. Felizmente, o que vemos é algo singelo, pois a direção de Zhao (que também edita, assina e produz o longa) não ignora a frieza da realidade, mas sabe encontrar a magia da naturalidade. Sim, rimei sem querer e parece meio poético, mas é assim que o filme funciona mesmo. Viva Chloé Zhao - para sempre! Logo, os holofotes voltaram para esta obra independente da cineasta que, sinceramente, merece toda a atenção que recebeu.",
            "spoiler": false,
        }

    Status: 201_CREATED
    Response:
        {
            "id": 39,
            "critic": {
                "id": 2,
                "first_name": "Jacques",
                "last_name": "Aumont"
                },
            "stars": 7,
            "review": "Nomadland podia ter dado muito errado. Podia ser dramático demais, monótono demais ou opaco demais. Felizmente, o que vemos é algo singelo, pois a direção de Zhao (que também edita, assina e produz o longa) não ignora a frieza da realidade, mas sabe encontrar a magia da naturalidade. Sim, rimei sem querer e parece meio poético, mas é assim que o filme funciona mesmo. Viva Chloé Zhao - para sempre! Logo, os holofotes voltaram para esta obra independente da cineasta que, sinceramente, merece toda a atenção que recebeu.",
            "spoilers": false
        }
```

"movies/<int:movie_id>/review/" ["PUT"] - To update a critical's review in a specific movie, all critic fields are requiered and must be logged as critical.

```

    Header -> Authorization: Token <critical-token>
    Body Request:
        {
            "stars": 8,
            "review": "Nomadland podia ter dado muito errado. Podia ser dramático demais, monótono demais ou opaco demais. Felizmente, o que vemos é algo singelo, pois a direção de Zhao (que também edita, assina e produz o longa) não ignora a frieza da realidade, mas sabe encontrar a magia da naturalidade. Sim, rimei sem querer e parece meio poético, mas é assim que o filme funciona mesmo. Viva Chloé Zhao - para sempre! Logo, os holofotes voltaram para esta obra independente da cineasta que, sinceramente, merece toda a atenção que recebeu.",
            "spoiler": false,
        }

    Status: 201_CREATED
    Response:
        {
            "id": 39,
            "critic": {
                "id": 2,
                "first_name": "Jacques",
                "last_name": "Aumont"
                },
            "stars": 8,
            "review": "Nomadland podia ter dado muito errado. Podia ser dramático demais, monótono demais ou opaco demais. Felizmente, o que vemos é algo singelo, pois a direção de Zhao (que também edita, assina e produz o longa) não ignora a frieza da realidade, mas sabe encontrar a magia da naturalidade. Sim, rimei sem querer e parece meio poético, mas é assim que o filme funciona mesmo. Viva Chloé Zhao - para sempre! Logo, os holofotes voltaram para esta obra independente da cineasta que, sinceramente, merece toda a atenção que recebeu.",
            "spoilers": false
        }

```

"/movies/<int:movie_id>/comments/" ["POST"] - To create an user's comment in a specific movie, must be logged as user.

```
    Header -> Authorization: Token <user-token>
    Body Request:
        {
            "comment": "Lindo filme. Com certeza assistam.",
        }

    Status: 201_CREATED
    Response:
        {
            "id": 1,
            "user": {
                "id": 1,
                "first_name": "John",
                "last_name": "Wick"
            },
            "comment": "Lindo filme. Com certeza assistam."
        }
```

"movies/<int:movie_id>/comments/" ["PUT"] - To update an user's comment in a specific movie, comment_id and comment is required. Must be logged as user.

```

    Header -> Authorization: Token <user-token>
    Body Request:
        {
            "comment_id": 1,
            "comment": "Lindo, nos faz refletir sobre a vida, os anos, envelhecer. Vale a pena assistir"
        }

    Status: 201_CREATED
    Response:
        {
            "id": 11,
            "user": {
            "id": 1,
            "first_name": "John",
            "last_name": "Wick"
            },
            "comment": "Lindo, nos faz refletir sobre a vida, os anos, envelhecer. Vale a pena assistir"
        }

```
