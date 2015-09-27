from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from libs.web_interface import get_user_by_handle

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('lookup_user', user_handle='sampleHandle'))

@app.route('/u/<user_handle>')
def lookup_user(user_handle):

    data = get_user_by_handle(user_handle)
    user_name = data['name']
    user_score = data['score']
    user_route = data['route']
    user_degree = len(user_route)
    user_kingpin = user_route[-1]

    return render_template('user_data_report.html', handle=user_handle,
                           name=user_name, score=user_score, degree=user_degree,
                           route=user_route, kingpin=user_kingpin)

if __name__ == '__main__':
    app.run(debug=True)
