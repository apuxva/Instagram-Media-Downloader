from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    user_input = request.form.get('user_input')
    action = request.form.get('action')

    # Perform specific action based on the selected option
    if action == 'action1':
        subprocess.run(['python', 'insta_vdo_img.py', user_input])
        result_message = f"Executed Script 1 with input: {user_input}"
    elif action == 'action2':
        subprocess.run(['python', 'scrap.py', user_input])
        result_message = f"Executed Script 2 with input: {user_input}"
    else:
        result_message = "Invalid action"

    return render_template('result.html', result_message=result_message)

if __name__ == '__main__':
    app.run(debug=True)
