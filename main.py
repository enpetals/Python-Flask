from app import create_app

# __name__ changes to __main__ whenever the file is running
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=3000)  # For Development purpose

