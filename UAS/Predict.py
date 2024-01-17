import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
page = 'index.html'

clf = pickle.load(open('models/random_forest4 (1).pickle', 'rb'))

@app.route("/")
def index():
    return render_template(page)

@app.route("/data", methods=['GET', 'POST'])
def data():
    radius_mean = request.form.get('radius_mean')
    texture_mean = request.form.get('texture_mean')
    perimeter_mean = request.form.get('perimeter_mean')
    area_mean = request.form.get('area_mean')
    smoothness_mean = request.form.get('smoothness_mean')
    compactness_mean = request.form.get('compactness_mean')
    concavity_mean = request.form.get('concavity_mean')
    symmetry_mean = request.form.get('symmetry_mean')
    fractal_dimension_mean = request.form.get('fractal_dimension_mean')
    radius_se = request.form.get('radius_se')
    texture_se = request.form.get('texture_se')
    perimeter_se = request.form.get('perimeter_se')
    area_se = request.form.get('area_se')
    smoothness_se = request.form.get('smoothness_se')
    compactness_se = request.form.get('compactness_se')
    concavity_se = request.form.get('concavity_se')
    symmetry_se = request.form.get('symmetry_se')
    fractal_dimension_se = request.form.get('fractal_dimension_se')
    radius_worst = request.form.get('radius_worst')
    texture_worst = request.form.get('texture_worst')
    perimeter_worst = request.form.get('perimeter_worst')
    area_worst = request.form.get('area_worst')
    smoothness_worst = request.form.get('smoothness_worst')
    compactness_worst = request.form.get('compactness_worst')
    concavity_worst = request.form.get('concavity_worst')
    symmetry_worst = request.form.get('symmetry_worst')
    fractal_dimension_worst = request.form.get('fractal_dimension_worst')

    arr = [[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
            concavity_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se,
            smoothness_se, compactness_se, concavity_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst,
            perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, symmetry_worst,
            fractal_dimension_worst]]

    predict = clf.predict(arr)
    predictstr = "Kanker Malignant"
    if predict == 1:
        predictstr = "Kanker Benign"

    return render_template('display.html',
                           radius_mean=radius_mean,
                           texture_mean=texture_mean,
                           perimeter_mean=perimeter_mean,
                           area_mean=area_mean,
                           smoothness_mean=smoothness_mean,
                           compactness_mean=compactness_mean,
                           concavity_mean=concavity_mean,
                           symmetry_mean=symmetry_mean,
                           fractal_dimension_mean=fractal_dimension_mean,
                           radius_se=radius_se,
                           texture_se=texture_se,
                           perimeter_se=perimeter_se,
                           area_se=area_se,
                           smoothness_se=smoothness_se,
                           compactness_se=compactness_se,
                           concavity_se=concavity_se,
                           symmetry_se=symmetry_se,
                           fractal_dimension_se=fractal_dimension_se,
                           radius_worst=radius_worst,
                           texture_worst=texture_worst,
                           perimeter_worst=perimeter_worst,
                           area_worst=area_worst,
                           smoothness_worst=smoothness_worst,
                           compactness_worst=compactness_worst,
                           concavity_worst=concavity_worst,
                           symmetry_worst=symmetry_worst,
                           fractal_dimension_worst=fractal_dimension_worst,
                           predict=predict,
                           predictstr=predictstr)

if __name__ == '__main__':
    app.run()