from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/student-details', methods=['GET'])
def student_details():
    return jsonify({
        "name": "Your Name",
        "roll_number": "Your Roll No",
        "register_number": "Your Register No"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)