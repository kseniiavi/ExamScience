from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'

db = SQLAlchemy(app)

# define the Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    # 50 how many characters allowed to enter
    author = db.Column(db.String(50), nullable=False)
    publication_year = db.Column(db.Integer, nullable=False)

def addcontext():
    with app.app_context():
        db.create_all()
#def create_db():
 #   with app.app_context():
  #      db.create_all()

# create the routes
@app.route('/books')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add_book', methods={'GET', 'POST'})
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        publication_year = request.form['publication_year']

        new_book = User(title=title, author=author,
                        publication_year=publication_year)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_book.html', title='Add Book')

if __name__ == '__main__':
    addcontext()
   # create_db()
    app.run(port=5001, debug=True)