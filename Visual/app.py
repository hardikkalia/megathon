from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_choice', methods=['POST'])
def process_choice():
    selected_option = request.form.get('choice')
    
    # Perform an action based on the selected option
    if selected_option == 'option1':
        result = "You are careful with everyone around you. You are responsible, reliable, and detail-oriented. You take your decisions after thinking carefully about everything. You will not rush into anything. You are highly observant and take notice of everyone’s body language and behavior.You are meticulous, systematic, analytical, and attentive to details. You may be a forward-thinking and assertive kind of person. You may not take decisions based entirely on emotions. You look for meaning and significance in life. You have a need to care, encourage, and contribute to your surroundings and relations. You are a natural visionary, non-conformist, and problem-solver kind of individual."
    elif selected_option == 'option2':
        result = "You are good at understanding people and not leaving their side during their troubled times. You may not judge or conclude opinions about people right away. You will try to know them first. You are a very conscientious person. You understand that people are not perfect and mistakes can happen to anyone.You value integrity and unity in relationships. You are a natural romantic and nurturer. You enjoy connections that encourage expressions and acceptance. You may be one of those extremely helpful individuals who give more importance to relationships than other aspects of life. You are likely to make decisions based on emotions. You want to be understood and appreciated."
    elif selected_option == 'option3':
        result = "You tend to possess exceptional confidence and leadership skills. You are able to recognize problems and the most apt solutions. You may be skilled at turning around situations and opportunities to your advantage. Under negative circumstances, you can also be pretentious, snobbish, and arrogant.You love living in the present. You enjoy every moment to the fullest. You love spontaneity in your work. You love creating new ideas. You have a strong independent streak. You may highly ambitious. You may like to be the center of attention. You may be highly competitive and may have learned to keep a good grip on your emotions. "
    elif selected_option == 'option4':
        result = " You may trust others easily. You may be sensitive and emotional. You want to be understood and appreciated. You may always try to be a better person. You prefer to lead by a 'head over heart' approach. You are easy to talk to and a good listener. However, you become uneasy if you feel controlled too much by your emotions.You like to work on yourself and your goals to achieve success. You love to learn new things and concepts. You abide by high morals while working also. In your adult life also, you may find yourself on a quest to discover yourself. You may seek outer validation a lot to feel good about yourself. You may be needed to be reminded about your uniqueness and abilities."
    else:
        result = "Invalid option selected."

    return result

if __name__ == '__main__':
    app.run(debug=True,port=8000)
