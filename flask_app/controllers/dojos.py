from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

#showall------------------------------------
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos = dojos)

#newdojo------------------------------------
@app.route('/dojos/new')
def new_user():
    return render_template("new_ninja.html")

#newdojo------------------------------------
@app.route('/dojos/new', methods=["POST"])
def create_new_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

#show------------------------------------
@app.route('/dojo/<int:id>')
def show(id):
    data = {
        "id":id
        }
    return render_template("show.html", dojo = Dojo.get_one(data))


