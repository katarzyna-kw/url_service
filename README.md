# URL Shortener

## Assignment by [Kat Wegrzynowicz](https://katarzyna-kw.github.io/portfolio-website/)

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Steps to Run Locally](#steps-to-run-locally)
- [Author Links](#author-links)

## Overview

This is a solution to a coding challenge to create a URL shortening service using an API with two endpoints:

<span style="color:plum">1. </span> /encode -- takes an original or long URL and encodes a short URL that redirects to the original/long URL

<span style="color:plum">2. </span> /decode -- takes an already created shortened URL that is stored in the database and returns the original or long URL in its response

___

## Tech Stack

* Django Rest Framework / Django / Python
* PostgreSQL database

___

## Steps to Run Locally

<span style="color:salmon"> 1. </span> Clone the repository:

```sh
$ git clone https://github.com/katarzyna-kw/url_service.git
$ cd url_service
$ code .
```

<span style="color:salmon">2.</span> Check whether python 3 is installed locally:

```sh
$ python -V
```

* If the version is Python 3.7.3 or higher, you may proceed to step 3. A. 

* Else, try running the following command: 


```sh
$ python3 -V
```

* If the version shown is Python 3.7.3 or higher, you may proceed to step 3. B. 

* If Python 3.7.3 or higher is not installed, please visit python.org to download the latest version - [python.org/downloads](https://www.python.org/downloads/). Once the download is complete, follow step 2 from the beginning to determine whether to use python or python3 in your command line.


<span style="color:salmon">3. A.</span>   In url_api directory, create virtual environment in which to install dependencies:

```sh
$ python -m venv .venv
```

<span style="color:salmon">3. B.</span> In url_api directory, create virtual environment in which to install dependencies:

```sh
$ python3 -m venv .venv
```

<span style="color:salmon">4.</span> Activate virtual environment:

```sh
$ source .venv/bin/activate
```


<span style="color:salmon">5.</span> Install dependencies:

```sh
$ (.venv) pip install -r requirements.txt
```

* Please note the (.venv) in front of the prompt. This indicates that this terminal session operates in a virtual environment.

* If that command results in an error, try:

```sh
$ (.venv) pip install --upgrade -r requirements.txt
```

<span style="color:salmon">6.</span> Create PostgreSQL database:

```sh
$ (.venv) createdb url_service_db
```


<span style="color:salmon">7.</span> Set up environmental variable secret key for Django secret key:

* Create a django secret key using this generator: [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)

* Copy secret key created by Django Secret Key Generator.

* In the command line, create .env file and place secret key inside:

```sh
$ (.venv) touch .env

$ (.venv) echo SECRET_KEY = 'insert secret key obtained from generator' > .env
```

<span style="color:salmon">8.</span> Make migrations:

```sh
$ python manage.py makemigrations
```

* Alternately, if you have been using python3, use the following command to make migrations:

```sh
$ python3 manage.py makemigrations
```

<span style="color:salmon">9.</span> Run migrations:

```sh
$ python manage.py migrate
```

* Alternately, if you have been using python3, use the following command to run migrations:

```sh
$ python3 manage.py migrate
```


<span style="color:salmon">10.</span> Run the server:

```sh
$ (.venv) python manage.py runserver
```

<span style="color:salmon">11.</span> In your browser, visit the link to view the API endpoints:

[http://localhost:8000/](http://localhost:8000/)

<span style="color:salmon">12.</span> Verify that the /encode endpoint works as expected. 

* Click on the encode/endpoint or go to the following link: [http://localhost:8000/encode/](http://localhost:8000/encode/)

* Navigate to the bottom of the page where there is an input field labelled "Long url". Enter a URL of your choice to shortener or copy and paste in this sample URL: https://docs.djangoproject.com/en/4.0/topics/db/models/

* Press the "POST" button. You will be directed to the newly created object with an id, long_url, and short_url. 

<span style="color:salmon">13.</span> Verify that the /decode endpoint works as expected. 

* Navigate back to the API home by clicking on Api Root at the top left side of the page or by going to http://localhost:8000/. 

* Click on the decode endpoint or go to the following link: [http://localhost:8000/decode/](http://localhost:8000/decode/)

* Navigate to the bottom of the page where there is an input field labelled "Short url". Copy and paste the short url that you created in Step 12 in the input field.

* Press the "POST" button. You will be directed to the object that matches the short url that you entered along with its id and long url. 


## Thank you for taking the time to look at my solution.
___

## Author

* Portfolio - [Katarzyna Wegrzynowicz](https://katarzyna-kw.github.io/portfolio-website)
* Github - [@katarzyna-kw](https://github.com/katarzyna-kw)
* LinkedIn - [@katarzyna-kw](https://www.linkedin.com/in/katarzyna-kw/)
* Frontend Mentor - [@katarzyna-kw](https://www.frontendmentor.io/profile/katarzyna-kw)
* Individual Final Project for Code Platoon - [Saved For a Rainy Day](https://saved-for-a-rainy-day.web.app/)