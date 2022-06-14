from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def counter():
    if "counter" in session:
        session["counter"] += 1
    else:
        session["counter"] = 0
    return render_template("index.html")

@app.route('/count')
def inc_counter():
    return redirect("/")

@app.route('/destroy_session')
def del_count():
    session.clear()
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)