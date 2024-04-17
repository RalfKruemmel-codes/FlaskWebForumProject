# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_wtf.file import FileField, FileAllowed 

class RegistrationForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Passwort', validators=[DataRequired(), Length(min=6, max=100)])
    confirm_password = PasswordField('Passwort bestätigen', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrieren')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Passwort', validators=[DataRequired()])
    remember = BooleanField('Angemeldet bleiben')  # Hinzufügen des 'remember' Feldes
    submit = SubmitField('Einloggen')

class UpdateAccountForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Aktualisieren')

class PostForm(FlaskForm):
    title = StringField('Titel', validators=[DataRequired()])
    content = TextAreaField('Inhalt', validators=[DataRequired()])
    image = FileField('Bild/GIF hochladen', validators=[FileAllowed(['jpg', 'png', 'gif'], 'Nur Bilder und GIFs!')])
    submit = SubmitField('Beitrag veröffentlichen')

class CommentForm(FlaskForm):
    content = TextAreaField('Kommentar', validators=[DataRequired()])
    submit = SubmitField('Kommentar absenden')

class CategoryForm(FlaskForm):
    name = StringField('Kategoriename', validators=[DataRequired()])
    description = TextAreaField('Beschreibung')
    submit = SubmitField('Kategorie erstellen')

class ForumForm(FlaskForm):
    name = StringField('Forumname', validators=[DataRequired()])
    description = TextAreaField('Beschreibung')
    submit = SubmitField('Forum erstellen')

class UpdateAccountForm(FlaskForm):
    Username = StringField('Benutzername', validators=[DataRequired(), Length(min=2, max=20)])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Aktualisieren')



