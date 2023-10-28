from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('comprehensive_puzzle.html')

@app.route('/submit', methods=['POST'])
def submit():
    score = 0

    response1 = request.form.get('response1')
    response2 = request.form.get('response2')
    response3 = request.form.get('response3')

    if response1 == '1':
        score += 2
    elif response1 == '2':
        score += 1

    if response2 == '1':
        score += 2
    elif response2 == '2':
        score += 1

    if response3 == '1':
        score += 2
    elif response3 == '2':
        score += 1

    if score >= 5:
        assessment = "Your decisions indicate strong leadership qualities and a willingness to take calculated risks."
    elif score >= 3:
        assessment = "You demonstrate a balanced approach, considering both safety and initiative."
    else:
        assessment = "You tend to prioritize caution and safety in decision-making."

    return render_template('result.html', score=score, assessment=assessment)

if __name__ == '__main__':
    app.run(debug=True)
