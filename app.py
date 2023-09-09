from flask import Flask, render_template

app = Flask(__name__)
JOBS = [{
    'Id': 1,
    'Title': 'Data Analyst',
    'Location': 'Minsk, Belarus',
    'Salary': '2,700 Byn'
}, {
    'Id': 2,
    'Title': 'Data Scientist',
    'Location': 'Grodno, Belarus',
    'Salary': '2,700 Byn'
}, {
    'Id': 3,
    'Title': 'Front End Engineer',
    'Location': 'Remote',
    'Salary': '1,500 Byn'
}]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0", debug=True)
