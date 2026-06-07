import json

with open('data/theme-5.json', 'r') as f:
    data = json.load(f)

# Fix existing applyIt items to have 5 options
data['applyIt'][0]['options'] = [
    "A. Ask him to stop warfarin for 5 days and recheck INR before proceeding",
    "B. Proceed with the extractions using appropriate local haemostatic measures; do not alter warfarin",
    "C. Refer to hospital for the extractions as INR >2 means he cannot be treated in primary care",
    "D. Reduce the warfarin dose and proceed when INR reaches 1.5",
    "E. Prescribe tranexamic acid tablets for 5 days prior to the extraction to reduce bleeding risk"
]

data['applyIt'][1]['options'] = [
    "A. Yes — antibiotic prophylaxis is routinely recommended for all patients with valvular heart disease before root canal treatment",
    "B. No — NICE guidelines do not routinely recommend antibiotic prophylaxis for dental procedures, and oral hygiene optimisation is the most important prevention",
    "C. Yes — amoxicillin 3g one hour before the procedure is required",
    "D. Only if she has previously had infective endocarditis — otherwise no prophylaxis is needed",
    "E. Only if the root canal is for a tooth with a periapical abscess — routine root canal requires no prophylaxis"
]

data['applyIt'][2]['options'] = [
    "A. Prescribe a chlorhexidine mouthwash for 2 weeks and discharge",
    "B. Optimise oral hygiene instruction and refer to periodontist; liaise with their physician about possible substitution of amlodipine with a non-dihydropyridine agent",
    "C. Inform the patient this is a normal side effect and no action is needed",
    "D. Immediately stop amlodipine and prescribe an alternative antihypertensive yourself",
    "E. Perform surgical gingivectomy immediately as this is the definitive treatment"
]

