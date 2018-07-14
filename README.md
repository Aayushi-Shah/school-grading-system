# school-grading-system
School grading system Rest APIS using Django Rest Framework
### Intro
Creating a school grading system using Django Rest Framework

### Key Functionalities
It has two users:
1) Teacher
2) Student

Both users have different authorizations access
Teacher can add marks for students using pdf
Teacher can view marks for all students of any grade
Student can view their own marks 


### Tech
certifi==2018.4.16
chardet==3.0.4
coreapi==2.3.3
coreschema==0.0.4
distro==1.3.0
Django==2.0.7
django-rest-swagger==2.2.0
djangorestframework==3.8.2
djangorestframework-jwt==1.11.0
idna==2.7
itypes==1.1.0
Jinja2==2.10
MarkupSafe==1.0
numpy==1.14.5
openapi-codec==1.3.2
pandas==0.23.3
pdftables-api==1.0.0
PyJWT==1.6.4
python-dateutil==2.7.3
pytz==2018.5
requests==2.19.1
simplejson==3.16.0
six==1.11.0
tabula-py==1.2.0
uritemplate==3.0.0
urllib3==1.23

### Steps for Installation
Make a directory where you want to store the project
    ```mkdir Gridle```
    ```cd Gridle```

Install virtual environment for python
    ``` pip install virtualenv```
    or
    ```python -m pip install virtualenv```

Create virtual environment for python
    ```mkdir vene_gridle```
    ```cd venv_gridle```
    ```virtualenv .```
Activate virtual environment
    ```.\Scripts\activate```

Download or clone folder

Install Requirments
    ```pip install -r requirements.txt```
    or
    ```python -m pip install -r requirements.txt```

Runserver python server
    ``` python manage.py runserver```
    
### Postman APIs
### Login 
 It checks whether user is present in the database
    ```http://127.0.0.1:8000/login```
In Body add following JSON as it is a POST request
    ```[{"email":"value","password":"value"}]```
### AddMarks
It adds marks from a pdf file to Marksheet Model 
    ```http://127.0.0.1:8000/addmarks/<filename>```
example:
```http://127.0.0.1:8000/addmarks/file```
Select form-data in the and select FILE option
Click on ```choose file``` option and select pdf file*
In Headers section add 
    ``` TOKEN ```  at key
    ```{id_value}``` at value where id_value is teacher's id 
    
'*' pdf file should have format
    student_id | grade| english| maths | science
    xlsx or xls file should be saved as pdf
    Copy of your pdf will be stored in your folder with a csv file
    
### GetMarks
This API views all the data for a particular student using student ID
    ```http://127.0.0.1:8000/getmarks```
It is a GET API 
In Headers section add 
    ``` TOKEN ```  at key
    ```{id_value}``` at value where id_value is students' id
### GetMarksByGrade
This API views students' data for that grade using student ID as well as grade parameter
    ```http://127.0.0.1:8000/getmarks/<grade>```
example:
```http://127.0.0.1:8000/getmarks/9```
```http://127.0.0.1:8000/getmarks/8```
It is a GET API
In Headers section add 
    ``` TOKEN ```  at key
    ```{id_value}``` at value where id_value is students' id
    
### GetMarksBYSubject
This API views marks of student for a particular subject using student ID as well as subject parameter
    ```http://127.0.0.1:8000/getmarks/<subject>```
example:
```http://127.0.0.1:8000/getmarks/english```
```http://127.0.0.1:8000/getmarks/maths```
```http://127.0.0.1:8000/getmarks/science```

It is a GET API
In Headers section add 
    ``` TOKEN ```  at key
    ```{id_value}``` at value where id_value is students' id  
    
### FetchMarks
This API views all the data of students using teacher's ID 
    ```http://127.0.0.1:8000/fetchmarks```
It is a GET API 
In Headers section add 
    ``` TOKEN ```  at key
    ```{id_value}``` at value where id_value is Teacher's id
    
### FetchmarksByGrade
This API views all the data of students of same grade using teacher's ID 
    ```http://127.0.0.1:8000/fetchmarks/<grade>```
example:
```http://127.0.0.1:8000/fetchmarks/8```
It is a GET API 
In Headers section add 
    ``` TOKEN ```  at key
    ```{id_value}``` at value where id_value is Teacher's id

### FetchmarksBySubject
This API views all the data of students for a particular subject using teacher's ID 
    ```http://127.0.0.1:8000/fetchmarks/<subject>```
example:
```http://127.0.0.1:8000/fetchmarks/english```
```http://127.0.0.1:8000/fetchmarks/maths```
```http://127.0.0.1:8000/fetchmarks/science```
It is a GET API 
In Headers section add 
    ``` TOKEN ```  at key
    ```{id_value}``` at value where id_value is Teacher's id
    
### UserProfile
This Api views the profile of a particular user
    ````http://127.0.0.1:8000/userprofile>```
It is a GET API
In Headers section add 
    ``` TOKEN ```  at key
    ```{id_value}``` at value where id_value is user's id
    
    

    


    
    
    




    
    
