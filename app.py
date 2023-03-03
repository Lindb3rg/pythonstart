from flask import Flask
from models import db, seedData,Product
from flask_migrate import Migrate, upgrade
from flask import  render_template,redirect
from forms import Contact_form
from models import Messages

app = Flask(__name__)
app.config.from_object('config.ConfigDebug')

db.app = app
db.init_app(app)
migrate = Migrate(app,db)


@app.route("/", methods=["GET"])
def startSida():
    return render_template('startsida.html')


@app.route("/products")
def products():
    products = Product.query.all()

    return render_template('products.html',products=products)


@app.route("/confirmation") 
def contact_confirmation():
    return render_template('contact_confirmation.html')


@app.route("/contact_page", methods=["GET","POST"])
def contact_us():
    form = Contact_form()
    if form.validate_on_submit():
        new_message = Messages()
        new_message.Namn = form.namn.data
        new_message.Epost = form.epost.data
        new_message.Telefon = form.telefon.data
        new_message.Rubrik = form.rubrik.data
        new_message.Text = form.text.data
        db.session.add(new_message)
        db.session.commit()
        return redirect("/confirmation")

    return render_template('contact_us.html',form=form)



if __name__  == "__main__":
    with app.app_context():
        upgrade()
        seedData()
        
    app.run()


