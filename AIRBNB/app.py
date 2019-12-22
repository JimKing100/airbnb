# Import Flask package

from decouple import config
from flask import Flask, request, jsonify, render_template
from AIRBNB.models import DB
from AIRBNB.explain import explains

import category_encoders as ce
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression

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

        train = pd.read_csv('https://raw.githubusercontent.com/JimKing100/airbnb-app-4/master/Datascience/data/train.csv')
        train = train.drop(columns=['old_index'])
        target = 'price'

        features = train.columns.drop(target)
        X_train = train[features]
        y_train = train[target]

        pipeline = make_pipeline(
            ce.OrdinalEncoder(),
            LinearRegression()
        )

        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(df)
        y_pred = y_pred[0]

        transformers = make_pipeline(
            ce.OrdinalEncoder(),
            SimpleImputer(strategy='mean')
        )

        X_train_transformed = transformers.fit_transform(X_train)

        model = LinearRegression()
        model.fit(X_train_transformed, y_train)

        pro, con = explains(df, model, X_train_transformed, transformers, 0)

        result = out_string + f'${y_pred:,.0f}'

        return render_template('home.html', title='Prediction', result=result)

    @app.route('/prediction', methods=['GET'])
    def api_return():

        if 'id' in request.args:
            id = int(request.args['id'])

            id = id + 0
            month = 12
            year = 19
            property_type = 'House'
            room_type = 'Entire home/apt'
            neighbourhood = 'East Downtown'
            accommodates = 4
            bedrooms = 2
            bathrooms = 2
            beds = 2

            df = pd.DataFrame(
                columns=['month', 'year', 'property_type', 'room_type',
                         'neighbourhood', 'accommodates', 'bedrooms',
                         'bathrooms', 'beds'],
                data=[[month, year, property_type, room_type, neighbourhood,
                       accommodates, bedrooms, bathrooms, beds]]
            )

            train = pd.read_csv('https://raw.githubusercontent.com/JimKing100/airbnb-app-4/master/Datascience/data/train.csv')
            train = train.drop(columns=['old_index'])
            target = 'price'

            features = train.columns.drop(target)
            X_train = train[features]
            y_train = train[target]

            pipeline = make_pipeline(
                ce.OrdinalEncoder(),
                LinearRegression()
            )

            pipeline.fit(X_train, y_train)
            y_pred = pipeline.predict(df)
            y_pred = y_pred[0]

            transformers = make_pipeline(
                ce.OrdinalEncoder(),
                SimpleImputer(strategy='mean')
            )

            X_train_transformed = transformers.fit_transform(X_train)

            model = LinearRegression()
            model.fit(X_train_transformed, y_train)

            pro, con = explains(df, model, X_train_transformed, transformers, 0)

            output_str = jsonify(prediction=str(int(y_pred)),
                                 pros1=pro[0],
                                 pros2=pro[1],
                                 cons1=con[0],
                                 cons2=con[1])

        else:
            return "Error: no id field provided"

        return output_str

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('db.html', title='DB Reset')
    return app
