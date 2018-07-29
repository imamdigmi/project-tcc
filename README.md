# Flask Simple RESTful API

## Requirements
1. Python 3.6
2. Pipenv
3. MySQL

## Installation
1. Grab this app: `git clone https://github.com/imamdigmi/project-tcc.git`
2. Go to the app directory: `cd project-tcc`
3. Install dependencies: `pipenv install`
4. Activate virtual envirounment: `pipenv shell`
5. Create database on your MySQL server
6. Migrate database table: `python migrate.py`
7. Have fun!: `python app.py`

## Usage
1. Create data
```bash
curl -X POST http://localhost:5000/review -H 'Content-Type: application/json' -d \
'{
    "order_id": 1,
    "product_id": 1,
    "user_id": 2,
    "rating": 4.5,
    "review": "enak!"
}'
```

2. Get all data
```bash
curl -X GET http://localhost:5000/
```

2. Get data by `id`
```bash
curl -X GET http://localhost:5000/review/2
```

4. Update data
```bash
curl -X PUT http://localhost:5000/review/1 -H 'Content-Type: application/json' -d \
'{
    "order_id": 1,
    "product_id": 1,
    "user_id": 1,
    "rating": 5,
    "review": "bagus banget!"
}'
```

5. Delete data
```bash
curl -X DELETE http://localhost:5000/review/1
```