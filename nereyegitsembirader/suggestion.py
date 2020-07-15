from flask import Blueprint, render_template, redirect, url_for,request, flash
from flask_login import login_required, current_user
from . import db
from .models import Travel

suggestion = Blueprint('suggestion', __name__)


@suggestion.route('/suggest')
def suggest():
    suggestions = Travel.query.all()
    return render_template('suggestion.html',suggestions=suggestions)

@suggestion.route('/suggest/create')
@login_required
def suggest_create():
    return render_template('suggestion_create.html')

@suggestion.route('/suggest/create', methods=['POST'])
@login_required
def suggest_create_post():
    name = request.form.get('name')

    travel = Travel.query.filter_by(
        name=name).first()

    if travel:
        flash('This travel address already exists')
        return redirect(url_for('suggestion.suggest_create'))

    new_travel = Travel(name=name)

    db.session.add(new_travel)
    db.session.commit()

    return redirect(url_for('suggestion.suggest'))


#@main.route('/profile')
#@login_required
#def profile():
#    return render_template('profile.html', name=current_user.name)
