from flask import Blueprint,render_template,request,redirect,url_for,flash
from models.contact import Contact #modelo
from utils.db import db #conexcion a la base

contacts = Blueprint('contacts',__name__)

@contacts.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html',contacts=contacts)

@contacts.route('/new',methods=['POST'])
def new_contact():
   
   fullname = request.form['fullname']
   email = request.form['email']
   phone = request.form['phone']
   
   new_contact = Contact(fullname,email,phone)
   
   db.session.add(new_contact)
   db.session.commit()

   flash('Contacto agregado!!!')

   return redirect(url_for('contacts.index'))


@contacts.route('/update/<id>',methods= ['GET','POST'])
def update_contact(id):
    if request.method == 'POST':

        contact = Contact.query.get(id)
        
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']

        db.session.commit()

        flash('Contacto editado!!!')
        
        return redirect(url_for('contacts.index'))
    else:
        contact = Contact.query.get(id)
        return render_template('update.html',contact=contact)

@contacts.route('/delete/<id>')
def delete_contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    
    flash('Contacto eliminado!!!')

    return redirect(url_for('contacts.index')) #redireciona a la funcion index

@contacts.route('/about')
def about():
    return render_template('about.html')