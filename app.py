from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import Result

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        # get url that the user has entered
        try:
            weight = request.form['weight']
            height = request.form['height']
            print(weight + " " + height)
        except:
            errors.append(
                "Unable to get Weight & Height. Please make sure it's valid and try again."
            )
            return render_template('index.html', errors=errors)
        if weight and height:
            bmi = (weight / (height * height)) * 703
            print "BMI: " + bmi
            # save the results
            results = sorted(
                bmi,
            )
            try:
                result = Result(
                    height=height,
                    weight=weight,
                    bmi=bmi
                )
                db.session.add(result)
                db.session.commit()
            except:
                errors.append("Unable to add item to database.")
        return render_template('index.html', errors=errors, results=results)

if __name__ == '__main__':
    app.run()