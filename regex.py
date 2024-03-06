from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regex_matcher', methods=['GET', 'POST'])
def regex_matcher():
    if request.method == 'POST':
        pattern = request.form['pattern']
        text = request.form['text']
        matches = re.findall(pattern, text)
        return render_template('regex_matcher.html', matches=matches,pattern=pattern,text=text)
    return render_template('regex_matcher.html')

@app.route('/email_validation', methods=['GET', 'POST'])
def email_validation():
    if request.method == 'POST':
        email = request.form['email']
        if re.match(r"[A-z0-9 ]+@\w+\.\w+", email):
            message = 'Valid email address.'
        else:
            message = 'Invalid email address.'
        return render_template('email_validation.html', message=message,email=email)
    return render_template('email_validation.html')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)