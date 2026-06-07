import json

with open('data/theme-5.json', 'r') as f:
    data = json.load(f)

# Add a 5th option E to each of m1-m15
e_options = {
    "t5-m1": "E. Always presents with absent pedal pulses at rest regardless of exercise",
    "t5-m2": "E. Growth rate exceeds 0.3 cm over 5 years on surveillance ultrasound",
    "t5-m3": "E. South Asian ethnicity",
    "t5-m4": "E. The spleen",
    "t5-m5": "E. Increased age",
    "t5-m6": "E. Septic/infective material",
    "t5-m7": "E. Aneurysm formation",
    "t5-m8": "E. Percutaneous carotid artery stenting as first-line in all patients",
    "t5-m9": "E. Enterococcus faecalis",
    "t5-m10": "E. Angioedema",
    "t5-m11": "E. Switch to low molecular weight heparin bridging therapy for the peri-operative period",
    "t5-m12": "E. Patients with a previous episode of angio-oedema caused by any ACE inhibitor",
    "t5-m13": "E. It has no significant interaction with warfarin at therapeutic doses",
    "t5-m14": "E. Elevated serum bilirubin and abnormal liver function from chronic hepatic venous congestion",
    "t5-m15": "E. Infective endocarditis",
}

for q in data['mockBank']:
    if q['id'] in e_options:
        q['options'].append(e_options[q['id']])

# verify
bad = [q['id'] for q in data['mockBank'] if len(q['options']) != 5]
print(f"Questions still with wrong option count: {bad if bad else 'None'}")

with open('data/theme-5.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"mockBank total: {len(data['mockBank'])}")
