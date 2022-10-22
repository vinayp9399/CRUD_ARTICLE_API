To run this project locally:  
  
1. Install requirements:  
  
```on the terminal  
$ pip install -r requirements.txt  
```  
  
2. Set up DB:   
   
```on the terminal  
$ python manage.py makemigrations   
$ python manage.py migrate   
```  
   
3. Run the app:   
  
```on the terminal   
$ python manage.py runserver  
```   
In the URL-
1. add extension- /api/article_details to access the api.

2. add extension- /api/article_details/<int:id> to access the article with a specific id.
   (example- /api/article_details/1 to access article with id=1.)