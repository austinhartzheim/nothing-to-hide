from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('lookup_user', user_handle='@sampleHandle'))

@app.route('/u/<user_handle>')
def lookup_user(user_handle):

    user_name = 'SAMPLE NAME'
    user_score = 'SAMPLE SCORE (in units of evil)'
    user_degree = 'SAMPLE DEGREE'

    return render_template('user_data_report.html', handle=user_handle, name=user_name,
                           score=user_score, degree=user_degree)

if __name__ == '__main__':
    app.run()