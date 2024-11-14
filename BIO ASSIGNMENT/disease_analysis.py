from fpdf import FPDF

print("\n\nDISEASE ANALYSIS :-- A SIMPLIFIED MODEL\n")
print("Write a 'q' to Finish\n")

def calculate_disease_risk(symptoms):
    risk_factors = {
        'fever': 0.2,
        'cough': 0.15,
        'fatigue': 0.1,
        'headache': 0.12,
        'sore_throat': 0.08,
        'runny_nose': 0.05,
        'muscle_aches': 0.1,
        'joint_pain': 0.1,
        'diarrhea': 0.08,
        'nausea': 0.07,
        'vomiting': 0.07,
        'loss_of_appetite': 0.05,
        'weight_loss': 0.1,
        'skin_rash': 0.08,
        'difficulty_breathing': 0.2,
        'chest_pain': 0.25,
        'swelling_in_legs': 0.15,
        'frequent_urination': 0.1,
        'blurred_vision': 0.12,
        'confusion': 0.2,
        'abdominal_pain': 0.1,
        'back_pain': 0.1,
        'chills': 0.15,
        'night_sweats': 0.12,
        'swollen_lymph_nodes': 0.1,
        'weakness': 0.1,
        'sensitivity_to_light': 0.08,
        'loss_of_smell': 0.1,
        'loss_of_taste': 0.1,
        'persistent_cough': 0.15,
        'cold_hands_and_feet': 0.1,
        'dry_skin': 0.08,
        'hair_loss': 0.05,
        'excessive_thirst': 0.1,
        'excessive_hunger': 0.1,
        'frequent_infections': 0.15,
        'slow_healing_wounds': 0.1,
        'mood_swings': 0.1,
        'anxiety': 0.1,
        'depression': 0.1,
        'insomnia': 0.08,
        'irregular_menstrual_cycle': 0.1,
        'painful_menstruation': 0.1,
        'infertility': 0.15,
        'erectile_dysfunction': 0.1,
        'decreased_libido': 0.08,
        'yellowing_of_skin_or_eyes': 0.2,
        'dark_urine': 0.15,
        'clay-colored_stools': 0.15,
        'itchy_skin': 0.1,
        'joint_swelling': 0.12,
        'stiff_joints': 0.1,
        'redness_or_swelling_in_joints': 0.15,
        'persistent_fever': 0.2,
        'unexplained_weight_loss': 0.15,
        'excessive_fatigue': 0.12,
        'frequent_nosebleeds': 0.1,
        'easy_bruising': 0.1,
        'pinpoint_red_spots': 0.12,
        'swollen_glands': 0.1,
        'persistent_sore_throat': 0.1,
        'hoarseness': 0.08,
        'difficulty_swallowing': 0.15,
        'mouth_sores': 0.1,
        'persistent_heartburn': 0.1,
        'blood_in_stool': 0.2,
        'change_in_bowel_habits': 0.15,
        'frequent_urination_at_night': 0.1,
        'painful_urination': 0.15,
        'blood_in_urine': 0.2,
        'frequent_headaches': 0.12,
        'dizziness': 0.1,
        'seizures': 0.2,
        'numbness_or_tingling': 0.1,
        'trouble_walking': 0.15,
        'vision_changes': 0.12,
        'double_vision': 0.15,
        'sudden_severe_headache': 0.2,
        'neck_stiffness': 0.15,
        'confusion_or_disorientation': 0.2,
        'weakness_on_one_side_of_body': 0.2,
        'trouble_speaking_or_understanding_speech': 0.2,
        'loss_of_balance_or_coordination': 0.15
    }

    total_risk = 0
    for symptom in symptoms:
        total_risk += risk_factors.get(symptom.lower(), 0)

    return min(total_risk, 1)

def get_patient_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ")
    medical_history = input("Enter any relevant medical history (comma-separated list): ")
    return name, age, gender, medical_history

def get_symptoms():
    symptoms = []
    critical_symptoms = []
    print("\nCurrent Medical Symptom\n")
    while True:
        symptom = input("Enter a symptom : ")
        if symptom.lower() == 'q':
            break
        if symptom.lower() in ['difficulty_breathing', 'chest_pain', 'difficulty_swallowing']:
            critical_symptoms.append(symptom)
            print("**Immediate medical attention is strongly advised.** \nPlease consult a professional healthcare doctor as soon as possible.")
            return symptoms, critical_symptoms  
        elif symptom.lower() not in [s.lower() for s in symptoms]:
            symptoms.append(symptom)
        else:
            print("You've already entered that symptom. Please enter a different one.")
    return symptoms, critical_symptoms

name, age, gender, medical_history = get_patient_info()

symptoms, critical_symptoms = get_symptoms()

if symptoms:
    risk_score = calculate_disease_risk(symptoms)

    print("\nYour calculated disease risk score is:", risk_score)

    if critical_symptoms:
        print("\n**Immediate medical attention is strongly advised.** \nPlease consult a professional healthcare doctor as soon as possible.")
    elif risk_score > 0.5:
        print("\n**High Risk of Illness Detected.**\nPlease consult a professional healthcare doctor for further evaluation and advice.")
    else:
        print("\nBased on the provided symptoms, your risk of illness is low.\n However, if symptoms persist or worsen, please consult a professional healthcare doctor.")

def generate_pdf_report(name, age, gender, medical_history, symptoms, risk_score, critical_symptoms):
    pdf = FPDF(orientation='L')
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Disease Analysis Report", ln=1, align='C')
    pdf.cell(200, 10, txt="Patient Information", ln=1, align='C')
    pdf.cell(50, 10, txt="Name:", ln=0)
    pdf.cell(150, 10, txt=name, ln=1)
    pdf.cell(50, 10, txt="Age:", ln=0)
    pdf.cell(150, 10, txt=str(age), ln=1)
    pdf.cell(50, 10, txt="Gender:", ln=0)
    pdf.cell(150, 10, txt=gender, ln=1)
    pdf.cell(50, 10, txt="Medical History:", ln=0)
    pdf.multi_cell(150, 10, txt=medical_history)

    pdf.cell(200, 10, txt="\nSymptoms Reported:", ln=1, align='C')
    for symptom in symptoms:
        pdf.cell(200, 10, txt=symptom, ln=1)

    pdf.cell(200, 10, txt="\nCalculated Disease Risk Score:", ln=1, align='C')
    pdf.cell(200, 10, txt=str(risk_score), ln=1, align='C')

    if critical_symptoms:
        pdf.cell(200, 10, txt="\n**Critical Symptoms Detected:**", ln=1, align='C')
        for symptom in critical_symptoms:
            pdf.cell(200, 10, txt=f"- {symptom}", ln=1)

        pdf.cell(275, 10, txt="\n**Immediate medical attention is strongly advised.**\nPlease consult a professional healthcare doctor as soon as possible.", ln=1, align='C')
    elif risk_score > 0.5:
        pdf.cell(275, 10, txt="\n**High Risk of Illness Detected.**\nPlease consult a professional healthcare doctor for further evaluation and advice.", ln=1, align='C')
    else:
        pdf.cell(275, 10, txt="\nBased on the provided symptoms, your risk of illness is low.\nHowever, if symptoms persist or worsen, please consult a healthcare professional.", ln=1, align='C')

    pdf.cell(200, 10, txt="\nGITHUB ACCOUNT ID :-- dsaisrih\n", ln=1, align='C')
    pdf.output("disease_analysis_report.pdf")
generate_pdf_report(name, age, gender, medical_history, symptoms, risk_score, critical_symptoms)

print("\nGITHUB ACCOUNT ID :-- dsaisrih\n")