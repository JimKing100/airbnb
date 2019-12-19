# Import Flask package

from decouple import config
from flask import Flask, render_template
from AIRBNB.models import DB

from joblib import load
import pandas as pd


def create_app():
    # Create Flask web server, makes the application
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    # Routes determine location
    @app.route("/")
    def home():

        month = 12
        year = 19
        property_type = 'House'
        room_type = 'Entire home/apt'
        neighbourhood = 'East Downtown'
        accommodates = 4
        bedrooms = 2
        bathrooms = 2
        beds = 2
        out_string = 'The predicted price for a ' + \
                     property_type.lower() + ' in the ' + \
                     neighbourhood + ' neighborhood '\
                     'accommodating ' + str(accommodates) + \
                     ' people in ' + str(bedrooms) + ' bedrooms ' + \
                     str(bathrooms) + ' baths is: '

        df = pd.DataFrame(
            columns=['month', 'year', 'property_type', 'room_type',
                     'neighbourhood', 'accommodates', 'bedrooms',
                     'bathrooms', 'beds'],
            data=[[month, year, property_type, room_type, neighbourhood,
                   accommodates, bedrooms, bathrooms, beds]]
        )

        pipeline = load('pipeline.joblib')
        y_pred_log = pipeline.predict(df)
        y_pred = y_pred_log[0]

        result = out_string + f'${y_pred:,.0f}'

        return render_template('home.html', title='Prediction', result=result)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('db.html', title='DB Reset')
    return app
