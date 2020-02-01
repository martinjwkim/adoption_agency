from flask import Flask, request, redirect, render_template, flash
from modules import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "sekrit key"

connect_db(app)
db.create_all()

@app.route('/')
def root():
    pets = Pet.query.all()

    return render_template('pets_list.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet_form():
    """"Add pet form; handle adding pet"""

    form = AddPetForm()

    if form.validate_on_submit():
        image_url = form.image_url.data 
        if image_url == '':
            image_url = None
        new_pet_added = Pet(name=form.name.data, species=form.species.data, 
                            image_url=image_url, age=form.age.data, notes=form.notes.data)
        db.session.add(new_pet_added)
        db.session.commit()
        flash(f"Added {form.name.data} to pets list.")
        return redirect('/')
    else:
        return render_template('pets_form.html', form=form)

@app.route("/pet/<pet_id>")
def pet_details(pet_id):

    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet=pet)


@app.route("/pet/<pet_id>/edit", methods=['GET','POST'])
def pet_edit(pet_id):

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    print(f'(******************(*(*I))()(*(*(*)*(*({form.data}')

    if form.validate_on_submit():
        [pet.name, pet.age, pet.species, pet.image_url, pet.available] = [form.name.data, form.age.data, 
                                                                          form.species.data, form.image_url.data, 
                                                                          form.available.data]
  
        db.session.commit()
        flash(f"Edited {pet.name}!")
        return redirect(f'/pet/{pet_id}')
    else:
        return render_template('pet_edit.html', pet=pet, form=form)