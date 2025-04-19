from flask import Flask, render_template, request

bmi_app = Flask(__name__)

@bmi_app.route('/', methods=['GET', 'POST'])
def index():
    bmi = ''
    if request.method == 'POST' and {'weight', 'height'} <= request.form.keys():
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            bmi = calc_bmi(weight, height)
        except ValueError:
            bmi = 'Only numbers please'
    return render_template('bmi_cal.html', bmi=bmi)

def calc_bmi(weight, height_cm):
    """Return BMI rounded to a whole number."""
    return round(weight / ((height_cm / 100) ** 2))

if __name__ == '__main__':
    bmi_app.run(debug=True)
