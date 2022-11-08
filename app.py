# from ast import Return
# from crypt import methods
from turtle import update
from flask import Flask, flash, redirect, render_template, request, session, url_for, request, jsonify, make_response
from flask_session import Session
from tempfile import mkdtemp
from sqlalchemy import delete
# https://blog.carsonevans.ca/2020/08/02/storing-passwords-in-flask/
from werkzeug.security import check_password_hash, generate_password_hash
from login_required import login_required
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# https://www.youtube.com/watch?v=vzaXBm-ZVOQ&ab_channel=PrettyPrinted
# https://www.digitalocean.com/community/tutorials/how-to-use-and-validate-web-forms-with-flask-wtf
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField,  PasswordField, EmailField, IntegerField
import re
from wtforms.validators import InputRequired, Length, EqualTo, Email, Regexp

from flask_migrate import Migrate
import decimal 

# pip3 install flask-session we need to run this command before beeing able to run the sesion

# Configure application
app = Flask(__name__)
#  starting db
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#installation
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_inventory.db'
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#  my secret key
app.config['SECRET_KEY'] = "jose"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lc4vxAiAAAAANg9quRNQepa48Fis7ajojz_ti_X'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Lc4vxAiAAAAAP7Wu_Bqk4mKM9g-IDKQKde9f-Fv'




# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# class RegistrationForm(FlaskForm):
#     username = StringField('Username', [validators.Length(min=4, max=25)])

max_character_userame = 20
max_character_email = 100
max_character_password = 50
max_character_name = 50


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(
        "Please Enter Username"), Regexp('^\w+$', message="Username must contain only letters numbers or underscore"), Length(max=max_character_userame)])
    # https://stackoverflow.com/questions/25324113/email-validation-from-wtform-using-flask
    # email validation
    email = EmailField('email', validators=[
        InputRequired(),
        Length(max=max_character_email), Email("This field requires a valid email address")])
    password = PasswordField('password', validators=[
                             InputRequired()])
    confirm = PasswordField('confirm', validators=[EqualTo(
        'password', message='Passwords must match')])
    recaptcha = RecaptchaField()


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(max_character_userame),
                         unique=True, nullable=False)
    email = db.Column(db.String(max_character_email),
                      unique=True, nullable=False)
    # this limit shouldnt be placed
    password = db.Column(db.String(max_character_password), nullable=False)
    inventory = db.relationship('Inventory', backref='userid_inventory')
    inventory_name = db.relationship(
        'InventoryName', backref='user_id_inventory_name')

    def __repr__(self):
        return '<User %r>' % self.username

# https://www.youtube.com/watch?v=yDuuYAPCeoU&ab_channel=PrettyPrinted
# use faker to generate data automatically
# p InventoryName.inventory


class InventoryName(db.Model):
    name_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(max_character_name),   nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))
    inventory = db.relationship('Inventory', backref='name_inventory_name')

    def __repr__(self):
        return '<Name %r>' % self.name


class Inventory(db.Model):
    inventory_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(max_character_name),
                     db.ForeignKey(InventoryName.name))
    sku = db.Column(db.String())
    title = db.Column(db.String())
    quantity = db.Column(db.Integer)
    # Numeric(9,2 ) allows numbers up to and including 9 999 999.99
    price = db.Column(db.Numeric(9, 2))
    location = db.Column(db.String())
    entry_date = db.Column(db.DateTime, default=datetime.utcnow)
    modify_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey(User.user_id))

    def __repr__(self):
        return '<Name %r>' % self.title


class InventoryForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(
        "Please Enter an Inventory Name"),  Length(max=max_character_name)])
    sku = StringField('SKU', validators=[InputRequired(
        "Please Enter sku")])
    title = StringField('TITLE', validators=[InputRequired(
        "Please Enter title")])
    location = StringField('LOCATION', validators=[InputRequired(
        "Please Enter location")])
    price = StringField('PRICE', validators=[InputRequired(
        "Please Enter location"), Regexp("^\d*(\.\d{0,2})?$", message="Price Must be a valid Numeric Value 00.99")])
    quantity = IntegerField('QUANTITY', validators=[InputRequired(
        "Please Enter quantity"), Length(max=9223372036854775807)])


