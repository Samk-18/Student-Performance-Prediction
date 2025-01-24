import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load student data from the JSON file
with open('student_data.json', 'r') as f:
    Student_Data = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_scores', methods=['POST'])
def get_scores():
    student_id = request.form['roll_no']
    if student_id in Student_Data:
        return jsonify({
            "student_id": student_id,
            "attendance": Student_Data[student_id]["attendance"],
            "ca": Student_Data[student_id]["CA"],
            "mid_sem": Student_Data[student_id]["MD"],
            "end_sem": Student_Data[student_id]["ESE"],
            "total_grade": Student_Data[student_id]["Total_Grade"],
            "previous_grade": Student_Data[student_id]["Previous_Grade"]
        })
    else:
        return jsonify({"error": "ID number not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)