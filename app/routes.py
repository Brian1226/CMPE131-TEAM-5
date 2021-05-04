from flask import render_template, flash, redirect, url_for, request, Response
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required

from werkzeug.urls import url_parse

from app import myapp_obj
from app.forms import LoginForm, registerForm

from app.models import User, Note
from app import db
from datetime import datetime

@myapp_obj.route("/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None:
            flash('Username does not exist')
            return redirect('/')

        elif not user.check_password(form.password.data):
            flash('Incorrect password')
            return redirect('/')

        else:
            login_user(user)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('view_note')
            return redirect(next_page)

    return render_template('login.html', title='Log In', form=form)



@myapp_obj.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



@myapp_obj.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        email = User.query.filter_by(email = form.email.data).first()

        if user:
            flash('Username is already taken')
            return redirect(url_for('register'))

        elif email:
            flash('Email is already taken')
            return redirect(url_for('register'))

        else:
            user = User(username = form.username.data, email = form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Successfully registered')
            return redirect(url_for('login'))

    return render_template('registerpage.html', title='Register', form=form)

#Incomplete create note function
'''
@myapp_obj.route('/create', methods=['POST'])
@login_required
def create_note():
    user = User.query.filter_by(username=username).first()
    note = Note(
        userID=current_user.id, time=timestamp.datetime
    )
    db.create_all
    db.session.add(note)
    db.session.commit()
    return render_template('note.html', title='Notes')
'''
@myapp_obj.route('/notes', methods=['GET', 'POST'])
@login_required
def view_note():
    user = current_user
    notes = user.notes.all()
    final = []
    for n in notes:
        information = []
        information.append(n.body)
        information.append(n.timestamp)
        final.append(information)
    return render_template('note.html', title='Notes', usernotes=final)


@myapp_obj.route('/delete', methods=['POST'])
@login_required
def delete_note(id):
    print(id)
    delNote = Note.query.filter_by(id=id).first()
    db.create_all
    db.session.delete(delNote)
    db.session.commit()

@myapp_obj.route('/task', methods=['GET', 'POST'])
@login_required
def task():
    return render_template('task.html', title='Tasks')
