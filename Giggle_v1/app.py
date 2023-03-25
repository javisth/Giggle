from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("mood.html")

@app.route("/jobs", methods=["POST"])
def get_matching_jobs():
    mood = request.json["mood"]
    # perform some logic to get matching jobs based on mood
    matching_jobs = [
        {"title": "Job 1", "description": "This is job 1"},
        {"title": "Job 2", "description": "This is job 2"},
        {"title": "Job 3", "description": "This is job 3"},
    ]
    return jsonify(matching_jobs)

if __name__ == "__main__":
    app.run(debug=True)

