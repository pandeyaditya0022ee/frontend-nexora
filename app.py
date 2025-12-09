from flask import Flask, render_template, redirect, url_for,request
app = Flask(__name__)

@app.route('/login/personal_info', methods=['GET', 'POST'])
def login1():
    if request.method == 'POST':
        # Handle login logic here
        f_name = request.form.get('first_name')
        s_name = request.form.get('surname')
        address = request.form.get('address')
        dob = request.form.get('dob')
        l=[f_name, s_name, address, dob]
        return redirect(url_for('login2', data=l))
    return render_template('login.html')
@app.route('/login/academic_info', methods=['GET', 'POST'])
def login2(data):
    if request.method == 'POST':
        # Handle academic info logic here
        course = request.form.get('course')
        year = request.form.get('year')
        roll_no = request.form.get('roll_no')
        l = data + [course, year]
        return redirect(url_for('login3', data=l))