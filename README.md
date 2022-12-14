# Inventory App
#### Video Demo:  <URL https://www.youtube.com/watch?v=7s42jXKgs7Y>
#### Description: Inventory App using JavaScript, Python, Flask and SQLite.

## App Explanation
This program is primarily made to help users keep track of the locations of various items, such as books, paper, and other items.People will have to log in to build, update, and delete their own data bases. 

The database will allow users to create their own lists of items that they have in their homes or offices. For example, if someone has a lot of books, they can create a list and use it to keep track of the different books they own. This program is great for people who are trying to organize their homes and offices.

 People can also use this database to keep track of their sports equipment, toys, and other items.

The program is great for people who have a lot of stuff and don’t know where to put it all.


## templates folder
Our HTML files are contained in this folder, so every time that one od the user visit a particular route they will render the template that is based on that route. 

We are going to use flask_render in order to make sure that when a user visits a particular route, the right template is rendered. The main reason why we are going to use flask_render is because it allows us to render templates based on the route. We will also use Jinja2 as our template engine.

 Jinja2 is a great template engine for Python and it is much easier to use than other templating engines like Mako, which Flask uses by default.
## static folder
this section houses static files like CSS and Javascript.

These files are not compiled, so they don’t need to be processed by Webpack.
## app.py
app.py is our primary application where you can find all of the route and backend logic. 

app.py is our primary application where you can find all of the route and backend logic. This file also includes a number of functions used by other files such as app_config() for configuring settings like database connection strings and secret keys, and app_run() for running commands on the server. 

The main application, which uses a number of other modules to run, including:

- routes

- connections to databases

- flask-login for user authentication and session management.

 One of the most important things to notice about app.py is that it doesn’t include any logic for running commands on the server or interacting with our database. This is because Flask-SQLAlchemy handles all of that for us and provides a layer of abstraction between our application and its database.

#   I n v e n t o r y - A p p  
 