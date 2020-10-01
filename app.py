from flask import Flask, render_template, request
import script

app = Flask(__name__)

@app.route('/')
def main():
    """ Main page """
    return render_template("front.html")

@app.route('/',methods=['POST'])
def test():
    text = request.form['text']
    result = 'Result = '+str(script.evaluate(text))
    return render_template("front.html", result = result)

if __name__=="__main__":
    app.run()

