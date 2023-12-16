from flask import Flask, request, render_template, redirect, flash
import os
import datetime
from werkzeug.utils import secure_filename
from flask_mail import Mail,  Message
from dotenv import dotenv_values


ENV = dotenv_values()
print("ENV", ENV)



def create_app():
    app = Flask(__name__)
    # CONFIGS
    app.config["SECRET_KEY"] = "test"
    app.config["SECRET_KEY"] = ENV["APP_SECRET"]


    # Mail configs
    app.config['MAIL_SERVER'] =ENV['MAIL_SERVER']
    app.config["MAIL_PORT"] = ENV["MAIL_PORT"]
    app.config["MAIL_USERNAME"] = ENV["MAIL_USERNAME"]
    app.config["MAIL_PASSWORD"] = ENV["MAIL_PASSWORD"]
    app.config["MAIL_USE_SSL"] = True

    mail = Mail(app)

    # BLUEPRINTS
    from .views.emproutes import emproutes
    app.register_blueprint(emproutes, url_prefix='/employee')

    from .views.todo_route import todo
    app.register_blueprint(todo, url_prefix="/todo")

    from .views.auth import auth
    app.register_blueprint(auth, url_prefix="/auth")

    # @app.route("/", methods=['GET', 'POST'])  # Slash(/) signifies our home page on the browser
    # def home_page():
    #     print("URL:", request.url)
    #     print("METHOD:", request.method)x
    #     return "Hello from Home page"


    #MAIL ROUTES
    @app.get('/mail')
    def mail_page():
        return render_template("mail.html")
    
    @app.post("/mail/send")
    def send_mail():
        form = request.form

        #  MESSAGES: takes in 
        #subject: string
        #recipients: [string]
        #body: string
        #html: string
        #sender: string
        message = Message( 
            subject='Test Mail Frrom Python Class', 
            recipients=[form.get('email')], 
            body=form.get('message'), 
            sender=("python class", "pythonclassaptech@gmail.com")
        ) 
        sent = mail.send(message)
        # if not sent:
        #     flash("MAIL did not SENT", "error")
        #     return redirect("/mail")
        
        flash("MAIL SENT", "success")
        return redirect("/mail")


    # END MAIL ROUTES


    @app.get("/upload")
    def view_upload_page():
        return render_template("/upload.html", title='upload file')

    @app.post("/upload/create")
    def upload_page():
        file = request.files['file']

        filename = file.filename
        print("FILE NAME", filename)

        filezize = file.content_length
        print(filezize)

        filetype = file.content_type
        print("TYPE", filetype)

        # restrict file types
        allowed_types = ['image/png', "image/jpg", "image/jpeg"]
        if filetype not in allowed_types:
            flash("file not allowed")
            return redirect("/upload")

        # UPLOAD THE FILLE
        # static folders are folders where all those files we wish to acess from our domain are stored
        file_path = os.path.abspath("./app/static/upload")
        timestamp = datetime.datetime.now().timestamp()
        new_filename = str(timestamp) + "_" + secure_filename(filename)

        # STORE FILE
        file.save(os.path.join(file_path, new_filename))

        flash("FILE UPLOADED")
        return redirect("/upload")

    return app

    # # Routes
    # @app.route("/", methods=['GET', 'POST']) # Slash(/) signifies our home page on the browser
    # def home_page():
    #     print("URL:", request.url)
    #     print("METHOD:", request.method)
    #     return "Hello from Home page"

    # @app.route("/about")
    # def about_page():
    #     return {"message": "Server running", "page": "About page"}

    # DYNAMIC ROUTES
    # @app.get("/profile/<name>")
    # def profile_page(name):
    #     return f"<p> Hello {name} </p>"

    # SPECIFY THE TYPE OF VALUE FOR THE DYNAMIC ROUTE
    # @app.get("/todo/<int:id>")
    # def todo_page(id):
    #     return f"<h2>This is the content of todo with the id of {id} </h2>"

    # REQUEST OBJECT
    # http://127.0.0.1:3000/test?name=hugo&age=50
    # @app.get("/test")
    # def test_page():
    #     return request.args

    # ERROR HANDLING IN ROUTES
    # 404
    # @app.errorhandler(404)
    # def errorhandler(error):
    #     return f"<h1>Page doesn't exist!!!</h1>"

    # return app

# STATUS CODES
# - 200 -> OK
# - 201 -> Created / Posted
# - 301 -> Redirecting
# - 400 -> Bad request
# - 401 -> Unauthorized
# - 403 -> Forbidden
# - 404 -> Not found
# - 500 -> Internet Server error