@app.route('/')
@login_required
def index():

    # when user login user should something that says my inventory, where user should be able to click and acces their inventory
    # user shoould be able to CRUD
    # dowload spreadsheet
    #  user should be able to search on the inventory
    #  user should see the name of their item and when click should be able to have everything display about that item on another page
    # input item will be in green if quanity is over 100 if less will be in yellow, if 0 they will be in red

    # when click on create db open modal with input to create db
    # when click send go to another route on post and fill the form to enter information for that

    # route

    # inventory
    # display all inventory
    # inventory/name of the inventory
    #  when user click an inventory they should have that particular inventory display
    # inventory/history
    #  user should see the hitory of all inventory
    # inventory/history/name of the inventory/
    # user should see a list of particul;ar inventory

    id = session["user_id"]
    select = User.query.filter_by
    user = select(user_id=id).first()
    print(type(user))
    print(user)
    names = InventoryName.query.filter_by(user_id=id).all()
    print(names)
    # return render_template('login.html')
    return render_template('index.html', username=user.username, names=names)

# https://pythonbasics.org/flask-http-methods/


@app.route('/register', methods=['POST', 'GET'])
def register():

    form = RegistrationForm()

    if request.method == "GET":
        print('get')
        return render_template('register.html', form=form)

    elif request.method == 'POST' and form.validate():
        print(form.username.data, type(form.username.data), form.email.data,
              form.password.data)
        # print(User.query.all)
        select = User.query.filter_by
        # print(generate_password_hash(form.password.data))
        user_name = form.username.data.lower()
        if select(username=user_name).count() != 0:
            flash("Username already exits")
            return render_template('register.html', form=form)
        elif select(email=form.email.data).count() != 0:
            flash("Email already exits")
            return render_template('register.html', form=form)

        me = User(
            username=user_name,
            password=generate_password_hash(form.password.data),
            email=form.email.data
        )

        # test = User.query.all()
        # for t in test:
        #     print(t)
        db.session.add(me)
        db.session.commit()
        print(me.user_id, "-----", me, "me.user_id,")
        session["user_id"] = me.user_id
        print("Validate")
        return redirect(url_for('index'))

    print("Something Went Wrong")
    flash("Something Went Wrong")
    return render_template('register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():

    # for testing only a
    # Forget any user_id
    session.clear()

    form = RegistrationForm()

    if request.method == "GET":
        print('get')
        return render_template('login.html', form=form)

    if request.method == 'POST':
        print(form.username.data)
        print(form.password.data)
        # select = User.query.filter_by
        # determine username and password
        # print(select(username=form.username.data))
        # User.query.filter_by(email='a@a.com').first().password

        user = User.query.filter_by(
            username=form.username.data).first()
        email = User.query.filter_by(
            email=form.username.data).first()

        # print(user, "user")
        # print(type(user))
        # print(email.password, "email")
        # print(user.password, "password")
# or email and check_password_hash(email.password, form.password.data)
        if user and check_password_hash(user.password, form.password.data):
            print("valid user")
            session["user_id"] = user.user_id
            return redirect(url_for('index'))

        elif email and check_password_hash(email.password, form.password.data):
            print("valid user")
            session["user_id"] = email.user_id
            return redirect(url_for('index'))

        # form.username.data = ""
        # form.email.data = form.email.data
        flash('username or password does not match')
        return render_template('login.html', form=form)

    return render_template('login.html', form=form)


@app.route('/api/inventory/<name>/<id>',  methods=['POST', 'GET', 'DELETE'])
@login_required
def api_inventory_name_id(name, id):
    # route declaration
    api_inventory_name_id = "api-inventory-name-id.html"
    form = InventoryForm()
    select = Inventory.query.filter_by
    user_id = session["user_id"]
    data = select(name=name, inventory_id=id, user_id=user_id).first()

    print(api_inventory_name_id)

    if request.method == 'GET':

        print('GET',)
        print("name")
        print(name)
        print("id")
        print(id)

        # req = request.get_json()
        # print(req)
        # print("req")

        # print(data)
        # print(data.sku)
        # print("data.sku")
        form.sku.data = data.sku
        form.title.data = data.title
        form.quantity.data = data.quantity
        form.price.data = data.price
        form.location.data = data.location

        # res = make_response(jsonify(req),200)
        # print("res")
        # print(res)
        # print("POST")

        return render_template(api_inventory_name_id,  name=name, id=id, form=form)
    if request.method == 'POST':
        print("POST")

        if form.quantity.data > 9223372036854775807:
            msg = "Quantity que cannot be bigger than 92,233,72,036,854,775,807"
            flash(msg)
            print(msg)
            data = select(name=name, inventory_id=id, user_id=user_id).first()
            return render_template(api_inventory_name_id,  name=name, form=form, id=id, data=data)

        sku = form.sku.data
        title = form.title.data
        location = form.location.data
        quantity = form.quantity.data
        price = form.price.data
        print(sku, title, location, quantity, price)

        if sku == "" or title == "" or location == "" or quantity == "" or price == "":
            print("Something is empty")
            flash("All Fields are required")
            return render_template(api_inventory_name_id, id=id, name=name, form=form, data=data)
        elif quantity == None:
            print("Quantity is not an Integer")
            flash("Quantity is not an Integer")
            return render_template(api_inventory_name_id,  id=id, name=name, form=form, data=data)
        elif not bool(re.search("^\d+(?:\.\d{1,2})?$", price)):
            msg = "Price must be either integer or decimal with two value after '.' ie: .00"
            print(msg)
            flash(msg)
            return render_template(api_inventory_name_id, id=id, name=name, form=form, data=data)

        SKUValidation = select(user_id=user_id, name=name, sku=sku).count()

        # if SKW Exist in he same ID is fine

        if SKUValidation != 0:
            #  this check to determine wether the SKU is the same that is in the invenotory
            SKUCheck = select(user_id=user_id, name=name,
                              sku=sku, inventory_id=id).first()
            # print(SKUCheck.sku,"SKUCheck")
            print("SKUCheck", SKUCheck)

            if SKUCheck == None:
                print("empty")
                print(msg)
                flash(msg)
                return render_template(api_inventory_name_id, id=id,  name=name, form=form, data=data)
            elif SKUCheck.sku == sku:
                # this means that SKU is the same which we are modifyin so we dont return anything
                print("fine")

            else:

                print(msg)
                flash(msg)
                return render_template(api_inventory_name_id, id=id,  name=name, form=form, data=data)

        #  here left do the patch
        update = select(name=name, inventory_id=id, user_id=user_id).first()

        print(update.title)
        update.sku = sku
        update.title = title
        update.location = location
        update.quantity = quantity
        update.price = price

        # sku = form.sku.data
        # title = form.title.data
        # location = form.location.data
        # quantity = form.quantity.data
        # price = form.price.data

        # add = Inventory(
        #     sku=sku,
        #     title=title,
        #     location=location,
        #     quantity=quantity,
        #     price=price
        # )

        # # test = User.query.all()
        # # for t in test:
        # #     print(t)
        # db.session.add(add)
        db.session.commit()
        # select(name=name, inventory_id=id, user_id=user_id).first()
        print("end")
        flash("Congratulations you have Sucessfully update your inventory")
        data = select(user_id=user_id, name=name).all()
        return render_template("api-inventory.html",  name=name, form=form, data=data)
        # return render_template(api_inventory_name_id,  name=name, id=id, form=form)

    # if request.method == 'DELETE':
    #     # https://www.youtube.com/watch?v=KMvh8MS1ASQ&ab_channel=Codemy.com
    #     print("DELETE")
    #     req = request.get_json()
    #     print(req)
    #     print("req")
    #     print(req['inventoryName'])
    #     res = make_response(jsonify(req), 200)

    #     print("res")
    #     print(res)
    #     print("POST")

    #     delete = select(
    #         user_id=user_id, name=req['inventoryName'], inventory_id=req['inventoryId']).first()

    #     db.session.delete(delete)
    #     db.session.commit()
    #     print("file delete it, you should be redicrected to apiinventory ")
    #     data = select(user_id=user_id, name=name).all()
    #     # the error is hapening in the javscript, you are ni the wrong file
    #     return redirect(url_for('apiinventory', name=name))
        # return render_template("inventory.html",  name=name, data=data)
        # return render_template("api-inventory.html",  name=name, form=form, data=data)
        # return render_template(api_inventory_name_id,  name=name, id=id, form=form)

        # return render_template("api-inventory.html",  name=name, form=form, data=data)
        # render_template("api-inventory.html",  name=name, form=form, data=data)

    print("ELSE")
    return render_template(api_inventory_name_id,  name=name, id=id, form=form)


@app.route('/api/inventory/<name>', methods=['POST', 'GET', 'DELETE'])
@login_required
def apiinventory(name):
    form = InventoryForm()
    select = Inventory.query.filter_by
    user_id = session["user_id"]
    data = select(user_id=user_id, name=name).all()
    if request.method == 'GET':
        # data = select(user_id=user_id, name=name).all()
        print("/api/inventory")
        print("GET")
        # select = Inventory.query.filter_by
        # user_id = session["user_id"]
        # data = select(name = name, user_id = user_id ).all()
        return render_template("api-inventory.html",  name=name, form=form, data=data)
    # POST
    if request.method == 'POST':
        print("/api/inventory")
        print("POST")
        # req = request.get_json()
        # print(req)
        # print("req")

        # res = make_response(jsonify(req),200)
        # print("res")
        # print(res)
        #  ^\d+(?:\.\d{1,2})?$
        print(form.quantity.data > 9223372036854775807)
        print(form.quantity.data, " QUANTITY")
        print(type(form.quantity.data), " type")
        if form.quantity.data > 9223372036854775807:
            msg = "Quantity que cannot be bigger than 92,233,72,036,854,775,807"
            flash(msg)
            flash("WAY")
            print(msg)
            data = select(name=name,  user_id=user_id).all()
            # return redirect(url_for("index"))
            return render_template("api-inventory.html",  name=name, form=form, data=data)

        sku = form.sku.data
        title = form.title.data
        location = form.location.data
        quantity = form.quantity.data
        price = form.price.data
        print(sku, title, location, quantity, price)
        print("sku", "title", "location", "quantity", "price")
        print(quantity, "quantity", type(quantity))
        # print(price, "price", type(price), float(price))
        print(not bool(re.search("^\d+(?:\.\d{1,2})?$", price)))

        # if not bool(re.search("^\d+(?:\.\d{1,2})?$", price)):
        #     flash("Inventory name must contain only letters, numbers or underscore")
        #     print("Only Letters, numbers or underscore")
        #     return render_template("index.html")

        if sku == "" or title == "" or location == "" or quantity == "" or price == "":
            print("Something is empty")
            flash("All Fields are required")
            return render_template("api-inventory.html",  name=name, form=form, data=data)
        elif quantity == None:
            print("Quantity is not an Integer")
            flash("Quantity is not an Integer")
            return render_template("api-inventory.html",  name=name, form=form, data=data)
        elif not bool(re.search("^\d+(?:\.\d{1,2})?$", price)):
            msg = "Price must be either integer or decimal with two value after '.' ie: .00"
            print(msg)
            flash(msg)
            return render_template("api-inventory.html",  name=name, form=form, data=data)

        SKUValidation = select(user_id=user_id, name=name, sku=sku).count()

        if SKUValidation != 0:
            msg = "Sku already exist in this inventory, try using another one"
            print(msg)
            flash(msg)
            return render_template("api-inventory.html",  name=name, form=form, data=data)

        add = Inventory(
            name=name,
            user_id=user_id,
            sku=sku,
            title=title,
            location=location,
            quantity=quantity,
            price=price
        )

        # test = User.query.all()
        # for t in test:
        #     print(t)
        db.session.add(add)
        db.session.commit()
        form.sku.data = ""
        form.title.data = ""
        form.location.data = ""
        form.quantity.data = ""
        form.price.data = ""
        data = select(user_id=user_id, name=name).all()
        return render_template("api-inventory.html",  name=name, form=form, data=data)

    if request.method == 'DELETE':
        # https://www.youtube.com/watch?v=KMvh8MS1ASQ&ab_channel=Codemy.com
        print("DELETE")
        req = request.get_json()
        print(req)
        print("req")
        print(req['inventoryName'])
        print(req['inventoryId'])
        res = make_response(jsonify(req), 200)

        print("res")
        print(res)

        delete = select(
            user_id=user_id, name=req['inventoryName'], inventory_id=req['inventoryId']).first()
        # delete = select(
        #     user_id=user_id, name=req['inventoryName'], inventory_id=req['inventoryId']).first()
        print(delete.name)
        print(delete.user_id)
        print(delete.inventory_id)

        print("DELETE")
        db.session.delete(delete)
        db.session.commit()
        print("commit")
        print("file delete it, you should be redicrected to apiinventory ")
        data = select(user_id=user_id, name=name).all()
        # the error is hapening in the javscript, you are ni the wrong file
        return render_template("api-inventory.html",  name=name, form=form, data=data)

    # else
    print("ELSE")
    flash("Something went wrong")

    return render_template("api-inventory.html",  name=name, form=form, data=data)


@app.route('/inventory', methods=['POST'])
@login_required
def inventory():

    # if request.method == 'GET':

    #     return "Welcome to the inventory"

    print("POST")
    name = request.form.get('inventoryname')
    user_id = session["user_id"]
    print(user_id)
    count = InventoryName.query.filter_by(name=name, user_id=user_id).count()
    # user input validation
    if name == "":
        flash("Inventory name is empty")
        print("empty Value")
        return redirect(url_for("index"))
        # https://stackoverflow.com/questions/6576962/python-regular-expressions-return-true-false
        # match = re.search(pattern, string)
    elif not bool(re.search('^\w+$', name)):
        flash("Inventory name must contain only letters, numbers or underscore")
        print("Only Letters, numbers or underscore")
        return redirect(url_for("index"))
    elif count != 0:
        flash("Inventory name already exists")
        print("already exists")
        return redirect(url_for("index"))

    # add name ot inventory
    addName = InventoryName(name=name, user_id=user_id)
    db.session.add(addName)
    db.session.commit()

    data = Inventory.query.filter_by(user_id=user_id, name=name).all()
    # Inventory name is valid

    # # select = InventoryName.query.filter_by

    # if select(username=name).count() != 0:

    print("name", name)
    return redirect(url_for('apiinventory', name=name))
    # return render_template("inventory.html",  name=name, data=data)


@app.route('/inventory/update',  methods=['GET', 'POST'])
@login_required
def inventory_update():

    if request.method == 'GET':
        print("GET")

        return redirect(url_for("index"))
    if request.method == 'POST':
        # name = request.form.get('inventoryname')
        req = request.get_json()
        # print(req)
        # print("req")

        # res = make_response(jsonify(req),200)
        user_id = session["user_id"]
        print(req)

        name_id = req['name_id']
        inventoryName = req['inventoryName']
        # InventoryName.query.filter_by(user_id=id).all()
        # delete_inventoryName = InventoryName.query.filter_by(user_id=user_id, name=inventoryName).first()

        # delete_inventory = Inventory.query.filter_by(user_id=user_id, name=inventoryName).all().
        # db.session.delete(delete_inventoryName)
        # db.session.commit()
        # db.session.delete(delete_inventory )

        InventoryName.query.filter_by(
            user_id=user_id, name=inventoryName).delete()

        Inventory.query.filter_by(user_id=user_id, name=inventoryName).delete()
        db.session.commit()
# http://127.0.0.1:5000/api/inventory/anotherrr
        print("req")

        return redirect(url_for("index"))
        # select(name=name, inventory_id=id, user_id=user_id).first()

    return redirect(url_for("index"))


@app.route('/logout')
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


# https://flask.palletsprojects.com/en/2.2.x/debugging/
if __name__ == '__main__':
    app.run(debug=True)

# ``````````````````````````````````````````````


# END OF THE APP

# template you will
# login page, this page should be required on every page, in case the customer doesn't login they shoulkd be redirected automcatically to the login page

# inventory page, should be display on tablet allooeing use to make modification


# RESOURCES USED
# https://www.youtube.com/watch?v=Q2QmST-cSwc
# https://www.digitalocean.com/community/tutorials how-to-query-tables-and-paginate-data-in-flask-sqlalchemy
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/


# https://www.geeksforgeeks.org/how-to-count-rows-with-select-count-with-sqlalchemy/

# is not None, undertanding how that works
# https://stackoverflow.com/questions/2710940/python-if-x-is-not-none-or-if-not-x-is-none

# Intro to Flask-SQLAlchemy Queries
# https://www.youtube.com/watch?v=JKoxrqis0Co

# Flask HTTP methods, handle GET & POST requests
# https://pythonbasics.org/flask-http-methods/

# Configuration
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

# Storing Passwords In Flask
# https://blog.carsonevans.ca/2020/08/02/storing-passwords-in-flask/

# app.run(debug=True)
# https://flask.palletsprojects.com/en/2.2.x/debugging/

# flask migration
# This is when the database migration comes in handy, as it keeps a track of database schema changes for you, and one can easily traverse back to an older or newer version of the database.
# https://www.youtube.com/watch?v=ca-Vj6kwK7M&ab_channel=Codemy.com
