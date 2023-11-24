from flask import Flask
app = Flask(name)

@app.route('/')
def crazybossisbacknigga():
    return 'The-Crazy-Boss'


if name == "main":
    app.run()
