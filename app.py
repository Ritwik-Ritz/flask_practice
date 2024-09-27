from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1, 
        "title": "Data Analyst",
        "location": "Bengaluru, India",
        "salary":"15000"
    },
    {
        "id": 2, 
        "title": "Data Scientist",
        "location": "Delhi, India",
        "salary":"25000"
    },
    {
        "id": 3, 
        "title": "Backend Engineer",
        "location": "Los Angeles, USA",
        "salary":"150000"
    },
    {
        "id": 4, 
        "title": "Software Tester",
        "location": "New York City, USA",
        "salary":"100000"
    },
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_of_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host ='0.0.0.0', debug=True)