# New applyIt items a4-a50
new_apply = [
    {
        "id": "t5-a4",
        "scenario": "A 72-year-old woman with atrial fibrillation on apixaban 5mg twice daily is booked for extraction of three teeth. Her last dose was at 8am this morning and the procedure is at 2pm. She has normal renal function. Which ONE of the following is the MOST appropriate management?",
        "options": [
            "A. Cancel the procedure and reschedule after she has stopped apixaban for 5 days",
            "B. Reverse the apixaban with andexanet alfa before proceeding",
            "C. Proceed with the extractions using local haemostatic measures; no dose alteration is needed for routine extractions",
            "D. Check her INR before proceeding and defer if above 3",
            "E. Halve her morning dose of apixaban on the day of surgery to reduce bleeding risk"
        ],
        "correctAnswer": "C",
        "explanation": "For patients on DOACs such as apixaban undergoing routine dental extractions (1–3 simple teeth), the procedure should proceed without stopping or altering the anticoagulant. INR testing is not relevant — DOACs do not affect the INR. Local haemostatic measures (oxidised cellulose, sutures, tranexamic acid 5% mouthwash four times daily for 2 days) are used. The risk of stopping apixaban — stroke from AF — far exceeds the risk of post-extraction bleeding. Andexanet alfa is reserved for life-threatening haemorrhage."
    },
    {
        "id": "t5-a5",
        "scenario": "During a dental extraction, a 65-year-old man with known angina develops central chest pain that is not relieved after two doses of his GTN spray 5 minutes apart. He is pale, sweaty, and nauseous. Which ONE of the following is the MOST appropriate immediate action?",
        "options": [
            "A. Administer a third dose of GTN spray and monitor for a further 10 minutes",
            "B. Place the patient in the supine position and give 100% oxygen; reassess in 5 minutes",
            "C. Call 999; administer aspirin 300mg chewed; give 100% oxygen at 15L/min via non-rebreathe mask",
            "D. Give IM adrenaline 500 micrograms immediately as this may be anaphylaxis",
            "E. Administer oral morphine 10mg for pain relief and call the GP"
        ],
        "correctAnswer": "C",
        "explanation": "Chest pain not relieved by two doses of GTN spray (given 5 minutes apart) should be treated as a suspected myocardial infarction. The immediate management is: call 999, give aspirin 300mg chewed (not swallowed whole — faster absorption), and administer 100% oxygen at 15L/min via non-rebreathe mask if the patient is hypoxic. A third GTN dose may be appropriate while waiting for the ambulance, but the emergency services must be called first. IM adrenaline is for anaphylaxis. Oral morphine is not available in dental practice; IV morphine would be given by paramedics."
    },
    {
        "id": "t5-a6",
        "scenario": "A 58-year-old woman taking lisinopril (an ACE inhibitor) for hypertension attends with an oral candidal infection. She is also on warfarin for atrial fibrillation (INR 2.6). Which ONE of the following antifungal prescriptions is MOST appropriate?",
        "options": [
            "A. Miconazole oral gel 24mg/g — apply four times daily for 7 days",
            "B. Fluconazole 150mg capsule — single dose",
            "C. Nystatin oral suspension 100,000 units/mL — 1mL four times daily for 7 days",
            "D. Itraconazole 200mg capsule — once daily for 3 days",
            "E. Clotrimazole 1% cream — apply to affected area three times daily"
        ],
        "correctAnswer": "C",
        "explanation": "Nystatin is the correct choice for a patient on warfarin. Nystatin is a topical antifungal that is not significantly absorbed systemically and does not inhibit CYP enzymes — it has no significant interaction with warfarin. All azole antifungals (miconazole, fluconazole, itraconazole, ketoconazole) inhibit CYP2C9 to varying degrees and will significantly raise the INR in a warfarin patient, risking dangerous bleeding. Miconazole oral gel is absolutely contraindicated with warfarin — even the topical form is substantially absorbed and can raise INR by a factor of 5–10. Clotrimazole cream is for skin infections, not oral candidiasis."
    },
    {
        "id": "t5-a7",
        "scenario": "A 70-year-old man with severe left-sided heart failure (NYHA class III) attends for a lower molar extraction under local anaesthetic. He sleeps on four pillows at night and gets breathless climbing one flight of stairs. Which ONE of the following is the MOST appropriate modification to his dental management?",
        "options": [
            "A. Treat him in the fully supine position to improve venous return and cardiac output during the procedure",
            "B. Treat him in a semi-reclined or upright position; use effective local anaesthetic; keep the appointment short",
            "C. Refer him to hospital as heart failure patients cannot be treated in primary care",
            "D. Prescribe ibuprofen 400mg three times daily for post-operative analgesia",
            "E. Use adrenaline-free local anaesthetic (prilocaine with felypressin) exclusively"
        ],
        "correctAnswer": "B",
        "explanation": "Patients with significant left-sided heart failure cannot lie flat because venous redistribution in the supine position worsens pulmonary oedema — this is orthopnoea. Four pillows at night confirms significant orthopnoea. He must be treated in a semi-reclined or upright position at whatever angle he finds comfortable. Effective local anaesthetic is critical — pain and anxiety trigger catecholamine surges equivalent to surgical stress, which significantly increase myocardial oxygen demand. Appointments should be short and in the morning. NSAIDs (ibuprofen) are contraindicated in heart failure — they cause sodium retention and worsen the condition. Adrenaline-containing LA is generally safe in mild-moderate CVD with careful technique."
    },
    {
        "id": "t5-a8",
        "scenario": "A 55-year-old man is referred with severe, non-healing oral ulceration affecting his lateral tongue and floor of mouth for 8 weeks. His medical history includes angina, for which he takes atenolol, nicorandil, and aspirin. Examination reveals two large (2cm), punched-out ulcers with clean bases. Which ONE of the following is the MOST likely cause?",
        "options": [
            "A. Atenolol-induced lichenoid reaction",
            "B. Aspirin-induced chemical burn",
            "C. Nicorandil-induced oral ulceration",
            "D. Squamous cell carcinoma — requires urgent biopsy",
            "E. Aphthous stomatitis (major aphthae)"
        ],
        "correctAnswer": "C",
        "explanation": "Nicorandil (a potassium channel opener/nitrate used for angina) is a well-documented cause of severe, non-healing oral ulceration. The ulcers are characteristically large, deep, and punched-out with clean edges — they can closely mimic malignancy or major aphthae. The crucial diagnostic clue is the medication history. Management: refer to the cardiologist to substitute nicorandil with an alternative antianginal; the ulcers typically heal within 4–8 weeks of drug cessation. Before attributing to nicorandil, malignancy should be excluded if the ulcer has suspicious features or does not heal after drug withdrawal. Atenolol causes lichenoid reactions (white striae), not ulcers of this type."
    },
    {
        "id": "t5-a9",
        "scenario": "A 68-year-old woman on amlodipine 10mg daily for hypertension presents with marked gingival overgrowth affecting all four quadrants. She has good oral hygiene. She has tried improved cleaning for 3 months with no improvement. Which ONE of the following is the MOST appropriate next step?",
        "options": [
            "A. Perform a gingivectomy immediately under local anaesthetic",
            "B. Refer to periodontist and write to her GP requesting consideration of changing amlodipine to a non-dihydropyridine antihypertensive",
            "C. Tell her the gingival hyperplasia is permanent and irreversible regardless of any change in medication",
            "D. Prescribe a course of oral metronidazole to reduce the gingival inflammation",
            "E. Advise her to stop amlodipine immediately and switch to a herbal supplement"
        ],
        "correctAnswer": "B",
        "explanation": "Drug-induced gingival overgrowth from amlodipine (a dihydropyridine calcium channel blocker) that has not responded to improved oral hygiene over 3 months warrants specialist periodontal assessment and liaison with the prescribing physician about possible drug substitution. Switching from a dihydropyridine CCB (amlodipine, nifedipine) to a non-dihydropyridine CCB or a different antihypertensive class often results in partial or complete resolution of the overgrowth, especially when combined with improved oral hygiene. The dentist should not directly change prescriptions — this is the GP's decision. Surgery (gingivectomy) is a last resort and will recur if the drug continues."
    },
    {
        "id": "t5-a10",
        "scenario": "A 45-year-old man with a bicuspid aortic valve develops fever, night sweats, and weight loss over 6 weeks. He had a dental extraction 8 weeks ago. Blood cultures grow Streptococcus viridans from two separate samples. His echocardiogram shows a 1cm oscillating mass on the aortic valve. According to the Duke criteria, what is the diagnosis?",
        "options": [
            "A. Possible infective endocarditis — only 1 major criterion met",
            "B. Rejected endocarditis — fever alone with blood cultures is insufficient",
            "C. Definite infective endocarditis — 2 major criteria are met",
            "D. Possible infective endocarditis — requires 5 minor criteria to confirm",
            "E. Definite infective endocarditis — 1 major and 4 minor criteria are met"
        ],
        "correctAnswer": "C",
        "explanation": "The Duke criteria for definite infective endocarditis require either: (a) 2 major criteria, (b) 1 major + 3 minor, or (c) 5 minor criteria. Here, two major criteria are met: (1) Positive blood cultures with typical IE organism (Streptococcus viridans — a viridans streptococcus — from two separate blood cultures); (2) Echo evidence of endocardial involvement (oscillating mass — vegetation on the aortic valve). Therefore, this is DEFINITE IE by Duke criteria. The bicuspid aortic valve is a predisposing cardiac condition (minor criterion), but this is not needed as the diagnosis is already met by 2 major criteria."
    },
    {
        "id": "t5-a11",
        "scenario": "A 62-year-old man on metoprolol (a cardioselective beta-blocker) and lisinopril for hypertension requires urgent dental extraction for an abscess. You plan to prescribe an antibiotic. Which ONE of the following antibiotics is MOST appropriate considering his cardiovascular medications?",
        "options": [
            "A. Metronidazole 400mg three times daily for 5 days",
            "B. Erythromycin 500mg four times daily for 5 days",
            "C. Clarithromycin 500mg twice daily for 5 days",
            "D. Amoxicillin 500mg three times daily for 5 days",
            "E. Ciprofloxacin 500mg twice daily for 5 days"
        ],
        "correctAnswer": "D",
        "explanation": "Amoxicillin is the safest choice in this patient. He is on metoprolol (beta-blocker) and lisinopril (ACE inhibitor) — this does not involve warfarin, so the major antibiotic interaction concern (drugs raising INR) is less relevant here. Metronidazole does not significantly interact with metoprolol or lisinopril. However, erythromycin and clarithromycin (macrolides) inhibit CYP3A4, which raises plasma levels of certain drugs and prolongs the QT interval — there is a meaningful drug interaction risk with many CVD medications, and they should be used cautiously. Ciprofloxacin (quinolone) also prolongs QT interval. Amoxicillin is the first-line choice for most dental infections without significant CVD drug interactions."
    },
    {
        "id": "t5-a12",
        "scenario": "A 79-year-old woman with a mechanical mitral valve has warfarin temporarily stopped by her cardiologist before elective hip surgery. Three days post-operatively, she develops a dense right hemiplegia and aphasia. Which ONE of the following BEST explains this complication?",
        "options": [
            "A. Intracerebral haemorrhage from anticoagulation being resumed too quickly post-operatively",
            "B. Cardioembolic stroke from left atrial thrombus during the period of inadequate anticoagulation",
            "C. Paradoxical embolism through a patent foramen ovale",
            "D. Hypotension-related watershed infarct from intra-operative blood loss",
            "E. Fat embolism from bone marrow exposed during hip surgery"
        ],
        "correctAnswer": "B",
        "explanation": "This patient has a mechanical mitral valve, which carries a very high risk of valve thrombosis and systemic embolism when anticoagulation is inadequate. Stopping warfarin — even briefly — allows thrombus to form on the mechanical valve (most commonly in the left atrium). This thrombus can embolise to the cerebral circulation, causing a large ischaemic stroke with dense hemiplegia and aphasia (left MCA territory from left atrial/valve embolus to right hemisphere). This is why mechanical prosthetic valve patients should be 'bridged' with therapeutic LMWH when warfarin must be stopped. The same applies to dental procedures — warfarin should never be stopped for dental extractions (INR ≤4: proceed with local haemostasis)."
    },
    {
        "id": "t5-a13",
        "scenario": "A 50-year-old male smoker with hypertension attends for routine dental treatment. His blood pressure measured at the start of the appointment is 195/115 mmHg. He is asymptomatic. Which ONE of the following is the MOST appropriate action?",
        "options": [
            "A. Proceed with routine treatment — a single elevated reading is not clinically significant",
            "B. Defer elective treatment; refer urgently to his GP; treat only a dental emergency if necessary with minimal adrenaline",
            "C. Administer sublingual nifedipine to lower blood pressure immediately before proceeding",
            "D. Call 999 immediately as this represents a hypertensive emergency requiring hospitalisation",
            "E. Repeat the blood pressure in 5 minutes; if still elevated, proceed with a maximum of 2 cartridges of LA"
        ],
        "correctAnswer": "B",
        "explanation": "A clinic blood pressure of 195/115 mmHg is stage 3 / severe hypertension (≥180/110 mmHg). In an asymptomatic patient, this is a hypertensive urgency, not a hypertensive emergency (no acute end-organ damage). Elective dental treatment should be deferred and the patient urgently referred to their GP (same day or next day) for BP assessment and initiation/optimisation of antihypertensive treatment. If a dental emergency (acute pain, abscess) must be treated, use the minimum effective adrenaline dose (1:100,000 or 1:200,000) with careful aspiration and slow injection. Sublingual nifedipine for acute BP lowering in dental practice is dangerous (causes unpredictable and sometimes catastrophic hypotension) and is not recommended."
    },
    {
        "id": "t5-a14",
        "scenario": "A patient presents with a red, swollen, hot, tender lower leg that has developed over 24 hours. They recently had a long-haul flight. You suspect a deep vein thrombosis. Which ONE of the following is the MOST appropriate first investigation?",
        "options": [
            "A. D-dimer blood test — if positive, start anticoagulation immediately",
            "B. Calculate the Wells score for DVT probability; if high probability proceed directly to compression duplex ultrasound",
            "C. Prescribe prophylactic LMWH and recheck in 1 week",
            "D. Arrange a CT pulmonary angiogram (CTPA) to look for pulmonary embolism",
            "E. Perform a chest X-ray to exclude pulmonary embolism before treating the leg"
        ],
        "correctAnswer": "B",
        "explanation": "The correct diagnostic pathway for suspected DVT uses the Wells score to determine pre-test probability. With a recent long-haul flight (immobility), the Wells score is likely ≥2 (high probability). In this case, a compression duplex ultrasound is the next step (without needing D-dimer first). If the Wells score is 0–1 (low probability), a D-dimer test is performed first; if negative, DVT is effectively excluded; if positive, proceed to ultrasound. D-dimer alone (option A) is not sufficient — a positive D-dimer is non-specific and does not establish the diagnosis. CTPA (option D) investigates for PE, not DVT."
    },
    {
        "id": "t5-a15",
        "scenario": "A 66-year-old woman is prescribed lisinopril (ACE inhibitor) for hypertension. Three months later she develops bilateral lip and tongue swelling without urticaria or other allergic features. Which ONE of the following BEST describes this reaction and its management?",
        "options": [
            "A. Allergic angioedema from lisinopril; treat with oral antihistamine; continue lisinopril at a lower dose",
            "B. Bradykinin-mediated angioedema from lisinopril; immediately stop lisinopril; treat airway as priority; switch to an ARB",
            "C. Hereditary angioedema; lisinopril is unrelated; refer to immunologist",
            "D. Drug hypersensitivity reaction; prescribe oral prednisolone and continue lisinopril",
            "E. Normal side effect of ACE inhibitors; reduce dose and monitor"
        ],
        "correctAnswer": "B",
        "explanation": "ACE inhibitor-induced angioedema is mediated by bradykinin accumulation (not IgE/histamine), caused by ACE enzyme inhibition preventing bradykinin degradation. It is not an allergic reaction — antihistamines and steroids are largely ineffective. It is NOT dose-related and can occur years after starting the drug. The airway must be secured immediately (adrenaline IM if threatened). Lisinopril must be stopped permanently. ARBs are usually substituted but should be used cautiously — rare cross-reactivity with ACE inhibitor angioedema. Notably, this bradykinin-mediated angioedema does NOT respond to adrenaline as readily as histamine-mediated anaphylaxis, making early intervention critical."
    },
    {
        "id": "t5-a16",
        "scenario": "A 74-year-old man with heart failure on furosemide, lisinopril, bisoprolol, and spironolactone develops muscle weakness and a potassium level of 6.4 mmol/L (normal 3.5–5.0). Which ONE of the following drug combinations MOST likely caused this dangerous electrolyte imbalance?",
        "options": [
            "A. Furosemide and bisoprolol — loop diuretics cause potassium retention",
            "B. Lisinopril and spironolactone — ACE inhibitor combined with a potassium-sparing diuretic causes hyperkalaemia",
            "C. Furosemide and lisinopril — loop diuretics and ACE inhibitors always cause hyperkalaemia together",
            "D. Bisoprolol and spironolactone — beta-blockers combined with aldosterone antagonists cause hyperkalaemia",
            "E. Furosemide alone — loop diuretics raise potassium as their main electrolyte effect"
        ],
        "correctAnswer": "B",
        "explanation": "Hyperkalaemia (K+ 6.4 mmol/L) in this patient is most likely caused by the combination of lisinopril (ACE inhibitor — blocks aldosterone secretion, reducing renal K+ excretion) and spironolactone (aldosterone antagonist — directly prevents K+ excretion in the distal nephron). Both drugs independently raise potassium, and the combination significantly amplifies this effect. This is a recognised and potentially fatal combination — regular electrolyte monitoring is essential when both are prescribed. Furosemide (loop diuretic) causes HYPOKALAEMIA (not hyperkalaemia) — it actually partially offsets the potassium-raising effect of ACE inhibitors and spironolactone in the heart failure regimen."
    },
    {
        "id": "t5-a17",
        "scenario": "A 60-year-old man with angina is on atenolol, aspirin, and isosorbide mononitrate. He is newly prescribed amlodipine by his GP. He calls the dental practice asking if the new drug will cause any changes in his mouth. Which ONE of the following is the MOST accurate response?",
        "options": [
            "A. Amlodipine commonly causes oral ulceration — he should stop it and call his GP",
            "B. Amlodipine may cause gingival hyperplasia — he should maintain excellent oral hygiene and attend for regular periodontal review",
            "C. Amlodipine is completely safe with no oral side effects",
            "D. Amlodipine commonly causes a metallic taste and dry mouth — chlorhexidine mouthwash will help",
            "E. Amlodipine causes oral lichenoid reactions which require an urgent biopsy"
        ],
        "correctAnswer": "B",
        "explanation": "Amlodipine is a dihydropyridine calcium channel blocker associated with drug-induced gingival overgrowth (hyperplasia) in approximately 10–20% of users. The severity is closely related to oral hygiene — meticulous plaque control significantly reduces the risk and severity of overgrowth. The patient should be advised to maintain excellent oral hygiene and attend for regular periodontal monitoring. If overgrowth becomes significant despite good oral hygiene, the dentist should liaise with the prescribing GP about possible drug substitution. Oral ulceration is associated with nicorandil, not amlodipine. Lichenoid reactions are associated with beta-blockers (atenolol) and diuretics."
    },
    {
        "id": "t5-a18",
        "scenario": "A 55-year-old woman with mitral stenosis and atrial fibrillation is on warfarin (INR target 2.5–3.5). Her INR today is 4.6. She requires an urgent extraction for a symptomatic periapical abscess causing facial swelling and difficulty swallowing. Which ONE of the following is the MOST appropriate course of action?",
        "options": [
            "A. Proceed with extraction immediately — the INR threshold for dental procedures is 5.0",
            "B. Defer extraction and prescribe oral antibiotics only; admit to hospital if airway compromise worsens; contact haematologist regarding INR",
            "C. Administer IV vitamin K 10mg to immediately reverse warfarin before extraction",
            "D. Proceed with extraction under general anaesthetic with an experienced surgeon",
            "E. Stop warfarin and recheck INR in 48 hours; proceed once INR is below 4"
        ],
        "correctAnswer": "B",
        "explanation": "With INR 4.6 (above the dental threshold of 4.0), elective or semi-urgent extraction should be deferred. The correct immediate action is to manage the infection medically (antibiotics — amoxicillin or clindamycin), monitor for worsening airway compromise, and contact the GP/haematologist to review and adjust the warfarin dose to bring the INR within the safe range (≤4.0). If airway compromise develops, this becomes a genuine emergency requiring hospital admission and surgical airway management. IV vitamin K 10mg would cause over-reversal and prolonged warfarin resistance — not appropriate for elective management. Simply stopping warfarin risks valve thrombosis in a patient with mechanical/valvular AF."
    },
    {
        "id": "t5-a19",
        "scenario": "A 48-year-old man who takes clopidogrel 75mg daily (following coronary artery stenting 6 months ago) and aspirin 75mg daily requires extraction of a non-restorable molar. He has no other significant medical history. Which ONE of the following BEST describes the correct management of his antiplatelet therapy?",
        "options": [
            "A. Stop both antiplatelet drugs 7 days before the extraction to minimise bleeding risk",
            "B. Stop clopidogrel only and continue aspirin — single antiplatelet therapy is sufficient",
            "C. Continue both antiplatelet agents; use local haemostatic measures; do not stop antiplatelet therapy",
            "D. Refer to hospital for the extraction as patients on dual antiplatelet therapy cannot be treated in primary care",
            "E. Reduce clopidogrel to alternate-day dosing for 2 weeks before the extraction"
        ],
        "correctAnswer": "C",
        "explanation": "Patients on dual antiplatelet therapy (DAPT) after coronary stenting must continue both drugs. Stopping clopidogrel or aspirin before dental procedures risks acute in-stent thrombosis (coronary stent occlusion), which carries a mortality of approximately 30–50%. This risk significantly outweighs the risk of post-extraction haemorrhage, which is manageable with local haemostatic measures (pressure, oxidised cellulose, sutures, tranexamic acid mouthwash). Routine dental extractions can safely be performed in primary care with DAPT — refer to hospital only for complex multi-stage surgery. Always check if the patient is still within the DAPT period (bare metal stent: 1 month; drug-eluting stent: 12 months minimum) before considering any changes."
    },
    {
        "id": "t5-a20",
        "scenario": "A 73-year-old man presents with a 3-week history of progressive breathlessness, ankle swelling, and inability to lie flat. He reports his heart was 'irregular' when checked recently. His JVP is elevated, he has bilateral ankle oedema, and his heart sounds include an irregular rhythm. Which ONE of the following BEST describes his likely diagnosis and the initial investigation to confirm it?",
        "options": [
            "A. Left ventricular failure from hypertension; 12-lead ECG and chest X-ray",
            "B. Right-sided heart failure from COPD; spirometry and peak flow measurement",
            "C. Heart failure with atrial fibrillation as a likely contributing cause; 12-lead ECG and BNP measurement",
            "D. Pulmonary embolism with right heart strain; CT pulmonary angiogram",
            "E. Constrictive pericarditis; echocardiogram"
        ],
        "correctAnswer": "C",
        "explanation": "The clinical picture — progressive breathlessness, orthopnoea (cannot lie flat), bilateral ankle oedema, elevated JVP, and irregular heart rhythm — is consistent with heart failure with concurrent atrial fibrillation. AF is a common cause of worsening heart failure (rapid, uncontrolled ventricular rate reduces diastolic filling and cardiac output). The initial investigations are a 12-lead ECG (to confirm AF and look for other causes — LVH, ischaemia) and BNP/NT-proBNP (elevated in heart failure — helps confirm diagnosis). A chest X-ray (cardiomegaly, pulmonary oedema) and echocardiogram (structural assessment, EF) would follow. Spirometry would investigate respiratory causes."
    },
    {
        "id": "t5-a21",
        "scenario": "A 67-year-old man with a known abdominal aortic aneurysm (AAA) of 4.8cm, measured 3 months ago, presents for routine dental treatment. He is asymptomatic and his aneurysm is under surveillance. Which ONE of the following BEST describes the most important consideration for his dental management?",
        "options": [
            "A. He requires antibiotic prophylaxis before any dental procedure to prevent infection of the aneurysm",
            "B. Dental treatment should be deferred until after surgical repair of the AAA, as dental procedures can cause aneurysm rupture",
            "C. No specific cardiovascular modification is needed beyond standard precautions; proceed with routine dental care",
            "D. Check his INR as all AAA patients are on warfarin",
            "E. Only adrenaline-free local anaesthetic should be used as vasoconstrictors are absolutely contraindicated"
        ],
        "correctAnswer": "C",
        "explanation": "An asymptomatic AAA of 4.8cm under surveillance (repair threshold is 5.5cm) does not require specific antibiotic prophylaxis for dental procedures — there is no evidence that dental bacteraemia causes aortic aneurysm infection in the absence of an endovascular graft. Routine dental care can proceed with standard precautions. The patient may be on antiplatelet therapy (aspirin/clopidogrel) or antihypertensives — standard management applies. AAA repair is not indicated at 4.8cm, and dental procedures do not risk aneurysm rupture. Check his medication list for antiplatelets or anticoagulants, but otherwise standard care is appropriate."
    },
    {
        "id": "t5-a22",
        "scenario": "You are about to administer inferior alveolar nerve block to a 62-year-old patient with well-controlled hypertension (BP 142/88 mmHg today, on amlodipine). He asks if the adrenaline in the local anaesthetic will be dangerous given his heart condition. Which ONE of the following BEST addresses his concern?",
        "options": [
            "A. Adrenaline is absolutely contraindicated in hypertension and you will use adrenaline-free local anaesthetic only",
            "B. Adrenaline at standard dental doses (1–3 cartridges of 1:80,000 or 1:100,000) is safe in well-controlled hypertension with careful technique — the benefit of effective pain control outweighs the risk",
            "C. You will limit treatment to one cartridge of LA maximum to avoid any cardiovascular risk",
            "D. Since he takes amlodipine, there is a specific drug interaction with adrenaline that makes it dangerous",
            "E. You will switch to a general anaesthetic referral as adrenaline cannot be safely used in this patient"
        ],
        "correctAnswer": "B",
        "explanation": "Adrenaline at standard dental doses (up to 3 cartridges of 1:80,000, giving approximately 75 micrograms total) is safe in patients with mild-to-moderate, well-controlled hypertension. The amount of adrenaline in dental cartridges is physiologically small — the catecholamine surge from inadequately controlled pain or dental anxiety is far greater than the adrenaline dose in 2–3 cartridges of LA. Effective anaesthesia actually protects the heart by preventing pain-induced catecholamine release. Aspiration before injection and slow injection technique minimise the risk of inadvertent intravascular injection. Adrenaline is only relatively contraindicated in uncontrolled severe hypertension, unstable angina, or within 3 months of MI. There is no specific interaction between amlodipine and adrenaline."
    },
    {
        "id": "t5-a23",
        "scenario": "A 52-year-old woman presents with a 2-month history of sharp, tearing mid-chest pain radiating to her back between the shoulder blades. She has a history of poorly controlled hypertension. On examination, her blood pressure is 170/100 mmHg in the right arm and 150/90 mmHg in the left arm. Which ONE of the following is the MOST likely diagnosis?",
        "options": [
            "A. Stable angina — typical radiation pattern; treat with GTN and refer to cardiologist",
            "B. Aortic dissection — tearing pain, radiation to back, asymmetric blood pressures; emergency referral",
            "C. Pulmonary embolism — pleuritic chest pain with hypertension and radiation",
            "D. Musculoskeletal chest pain from poor posture — reassure and prescribe NSAIDs",
            "E. Pericarditis — sharp chest pain in hypertensive patient; treat with aspirin and colchicine"
        ],
        "correctAnswer": "B",
        "explanation": "Aortic dissection classically presents with sudden, severe, tearing or ripping pain radiating to the back or between the shoulder blades — this is distinct from the squeezing/pressure of angina. The critical diagnostic finding here is the blood pressure differential between arms (20 mmHg systolic difference), caused by dissection compromising blood flow to one subclavian artery. Hypertension is the most important risk factor (medial degeneration). This is a life-threatening emergency — immediate imaging (CT aortogram) and surgical/interventional management are required. NSAIDs and aspirin are inappropriate and dangerous. GTN for angina would not treat this condition."
    },
    {
        "id": "t5-a24",
        "scenario": "A patient with paroxysmal atrial fibrillation managed with bisoprolol and warfarin (INR 2.4) asks you about the best way to prevent infective endocarditis, as she has heard that dental treatment is a risk. She has no prosthetic valves, no previous IE, and no structural heart disease. Which ONE of the following is the MOST accurate and helpful response?",
        "options": [
            "A. She does not need any specific IE prevention as she has no structural heart disease — maintain good oral hygiene",
            "B. She should receive amoxicillin 3g one hour before every dental procedure involving bleeding",
            "C. She needs a cardiologist assessment before any dental procedure",
            "D. She should be referred to hospital for all dental procedures to reduce bacteraemia risk",
            "E. She should receive antibiotic prophylaxis for extractions but not for scaling procedures"
        ],
        "correctAnswer": "A",
        "explanation": "This patient has lone AF with no structural heart disease, no prosthetic valves, and no previous IE. She is not in any NICE or SDCEP high-risk or moderate-risk category for IE. NICE guidelines (2016) do not recommend routine antibiotic prophylaxis for dental procedures in any patient, and certainly not in someone without structural cardiac abnormalities. The most effective IE prevention strategy is to maintain excellent oral hygiene, which minimises the daily bacteraemia from toothbrushing — far more important than antibiotic prophylaxis before procedures. She should be encouraged to attend regularly, maintain meticulous oral hygiene, and be aware of IE symptoms to report promptly."
    },
    {
        "id": "t5-a25",
        "scenario": "A 71-year-old woman on digoxin 125 micrograms daily for AF and heart failure develops nausea, vomiting, and describes seeing a yellow-green tinge to everything she looks at. Her renal function has recently deteriorated (eGFR fallen from 65 to 38 mL/min). Which ONE of the following BEST describes this clinical situation?",
        "options": [
            "A. These are unrelated symptoms — continue digoxin and refer to gastroenterology for the visual disturbance",
            "B. Likely digoxin toxicity, exacerbated by reduced renal clearance; stop digoxin; measure plasma digoxin level and electrolytes; treat cardiac arrhythmias if present",
            "C. This is a normal side effect of digoxin — reduce the dose to 62.5 micrograms and continue",
            "D. Start IV furosemide to improve renal function and clear the digoxin more rapidly",
            "E. Give oral vitamin K to reverse the toxic effects of digoxin"
        ],
        "correctAnswer": "B",
        "explanation": "This patient has classic features of digoxin toxicity: GI symptoms (nausea, vomiting) and the pathognomonic visual disturbance — xanthopsia (yellow-green tinge to vision), which represents toxicity affecting the retinal cones. Digoxin is almost entirely renally excreted, and its half-life significantly prolongs when renal function deteriorates — the same dose now produces higher plasma levels. Management: stop digoxin immediately; measure plasma digoxin level (>2 ng/mL is toxic), serum potassium (hypokalaemia greatly worsens toxicity by competing with digoxin at the Na/K-ATPase pump), and other electrolytes. ECG for arrhythmias. If severe, Digibind (digoxin-specific antibody fragments) is the antidote. Vitamin K reverses warfarin — it has no role in digoxin toxicity."
    },
    {
        "id": "t5-a26",
        "scenario": "A 59-year-old man describes calf pain that reliably comes on after walking 200 metres and resolves within 5 minutes of stopping. He smokes 20 cigarettes per day. His ABPI is 0.7 in the right leg. Which ONE of the following BEST describes the correct management strategy?",
        "options": [
            "A. Urgent surgical bypass grafting — ABPI of 0.7 indicates critical ischaemia requiring immediate revascularisation",
            "B. Medical management: antiplatelet therapy (clopidogrel preferred), statin, smoking cessation, structured exercise programme, antihypertensives if needed",
            "C. Immediate below-knee amputation to prevent progression to critical ischaemia",
            "D. Start warfarin anticoagulation as PAD always requires anticoagulation",
            "E. Advise the patient to rest completely and avoid exercise to prevent progression"
        ],
        "correctAnswer": "B",
        "explanation": "This patient has intermittent claudication (moderate PAD — ABPI 0.7). The majority of claudicants are managed conservatively — the priority is reducing cardiovascular mortality (these patients die of MI, not limb loss). Medical management: clopidogrel (preferred over aspirin for PAD based on CAPRIE trial), high-intensity statin (reduces cardiovascular events and may slow PAD progression), smoking cessation (most important modifiable factor — also reduces claudication distance), antihypertensives if hypertensive, blood sugar control if diabetic. Structured supervised exercise significantly improves walking distance. Revascularisation (angioplasty or bypass) is reserved for claudication that significantly limits lifestyle and fails medical management, or critical ischaemia."
    },
    {
        "id": "t5-a27",
        "scenario": "A 64-year-old man with a history of myocardial infarction 4 months ago is taking aspirin, atorvastatin, ramipril, bisoprolol, and ticagrelor. He requires extraction of an upper left molar due to irreversible pulpitis. Which ONE of the following represents the MOST appropriate management?",
        "options": [
            "A. Defer all dental treatment for a further 2 months until 6 months post-MI have elapsed",
            "B. Proceed with extraction; do not stop either antiplatelet drug; use local haemostatic measures; morning appointment",
            "C. Stop ticagrelor 5 days before extraction and continue aspirin only",
            "D. Refer to a hospital oral surgery department as no extractions can be performed within 12 months of MI",
            "E. Administer adrenaline-free local anaesthetic as any adrenaline is absolutely contraindicated within 6 months of MI"
        ],
        "correctAnswer": "B",
        "explanation": "At 4 months post-MI the patient is within the high-risk period (elective non-urgent treatment is typically deferred for 3–6 months), but a symptomatic tooth causing pain (irreversible pulpitis) represents a necessary intervention, not elective treatment. The infection and pain from leaving the tooth untreated poses its own cardiovascular risk. The extraction should proceed with: DAPT (aspirin + ticagrelor) continued — stopping either risks acute coronary stent re-thrombosis if a stent was placed; morning appointment; effective LA; local haemostasis. Adrenaline-containing LA is not absolutely contraindicated — adequate pain control is essential for cardiovascular protection. Hospital referral is not necessary for a routine single extraction."
    },
    {
        "id": "t5-a28",
        "scenario": "A 78-year-old woman has Roth spots noted on fundoscopy, a pansystolic murmur at the apex radiating to the axilla, and has had unexplained weight loss, fever, and malaise for 4 weeks. Blood cultures from 2 sets are growing Enterococcus faecalis. Which ONE of the following BEST describes the treatment of this infection?",
        "options": [
            "A. Oral amoxicillin 500mg three times daily for 7 days",
            "B. Intravenous ampicillin plus gentamicin for 4–6 weeks (with gentamicin monitoring)",
            "C. Single-dose IV benzylpenicillin followed by oral amoxicillin for 2 weeks",
            "D. Oral clarithromycin 500mg twice daily for 2 weeks",
            "E. IV vancomycin monotherapy for 2 weeks"
        ],
        "correctAnswer": "B",
        "explanation": "Enterococcal infective endocarditis requires prolonged intravenous combination antibiotic therapy. The standard regimen is ampicillin (or penicillin) combined with gentamicin (aminoglycoside — synergistic bactericidal activity against enterococci) for 4–6 weeks. Aminoglycoside monitoring (trough and peak levels, renal function) is essential due to nephrotoxicity and ototoxicity. The bacteria embedded within vegetations are protected from host defences and require bactericidal (not just bacteriostatic) antibiotics at high concentrations for a prolonged period. Short-course oral antibiotics (A, C, D) are wholly inadequate for IE — they will fail and the patient will relapse with progressive valve destruction and potentially fatal complications."
    },
    {
        "id": "t5-a29",
        "scenario": "A 68-year-old man on warfarin (INR target 2–3 for AF) is prescribed metronidazole 400mg three times daily for a dental abscess. Three days later he attends the emergency department with a large haematoma of the floor of mouth. His INR is now 6.8. Which ONE of the following BEST explains the drug interaction?",
        "options": [
            "A. Metronidazole reduces warfarin absorption from the gut, causing an unpredictable rise in INR",
            "B. Metronidazole inhibits CYP2C9 (and has direct anticoagulant properties), reducing warfarin metabolism and dramatically raising the INR",
            "C. Metronidazole kills gut bacteria that normally produce vitamin K, resulting in the raised INR",
            "D. Metronidazole displaces warfarin from plasma proteins, temporarily raising free warfarin levels",
            "E. Metronidazole increases renal excretion of warfarin's metabolites, concentrating the active drug"
        ],
        "correctAnswer": "B",
        "explanation": "Metronidazole inhibits CYP2C9 — the major hepatic enzyme responsible for metabolising the more potent S-enantiomer of warfarin. Reduced metabolism → higher plasma warfarin levels → dramatically elevated INR. Metronidazole also inhibits CYP3A4 and has some direct anticoagulant properties. The clinical consequence can be life-threatening — INR can rise from 2 to >6 within 2–3 days of starting metronidazole. This is one of the most important and dangerous drug interactions in dental practice. Alternative antibiotics for dental infections in warfarin patients: amoxicillin (minor, predictable interaction — monitor INR), cefalexin (generally safe). If metronidazole is unavoidable: inform the patient, check INR 2–3 days after starting, and monitor closely."
    },
    {
        "id": "t5-a30",
        "scenario": "A 45-year-old woman with systemic lupus erythematosus (SLE) on hydroxychloroquine and prednisolone is found to have a BP of 165/100 mmHg at her dental appointment. She has no known cardiac history. Which ONE of the following conditions might DIRECTLY explain her elevated blood pressure?",
        "options": [
            "A. Hydroxychloroquine causes hypertension as a common side effect",
            "B. Prednisolone (corticosteroid) causes sodium and water retention, contributing to hypertension",
            "C. Systemic lupus erythematosus is not associated with cardiovascular disease",
            "D. This reading is within normal limits for a patient under dental stress",
            "E. SLE-related pericarditis is directly causing the elevated blood pressure"
        ],
        "correctAnswer": "B",
        "explanation": "Prednisolone and other corticosteroids cause sodium and water retention (via mineralocorticoid-like activity) and increase vascular sensitivity to catecholamines — both contribute to hypertension. Additionally, SLE itself is associated with accelerated atherosclerosis and cardiovascular disease (systemic inflammation, renal involvement, antiphospholipid syndrome — all contributing to hypertension and CVD risk). A BP of 165/100 mmHg is stage 2 hypertension, not a normal stress response. Hydroxychloroquine is actually associated with some cardioprotective effects in SLE. This patient should be referred to her rheumatologist/GP for BP review."
    },
    {
        "id": "t5-a31",
        "scenario": "A 77-year-old man had a stroke 10 days ago from which he has largely recovered (mild residual dysarthria). He has AF and is now on apixaban. He needs urgent treatment for a broken tooth causing pain and a developing abscess. Which ONE of the following is the MOST appropriate course of action?",
        "options": [
            "A. Defer all dental treatment for 3–6 months as for post-MI patients",
            "B. Treat the dental infection with antibiotics only; defer any extraction for 6 months",
            "C. Treat the acute dental infection (antibiotics, emergency extraction if needed); continue apixaban; use local haemostatic measures",
            "D. Stop apixaban for 5 days before any dental procedure to minimise haemorrhagic stroke risk",
            "E. Refer to hospital neurology team for clearance before any dental treatment"
        ],
        "correctAnswer": "C",
        "explanation": "An acute dental infection with pain and early abscess cannot be deferred indefinitely — untreated dental infections can spread and worsen systemic health. Unlike post-MI management where elective treatment is deferred 3–6 months, dental infections are not 'elective' — they require urgent intervention. Apixaban should be continued — stopping it within 10 days of a cardioembolic stroke (from AF) risks devastating recurrent stroke. For simple extraction: proceed with apixaban, use local haemostatic measures, treat in the morning, and monitor post-procedurally. The bleeding risk from extraction is manageable; the risk of stopping anticoagulation in a patient who just had an AF-related stroke is not."
    },
    {
        "id": "t5-a32",
        "scenario": "During a routine dental appointment, a patient mentions he was recently told he has 'second degree Mobitz type II heart block' and was referred to a cardiologist. He wants to know if he needs a pacemaker. Which ONE of the following BEST describes the significance of Mobitz type II second degree heart block?",
        "options": [
            "A. It is a benign variant of normal — no treatment needed; he can be reassured",
            "B. It is a significant finding at high risk of progressing to complete heart block; he likely needs a pacemaker",
            "C. It is caused by anxiety and will resolve when he feels calmer",
            "D. It only requires treatment if his resting heart rate falls below 40 bpm",
            "E. Treatment is with verapamil to slow the arrhythmia"
        ],
        "correctAnswer": "B",
        "explanation": "Mobitz type II second degree heart block is a significant and potentially dangerous arrhythmia. Unlike Mobitz type I (Wenckebach — benign, occurs at the AV node, often reversible), Mobitz type II occurs below the AV node at the bundle branches. Features: constant PR interval with sudden non-conducted P-waves (dropped beats). It carries a high risk of progressing unpredictably to complete (third degree) heart block with a very slow escape rhythm (<40 bpm), risk of syncope (Stokes-Adams attacks), and sudden death. A permanent pacemaker is typically indicated. Verapamil would worsen conduction block — it is contraindicated in heart block."
    },
    {
        "id": "t5-a33",
        "scenario": "A patient on warfarin for DVT has a routine INR check showing an INR of 5.8. He is currently asymptomatic with no bleeding. He has no dental procedure planned. Which ONE of the following is the MOST appropriate management?",
        "options": [
            "A. Hospitalise immediately for IV fresh frozen plasma administration",
            "B. Omit 1–2 doses of warfarin; give low-dose oral vitamin K (1–2mg); recheck INR in 1–2 days; contact GP",
            "C. Continue warfarin at the same dose — the INR will self-correct within a week",
            "D. Stop warfarin permanently and switch to a DOAC immediately",
            "E. Administer vitamin K 10mg IV immediately to fully reverse anticoagulation"
        ],
        "correctAnswer": "B",
        "explanation": "An asymptomatic elevated INR of 5.8 (without active bleeding) is managed conservatively. NICE guidelines recommend: omitting 1–2 doses of warfarin and giving low-dose oral vitamin K (1–2mg phytomenadione — this provides partial reversal without completely reversing the anticoagulation). Recheck INR in 1–2 days and adjust the maintenance dose when back in range. Contact the GP/anticoagulant clinic to investigate the reason for over-anticoagulation (dietary change, drug interaction, intercurrent illness). IV FFP or high-dose IV vitamin K (option A, E) are reserved for serious bleeding or emergency surgery — not appropriate for asymptomatic over-anticoagulation. Stopping warfarin completely risks VTE recurrence."
    },
    {
        "id": "t5-a34",
        "scenario": "A 66-year-old woman with severe aortic stenosis (valve area 0.7 cm²) and moderate LV systolic dysfunction is referred for dental treatment before TAVI. She is breathless at minimal exertion (NYHA III). Which ONE of the following represents the MOST appropriate approach to her dental care?",
        "options": [
            "A. Defer all dental treatment until after TAVI — no dental procedures are safe in severe aortic stenosis",
            "B. Provide necessary dental treatment before TAVI with an appropriate clinical setting; semi-reclined position; effective LA; minimal adrenaline; short morning appointments",
            "C. Treat her in the fully supine position to maximise cardiac output during procedures",
            "D. Refer to a hospital dental service but insist on GA for all procedures to ensure comfort",
            "E. No special modifications are needed — treat exactly as a healthy patient"
        ],
        "correctAnswer": "B",
        "explanation": "Dental clearance before TAVI (transcatheter aortic valve implantation) is important — active dental infection post-TAVI in the presence of prosthetic valve material significantly increases IE risk. Necessary dental treatment should be completed pre-TAVI. Modifications: semi-reclined or upright position (reduced cardiac output means supine position is poorly tolerated and may cause syncope — fixed cardiac output syndrome); effective LA to minimise catecholamine surge from pain; minimal adrenaline in context of severe AS (avoid exacerbating LVOTO or arrhythmia); short morning appointments; BP and SpO2 monitoring; emergency GTN and AED available; consideration of hospital setting if complex. Completely deferring dental treatment (A) risks untreated infection becoming a source of post-TAVI bacteraemia and IE."
    },
    {
        "id": "t5-a35",
        "scenario": "A 55-year-old man is prescribed clarithromycin 500mg twice daily by his dentist for a dental abscess. He is known to take simvastatin 40mg at night for hypercholesterolaemia. Three days later he develops severe bilateral thigh and calf muscle pain and passes dark (tea-coloured) urine. Which ONE of the following BEST explains this complication?",
        "options": [
            "A. Clarithromycin causes myalgia directly as a common side effect; this will resolve when the antibiotic is stopped",
            "B. Clarithromycin inhibits CYP3A4, dramatically increasing simvastatin plasma levels, causing rhabdomyolysis",
            "C. Dark urine is caused by clarithromycin discolouring the urine — this is a benign side effect",
            "D. The patient is having an allergic reaction to clarithromycin — prescribe antihistamine and continue the antibiotic",
            "E. Clarithromycin and simvastatin both cause gout, resulting in muscle symptoms"
        ],
        "correctAnswer": "B",
        "explanation": "Clarithromycin is a potent inhibitor of CYP3A4, the hepatic enzyme responsible for metabolising simvastatin and lovastatin (both 'simvastatin-class' statins). Inhibiting CYP3A4 dramatically raises plasma simvastatin levels → myopathy progressing to rhabdomyolysis (breakdown of skeletal muscle). Dark urine (tea or cola-coloured) is caused by myoglobinuria from muscle breakdown — a sign of rhabdomyolysis. This can cause acute kidney injury and is potentially fatal. Management: stop both drugs immediately; vigorous IV fluid hydration to prevent renal tubular obstruction; monitor CK levels, renal function, potassium. Prevention: prescribe azithromycin (a safer alternative) or amoxicillin instead of clarithromycin in statin patients. Atorvastatin is metabolised differently and is less affected."
    },
    {
        "id": "t5-a36",
        "scenario": "A 61-year-old man with hypertension is taking ramipril 10mg. He reports a persistent dry cough for the past 3 months. The cough is worse at night and is described as tickling/irritating. There are no other respiratory symptoms, and a chest X-ray is normal. Which ONE of the following is the MOST appropriate management?",
        "options": [
            "A. Prescribe codeine linctus for the cough and continue ramipril",
            "B. The cough is caused by ramipril (ACE inhibitor) — switch to an ARB (e.g. losartan) in consultation with the GP",
            "C. Start a course of antibiotics for probable respiratory tract infection",
            "D. Refer to respiratory medicine for bronchoscopy to exclude lung malignancy",
            "E. Add a low-dose beta-blocker to counteract the cough side effect of ramipril"
        ],
        "correctAnswer": "B",
        "explanation": "A persistent dry cough in a patient taking an ACE inhibitor is a classic and very common side effect — affecting 10–15% of users, more common in women and patients of East Asian ethnicity. The mechanism is bradykinin accumulation (ACE inhibitors prevent bradykinin degradation → bradykinin irritates bronchial mucosa). The cough resolves completely within 1–4 weeks of stopping the drug. The correct management is to switch to an ARB (e.g. losartan, candesartan), which provides equivalent antihypertensive efficacy without the cough (ARBs do not affect bradykinin metabolism). This decision is made in consultation with the GP. Codeine cough suppressants, antibiotics, and bronchoscopy would miss the diagnosis and subject the patient to unnecessary medication and investigation."
    },
    {
        "id": "t5-a37",
        "scenario": "A 69-year-old man with chronic atrial fibrillation on warfarin (INR 2.3) requires a course of metronidazole for acute necrotising ulcerative gingivitis. He is in significant pain. Which ONE of the following represents the MOST appropriate management?",
        "options": [
            "A. Prescribe metronidazole as planned — the drug interaction with warfarin is a theoretical risk only and rarely clinically significant",
            "B. Prescribe metronidazole but double the warfarin dose simultaneously to prevent the INR from falling",
            "C. Avoid metronidazole; use mechanical debridement and oral hygiene instruction; prescribe amoxicillin if systemic treatment is required; inform the patient's GP",
            "D. Stop warfarin for the duration of the metronidazole course to avoid the drug interaction",
            "E. Refer immediately to hospital as this combination is always fatal"
        ],
        "correctAnswer": "C",
        "explanation": "Metronidazole should be avoided in patients on warfarin wherever possible, because it significantly raises the INR by inhibiting CYP2C9 — the enzyme metabolising warfarin — creating serious bleeding risk. For acute necrotising ulcerative gingivitis (ANUG), first-line management is intensive mechanical debridement and oral hygiene instruction. If systemic antibiotic treatment is deemed necessary, amoxicillin is the safer choice (minor, predictable interaction with warfarin). The patient's GP should be informed of any antibiotic prescribed so INR can be monitored. Stopping warfarin (option D) risks stroke from AF — never stop anticoagulation without haematologist/cardiologist input. The interaction is well-documented and clinically significant — not merely theoretical."
    },
    {
        "id": "t5-a38",
        "scenario": "A 73-year-old woman has an INR of 3.1 on warfarin for a mechanical aortic valve. She requires surgical debridement of a peri-implant abscess with elevation of a mucoperiosteal flap. Which ONE of the following is the MOST appropriate management?",
        "options": [
            "A. Proceed in primary care — INR 3.1 is within the safe threshold of ≤4 and local haemostatic measures are sufficient",
            "B. Ask the GP to reduce the warfarin dose to bring INR below 2.0 before proceeding",
            "C. Refer to hospital oral and maxillofacial surgery for the procedure — complex flap surgery with elevated INR warrants specialist-supported environment",
            "D. Stop warfarin 5 days preoperatively, perform the procedure, then restart warfarin",
            "E. Administer protamine sulphate to reverse the warfarin immediately before the procedure"
        ],
        "correctAnswer": "C",
        "explanation": "For routine simple extractions (1–3 teeth), an INR ≤4.0 with local haemostatic measures is safe in primary care. However, a flap procedure (elevation of mucoperiosteal flap for surgical debridement) is more extensive — it involves incisions, retraction, bone exposure, and greater surgical bleeding risk. In a patient with an INR of 3.1 on a mechanical valve (where stopping warfarin carries high thromboembolism risk), this procedure is best performed in a hospital/specialist setting where transfusion support, surgical haemostasis, and anaesthetic support are available if needed. Stopping warfarin for a mechanical valve patient risks valve thrombosis. Protamine sulphate reverses heparin, not warfarin. Reducing warfarin to INR <2.0 would risk valve thromboembolism."
    },
    {
        "id": "t5-a39",
        "scenario": "A patient with known severe COPD and right-sided heart failure (cor pulmonale) attends for multiple dental extractions. He uses inhalers and his SpO2 is 90% on room air. Which ONE of the following considerations is MOST important during his dental management?",
        "options": [
            "A. Administer high-flow oxygen at 15L/min during the procedure to maintain saturations above 95%",
            "B. Use controlled low-flow oxygen only if saturations fall below 88%; semi-reclined position; monitor SpO2 throughout",
            "C. Avoid all supplemental oxygen as it is absolutely contraindicated in COPD",
            "D. Proceed without any oxygen monitoring as COPD does not affect dental anaesthetic management",
            "E. Prescribe a short course of prednisolone before the appointment to reduce airway inflammation"
        ],
        "correctAnswer": "B",
        "explanation": "In severe COPD with CO2 retention, high-flow oxygen can suppress the hypoxic respiratory drive and cause respiratory depression ('type 2 respiratory failure'). Controlled, low-flow supplemental oxygen (2–4L/min via nasal cannula or a Venturi mask delivering 24–28% FiO2) can be given to maintain SpO2 88–92% — the appropriate target range for COPD. High-flow oxygen (15L/min via non-rebreathe mask) risks hypercapnia and respiratory arrest in this patient. SpO2 monitoring is essential throughout. The patient has cor pulmonale — he should be treated in a semi-reclined position (not supine) to avoid worsening dyspnoea and right heart strain. Short courses of prednisolone require steroid cover consideration if the dose is significant."
    },
    {
        "id": "t5-a40",
        "scenario": "A 58-year-old man is taking atenolol for hypertension. He develops a white, bilateral reticulate pattern on his buccal mucosae that has been present for 4 months. Biopsy shows a band-like lymphocytic infiltrate at the basement membrane zone. Which ONE of the following is the MOST appropriate management?",
        "options": [
            "A. Diagnose as oral lichen planus — start topical corticosteroids and discharge",
            "B. Diagnose as a atenolol-induced lichenoid reaction — liaise with GP about substituting atenolol with a non-beta-blocker antihypertensive; topical corticosteroids for symptomatic relief if needed",
            "C. Diagnose as erythema multiforme — refer urgently to dermatology",
            "D. Diagnose as candidosis — prescribe nystatin suspension",
            "E. Immediately biopsy a second site and refer to oral medicine as a suspected premalignant lesion"
        ],
        "correctAnswer": "B",
        "explanation": "Lichenoid drug reactions are clinically and histologically indistinguishable from idiopathic oral lichen planus — both show a band-like lymphocytic infiltrate at the basement membrane. The key clue is the medication history: atenolol (beta-blocker) is one of the most common causes of oral lichenoid reactions. Other common culprits: thiazide diuretics, ACE inhibitors, NSAIDs, oral hypoglycaemics, and statins. Management: liaise with GP about substituting atenolol — resolution of the lesion after drug cessation confirms the drug as the cause. This distinction from true OLP is clinically important as lichenoid reactions resolve with drug withdrawal. Topical corticosteroids provide symptomatic relief in the interim. The lesion does not require urgent referral for suspected malignancy in this context."
    },
    {
        "id": "t5-a41",
        "scenario": "A 77-year-old woman is on warfarin (INR 2.2) for permanent atrial fibrillation. She also takes atorvastatin, ramipril, and bisoprolol. She develops a denture-related candidal stomatitis. What is the MOST appropriate antifungal treatment?",
        "options": [
            "A. Miconazole dental gel — apply to the fitting surface of the denture and leave in situ",
            "B. Fluconazole 50mg daily for 14 days",
            "C. Nystatin pastilles 100,000 units — dissolve one in the mouth four times daily after meals for 14 days",
            "D. Itraconazole 200mg daily for 7 days",
            "E. Amphotericin B lozenges — dissolve slowly in mouth four times daily for 14 days"
        ],
        "correctAnswer": "C",
        "explanation": "In a patient on warfarin, nystatin is the safe antifungal choice. Nystatin is not systemically absorbed and does not inhibit CYP enzymes — no interaction with warfarin. All azole antifungals (miconazole, fluconazole, itraconazole, ketoconazole, clotrimazole) inhibit CYP2C9 to varying degrees and will raise the INR dangerously. Miconazole dental gel in particular is absolutely contraindicated — even the topical/adhesive form is substantially absorbed and is one of the most dangerous drug interactions in dentistry. Amphotericin B lozenges are an alternative polyene (like nystatin) with no CYP interactions — also acceptable but less commonly used. Denture hygiene (remove at night, soak in antiseptic) must accompany antifungal treatment."
    },
    {
        "id": "t5-a42",
        "scenario": "A 52-year-old woman on enalapril (ACE inhibitor) for hypertension attends for an emergency appointment with acute onset bilateral lip and tongue swelling, which developed over 2 hours. There is no urticaria and she has not eaten any unusual food. Her tongue is markedly enlarged. Which ONE of the following is the MOST important IMMEDIATE action?",
        "options": [
            "A. Prescribe chlorphenamine 4mg orally and review in 24 hours",
            "B. Assess and protect the airway; call 999; administer IM adrenaline 500 micrograms if airway is compromised; stop enalapril permanently",
            "C. Prescribe prednisolone 40mg orally and advise to attend A&E if symptoms worsen",
            "D. Perform an allergy skin prick test to identify the cause before administering any treatment",
            "E. Administer IV icatibant (bradykinin receptor antagonist) as the first-line treatment in the dental surgery"
        ],
        "correctAnswer": "B",
        "explanation": "ACE inhibitor-induced angioedema with tongue involvement is a potentially life-threatening airway emergency. The tongue swelling can progress rapidly and obstruct the airway completely. Immediate priorities: assess airway and be prepared for emergency management; call 999; if airway compromise is present, administer IM adrenaline 500 micrograms (1:1000) into the anterolateral thigh. Unlike histamine-mediated (IgE-mediated) angioedema, bradykinin-mediated ACE inhibitor angioedema responds less reliably to antihistamines and steroids — but these are still given as part of management. Enalapril must be stopped permanently. Icatibant (bradykinin B2 receptor antagonist) is a specific treatment but not available in dental surgeries. The patient needs hospital emergency management."
    },
    {
        "id": "t5-a43",
        "scenario": "A 63-year-old man who suffered a subarachnoid haemorrhage (SAH) 3 weeks ago is now recovering and needs treatment for dental pain. He was taking aspirin 75mg pre-SAH. This was stopped at the time of the SAH. His neurosurgeon has not yet provided guidance on restarting antiplatelets. Which ONE of the following BEST describes the approach to prescribing analgesia for this patient?",
        "options": [
            "A. Prescribe ibuprofen 400mg three times daily — NSAIDs are safe after SAH",
            "B. Prescribe aspirin 600mg as a single analgesic dose — this will also treat the dental pain and help prevent recurrent SAH",
            "C. Prescribe paracetamol 1g up to four times daily as the safest analgesic; avoid NSAIDs and aspirin",
            "D. Prescribe diclofenac 75mg twice daily as it has better anti-inflammatory properties needed for dental pain",
            "E. Avoid all analgesics and advise rest until neurosurgery clearance is obtained"
        ],
        "correctAnswer": "C",
        "explanation": "After subarachnoid haemorrhage, NSAIDs and aspirin are contraindicated because: (1) they inhibit platelet function, worsening bleeding risk; (2) NSAIDs can worsen renal function and raise intracranial pressure; (3) aspirin reinitiation after SAH requires careful specialist input. Paracetamol is the safest analgesic in this scenario — it has no antiplatelet or anti-inflammatory effects on the vasculature and does not affect coagulation at standard doses. Up to 4g/day in divided doses is safe in normal hepatic function. Dental pain causing significant distress can be treated with paracetamol while awaiting neurosurgeon guidance regarding long-term antiplatelet management."
    },
    {
        "id": "t5-a44",
        "scenario": "A 70-year-old man with peripheral arterial disease and intermittent claudication is on clopidogrel and a statin. He develops an acute dental infection (periapical abscess) requiring extraction. Which ONE of the following BEST describes the management of his antiplatelet therapy?",
        "options": [
            "A. Stop clopidogrel 7 days before the extraction to ensure normal platelet function",
            "B. Continue clopidogrel; perform the extraction with local haemostatic measures; do not alter antiplatelet therapy",
            "C. Switch clopidogrel to aspirin 75mg for the week of the procedure",
            "D. Refer to vascular surgery for clearance before any dental extraction",
            "E. Only extract under general anaesthetic in hospital as clopidogrel makes primary care extraction too dangerous"
        ],
        "correctAnswer": "B",
        "explanation": "Clopidogrel for peripheral arterial disease (PAD) should not be stopped before dental extractions. Antiplatelet therapy significantly reduces the risk of major adverse cardiovascular events (MI, stroke) in PAD patients — stopping it risks acute arterial thrombosis. Local haemostatic measures (pressure, oxidised cellulose, sutures, tranexamic acid mouthwash) are sufficient to manage post-extraction bleeding. The increased bleeding from clopidogrel is manageable locally. PAD patients do not require vascular surgery clearance for dental procedures unless there are specific concerns. Routine extractions can be safely performed in primary care in patients on clopidogrel monotherapy."
    },
    {
        "id": "t5-a45",
        "scenario": "A 61-year-old woman's notes show she had rheumatic fever as a child and has a moderate mitral regurgitation on her last echocardiogram. She is about to undergo a routine scale and polish. She asks if she needs antibiotics to prevent endocarditis. Which ONE of the following is the MOST accurate response under current UK guidelines?",
        "options": [
            "A. Yes — amoxicillin 3g orally 1 hour before is required for all valvular disease patients",
            "B. No — NICE does not routinely recommend antibiotic prophylaxis for any patient before dental procedures, including those with valvular disease",
            "C. Yes — but only for invasive procedures such as extractions, not for scale and polish",
            "D. Only if she has previously had infective endocarditis",
            "E. Yes — clindamycin 600mg is required as penicillin allergy is likely in rheumatic fever patients"
        ],
        "correctAnswer": "B",
        "explanation": "NICE guidelines (updated 2016) clearly state that antibiotic prophylaxis for IE is NOT routinely recommended before dental procedures for any patient — including those with valvular heart disease such as mitral regurgitation from rheumatic fever. SDCEP categorises her as 'moderate risk' (native valve disease from rheumatic fever) but still does not recommend routine prophylaxis for this group. The evidence does not support prophylaxis reducing IE incidence, and the risk of antibiotic adverse effects (including anaphylaxis) may outweigh any benefit. The most important message to give her is to maintain excellent oral hygiene, attend regularly, and seek prompt medical attention if she develops unexplained fever, sweats, or malaise."
    },
    {
        "id": "t5-a46",
        "scenario": "A 55-year-old man with poorly controlled hypertension (usually 160–180/100–110 mmHg) and no other cardiac history attends for an emergency appointment with acute pulpitis. He is in severe pain. His BP today measures 175/108 mmHg. Which ONE of the following BEST describes the appropriate management?",
        "options": [
            "A. Refuse treatment and send him immediately to A&E as BP 175/108 mmHg is a hypertensive crisis",
            "B. Provide effective emergency treatment (pulpotomy or extraction) to relieve pain; use adrenaline-containing LA with standard precautions; refer to GP to optimise BP control",
            "C. Treat only with analgesics today; defer all dental treatment until BP is consistently below 140/90 mmHg",
            "D. Administer IV antihypertensive medication in the dental surgery before treating",
            "E. Use only adrenaline-free LA (prilocaine with felypressin) as any adrenaline is absolutely contraindicated at this BP"
        ],
        "correctAnswer": "B",
        "explanation": "A BP of 175/108 mmHg represents stage 2 hypertension. This is NOT a hypertensive emergency (no acute end-organ damage) — it is a hypertensive urgency. In the context of severe dental pain (which itself drives BP and catecholamine levels up), providing effective treatment is the appropriate clinical decision. Effective local anaesthesia will relieve pain, which paradoxically lowers the sympathetic-driven BP elevation. Deferring treatment without effective analgesia would leave the patient in ongoing pain — a greater cardiovascular stressor than the procedure itself. Adrenaline-containing LA at standard doses is acceptable with careful technique and aspiration. After the emergency is resolved, refer to GP for BP optimisation. IV antihypertensives have no role in the dental surgery."
    },
    {
        "id": "t5-a47",
        "scenario": "A 68-year-old man is admitted to the dental school emergency clinic with a large swelling of the left submandibular space, elevated temperature of 38.4°C, difficulty swallowing, and stridor. He mentions he had a tooth extracted at a private practice two days ago. He has a history of ischaemic heart disease on aspirin and bisoprolol. Which ONE of the following is the MOST appropriate immediate action?",
        "options": [
            "A. Prescribe oral amoxicillin 500mg three times daily and review in 48 hours",
            "B. Call 999 / transfer to hospital immediately — this is a potentially life-threatening deep space neck infection with airway compromise",
            "C. Incise and drain the abscess in the dental clinic under local anaesthetic",
            "D. Arrange an urgent OPG X-ray and panoramic assessment before any further treatment",
            "E. Prescribe IV metronidazole alone and observe for 4 hours"
        ],
        "correctAnswer": "B",
        "explanation": "Stridor (a high-pitched breathing sound from upper airway obstruction) in the context of a rapidly progressing submandibular space infection following dental extraction is a medical emergency — potentially Ludwig's angina. The airway is compromised. Immediate transfer to hospital is required — this patient needs airway control by experienced anaesthetic/ENT/maxillofacial teams (awake fibreoptic intubation, surgical tracheostomy may be required), IV broad-spectrum antibiotics, and surgical drainage under GA. Attempting incision and drainage in the dental clinic (option C) without secured airway is dangerous. Oral antibiotics (option A) are wholly inadequate for severe deep space infections. Do NOT delay transfer for investigations — stridor indicates a critically compromised airway."
    },
    {
        "id": "t5-a48",
        "scenario": "A 74-year-old woman on warfarin (INR 2.6) for AF and on amlodipine for hypertension presents with a gingival swelling over the buccal aspect of the upper right first molar, which has been slowly enlarging for 6 months. Which ONE of the following is the MOST likely aetiology?",
        "options": [
            "A. Warfarin-induced gingival haemorrhage forming an organised haematoma",
            "B. Drug-induced gingival hyperplasia from amlodipine, exacerbated by local plaque-induced inflammation",
            "C. Peripheral giant cell granuloma from trauma",
            "D. Early gingival squamous cell carcinoma requiring urgent biopsy",
            "E. Hereditary gingival fibromatosis"
        ],
        "correctAnswer": "B",
        "explanation": "Amlodipine (dihydropyridine calcium channel blocker) is the most common current cause of drug-induced gingival overgrowth, occurring in approximately 15–20% of users. The overgrowth typically affects the interdental papillae first, expanding to involve the free and attached gingiva. Local factors (plaque, poor oral hygiene) significantly worsen the severity of the overgrowth — hence the swelling localised to a specific area. Warfarin causes bleeding tendency but does not cause gingival overgrowth. Management: intensive oral hygiene instruction; periodontal referral; liaise with GP about substituting amlodipine. Biopsy may be needed to confirm the diagnosis histologically and exclude other pathology if the presentation is atypical."
    },
    {
        "id": "t5-a49",
        "scenario": "A 66-year-old man with heart failure (EF 30%) on furosemide, bisoprolol, ramipril, and spironolactone has significant dental disease requiring multiple extractions over two to three appointments. Which ONE of the following post-operative analgesics is MOST appropriate?",
        "options": [
            "A. Ibuprofen 400mg three times daily for 5 days",
            "B. Naproxen 500mg twice daily for 5 days",
            "C. Paracetamol 1g four times daily for 3–5 days as required",
            "D. Aspirin 600mg four times daily for 5 days",
            "E. Diclofenac 50mg three times daily for 5 days"
        ],
        "correctAnswer": "C",
        "explanation": "All NSAIDs (ibuprofen, naproxen, diclofenac, aspirin at anti-inflammatory doses) are contraindicated in heart failure for multiple reasons: (1) they cause sodium and water retention by inhibiting prostaglandin-mediated renal vasodilation, worsening fluid overload and oedema; (2) they reduce the effect of ACE inhibitors, diuretics, and other heart failure medications; (3) the 'triple whammy' combination of ACE inhibitor + diuretic + NSAID can cause acute renal failure; (4) NSAIDs increase cardiovascular event risk independently. Paracetamol (acetaminophen) at up to 4g/day in divided doses is the only safe analgesic in heart failure. It has no cardiovascular or renal effects at standard doses. Codeine or dihydrocodeine can be added if paracetamol alone is insufficient."
    },
    {
        "id": "t5-a50",
        "scenario": "A 72-year-old man describes that when he sits up after lying in the dental chair for a prolonged appointment, he feels light-headed and nearly faints. He is on doxazosin (alpha-blocker), amlodipine, and lisinopril for hypertension. Which ONE of the following BEST explains this episode and the most appropriate preventive measure?",
        "options": [
            "A. Vasovagal syncope from dental anxiety — premedicate with oral diazepam before future appointments",
            "B. Orthostatic hypotension from his antihypertensive medications — tilt the chair slowly to upright; allow him to sit for 2 minutes before standing",
            "C. Carotid sinus hypersensitivity — avoid turning his head during dental procedures",
            "D. Hypoglycaemia — advise him to eat before dental appointments",
            "E. Cardiac arrhythmia — arrange 24-hour Holter monitor before future dental treatment"
        ],
        "correctAnswer": "B",
        "explanation": "Orthostatic (postural) hypotension is the most likely explanation — a fall in BP on moving from supine to upright. This is a recognised side effect of several of his medications: doxazosin (alpha-1 blocker — prevents compensatory vasoconstriction on standing; causes 'first-dose hypotension'), amlodipine (vasodilator), and lisinopril (ACE inhibitor — reduces SVR). The combination of three antihypertensive agents significantly increases this risk. Prevention: tilt the dental chair slowly from supine to seated; allow the patient to sit in the upright position for at least 1–2 minutes before standing; warn the patient; assist with standing. Advise the patient to mention this to their GP — medication review may reduce the number or doses of antihypertensives."
    }
]

