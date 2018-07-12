# MY PORTFOLIO



Welcome to my PORTFOLIO! Discover more about me and what I'm all about in this **Django** based web application.




## 1. Building the app

It is best to use the python `virtualenv` tool to build locally:

```
$ virtualenv venv --python-3.6.2
$ source venv/bin/activate
$ pip install -r requirements.txt
$ DEVELOPMENT=1 python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. 



## 2. requirements.txt

**The requirements.txt file serves as a placeholder for python dependancies.**

    Contents:
- astroid==1.6.3
- click==6.7
- dj-database-url==0.5.0
- Django==1.11
- django-bootstrap3==10.0.1
- dominate==2.3.1
- Flask==1.0.2
- Flask-Bootstrap==3.3.7.1
- Flask-Script==2.0.6
- Flask-WTF==0.14.2
- gunicorn==19.8.1
- isort==4.3.4
- itsdangerous==0.24
- Jinja2==2.10
- lazy-object-proxy==1.3.1
- MarkupSafe==1.0
- mccabe==0.6.1
- Pillow==5.1.0
- psycopg2==2.7.4
- psycopg2-binary==2.7.4
- pyperclip==1.6.2
- python-decouple==3.1
- pytz==2018.4
- six==1.11.0
- visitor==0.1.3
- Werkzeug==0.14.1
- whitenoise==3.3.1
- wrapt==1.10.11
- WTForms==2.1

**Once you have run the ```pip installation```, verify that you have all the necessary requirements with the following command:**


 ```
 pip3 freeze
 ```

![alt text](./media/thatsall.jpg "Logo Title Text 1")

The app should now run smoothly on your local server.......

__If it doesn't work or you are experiencing errors__, please report to: 

<plucaslambert@gmail.com>



## Functionality breakdown

__Let's get down and dirty & see how this app code works:__

1. Components:

The **Django** framework allows for fast and effective control over new objects.

In this application **I made use of this** by creating **project categories** that are then templated **conditionally**.

EXAMPLE:

```models.py```

```python
from django.db import models
import datetime



class Resume(models.Model):
    cat_choices = (
        ("PYTHON","PYTHON"),
        ("HTML","HTML"),
        ("BLENDER","BLENDER"),
    )

    category = models.CharField(max_length = 7 , choices = cat_choices , default = "HTML")
    title = models.CharField(max_length = 30)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add= True)
    githuburl = models.CharField(max_length = 255, blank = True)
    live_app_deployment = models.CharField(max_length = 255 , blank = True)
    article_image = models.ImageField(blank = True)

    def __str__(self):
        return self.title
```
The **Resume** class takes in a choice feild, which is then handled in the templates with the ```{% for items in blender %}``` and ```{% if items.category == "BLENDER" %}``` templating functions.
it **conpares** if the value of the category of the object is equal to BLENDER (in this case). 

In our **views.py** file we handle what happens with this classmethod:

```views.py```


```python
def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article") 
        searched_images = Image.search_by_title(search_term) or Tag.search_by_tag(search_term) or Category.search_by_cat(search_term)
        message = f"{search_term}"
        date = dt.date.today()

        return render(request, 'all_images/search.html', {"message":message, "images": searched_images, "date":date})
    else:
        message = "You havne't searched for any term"
        date = dt.date.today()
        return render(request, 'all_images/search.html',{"message":message, "date":date})
```
First we define the GET request by saying:
- First we make sure the object "article" really exists in our request.
- The search terms is the gotten from the requested object by passing the __key__ "article"



Django allows us to connect this model to a postgresql db:


```settings.py```

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'zoominphotos',
        'USER': '***...***',
        'PASSWORD': '***...***',
    }
}
```

The __engine__ key defines what kind of database you want to use.



## Get involved!

We are happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[github issue tracker](https://github.com/lucasLB7/Zoomin-Photos-/issues).

Master [git repository](https://github.com/lucasLB7/Zoomin-Photos-):


## Licensing

This library is MIT-licensed.


```The MIT License

Copyright (c) 2010-2018 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.```
