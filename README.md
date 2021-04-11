# ScrapperAPI
A News Scrapper API for scraping news headlines, in this case the original website is https://lite.cnn.com . This API also can use to show all list news headlines, edit, and delete the headlines also can create the headline using Django REST Framework

# Endpoint Description
This below is all endpoint that have been created and one endpoint accept search keyword(s) to search the news headlines and return a list of news headlines details as a response.

## [GET] / (Show the API Schema)

example : http://localhost:8000/
if success, then the response is :

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/vnd.oai.openapi
Vary: Accept

!!python/object/apply:collections.OrderedDict
- - - name
    - Schema
  - - description
    - ''
  - - renders
    - - application/vnd.oai.openapi
      - application/vnd.oai.openapi+json
      - text/html
  - - parses
    - - application/json
      - application/x-www-form-urlencoded
      - multipart/form-data
```

## [GET] /news (Show all list news headlines)
example : http://localhost:8000/news/
if success, then the response is :

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "statusCode": 200,
    "data": [
        {
            "id": 1,
            "title": "military branch to disclose service-wide numbers said it is working to build vaccine confidence among its ranks",
            "category": "vaccine",
            "url": "/en/article/h_60acf409e075eff532878b2b9778f89f"
        },
        {
            "id": 2,
            "title": "Supreme Court again blocks California Covid restriction on religious activities",
            "category": "religious activities",
            "url": "/en/article/h_4069f22422cb3aa4ee52530e4616e4f8"
        }
    ],
    "successMessage": "Success Load Data",
    "errorMessage": ""
}
```

## [POST] /news/add (Add a single news headlines)
example : http://localhost:8000/news/add
```
Body Request (JSON) :
{
  "title" : "Cuaca Ekstrim Melanda Jakarta",
  "category" : "cuaca",
  "url" : "https://google.com/"
}
```
if success, then the response is :

```
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Location: https://google.com
Vary: Accept

{
    "id": 1,
    "title": "Cuaca Ekstrim Melanda Jakarta",
    "category": "cuaca",
    "url": "https://google.com"
}

```
if there is error or validation error :
```
HTTP 400 Bad Request
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "title": [
        "This field may not be blank."
    ],
    "url": [
        "This field may not be blank."
    ]
}
```
## [GET] /news/?param= (Get list news that contain search keyword from param)
example : http://localhost:8000/news/?search=vaccine

if success, then the response is :

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "statusCode": 200,
    "data": [
        {
            "id": 1,
            "title": "military branch to disclose service-wide numbers said it is working to build vaccine confidence among its ranks",
            "category": "vaccine",
            "url": "/en/article/h_60acf409e075eff532878b2b9778f89f"
        },
        {
            "id": 82,
            "title": "The first military branch to disclose service-wide numbers said it is working to build vaccine confidence among its ranks",
            "category": null,
            "url": "/en/article/h_60acf409e075eff532878b2b9778f89f"
        }
    ]
    "successMessage": "Success Load Data",
    "errorMessage": ""
}

```
If data is not found or null :

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "statusCode": 204,
    "data": "",
    "successMessage": "",
    "errorMessage": "No Content"
}
```

## [GET] /news/:id (Get a single news headlines)
example : http://localhost:8000/news/2
if success, then the response is :
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "statusCode": 200,
    "data": {
        "id": 2,
        "title": "Supreme Court again blocks California Covid restriction on religious activities",
        "category": "religious activities",
        "url": "/en/article/h_4069f22422cb3aa4ee52530e4616e4f8"
    },
    "successMessage": "Success",
    "errorMessage": ""
}
```
if error or no data :
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "statusCode": 204,
    "data": "",
    "successMessage": "",
    "errorMessage": "No Content"
}
```
## [PUT] /news/:id (Update a single news headlines)
example : http://localhost:8000/news/1
```
Body Request (JSON) :
{
  "title" : "Cuaca Ekstrim Melanda Indonesia",
  "category" : "cuaca",
  "url" : "https://google.com/"
}
```
if success, then the response is :
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "statusCode": 200,
    "data": {
        "id": 1,
        "title": "Cuaca Ekstrim Melanda Jakarta",
        "category": "cuaca",
        "url": "https://google.com"
    },
    "successMessages": "Success Updated Data",
    "errorMessage": ""
}
```
if error or validation error :
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "statusCode": 409,
    "data": {
        "title": [
            "This field may not be blank."
        ],
        "url": [
            "This field may not be blank."
        ]
    },
    "successMessage": "",
    "errorMessage": "Terjadi Kesalahan"
}
```
## [DELETE] /news/:id (Delete a single news headlines)
example : http://localhost:8000/news/1
```
Body Request (JSON) :
{
  "id" : 1
}
```
if success, then the response is :
```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "statusCode": 200,
    "data": "",
    "successMessage": "Success Delete Data",
    "errorMessage": ""
}
```
## [GET] /scrape (Scrapping Website)
example : http://localhost:8000/scrape/
the response is : Success Scrapping Data

# How to setup the API
First Create and start your virtual environment (I'm Using Windows Environment): Clone or download this repository

```
$ py -m venv project-name
$ project-name\Scripts\activate.bat
$ pip install -r requirement.txt
$ python manage.py runserver
```


# How to test the API
If you want to get unit testing of the endpoint that have been create, then you can just run this command :
```
$ python manage.py test
```
If you want to test the API running well or not, after run the server ```python manage.py runserver``` , you'll able to test the API directly because Django Rest Framework is Browsable, or you can test the API using Postman.

Here the link of documentation that contain API testing result : 
https://docs.google.com/document/d/1EX8pHxlHB4EC3EDC7aP1_gib18QjoKZIv9eKH3tgRXk/edit?usp=sharing

