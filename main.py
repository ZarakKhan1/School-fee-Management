from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sab.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Sab(db.Model):
    roll = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True,)
    fee = db.Column(db.String(120), unique=True,)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        fee = request.form['fee']
        fee = Sab(title=title, desc=desc, fee=fee)
        db.session.add(fee)
        db.session.commit()

    allfee = Sab.query.all()
    return render_template('index.html', allfee=allfee)

if __name__ == "__main__":
    app.run(debug=True)