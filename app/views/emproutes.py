from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime


emproutes = Blueprint('emproutes', __name__)

# A list to store employee data (should ideally be a database in a real app)
employees = []

@emproutes.route('/')
def index():
    return render_template('index.html')

@emproutes.get('/employee_list')
def employee_list():
    return render_template('employee.html', employees=enumerate(employees))

@emproutes.post('/employee_list')
def add_employee():
    
    form = request.form


    employees.append(form)

    return redirect(url_for('emproutes.employee_list'))

@emproutes.get('/edit/<int:index>')
def edit_employee(index):
    employee = employees[index]
    return render_template('edit.html', index=index, employee=employee )

@emproutes.post("/edit/<int:index>")
def handle_edit(index):
    form_data = request.form
    info = form_data

    # REPLACE THE OLD VALUE WITH THE NEW ONE
    employees[index] = info

    # REDIRECT BACK TO THE emplyeelist PAGE
    return redirect(url_for('emproutes.employee_list'))



# @emproutes.route("/edit/<int:index>", methods=['GET', 'POST'])
# def edit_employee(index):
#     if request.method == 'POST':
#         form_data = request.form
#         name = form_data.get("name")
#         age = form_data.get("age")
#         salary = form_data.get("salary")
#         qualification = form_data.get("qualification")

#         employees[index] = {
#             'name': name,
#             'age': age,
#             'salary': salary,
#             'qualification': qualification
#         }

#         # flash("Employee updated", "success")
#         return redirect(url_for('employee.employee_list'))

#     employee = employees[index]
#     return render_template("edit.html", index=index, employee=employee)

@emproutes.route('/employee/<int:index>/delete', methods=['POST'])
def delete_employee(index):
    employees.pop(index)
    return redirect(url_for('emproutes.employee_list'))
