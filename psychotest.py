#extraversion (E) vs. introversion (I), sensing (S) vs. intuition (N), thinking (TH) vs. feeling (F), and judging (J) vs. perceiving (P)
#Loner(L) vs. TeamWorker(TE),Calm & Composed(C&C) vs. Anxious in Pressure Conditions(AX),
def mbti_test():
    # Define the questions for each MBTI dimension
    questions = {
        'E': 'I prefer to socialize with others rather than spending time alone.',
        'I': 'I prefer to spend time alone rather than socializing with others.',
        'S': 'I focus on details and practicality in decision-making.',
        'N': 'I focus on possibilities and abstract concepts in decision-making.',
        'TH': 'I rely on logic and objective analysis when making decisions.',
        'F': 'I rely on personal values and empathy when making decisions.',
        'J': 'I prefer to have a plan and stick to it.',
        'P': 'I prefer to stay flexible and adapt to changing circumstances.',
        'L': 'Do you prefer to work alone?',
        'TE': 'Do you prefer to work with team?',
        'C&C': 'Are you good at handling stressful situations and remaining calm under pressure?',
        'AX': 'Are you anxious in stressful situations?'
    }

    # Initialize the user's MBTI type
    mbti_type = ''

    # Iterate through the questions and gather responses
    for dimension, question in questions.items():
        response = input(f"{question} (Enter 'A' for Agree or 'D' for Disagree): ").strip().lower()
        if response == 'a':
            mbti_type += dimension
        elif response == 'd':
            mbti_type += dimension

    # Determine the MBTI type based on the responses
    mbti_result = ''
    if 'E' in mbti_type:
        mbti_result += 'E'
    else:
        mbti_result += 'I'

    if 'S' in mbti_type:
        mbti_result += 'S'
    else:
        mbti_result += 'N'

    if 'TH' in mbti_type:
        mbti_result += 'TH'
    else:
        mbti_result += 'F'

    if 'J' in mbti_type:
        mbti_result += 'J'
    else:
        mbti_result += 'P'

    if 'L' in mbti_type:
        mbti_result += 'L'
    else:
        mbti_result += 'TE'
    if 'C&C' in mbti_type:
        mbti_result += 'C&C'
    else:
        mbti_result += 'AX'
    


    # Display the MBTI result
    print(f"Your MBTI Personality Type: {mbti_result}")

if __name__ == "__main__":
    print("Welcome to the MBTI Test!")
    mbti_test()
