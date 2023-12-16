from flask import Blueprint, request, flash, render_template, redirect, url_for

todo = Blueprint("todo", __name__)

todo_db = []


@todo.get("/")
def todo_page():
    html = render_template("todo.html", todos=enumerate(todo_db), title="Todo App")
    print(html)
    return html


@todo.post("/create")
def todo_create():
    form_data = request.form
    task = form_data.get("task")
    # print("FORM DATA:", form_data)
    # print("MY TASK:", task)

    # ADD TASK TO DB
    todo_db.append(task)

    #set the message
    flash("task added", 'success')

    return redirect(url_for('todo.todo_page'))


@todo.get("/delete/<int:index>")
def todo_delete(index):
    idx = int(index)
    todo_db.pop(idx)

    # redirect to todo page
    return redirect(url_for('todo.todo_page'))


# Todo Save route
# POST: /todo/update/<id>
@todo.post("/update/<int:index>")
def handle_save_todo(index):
    # GET THE NEW VALUE FROM THE INPUT
    form = request.form
    task = form.get("task")

    # REPLACE THE OLD VALUE WITH THE NEW ONE
    todo_db[index] = task

    # REDIRECT BACK TO THE TODO PAGE
    return redirect("/todo")





