from flask import render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app import app
from models import *
from forms import *


@app.route('/index')
def indexolann():
    return render_template('index.html')

@app.route('/qeydiyyat', methods = ['GET', 'POST'])
def qeydiyyat():
    form = QeydiyyatFormu()
    if request.method == 'POST':
        butun = request.form
        form = QeydiyyatFormu(data = butun)
        if form.validate_on_submit():
            yeni = User(name = form.name.data, last_name=form.last_name.data, username=form.username.data, email=form.email.data, phone=form.phone.data, password=form.password.data)
            yeni.save()
            return redirect('/login')
    return render_template('qeydiyyat.html', form=form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    form = GirisFormu()
    if request.method == 'POST':
        if request.form['username'] != 'username' or request.form['password'] != 'password':
            error = 'Yalnış istifadəçi adı vəya şifrə.'
        else:
            return render_template('login.html')
        butun = request.form
        form = GirisFormu(data = butun)
        if form.validate_on_submit():
            istifadeci = User.query.filter_by(username = form.username.data).first()
            if check_password_hash(istifadeci.password, form.password.data):
                login_user(istifadeci)
                print('User girdi')
                return redirect('/profil')
            else:
                print('User girmedi')
    return render_template('login.html', form = form,  error=error)


@app.route('/profil')
def profilimm():
    return render_template('profil.html')


@app.route('/cixis')
@login_required
def cixis():
    logout_user()
    return redirect('/login')




@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    all_data = request.form
    print(all_data)
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data = all_data)
        print(form.validate_on_submit())
        if form.validate_on_submit():
            contactinfo = ContactUs(full_name = form.full_name.data, email = form.email.data, phone = form.phone.data, comment = form.comment.data)
            contactinfo.save()
    return render_template('contact.html', form = form)