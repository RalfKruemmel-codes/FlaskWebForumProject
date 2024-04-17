from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    UserID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='commenter', lazy='dynamic')
    
    def get_id(self):
        return str(self.UserID)

class Post(db.Model):
    __tablename__ = 'posts'
    PostID = db.Column(db.Integer, primary_key=True)  # Anpassung an den tatsächlichen Spaltennamen
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), nullable=False)
    CategoryID = db.Column(db.Integer, db.ForeignKey('categories.CategoryID'), nullable=False)
    Title = db.Column(db.String(255), nullable=False)
    Content = db.Column(db.Text, nullable=False)
    PostDate = db.Column(db.DateTime, server_default=db.func.now())
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

class Comment(db.Model):
    __tablename__ = 'comments'
    CommentID = db.Column(db.Integer, primary_key=True)  # Anpassung an den tatsächlichen Spaltennamen
    PostID = db.Column(db.Integer, db.ForeignKey('posts.PostID'), nullable=False)
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), nullable=False)
    Content = db.Column(db.Text, nullable=False)
    CommentDate = db.Column(db.DateTime, server_default=db.func.now())

class Category(db.Model):
    __tablename__ = 'categories'
    CategoryID = db.Column(db.Integer, primary_key=True)  # Anpassung an den tatsächlichen Spaltennamen
    ForumID = db.Column(db.Integer, db.ForeignKey('forums.ForumID'), nullable=False)
    Name = db.Column(db.String(255), nullable=False)
    Description = db.Column(db.Text)
    posts = db.relationship('Post', backref='category', lazy='dynamic')

class Forum(db.Model):
    __tablename__ = 'forums'
    ForumID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Description = db.Column(db.Text)
    categories = db.relationship('Category', backref='forum', lazy='dynamic')
