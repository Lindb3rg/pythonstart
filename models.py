# from flask_sqlalchemy import SQLAlchemy
# from flask_security import hash_password
# from flask_security import Security, SQLAlchemyUserDatastore, hash_password
# from flask_security.models import fsqla_v3 as fsqla



# db = SQLAlchemy()

# fsqla.FsModels.set_db_info(db)

# class Role(db.Model, fsqla.FsRoleMixin):
#     pass

# class User(db.Model, fsqla.FsUserMixin):
#     pass




import json
import requests
from flask import request,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, Security,SQLAlchemyUserDatastore
from datetime import datetime
from faker import Faker

db = SQLAlchemy()




class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

    # User authentication information. The collation='NOCASE' is required
    # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime()) 

    password = db.Column(db.String(255), nullable=False, server_default='')

    # User information
    first_name = db.Column(db.String(100), nullable=False, server_default='')
    last_name = db.Column(db.String(100), nullable=False, server_default='')

    # Define the relationship to Role via UserRoles
    roles = db.relationship('Role', secondary='user_roles')

# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
# user_manager = UserManager(None, db, User) 


    
class Product(db.Model):
    __tablename__= "Products"
    ProductID = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(100), unique=False, nullable=False)
    Color = db.Column(db.String(40), unique=False, nullable=False)
    Created = db.Column(db.DateTime, unique=False, nullable=False)
    LastBought = db.Column(db.DateTime, unique=False, nullable=True)
    ImageUrl = db.Column(db.String(100), unique=False, nullable=False)
    Rating = db.Column(db.Float, unique=False, nullable=False)
    RatingCount = db.Column(db.Integer, unique=False, nullable=False)
    CategoryName = db.Column(db.String(40), unique=False, nullable=False)
    Price = db.Column(db.Integer, unique=False, nullable=False)

class Messages(db.Model):
    __tablename__= "Messages"
    MessageID = db.Column(db.Integer, primary_key=True)
    Namn = db.Column(db.String(100), unique=False, nullable=False)
    Epost = db.Column(db.String(100), unique=False, nullable=False)
    Telefon = db.Column(db.String(100), unique=False, nullable=False)
    Rubrik = db.Column(db.String(100), unique=False, nullable=False)
    Text = db.Column(db.String(100), unique=False, nullable=False)



# class Contact_form(FlaskForm):
#     namn = StringField("namn", validators=[validators.DataRequired(), validators.length(max=20)])
#     epost = EmailField("epost",validators=[validators.Email()])
#     telefon = TelField("telefon")
#     rubrik = SelectField("rubrik", choices=["Support", "Försäljning", "Samarbeten", "Övrigt"])
#     text = TextAreaField(validators=[validators.length(max=512)])





def seedData():
    # jkdasjkdajkdas
    antal =  Product.query.count()


    if antal < 1:
        url = requests.get("https://fakestoreapi.com/products")
        text = url.text
        data = json.loads(text)
        
        fake = Faker()
        for prod in data:
            dat1 = fake.past_date("-365d")
            dat2 = fake.past_date("-365d")
            if dat1 > dat2:
                d = dat1
                dat1 = dat2
                dat2 = d
            product = Product()
            product.ProductName = prod['title']
            product.Color = fake.color_name()
            product.ImageUrl = prod['image']
            product.Price = prod['price']
            product.Created = dat1
            product.LastBought = dat2
            product.CategoryName = prod['category']
            product.Rating = prod['rating']['rate']
            product.RatingCount =prod['rating']['count']

            db.session.add(product)
        db.session.commit()        


    