data['applyIt'].extend(new_apply)

# New writeIt items w3-w20
new_write = [
    {
        "id": "t5-w3",
        "prompt": "A 65-year-old man on warfarin for atrial fibrillation (INR 2.7) requires three simple dental extractions. Outline your complete management plan, covering: assessment, haemostatic measures, drug considerations, and post-operative instructions.",
        "totalMarks": 10,
        "markScheme": [
            {"point": "Check INR within 72 hours pre-procedure (ideally on the day); confirm INR ≤4.0 before proceeding", "marks": 1},
            {"point": "Do NOT stop warfarin — risk of thromboembolic stroke/AF-related embolism far exceeds risk of controlled dental haemorrhage", "marks": 1},
            {"point": "Avoid NSAIDs, COX-2 inhibitors, and aspirin as analgesics (further impair haemostasis)", "marks": 1},
            {"point": "Avoid metronidazole and azole antifungals (raise INR) — use amoxicillin or cefalexin if antibiotics needed", "marks": 1},
            {"point": "Use atraumatic surgical technique; achieve primary closure with sutures (resorbable)", "marks": 1},
            {"point": "Apply local haemostatic agents: oxidised cellulose (Surgicel), gelatin sponge (Gelfoam), or resorbable collagen in socket", "marks": 1},
            {"point": "Prescribe tranexamic acid 5% mouthwash — 10mL, hold in mouth for 2 minutes, four times daily for 2 days post-operatively", "marks": 1},
            {"point": "Paracetamol as first-line analgesia post-operatively", "marks": 1},
            {"point": "Post-operative instructions: bite on gauze for 30 minutes; avoid hot food/drink for 24 hours; avoid vigorous rinsing; return immediately if uncontrolled bleeding", "marks": 1},
            {"point": "Follow up within 24–48 hours if any concerns; document INR value, date checked, and haemostatic measures used in notes", "marks": 1}
        ]
    },
    {
        "id": "t5-w4",
        "prompt": "Describe the pathogenesis, clinical features, and dental management of infective endocarditis. Your answer should include the NICE guideline position on antibiotic prophylaxis.",
        "totalMarks": 12,
        "markScheme": [
            {"point": "Pathogenesis: bacteraemia deposits bacteria on damaged/irregular valve surface; platelet–fibrin matrix forms; bacteria embed within — vegetation", "marks": 1},
            {"point": "Most commonly affects left heart valves (mitral and aortic — 95%); right-sided IE in IV drug users (tricuspid)", "marks": 1},
            {"point": "Most common organisms: oral streptococci (pre-existing valve disease); Staphylococcus aureus (normal valves/acute IE; higher mortality)", "marks": 1},
            {"point": "HACEK organisms: Haemophilus, Aggregatibacter, Cardiobacterium, Eikenella, Kingella — 5% of IE cases", "marks": 1},
            {"point": "Clinical features: fever (most common), malaise, weight loss, night sweats, anaemia, splenomegaly", "marks": 1},
            {"point": "Peripheral signs: Osler's nodes (painful finger/toe nodules), Janeway lesions (painless palmar/plantar macules), splinter haemorrhages (>8 significant), Roth spots (retinal haemorrhages), petechiae", "marks": 2},
            {"point": "Duke criteria: definite IE = 2 major OR 1 major + 3 minor OR 5 minor criteria; major = positive blood cultures with typical organisms + echographic evidence of endocardial involvement", "marks": 1},
            {"point": "NICE guideline (2016): antibiotic prophylaxis NOT routinely recommended for any dental procedure — evidence insufficient and cumulative bacteraemia from daily toothbrushing exceeds procedural risk", "marks": 2},
            {"point": "Most important prevention: excellent oral hygiene; regular dental attendance; advise high-risk patients (previous IE, prosthetic valves) to report fever/malaise promptly", "marks": 1},
            {"point": "Advise high-risk patients: avoid body piercing/tattooing; carry IE alert card; maintain scrupulous oral hygiene", "marks": 1}
        ]
    },
    {
        "id": "t5-w5",
        "prompt": "A patient on antihypertensive medication presents with gingival enlargement. Describe the drugs associated with gingival overgrowth, the mechanism, and your management approach.",
        "totalMarks": 8,
        "markScheme": [
            {"point": "Three main drug classes: calcium channel blockers (especially dihydropyridines — nifedipine most common, amlodipine less severe); ciclosporin (immunosuppressant); phenytoin (anti-epileptic)", "marks": 2},
            {"point": "Mechanism: increased fibroblast collagen synthesis; reduced collagen degradation; altered fibroblast responsiveness to inflammatory mediators; local plaque exacerbates severity", "marks": 1},
            {"point": "Clinical features: starts interdentally; firm, nodular overgrowth; pale pink, non-bleeding if good OH; more severe anteriorly; may cover crowns in severe cases", "marks": 1},
            {"point": "Management: intensive oral hygiene instruction (reduces severity and recurrence post-surgery)", "marks": 1},
            {"point": "Refer to periodontist for specialist periodontal therapy and monitoring", "marks": 1},
            {"point": "Liaise with GP/specialist about possible drug substitution (e.g. switch from nifedipine to amlodipine or to a different antihypertensive class — some improvement but may not fully resolve)", "marks": 1},
            {"point": "Surgical gingivectomy or periodontal flap surgery as last resort if overgrowth causes functional or aesthetic problems — warn that overgrowth will recur if drug continues and OH is not maintained", "marks": 1}
        ]
    },
    {
        "id": "t5-w6",
        "prompt": "Describe the ABCD drug framework for hypertension management. Include mechanisms of action, which patient groups receive which drugs first-line, and the combination to avoid.",
        "totalMarks": 10,
        "markScheme": [
            {"point": "A — ACE inhibitors (lisinopril, ramipril) or ARBs (losartan): inhibit RAAS; reduce angiotensin II; reduce aldosterone; vasodilate; reduce Na+/water retention", "marks": 1},
            {"point": "B — Beta-blockers (atenolol, bisoprolol): reduce heart rate and contractility; reduce renin release; less effective antihypertensives than A/C/D in primary hypertension; used for specific indications (heart failure, post-MI, AF)", "marks": 1},
            {"point": "C — Calcium channel blockers (amlodipine — dihydropyridine; verapamil/diltiazem — rate-limiting): peripheral vasodilation (dihydropyridines); slow SA/AV node conduction (non-dihydropyridines)", "marks": 1},
            {"point": "D — Diuretics (indapamide — thiazide-like; bendroflumethiazide): reduce blood volume; increase Na+/water excretion; may increase blood glucose and uric acid", "marks": 1},
            {"point": "Under 55 years, non-African/Caribbean: start with A; add C; then add D; then add alpha-blocker (doxazosin) or aldosterone antagonist (spironolactone)", "marks": 1},
            {"point": "Over 55 years or African/Caribbean origin: start with C; add A; then add D (C preferred first as lower renin levels mean less RAAS activity to block)", "marks": 1},
            {"point": "AVOID B+D combination: both drugs impair insulin secretion and sensitivity → significantly increased risk of new-onset type 2 diabetes mellitus", "marks": 2},
            {"point": "AVOID verapamil/diltiazem + beta-blocker: both slow AV node conduction → risk of complete heart block and cardiac arrest", "marks": 1},
            {"point": "Dental implications: ACE inhibitors → dry cough, angioedema; CCBs → gingival hyperplasia; diuretics → xerostomia; beta-blockers → lichenoid reactions, increased tooth demineralisation", "marks": 1}
        ]
    },
    {
        "id": "t5-w7",
        "prompt": "Describe the mechanism of action, monitoring, dental threshold, and drug interactions of warfarin relevant to dental practice.",
        "totalMarks": 10,
        "markScheme": [
            {"point": "Mechanism: vitamin K antagonist; inhibits vitamin K epoxide reductase; depletes active vitamin K; prevents gamma-carboxylation of factors II, VII, IX, X (and protein C, S); onset delayed 2–5 days", "marks": 2},
            {"point": "98% protein-bound; half-life 35–37 hours; extensively metabolised by CYP2C9", "marks": 1},
            {"point": "Monitoring: INR (International Normalised Ratio); normal ~1.0; therapeutic 2–3 for AF/VTE; 2.5–3.5 for mechanical valves", "marks": 1},
            {"point": "Dental threshold: INR ≤4.0 — proceed with local haemostasis; INR >4.0 — defer and contact GP; check within 72 hours pre-procedure (ideally same day)", "marks": 1},
            {"point": "Never stop warfarin for routine dental extractions — thromboembolism risk (prosthetic valve, AF) far exceeds bleeding risk", "marks": 1},
            {"point": "Dangerous interactions raising INR: miconazole (absolutely contraindicated — CYP2C9 inhibitor; use nystatin); fluconazole (CYP2C9/3A4 inhibitor); metronidazole (CYP2C9 inhibitor); erythromycin/clarithromycin", "marks": 2},
            {"point": "Analgesic: avoid NSAIDs and aspirin (impair haemostasis further); use paracetamol", "marks": 1},
            {"point": "Antibiotic: avoid metronidazole; amoxicillin is safest (minor interaction — check INR); cefalexin safe", "marks": 1}
        ]
    },
    {
        "id": "t5-w8",
        "prompt": "Outline the Vaughan Williams classification of antiarrhythmic drugs, giving the mechanism and one named drug for each class, and describe the side effects of amiodarone.",
        "totalMarks": 10,
        "markScheme": [
            {"point": "Class I — sodium channel blockers: slow conduction velocity in myocardium; three subclasses (Ia — quinidine; Ib — lidocaine; Ic — flecainide)", "marks": 2},
            {"point": "Class II — beta-blockers (e.g. atenolol, propranolol): reduce automaticity of SA node; reduce AV conduction; used for AF rate control, post-MI", "marks": 1},
            {"point": "Class III — potassium channel blockers (amiodarone, sotalol): prolong action potential duration and refractory period; prevent re-entry; used for VF, AF", "marks": 1},
            {"point": "Class IV — calcium channel blockers (verapamil, diltiazem): slow SA and AV node conduction; used for SVT, AF rate control; NEVER combine verapamil with beta-blockers", "marks": 1},
            {"point": "Amiodarone side effects — thyroid: hypo- or hyperthyroidism (contains 37% iodine; regular TFT monitoring required)", "marks": 1},
            {"point": "Amiodarone — pulmonary fibrosis: progressive breathlessness; most serious organ toxicity; requires regular CXR and pulmonary function tests", "marks": 1},
            {"point": "Amiodarone — irreversible blue-grey skin and corneal microdeposit discolouration; photosensitivity", "marks": 1},
            {"point": "Amiodarone — peripheral neuropathy, hepatitis, pro-arrhythmic (torsade de pointes), very long half-life (40–55 days)", "marks": 1},
            {"point": "Amiodarone indications: first-line for VF resuscitation; haemodynamically unstable VT; rhythm control in AF with structural heart disease", "marks": 1}
        ]
    },
    {
        "id": "t5-w9",
        "prompt": "Describe the staging of hypertension, the physiological consequences of sustained hypertension ('target organ damage'), and the lifestyle modifications that reduce blood pressure.",
        "totalMarks": 8,
        "markScheme": [
            {"point": "Stage 1: clinic BP ≥140/90 mmHg (daytime ABPM ≥135/85 mmHg); Stage 2: ≥160/100 mmHg; Severe: ≥180/110 mmHg", "marks": 1},
            {"point": "Target organ damage — heart: LV hypertrophy; diastolic dysfunction; heart failure; atrial fibrillation; accelerated coronary atherosclerosis → MI", "marks": 1},
            {"point": "Target organ damage — brain: ischaemic stroke; haemorrhagic stroke (most specifically linked); TIA; vascular dementia; hypertensive encephalopathy", "marks": 1},
            {"point": "Target organ damage — kidney: hypertensive nephrosclerosis; CKD; proteinuria; fibrinoid necrosis of arterioles (malignant hypertension)", "marks": 1},
            {"point": "Target organ damage — eyes: hypertensive retinopathy (grades I–IV); papilloedema (grade IV = emergency); arteriovenous nipping", "marks": 1},
            {"point": "Target organ damage — vessels: aortic aneurysm; aortic dissection; peripheral arterial disease", "marks": 1},
            {"point": "Lifestyle: reduce dietary salt (to <6g/day); reduce excess alcohol (≤14 units/week); increase physical activity (≥150 minutes moderate aerobic/week); lose weight (target BMI <25)", "marks": 1},
            {"point": "Lifestyle continued: DASH diet (fruits, vegetables, low-fat dairy); stop smoking; reduce caffeine intake; manage stress", "marks": 1}
        ]
    },
    {
        "id": "t5-w10",
        "prompt": "Describe the clinical presentation of a myocardial infarction, the immediate management in the dental surgery, and the long-term medical management following an MI.",
        "totalMarks": 10,
        "markScheme": [
            {"point": "Presentation: severe central crushing/squeezing chest pain; radiation to jaw, left arm, or back; associated breathlessness, sweating, nausea, vomiting, pallor", "marks": 1},
            {"point": "Key distinguishing feature: pain at rest, lasting >20 minutes, NOT relieved by GTN (or only partially relieved)", "marks": 1},
            {"point": "Immediate dental surgery management: call 999 immediately; sit patient comfortably upright", "marks": 1},
            {"point": "Aspirin 300mg chewed (not swallowed whole — faster absorption); administer to ALL suspected MI patients without aspirin allergy", "marks": 1},
            {"point": "GTN spray 2 puffs sublingually if systolic BP >90 mmHg; oxygen 15L/min via non-rebreathe mask if SpO2 <94%", "marks": 1},
            {"point": "Monitor pulse and consciousness; be prepared to commence CPR if cardiac arrest occurs; use AED for shockable rhythm (VF/pVT)", "marks": 1},
            {"point": "Long-term medical management: aspirin 75mg daily (antiplatelet) lifelong; clopidogrel/ticagrelor for 12 months (dual antiplatelet post-PCI)", "marks": 1},
            {"point": "High-intensity statin (atorvastatin 80mg) — reduce LDL; beta-blocker (reduce reinfarction risk and arrhythmia); ACE inhibitor (cardioprotective, reduce remodelling)", "marks": 1},
            {"point": "Coronary revascularisation: primary PCI (STEMI — door-to-balloon <90 min); thrombolysis if PCI unavailable within 120 min", "marks": 1},
            {"point": "Dental: defer elective treatment 3–6 months post-MI; continue antiplatelet therapy for dental procedures; avoid NSAIDs; effective LA essential", "marks": 1}
        ]
    },
    {
        "id": "t5-w11",
        "prompt": "Describe the pathophysiology, types, and management of heart failure, including both pharmacological and non-pharmacological treatments.",
        "totalMarks": 12,
        "markScheme": [
            {"point": "Heart failure definition: clinical syndrome of breathlessness, fatigue and fluid retention due to failure of the heart to maintain adequate cardiac output", "marks": 1},
            {"point": "Systolic (HFrEF, EF <40%): reduced contractility — MI/IHD most common cause; dilated cardiomyopathy, alcohol; responds to standard HF drugs", "marks": 1},
            {"point": "Diastolic (HFpEF, EF ≥50%): impaired relaxation/stiff LV — hypertension, hypertrophic cardiomyopathy; largely symptom-based management", "marks": 1},
            {"point": "Left-sided HF: pulmonary oedema; orthopnoea; PND; dyspnoea on exertion; pink frothy sputum in severe cases", "marks": 1},
            {"point": "Right-sided HF: peripheral oedema; raised JVP; hepatomegaly; ascites; fatigue", "marks": 1},
            {"point": "Neurohormonal activation: sympathetic system (tachycardia, vasoconstriction — initially compensatory, long-term harmful); RAAS (aldosterone → fluid overload, fibrosis); BNP released (counter-regulatory)", "marks": 1},
            {"point": "Pharmacological: ACE inhibitors/ARBs — improve survival; reduce preload and afterload; reduce remodelling", "marks": 1},
            {"point": "Beta-blockers (stable HF only) — improve survival; reduce sympathetic myocardial damage; start at low dose and uptitrate slowly", "marks": 1},
            {"point": "Loop diuretics (furosemide) — symptomatic relief; correct fluid overload; monitor K+ (hypokalaemia risk)", "marks": 1},
            {"point": "Spironolactone — improve survival; K+-sparing; anti-fibrotic; hyperkalaemia risk — monitor electrolytes", "marks": 1},
            {"point": "Non-pharmacological: fluid restriction (1.5–2L/day in severe cases); daily weight monitoring; sodium restriction; smoking cessation; supervised exercise programme", "marks": 1},
            {"point": "Device therapy: CRT (cardiac resynchronisation — biventricular pacing for LBBB + EF <35%); ICD (for EF <35% with sudden death risk); transplantation for end-stage refractory failure", "marks": 1}
        ]
    },
    {
        "id": "t5-w12",
        "prompt": "A patient with atrial fibrillation is started on warfarin. Explain the mechanism of AF-related stroke, how warfarin prevents it, and how you would manage this patient's dental care.",
        "totalMarks": 8,
        "markScheme": [
            {"point": "AF mechanism of stroke: loss of coordinated atrial contraction → blood pools in left atrial appendage → thrombus formation → embolism → cerebral infarction; AF-related strokes tend to be large and disabling", "marks": 2},
            {"point": "Warfarin mechanism: vitamin K antagonist; inhibits synthesis of factors II, VII, IX, X → prolongs clotting time → prevents thrombus formation in stagnant atrial blood", "marks": 1},
            {"point": "CHA2DS2-VASc score used to assess stroke risk and guide anticoagulation need (≥2 in males = anticoagulate)", "marks": 1},
            {"point": "Dental care: check INR within 72 hours pre-procedure; proceed if ≤4.0; do not stop warfarin", "marks": 1},
            {"point": "Avoid: metronidazole (raises INR dramatically); miconazole/fluconazole (raise INR — use nystatin); NSAIDs (impair haemostasis)", "marks": 1},
            {"point": "Use local haemostatic measures: oxidised cellulose, sutures, tranexamic acid 5% mouthwash four times daily for 2 days", "marks": 1},
            {"point": "Analgesia: paracetamol first-line; codeine second-line; never NSAIDs or high-dose aspirin", "marks": 1}
        ]
    },
    {
        "id": "t5-w13",
        "prompt": "Outline the clinical features, investigations, and immediate management of a massive pulmonary embolism.",
        "totalMarks": 8,
        "markScheme": [
            {"point": "Predisposing factors: DVT (leg vein thrombus travels via IVC → right heart → pulmonary artery); immobility, surgery, malignancy, pregnancy, thrombophilia", "marks": 1},
            {"point": "Clinical features: sudden severe breathlessness (most common); pleuritic chest pain; haemoptysis; tachycardia; hypoxia; hypotension (massive PE); leg swelling/DVT signs", "marks": 2},
            {"point": "ECG: sinus tachycardia (most common); S1Q3T3 pattern; right bundle branch block; right heart strain", "marks": 1},
            {"point": "Investigations: D-dimer (high sensitivity, low specificity — excludes if negative in low probability); CT pulmonary angiogram (CTPA) — gold standard; V/Q scan if CTPA contraindicated", "marks": 1},
            {"point": "Massive PE management: immediate systemic thrombolysis (alteplase) — if haemodynamically unstable; IV heparin anticoagulation; surgical embolectomy if thrombolysis contraindicated", "marks": 2},
            {"point": "Long-term: LMWH bridging then warfarin (INR 2–3) for minimum 3 months; DOACs preferred (rivaroxaban, apixaban); investigate underlying cause (malignancy, thrombophilia screening)", "marks": 1}
        ]
    },
    {
        "id": "t5-w14",
        "prompt": "Describe the four stages of atherosclerotic plaque formation, the concept of a 'vulnerable plaque', and the clinical consequences of plaque rupture.",
        "totalMarks": 10,
        "markScheme": [
            {"point": "Stage 1 — Endothelial dysfunction: turbulent flow at bifurcations; triggered by hypertension, hyperlipidaemia, smoking (CO) damage; increased permeability", "marks": 1},
            {"point": "Stage 2 — Fatty streak: monocytes adhere via VCAM-1; diapedesis into intima; differentiate into macrophages; engulf oxidised LDL → foam cells (characteristic histological feature)", "marks": 2},
            {"point": "Stage 3 — Fibrolipid plaque: smooth muscle cells migrate from tunica media → secrete collagen → fibrous cap; lipid core; endothelium intact; lumen narrows; cholesterol clefts form", "marks": 2},
            {"point": "Stage 4 — Complicated lesion: endothelium stripped; platelets activate → thrombus; calcification; haemorrhage into plaque; embolism; plaque fissure", "marks": 1},
            {"point": "Vulnerable plaque characteristics: large lipid pool; thin fibrous cap; many macrophages (MMP secretion degrades cap); few smooth muscle cells; prone to rupture despite less stenosis than stable plaque", "marks": 2},
            {"point": "Plaque rupture consequences: exposes lipid core → massive platelet activation → coronary thrombosis → STEMI; or partial occlusion → NSTEMI/unstable angina; cerebral plaque → stroke; femoral → acute limb ischaemia", "marks": 2}
        ]
    },
    {
        "id": "t5-w15",
        "prompt": "Describe the peripheral stigmata of infective endocarditis. For each, explain what structure is affected and the underlying mechanism.",
        "totalMarks": 10,
        "markScheme": [
            {"point": "Osler's nodes: painful raised purplish nodules on finger/toe pulps; mechanism: immune complex deposition (type III hypersensitivity) in capillaries of digit pulps; minor Duke criterion", "marks": 2},
            {"point": "Janeway lesions: painless erythematous haemorrhagic macules on palms and soles; mechanism: septic microemboli or immune complex vasculitis; non-tender (contrast with Osler's)", "marks": 2},
            {"point": "Splinter haemorrhages: linear dark streaks in nail beds running longitudinally; mechanism: septic microemboli to nail bed capillaries or immune vasculitis; >8 clinically significant; minor Duke criterion (vascular phenomena)", "marks": 2},
            {"point": "Roth spots: oval haemorrhages with pale centres on retinal examination; mechanism: septic microemboli or immune complex deposition in retinal capillaries; found on fundoscopy", "marks": 2},
            {"point": "Petechiae: small red/purple non-blanching skin lesions; mechanism: microemboli or vasculitis damaging capillaries; may appear on skin, conjunctivae, or palate; minor Duke criterion", "marks": 1},
            {"point": "Finger clubbing: painless, bulbous enlargement of distal finger phalanges; chronic IE sign; mechanism unclear — thought to involve local vascular changes", "marks": 1}
        ]
    },
    {
        "id": "t5-w16",
        "prompt": "A patient presents with calf pain that reliably comes on after walking 300 metres and resolves at rest. Describe the condition, explain the physiological basis of symptoms, outline investigations, and detail management.",
        "totalMarks": 10,
        "markScheme": [
            {"point": "Diagnosis: intermittent claudication — peripheral arterial disease (PAD); atherosclerotic narrowing of leg arteries (most commonly femoral/popliteal)", "marks": 1},
            {"point": "Physiological basis: exercise → increased metabolic demand in calf muscles → atherosclerotic artery cannot deliver sufficient blood → anaerobic metabolism → lactic acid accumulation → pain; rest → demand falls, lactate clears → pain resolves", "marks": 2},
            {"point": "History: walking distance before pain onset (claudication distance); site (calf = femoral disease; buttock/thigh = iliac disease); bilateral vs unilateral; rest pain absent (distinguishes from critical ischaemia)", "marks": 1},
            {"point": "Investigations: ABPI (ankle-brachial pressure index) by Doppler — <0.9 confirms PAD; colour duplex ultrasound; CT/MR angiography for pre-intervention planning", "marks": 2},
            {"point": "Medical management (most important — reduces cardiovascular mortality): antiplatelet (clopidogrel preferred); high-intensity statin; antihypertensive; glycaemic control in diabetes; smoking cessation (most important modifiable factor)", "marks": 2},
            {"point": "Structured supervised exercise programme — 30+ minutes walking three times weekly — improves claudication distance equivalent to angioplasty; improves cardiovascular fitness", "marks": 1},
            {"point": "Revascularisation (for lifestyle-limiting claudication failing medical management): angioplasty ± stenting; surgical bypass; reserved for significant disability", "marks": 1}
        ]
    },
    {
        "id": "t5-w17",
        "prompt": "Describe the mechanism of action, types, monitoring, and dental implications of the four main classes of direct oral anticoagulants (DOACs).",
        "totalMarks": 8,
        "markScheme": [
            {"point": "Dabigatran: direct thrombin (factor IIa) inhibitor; twice daily; 80% renal excretion — most renal-dependent; risk of GI side effects; reversal: idarucizumab", "marks": 1},
            {"point": "Rivaroxaban: direct factor Xa inhibitor; once daily (with food for AF/VTE); 33% renal excretion; reversal: andexanet alfa or 4-factor PCC", "marks": 1},
            {"point": "Apixaban: direct factor Xa inhibitor; twice daily; 27% renal excretion (safest in moderate renal impairment); reversal: andexanet alfa", "marks": 1},
            {"point": "Edoxaban: direct factor Xa inhibitor; once daily; 50% renal excretion; requires initial parenteral anticoagulation for VTE treatment", "marks": 1},
            {"point": "Advantages over warfarin: no routine monitoring; fewer drug/food interactions; predictable pharmacokinetics; similar or better efficacy and safety profile; no bridging therapy needed", "marks": 1},
            {"point": "Dental management: INR NOT applicable (DOACs do not affect INR); for routine extractions (1–3 teeth) — proceed without stopping DOAC; use local haemostatic measures", "marks": 1},
            {"point": "For complex surgery: consult prescriber; time procedure appropriately (≥12–24 hours after last dose); andexanet alfa/idarucizumab for life-threatening haemorrhage only", "marks": 1},
            {"point": "Key interactions: avoid strong P-gp inhibitors (amiodarone, verapamil raise DOAC levels); avoid strong CYP3A4 inducers (rifampicin reduces levels); renal function must be checked regularly", "marks": 1}
        ]
    },
    {
        "id": "t5-w18",
        "prompt": "Describe the clinical features, ECG findings, and management of atrial fibrillation, including both rate control and rhythm control strategies and the role of anticoagulation.",
        "totalMarks": 10,
        "markScheme": [
            {"point": "Clinical features: palpitations; breathlessness; fatigue; dizziness; reduced exercise tolerance; irregularly irregular pulse on examination; may be asymptomatic", "marks": 1},
            {"point": "Complications: stroke (5× increased risk — cardioembolic from LAA thrombus); heart failure (tachycardia-induced cardiomyopathy); systemic embolism", "marks": 1},
            {"point": "ECG: absent P-waves (replaced by fibrillatory baseline); irregularly irregular R-R intervals; narrow QRS (unless aberrant conduction/BBB)", "marks": 1},
            {"point": "Causes: hypertension (most common); ischaemic heart disease; valvular disease (especially mitral stenosis); thyrotoxicosis; COPD; alcohol; idiopathic", "marks": 1},
            {"point": "Rate control strategy: target HR <110 bpm at rest; drugs: beta-blockers (first line), digoxin (sedentary/elderly), rate-limiting CCBs (diltiazem/verapamil — not with beta-blockers)", "marks": 2},
            {"point": "Rhythm control strategy: restore sinus rhythm; flecainide (no structural heart disease); amiodarone (structural heart disease); DC cardioversion; catheter ablation (pulmonary vein isolation)", "marks": 1},
            {"point": "Anticoagulation: CHA2DS2-VASc score ≥2 in males (≥3 in females) → anticoagulate; DOACs preferred over warfarin in non-valvular AF; warfarin for mechanical valves/rheumatic MS", "marks": 2},
            {"point": "Dental: check INR (if warfarin) or continue DOAC; never stop anticoagulation for routine dental procedures; avoid metronidazole/azoles with warfarin", "marks": 1}
        ]
    },
    {
        "id": "t5-w19",
        "prompt": "A patient with hypertension is about to start a new antihypertensive. Describe the mechanism and main oral/dental adverse effects of each of the four ABCD drug classes.",
        "totalMarks": 10,
        "markScheme": [
            {"point": "ACE inhibitors (A): inhibit ACE → prevent Ang I→Ang II; reduce aldosterone; vasodilate. Dental: dry cough (10–15%); angioedema (tongue/lip — emergency; rare); burning mouth; postural hypotension on standing from chair", "marks": 2},
            {"point": "Beta-blockers (B): block beta-1/2 adrenoceptors; reduce HR and contractility; reduce renin. Dental: xerostomia (reduced salivary flow); increased tooth demineralisation; lichenoid reactions (white striae, erosions)", "marks": 2},
            {"point": "Calcium channel blockers (C — dihydropyridines): block L-type Ca2+ channels in vascular smooth muscle; vasodilate. Dental: gingival hyperplasia (nifedipine most common, amlodipine less so); xerostomia; peripheral oedema (not dental but noted at appointments)", "marks": 2},
            {"point": "Diuretics (D — thiazide-like): block Na-Cl cotransport; reduce blood volume. Dental: xerostomia (reduced salivary flow → caries risk, denture soreness); lichenoid reactions; taste disturbance (hydrochlorothiazide)", "marks": 2},
            {"point": "Additional consideration: nicorandil (not ABCD but common antianginal) → severe oral ulceration; NSAIDs interact with antihypertensives by causing sodium retention — avoid in dental analgesic prescribing", "marks": 1},
            {"point": "Clinical approach: always take drug history at first appointment; monitor for new oral changes at review appointments; report unexpected ADRs via Yellow Card scheme", "marks": 1}
        ]
    },
    {
        "id": "t5-w20",
        "prompt": "Describe the management of a patient who requires dental treatment and has a cardiac pacemaker or implantable cardioverter defibrillator (ICD). Include what dental equipment poses risk and what safety modifications are appropriate.",
        "totalMarks": 8,
        "markScheme": [
            {"point": "Pre-treatment assessment: obtain patient's device identity card (device manufacturer, model number, date of implant, programming, last check); establish if pacemaker dependent", "marks": 1},
            {"point": "Mechanism of concern: electromagnetic interference (EMI) from dental equipment can inhibit pacemaker output (causing bradycardia or asystole in pacemaker-dependent patients) or trigger ICD shock", "marks": 1},
            {"point": "Modern devices (post-2000): better shielded; bipolar sensing configurations; largely safe with most dental equipment", "marks": 1},
            {"point": "Higher-risk dental equipment: ultrasonic scalers (produce EMI at device implant site if <15cm); electrosurgery/diathermy (monopolar — high EMI; avoid; use bipolar if essential); pulp testers", "marks": 2},
            {"point": "Safe dental equipment: conventional rotary handpieces; dental suction; curing lights; X-ray units; conventional matrix bands; compressed air turbines — all generally safe", "marks": 1},
            {"point": "Modifications: if using ultrasonic scaler — keep handpiece tip >15cm from device; use manual or sonic scalers as alternative; avoid monopolar electrosurgery", "marks": 1},
            {"point": "If ICD fires: stop treatment immediately; assess patient; ensure device has returned to standby mode; arrange urgent cardiology review; document incident", "marks": 1}
        ]
    }
]

data['writeIt'].extend(new_write)

with open('data/theme-5.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"applyIt: {len(data['applyIt'])}")
print(f"writeIt: {len(data['writeIt'])}")
