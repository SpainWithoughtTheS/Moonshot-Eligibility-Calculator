from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows frontend to communicate with the backend

def check_eligibility(grade, mentor_meetings, webinars, assignments_missed, assignments_caught, assignments_late):
    return (
        grade > 70 and
        mentor_meetings >= 5 and
        webinars >= 1 and
        assignments_missed <= 3 and
        assignments_caught <= 2 and
        assignments_late <= 2
    )

@app.route('/check', methods=['POST'])
def check():
    try:
        data = request.json
        grade = float(data.get('grade', 0))
        mentor_meetings = int(data.get('mentor_meetings', 0))
        webinars = int(data.get('webinars', 0))
        assignments_missed = int(data.get('assignments_missed', 0))
        assignments_caught = int(data.get('assignments_caught', 0))
        assignments_late = int(data.get('assignments_late', 0))

        eligible = check_eligibility(grade, mentor_meetings, webinars, assignments_missed, assignments_caught, assignments_late)
        return jsonify({'eligible': eligible})

    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True)
