import json

with open('data/theme-5.json', 'r') as f:
    data = json.load(f)

new_mock = [
    # --- CVD OVERVIEW ---
    {
        "id": "t5-m81", "theme": 5, "topicTag": "cvd-overview",
        "question": "Which ONE of the following BEST describes the Frank-Starling mechanism in the heart?",
        "options": ["A. Increased heart rate leads to proportionally increased stroke volume", "B. Greater ventricular filling (preload) leads to a stronger subsequent contraction", "C. Increased afterload always increases cardiac output in the healthy heart", "D. Sympathetic stimulation reduces end-diastolic volume to increase ejection fraction", "E. The SA node sets the rate regardless of ventricular filling pressure"],
        "correctAnswer": "B",
        "explanation": "The Frank-Starling law states that the strength of cardiac muscle contraction is proportional to the initial length of the muscle fibre (end-diastolic volume). Greater filling → increased stretch → stronger contraction → higher stroke volume. This allows the heart to match output to venous return without neural input."
    },
    {
        "id": "t5-m82", "theme": 5, "topicTag": "cvd-overview",
        "question": "Which ONE of the following is the MOST common modifiable risk factor for cardiovascular disease in the UK?",
        "options": ["A. Diabetes mellitus", "B. Smoking", "C. Hypertension", "D. Physical inactivity", "E. Hypercholesterolaemia"],
        "correctAnswer": "C",
        "explanation": "Hypertension is the most prevalent and most important modifiable cardiovascular risk factor globally and in the UK. It affects approximately 30% of adults and is a major driver of stroke, MI, heart failure, and CKD. It multiplies risk by interacting with other risk factors."
    },
    {
        "id": "t5-m83", "theme": 5, "topicTag": "cvd-overview",
        "question": "Which ONE of the following BEST describes the role of the atrioventricular (AV) node in cardiac conduction?",
        "options": ["A. It generates the primary pacemaker impulse for the heartbeat", "B. It delays conduction between atria and ventricles to allow atrial emptying before ventricular contraction", "C. It conducts impulses from Purkinje fibres back to the bundle of His", "D. It controls ventricular repolarisation and determines the QT interval", "E. It maintains the resting membrane potential of ventricular myocytes"],
        "correctAnswer": "B",
        "explanation": "The AV node introduces a critical delay (approximately 0.12s) between atrial and ventricular depolarisation. This ensures the atria complete their contraction and empty fully into the ventricles before ventricular systole begins, maximising ventricular filling and cardiac output."
    },
    {
        "id": "t5-m84", "theme": 5, "topicTag": "cvd-overview",
        "question": "Which ONE of the following values represents a NORMAL adult resting cardiac output?",
        "options": ["A. 1–2 litres per minute", "B. 3–4 litres per minute", "C. 5–6 litres per minute", "D. 8–10 litres per minute", "E. 12–15 litres per minute"],
        "correctAnswer": "C",
        "explanation": "Normal resting cardiac output in an adult is approximately 5–6 litres per minute (stroke volume ~70–80 mL × heart rate ~70 bpm). Cardiac output is maintained across a wide range of physiological demands by increasing heart rate and/or stroke volume (via sympathetic stimulation)."
    },
    {
        "id": "t5-m85", "theme": 5, "topicTag": "cvd-overview",
        "question": "A 55-year-old man is found to have a fasting LDL-cholesterol of 5.2 mmol/L on a routine blood test. Which ONE of the following is the MOST effective pharmacological treatment to reduce his cardiovascular risk?",
        "options": ["A. Fibrate (e.g. fenofibrate) — primarily lowers triglycerides", "B. Nicotinic acid — raises HDL and lowers LDL", "C. High-intensity statin (e.g. atorvastatin 80mg) — inhibits HMG-CoA reductase", "D. Ezetimibe monotherapy — inhibits intestinal cholesterol absorption", "E. Bile acid sequestrant (e.g. cholestyramine) — reduces LDL by 15%"],
        "correctAnswer": "C",
        "explanation": "High-intensity statins (atorvastatin 40–80mg, rosuvastatin 20–40mg) are the first-line pharmacological treatment for primary and secondary cardiovascular risk reduction. They inhibit HMG-CoA reductase (rate-limiting step of hepatic cholesterol synthesis), reduce LDL by 40–55%, and have proven mortality benefit in primary and secondary prevention trials."
    },
    # --- ATHEROSCLEROSIS ---
    {
        "id": "t5-m86", "theme": 5, "topicTag": "atherosclerosis",
        "question": "Which ONE of the following cell types is MOST important in the early development of an atherosclerotic fatty streak?",
        "options": ["A. Neutrophils — the first cells to arrive at sites of vascular injury", "B. T lymphocytes — orchestrate the adaptive immune response to oxidised LDL", "C. Macrophages (foam cells) — engulf oxidised LDL within the intima", "D. Mast cells — release histamine to increase vascular permeability", "E. Platelets — the primary mediators of the initial endothelial injury"],
        "correctAnswer": "C",
        "explanation": "Foam cells are the hallmark of the fatty streak. Monocytes adhere to damaged endothelium (via ICAM-1/VCAM-1), migrate into the intima, differentiate into macrophages, and engulf oxidised LDL via scavenger receptors. Lipid-laden macrophages (foam cells) accumulate to form the fatty streak — the earliest visible atherosclerotic lesion."
    },
    {
        "id": "t5-m87", "theme": 5, "topicTag": "atherosclerosis",
        "question": "Which ONE of the following BEST describes the composition of a 'vulnerable' atherosclerotic plaque that is at high risk of rupture?",
        "options": ["A. Large, densely calcified plaque with thick fibrous cap and minimal lipid core", "B. Small plaque with thin fibrous cap, large lipid pool, and high macrophage density", "C. Plaque with abundant smooth muscle cells and dense extracellular collagen matrix", "D. Plaque located at a straight vascular segment with laminar flow", "E. Old, stable plaque with a small lipid core and significant luminal narrowing"],
        "correctAnswer": "B",
        "explanation": "A vulnerable plaque has: a large necrotic lipid core (occupying >40% of plaque volume), a thin fibrous cap (<65 μm), dense macrophage infiltration (which secrete MMPs that degrade the fibrous cap), and few smooth muscle cells. Paradoxically, these plaques cause less stenosis than stable plaques but are far more likely to rupture, causing acute MI."
    },
    {
        "id": "t5-m88", "theme": 5, "topicTag": "atherosclerosis",
        "question": "Which ONE of the following mechanisms BEST explains why oxidised LDL is more atherogenic than native LDL?",
        "options": ["A. Oxidised LDL is taken up by LDL receptors on macrophages more rapidly than native LDL", "B. Oxidised LDL is recognised by scavenger receptors on macrophages without downregulation, leading to unlimited lipid accumulation", "C. Oxidised LDL directly damages cardiac myocytes causing heart failure", "D. Oxidised LDL is excreted by the kidneys more slowly, causing it to circulate longer", "E. Oxidised LDL stimulates HDL production, which paradoxically worsens vascular disease"],
        "correctAnswer": "B",
        "explanation": "Native LDL enters macrophages via LDL receptors, which downregulate when intracellular cholesterol rises (a safety mechanism). Oxidised LDL is taken up by scavenger receptors (SR-A, CD36), which are NOT subject to downregulation — macrophages continue to accumulate lipid indefinitely, becoming foam cells. This unregulated uptake drives atherogenesis."
    },
    {
        "id": "t5-m89", "theme": 5, "topicTag": "atherosclerosis",
        "question": "Which ONE of the following is the MOST typical site for atherosclerotic plaque formation within the arterial tree?",
        "options": ["A. Straight segments of large arteries where laminar flow is maintained", "B. Arterioles where blood pressure is highest", "C. Bifurcations, bends, and branch points where turbulent flow occurs", "D. The venous side of capillary beds where shear stress is lowest", "E. Pulmonary arteries, which receive the highest cardiac output"],
        "correctAnswer": "C",
        "explanation": "Atherosclerosis preferentially develops at bifurcations (carotid artery bifurcation, coronary artery ostia, aortoiliac bifurcation) and bends — sites of disturbed/turbulent flow and low oscillatory shear stress. Turbulent flow reduces the normal protective effects of laminar shear stress on endothelial cells (normal laminar shear upregulates eNOS and anti-inflammatory genes)."
    },
    {
        "id": "t5-m90", "theme": 5, "topicTag": "atherosclerosis",
        "question": "Which ONE of the following BEST describes the role of high-density lipoprotein (HDL) in cardiovascular protection?",
        "options": ["A. HDL transports dietary fats from the gut to peripheral tissues for energy use", "B. HDL mediates reverse cholesterol transport — removing cholesterol from peripheral cells and returning it to the liver for excretion", "C. HDL directly inhibits LDL oxidation by neutralising free radicals in the bloodstream", "D. HDL activates HMG-CoA reductase to reduce hepatic cholesterol synthesis", "E. HDL promotes platelet aggregation to prevent thrombosis at sites of endothelial damage"],
        "correctAnswer": "B",
        "explanation": "HDL mediates reverse cholesterol transport (RCT): it collects excess cholesterol from peripheral tissues including foam cells in atherosclerotic plaques, and transports it to the liver for excretion in bile. Higher HDL → more efficient RCT → less cholesterol accumulation in vessel walls. HDL also has antioxidant and anti-inflammatory properties."
    },
    # --- IHD / ANGINA / MI ---
    {
        "id": "t5-m91", "theme": 5, "topicTag": "ischaemic-heart-disease",
        "question": "A 60-year-old man describes central chest pain on exertion that reliably resolves within 3 minutes of rest. Which ONE of the following BEST describes the pathophysiology of his symptoms?",
        "options": ["A. Coronary artery spasm (Prinzmetal's angina) causing intermittent total coronary occlusion", "B. Fixed coronary stenosis causing supply-demand mismatch during increased myocardial oxygen demand", "C. Plaque rupture causing partial coronary occlusion at rest", "D. Microvascular disease causing global myocardial underperfusion", "E. Aortic stenosis causing reduced coronary filling pressure during systole"],
        "correctAnswer": "B",
        "explanation": "Stable angina is caused by a fixed atherosclerotic stenosis (typically >70% luminal narrowing). At rest, the residual lumen provides adequate myocardial perfusion. On exertion, myocardial oxygen demand increases (↑HR, ↑contractility, ↑wall stress) but flow cannot increase through the fixed stenosis → supply-demand mismatch → ischaemia → anginal pain, which resolves rapidly with rest as demand falls."
    },
    {
        "id": "t5-m92", "theme": 5, "topicTag": "ischaemic-heart-disease",
        "question": "Which ONE of the following ECG findings is MOST characteristic of an acute STEMI in the anterior leads (V1–V4)?",
        "options": ["A. T-wave inversion with normal ST segment — suggests NSTEMI or unstable angina", "B. ST segment elevation of >1mm with hyperacute T-waves — indicates full-thickness anterior myocardial ischaemia", "C. Pathological Q-waves without ST change — indicates old transmural MI", "D. Right bundle branch block pattern — indicates right-sided MI", "E. Prolonged QT interval — indicates electrolyte imbalance rather than ischaemia"],
        "correctAnswer": "B",
        "explanation": "Acute STEMI is characterised by ST segment elevation ≥1mm in two or more contiguous leads. Anterior STEMI (V1–V4) indicates proximal LAD occlusion. Hyperacute T-waves may precede ST elevation in the very early minutes. Pathological Q-waves develop later (hours to days) as myocardium dies. ST elevation triggers the STEMI pathway — emergency reperfusion within 90 minutes."
    },
    {
        "id": "t5-m93", "theme": 5, "topicTag": "ischaemic-heart-disease",
        "question": "Which ONE of the following is the MOST sensitive and specific biomarker for acute myocardial infarction?",
        "options": ["A. Creatine kinase (CK-MB) — rises within 4 hours and normalises by 36 hours", "B. Myoglobin — earliest to rise but non-specific; also elevated in skeletal muscle injury", "C. High-sensitivity cardiac troponin I or T (hs-cTnI/T) — highly sensitive and cardiac-specific", "D. Lactate dehydrogenase (LDH) — peaks at 3–5 days; useful for late presentation", "E. C-reactive protein (CRP) — elevated in all causes of myocardial inflammation"],
        "correctAnswer": "C",
        "explanation": "High-sensitivity cardiac troponins (hs-cTnI or hs-cTnT) are the gold standard biomarkers for AMI. They are highly specific to cardiac muscle, detectable within 1–3 hours of infarction, peak at 12–24 hours, and remain elevated for 7–14 days (allowing late diagnoses). Serial measurements (0h and 3h) with a significant rise/fall pattern confirm NSTEMI. CK-MB and myoglobin are older, less specific markers."
    },
    {
        "id": "t5-m94", "theme": 5, "topicTag": "ischaemic-heart-disease",
        "question": "A 55-year-old man presents to his dental appointment with central chest pain at rest that started 2 hours ago and was initially dismissed as indigestion. He has diaphoresis and nausea. What is the MOST appropriate immediate action?",
        "options": ["A. Give him two doses of GTN spray and wait 15 minutes to see if the pain resolves", "B. Call 999 immediately; give aspirin 300mg chewed; provide 100% oxygen via non-rebreathe mask; prepare AED", "C. Administer IM adrenaline 500 micrograms as this may represent anaphylaxis with chest involvement", "D. Take a detailed dental history and schedule him for review the following week", "E. Refer him urgently to his GP practice as a semi-emergency"],
        "correctAnswer": "B",
        "explanation": "Chest pain at rest lasting >20 minutes with diaphoresis and nausea strongly suggests acute MI. The immediate actions are: call 999; give aspirin 300mg chewed; administer 100% O2 at 15L/min if SpO2 <94%; prepare the AED and be ready for CPR. GTN may be given while waiting for the ambulance (if systolic BP >90 mmHg) but is not the priority action. IM adrenaline is for anaphylaxis — this is not the presentation here."
    },
    {
        "id": "t5-m95", "theme": 5, "topicTag": "ischaemic-heart-disease",
        "question": "Which ONE of the following BEST distinguishes NSTEMI from unstable angina?",
        "options": ["A. The presence of ST elevation on the ECG — NSTEMI shows ST elevation; unstable angina does not", "B. The severity of chest pain — NSTEMI is always more painful than unstable angina", "C. The presence of elevated cardiac troponin — NSTEMI has detectable troponin rise; unstable angina does not", "D. The coronary anatomy — NSTEMI always involves the LAD; unstable angina involves the RCA", "E. The response to GTN — NSTEMI pain does not respond to GTN; unstable angina always does"],
        "correctAnswer": "C",
        "explanation": "Both NSTEMI and unstable angina (UA) are non-ST elevation acute coronary syndromes (NSTE-ACS) caused by plaque rupture/erosion without complete coronary occlusion. The distinguishing feature is myocardial necrosis: NSTEMI involves actual myocyte death (detectable troponin rise), while UA is severe ischaemia without necrosis (troponin remains negative). Both require urgent management but NSTEMI carries a higher short-term risk."
    },
    # --- VALVULAR DISEASE & IE ---
    {
        "id": "t5-m96", "theme": 5, "topicTag": "infective-endocarditis",
        "question": "Which ONE of the following organisms is MOST commonly responsible for infective endocarditis in patients with native valve abnormalities after a dental procedure?",
        "options": ["A. Staphylococcus aureus — most common cause of acute IE overall", "B. Viridans group streptococci (e.g. Streptococcus sanguinis) — oral flora causing subacute IE", "C. Enterococcus faecalis — gut flora; typically associated with GI or GU procedures", "D. Pseudomonas aeruginosa — IV drug user-associated IE", "E. HACEK organisms — slow-growing Gram-negative bacteria typically requiring serology"],
        "correctAnswer": "B",
        "explanation": "Viridans group streptococci (S. sanguinis, S. mitis, S. oralis, S. mutans) are commensal oral bacteria that cause subacute bacterial endocarditis (SBE) on previously damaged or structurally abnormal valves. They produce dextran, which facilitates binding to platelet-fibrin matrices on damaged valves. Dental procedures cause transient bacteraemia with these organisms. Staphylococcus aureus is most common overall but typically infects normal valves (acute IE)."
    },
    {
        "id": "t5-m97", "theme": 5, "topicTag": "infective-endocarditis",
        "question": "Which ONE of the following represents a MAJOR criterion in the Duke diagnostic criteria for infective endocarditis?",
        "options": ["A. Fever >38°C", "B. Predisposing cardiac condition (e.g. bicuspid aortic valve)", "C. Positive blood cultures with a typical IE organism from two separate samples", "D. Vascular phenomena (Janeway lesions, splinter haemorrhages)", "E. Splenomegaly on examination"],
        "correctAnswer": "C",
        "explanation": "The Duke major criteria for IE are: (1) positive blood cultures — typical IE organisms (viridans streptococci, S. aureus, HACEK, Enterococcus) from two separate cultures, or persistently positive cultures, or single positive culture with Coxiella burnetii; (2) evidence of endocardial involvement on echocardiography — oscillating mass (vegetation), abscess, new dehiscence of prosthetic valve, or new valvular regurgitation. Minor criteria include fever, predisposing cardiac condition, vascular phenomena, immunological phenomena, and microbiological criteria not meeting major criteria."
    },
    {
        "id": "t5-m98", "theme": 5, "topicTag": "infective-endocarditis",
        "question": "According to NICE guidelines (2016), which ONE of the following patient groups should be considered for antibiotic prophylaxis before high-risk dental procedures, according to SDCEP guidance?",
        "options": ["A. All patients with any form of valvular heart disease", "B. Patients with a history of rheumatic fever only", "C. Patients with previous infective endocarditis, prosthetic valves, or certain congenital heart defects", "D. All patients with structural cardiac abnormalities, regardless of IE history", "E. No patients — NICE explicitly recommends against antibiotic prophylaxis for all dental procedures"],
        "correctAnswer": "C",
        "explanation": "NICE guidelines (2016) do not routinely recommend antibiotic prophylaxis for ANY dental procedure. However, SDCEP and the BCS identify patients with the highest IE risk who may benefit from prophylaxis in selected circumstances: those with prosthetic heart valves (including TAVI), history of IE, or complex congenital heart disease. Even for these, antibiotic prophylaxis is not routine — the most important intervention is optimal oral hygiene. NICE's position is that the routine use of antibiotics does more harm than good across the population."
    },
    {
        "id": "t5-m99", "theme": 5, "topicTag": "valvular-heart-disease",
        "question": "A 70-year-old man has a loud systolic murmur heard loudest at the aortic area (right 2nd intercostal space) with radiation to the carotid arteries. Echocardiography shows reduced aortic valve area and a mean gradient of 48 mmHg. Which ONE of the following is the MOST likely diagnosis?",
        "options": ["A. Mitral regurgitation — pansystolic murmur at the apex radiating to the axilla", "B. Aortic regurgitation — early diastolic murmur at the left sternal edge", "C. Severe aortic stenosis — systolic murmur radiating to carotids with reduced valve area", "D. Mitral stenosis — mid-diastolic murmur with opening snap at the apex", "E. Pulmonary stenosis — systolic murmur at the left 2nd intercostal space"],
        "correctAnswer": "C",
        "explanation": "Aortic stenosis (AS) produces an ejection systolic murmur at the aortic area (right 2nd ICS) radiating to the carotid arteries with a slow-rising pulse (pulsus parvus et tardus). Severe AS is defined by mean gradient >40 mmHg and valve area <1.0 cm². Symptoms — angina, syncope, dyspnoea — indicate severe disease and require valve replacement (surgical AVR or TAVI). 2-year mortality without intervention is approximately 50%."
    },
    {
        "id": "t5-m100", "theme": 5, "topicTag": "valvular-heart-disease",
        "question": "A 35-year-old woman with a history of rheumatic fever develops progressive dyspnoea and haemoptysis. Her ECG shows left atrial enlargement and her chest X-ray shows a double cardiac silhouette. Which ONE of the following is the MOST likely valve lesion?",
        "options": ["A. Aortic stenosis — common after rheumatic fever; causes left ventricular hypertrophy", "B. Tricuspid regurgitation — causes right atrial enlargement and peripheral oedema", "C. Mitral stenosis — rheumatic fever is the most common cause; causes left atrial enlargement and pulmonary hypertension", "D. Aortic regurgitation — causes collapsing pulse and wide pulse pressure", "E. Pulmonary regurgitation — causes right heart dilation"],
        "correctAnswer": "C",
        "explanation": "Rheumatic mitral stenosis is by far the most common cause of mitral stenosis. Chronic inflammation → fibrosis and commissural fusion of mitral valve leaflets → obstructed left atrial emptying → left atrial enlargement (double cardiac silhouette on CXR) → pulmonary venous hypertension → dyspnoea and haemoptysis (pink frothy sputum or frank haemoptysis from pulmonary venous congestion or pulmonary capillary rupture). A low-pitched mid-diastolic murmur with opening snap is heard at the apex."
    },
    # --- HEART FAILURE ---
    {
        "id": "t5-m101", "theme": 5, "topicTag": "heart-failure",
        "question": "Which ONE of the following is the MOST common cause of chronic heart failure in the UK?",
        "options": ["A. Hypertrophic obstructive cardiomyopathy (HOCM)", "B. Rheumatic valve disease leading to mitral regurgitation", "C. Ischaemic heart disease (coronary artery disease)", "D. Dilated cardiomyopathy from alcohol excess", "E. Hypertension in isolation without coronary artery disease"],
        "correctAnswer": "C",
        "explanation": "Ischaemic heart disease (IHD/CAD) is responsible for approximately 60–70% of all cases of heart failure in the UK. Myocardial infarction causes irreversible loss of functioning myocardium → reduced systolic function. Hypertension is the second most common cause (causes diastolic dysfunction, LV hypertrophy). Dilated cardiomyopathy from alcohol and HOCM are less common."
    },
    {
        "id": "t5-m102", "theme": 5, "topicTag": "heart-failure",
        "question": "Which ONE of the following symptoms is MOST characteristic of left-sided heart failure?",
        "options": ["A. Bilateral ankle and leg oedema progressing to ascites", "B. Raised JVP (jugular venous pressure) on examination", "C. Hepatomegaly with right upper quadrant discomfort", "D. Orthopnoea and paroxysmal nocturnal dyspnoea from pulmonary congestion", "E. Weight gain from fluid retention without breathlessness"],
        "correctAnswer": "D",
        "explanation": "Left-sided heart failure causes pulmonary venous hypertension. Orthopnoea (breathlessness on lying flat) results from redistribution of fluid from the peripheries into the pulmonary circulation in the supine position — the same mechanism causes paroxysmal nocturnal dyspnoea (patient wakes 1–3 hours after sleep with severe breathlessness). Options A, B, and C are features of RIGHT-sided heart failure (raised venous pressure causing peripheral oedema, raised JVP, and hepatic congestion)."
    },
    {
        "id": "t5-m103", "theme": 5, "topicTag": "heart-failure",
        "question": "Which ONE of the following drug combinations has been shown to IMPROVE MORTALITY in patients with symptomatic heart failure with reduced ejection fraction (HFrEF)?",
        "options": ["A. Loop diuretic (furosemide) + digoxin", "B. ACE inhibitor + beta-blocker + mineralocorticoid receptor antagonist (spironolactone)", "C. Calcium channel blocker (amlodipine) + nitrate + diuretic", "D. Alpha-blocker + ARB + furosemide", "E. Digoxin + ARB + fibrate"],
        "correctAnswer": "B",
        "explanation": "The mortality-reducing drugs in HFrEF (EF <40%) are: ACE inhibitors/ARBs (reduce cardiac remodelling, prevent Ang II effects), beta-blockers (reduce sympathetic myocardial damage; must be started when stable, not acutely decompensated), and spironolactone/eplerenone (MRAs reduce fibrosis and aldosterone-mediated harm). SGLT2 inhibitors (empagliflozin, dapagliflozin) are the newest addition. Furosemide relieves symptoms but does NOT reduce mortality. Digoxin reduces hospitalisation but not mortality."
    },
    {
        "id": "t5-m104", "theme": 5, "topicTag": "heart-failure",
        "question": "A 78-year-old woman with heart failure (EF 28%) is on furosemide, ramipril, bisoprolol, and spironolactone. She requires extraction of two posterior teeth. Which analgesic is MOST appropriate for post-operative pain?",
        "options": ["A. Ibuprofen 400mg three times daily for 5 days", "B. Naproxen 500mg twice daily for 5 days", "C. Diclofenac 50mg three times daily for 5 days", "D. Paracetamol 1g four times daily for 3 days as required", "E. Celecoxib 200mg daily — selective COX-2 inhibitor with less renal effect than non-selective NSAIDs"],
        "correctAnswer": "D",
        "explanation": "All NSAIDs (including COX-2 inhibitors) are contraindicated in heart failure: they cause sodium and water retention (worsening fluid overload), reduce the efficacy of ACE inhibitors and diuretics, and the 'triple whammy' combination (ACE inhibitor + diuretic + NSAID) can precipitate acute kidney injury. Paracetamol is the only safe analgesic for dental pain in heart failure patients. COX-2 inhibitors do NOT avoid the renal/cardiac effects of NSAIDs in heart failure."
    },
    {
        "id": "t5-m105", "theme": 5, "topicTag": "heart-failure",
        "question": "BNP (B-type natriuretic peptide) is released in heart failure. Which ONE of the following BEST describes its physiological role?",
        "options": ["A. BNP is a pro-inflammatory cytokine that worsens ventricular remodelling after MI", "B. BNP is released from overstretched ventricular myocardium; it causes natriuresis, vasodilation, and inhibition of RAAS — opposing the effects of fluid overload", "C. BNP directly increases heart rate and myocardial contractility as a compensatory response", "D. BNP is secreted from the liver in response to cardiac ischaemia and is a marker of hepatic damage", "E. BNP reduces pulmonary vascular resistance by inhibiting prostacyclin synthesis"],
        "correctAnswer": "B",
        "explanation": "BNP (and NT-proBNP) is released from stretched ventricular myocytes in response to pressure/volume overload. It acts as a counter-regulatory hormone opposing the RAAS and sympathetic activation: it causes natriuresis/diuresis, peripheral vasodilation, and directly inhibits renin and aldosterone secretion — all reducing preload/afterload. Plasma BNP/NT-proBNP is elevated in heart failure and is used diagnostically (excludes HF if normal) and for monitoring treatment response."
    },
    # --- CARDIAC ARRHYTHMIAS ---
    {
        "id": "t5-m106", "theme": 5, "topicTag": "cardiac-arrhythmias",
        "question": "Which ONE of the following ECG findings is DIAGNOSTIC of atrial fibrillation?",
        "options": ["A. Regular narrow complex tachycardia at 150 bpm with no visible P-waves", "B. Irregularly irregular rhythm with absent P-waves replaced by a fibrillatory baseline and variable R-R intervals", "C. Regular broad complex tachycardia with no P-waves — confirms AF with aberrant conduction", "D. Regularly irregular rhythm with dropped beats and progressive PR prolongation", "E. Narrow complex tachycardia with retrograde P-waves visible after each QRS complex"],
        "correctAnswer": "B",
        "explanation": "AF on ECG: (1) absence of organised P-waves — replaced by fibrillatory irregular baseline (350–700 impulses/min from multiple micro re-entry circuits in atria); (2) irregularly irregular ventricular response (variable R-R intervals due to random conduction through AV node); (3) typically narrow QRS unless aberrant conduction/BBB. Rate of 150 bpm regular with no P-waves suggests atrial flutter with 2:1 block. Progressive PR prolongation = Wenckebach (Mobitz I)."
    },
    {
        "id": "t5-m107", "theme": 5, "topicTag": "cardiac-arrhythmias",
        "question": "A patient collapses in the dental waiting room. The AED analyses the rhythm and announces 'Shock advised'. Which ONE of the following rhythms is the MOST likely diagnosis?",
        "options": ["A. Asystole — flat line on the monitor; AED correctly identifies this as not shockable", "B. Pulseless electrical activity (PEA) — organised ECG without cardiac output; not shockable", "C. Ventricular fibrillation (VF) — chaotic ventricular depolarisation; the primary shockable rhythm in cardiac arrest", "D. Complete heart block — regular slow rhythm without P-wave/QRS association; not shockable", "E. Sinus bradycardia at 30 bpm — AEDs shock any rhythm below 40 bpm"],
        "correctAnswer": "C",
        "explanation": "The two shockable rhythms in cardiac arrest are ventricular fibrillation (VF) and pulseless ventricular tachycardia (pVT). VF is chaotic depolarisation with no coordinated contraction — most common initial rhythm in witnessed cardiac arrest. AEDs are programmed to detect and shock VF/pVT. Non-shockable rhythms are asystole and PEA — for these, high-quality CPR, adrenaline 1mg IV, and treatment of reversible causes are the management, not defibrillation."
    },
    {
        "id": "t5-m108", "theme": 5, "topicTag": "cardiac-arrhythmias",
        "question": "A patient has supraventricular tachycardia (SVT) with a heart rate of 188 bpm. He is haemodynamically stable. Which ONE of the following is the MOST appropriate FIRST-LINE acute management?",
        "options": ["A. Immediate synchronised DC cardioversion under sedation", "B. Carotid sinus massage or Valsalva manoeuvre (vagal manoeuvres) as first-line", "C. IV amiodarone 300mg over 10 minutes", "D. Oral bisoprolol 5mg stat", "E. IV digoxin loading dose"],
        "correctAnswer": "B",
        "explanation": "For haemodynamically stable SVT (AVNRT or AVRT), the first-line intervention is vagal manoeuvres: Valsalva manoeuvre (bearing down/blowing against a closed glottis) or carotid sinus massage (unilateral, avoiding if carotid bruit present). These increase vagal tone → slow AV node conduction → may terminate re-entrant tachycardia. If vagal manoeuvres fail → IV adenosine 6mg rapid bolus (first-line pharmacological). DC cardioversion is reserved for haemodynamically unstable SVT."
    },
    {
        "id": "t5-m109", "theme": 5, "topicTag": "cardiac-arrhythmias",
        "question": "Which ONE of the following antiarrhythmic drugs is ABSOLUTELY CONTRAINDICATED in patients with second- or third-degree heart block?",
        "options": ["A. Amiodarone — it is safe in all degrees of heart block", "B. Adenosine — it is the treatment of choice for heart block", "C. Digoxin — it actually improves conduction in heart block", "D. Verapamil (a rate-limiting calcium channel blocker) — it worsens AV nodal block", "E. Flecainide — the risk in heart block is minimal as it acts on atria only"],
        "correctAnswer": "D",
        "explanation": "Verapamil and diltiazem (non-dihydropyridine calcium channel blockers) slow AV nodal conduction. In patients with second- or third-degree heart block, additional slowing of the already impaired AV node can cause complete heart block and cardiac arrest. Equally, combining verapamil with a beta-blocker is extremely dangerous and can cause fatal bradycardia/heart block. Verapamil is also contraindicated in WPW syndrome (may preferentially conduct via the accessory pathway, causing VF)."
    },
    {
        "id": "t5-m110", "theme": 5, "topicTag": "cardiac-arrhythmias",
        "question": "Which ONE of the following BEST describes the mechanism of action of adenosine in treating supraventricular tachycardia?",
        "options": ["A. It blocks sodium channels in the bundle of His, terminating re-entry circuits", "B. It activates A1 adenosine receptors → increases K+ conductance in the AV node → hyperpolarises and blocks AV nodal conduction, terminating re-entry", "C. It inhibits the Na/K-ATPase pump in atrial myocytes, increasing intracellular calcium", "D. It directly cardioverts the atria by delivering a pharmacological defibrillatory shock", "E. It activates beta-2 receptors in the AV node, increasing the refractory period"],
        "correctAnswer": "B",
        "explanation": "Adenosine binds A1 adenosine receptors on AV node cells → activates GIRK (G protein-coupled inwardly rectifying K+) channels → increased K+ efflux → hyperpolarisation of AV nodal cells → block of AV node conduction. This terminates re-entrant SVTs that depend on the AV node. Its half-life is 10–15 seconds (metabolised by erythrocytes), which limits both its effect and its adverse effects (transient flushing, dyspnoea, chest pain). It is given as a rapid IV bolus followed by a fast flush."
    },
    # --- HYPERTENSION & STROKE ---
    {
        "id": "t5-m111", "theme": 5, "topicTag": "hypertension",
        "question": "According to NICE guidelines, which ONE of the following is the recommended FIRST-LINE antihypertensive for a 45-year-old white British man with no other medical conditions?",
        "options": ["A. Calcium channel blocker (amlodipine)", "B. Thiazide-like diuretic (indapamide)", "C. ACE inhibitor (lisinopril) or ARB (losartan)", "D. Beta-blocker (atenolol)", "E. Alpha-blocker (doxazosin)"],
        "correctAnswer": "C",
        "explanation": "NICE guidelines recommend ACE inhibitors (or ARBs if ACE inhibitor is not tolerated) as first-line antihypertensives for patients under 55 years of age who are not of African or Caribbean family origin. This is because younger white patients tend to have higher-renin hypertension, which is particularly sensitive to RAAS blockade. Patients over 55 or of African/Caribbean origin start with a CCB (amlodipine)."
    },
    {
        "id": "t5-m112", "theme": 5, "topicTag": "hypertension",
        "question": "A patient's clinic blood pressure readings are consistently 150/95 mmHg over 3 visits. NICE recommends confirming this with home blood pressure monitoring (HBPM) or ambulatory blood pressure monitoring (ABPM). Which ONE of the following BEST describes the threshold for hypertension on ABPM?",
        "options": ["A. Daytime average ≥135/85 mmHg on ABPM confirms hypertension", "B. ABPM average ≥140/90 mmHg — the same threshold as clinic readings", "C. Any single reading above 130/80 mmHg on ABPM confirms hypertension", "D. 24-hour average ≥135/85 mmHg on ABPM regardless of day/night variation", "E. ABPM is not recommended — multiple clinic readings are the gold standard"],
        "correctAnswer": "A",
        "explanation": "ABPM provides daytime, night-time, and 24-hour average BP values. NICE uses a daytime ABPM average of ≥135/85 mmHg (or 24-hour average ≥130/80 mmHg) to confirm stage 1 hypertension (clinic ≥140/90). ABPM/HBPM are preferred because they eliminate 'white coat hypertension' (clinic readings artificially elevated by medical anxiety), provide more reliable data, and guide treatment decisions. True hypertension on ABPM has better prediction of cardiovascular risk than single clinic readings."
    },
    {
        "id": "t5-m113", "theme": 5, "topicTag": "hypertension-stroke",
        "question": "A 68-year-old woman with hypertension suddenly develops right-sided facial droop, arm weakness, and speech difficulty. Symptoms began 45 minutes ago and are still present. Which ONE of the following is the MOST appropriate immediate action?",
        "options": ["A. Refer her to her GP urgently for review within 24 hours", "B. Perform a CT head scan before calling the ambulance to exclude haemorrhage", "C. Call 999 immediately — this is a suspected stroke requiring thrombolysis within 4.5 hours of onset if haemorrhage excluded", "D. Give aspirin 300mg immediately and refer to neurology as an outpatient", "E. Wait 24 hours to see if symptoms resolve — it may be a TIA"],
        "correctAnswer": "C",
        "explanation": "This is a recognised stroke presentation (facial droop, arm weakness, speech difficulty = FAST positive). The time window for IV thrombolysis (alteplase) is 4.5 hours from symptom onset, but the earlier treatment is given, the better ('time is brain'). Call 999 immediately. CT head scan is required at hospital to exclude haemorrhagic stroke before giving thrombolysis — the CT must not delay the 999 call. Aspirin alone (option D) is not the first response; aspirin is given AFTER haemorrhage is excluded. Do NOT wait — symptoms that resolve within 24 hours are TIA, but you cannot know this prospectively."
    },
    {
        "id": "t5-m114", "theme": 5, "topicTag": "hypertension-stroke",
        "question": "Which ONE of the following BEST describes the pathophysiology of a hypertensive haemorrhagic stroke?",
        "options": ["A. Cardioembolic thrombus occludes the middle cerebral artery, causing ischaemic infarction", "B. Hypertension-induced lipohyalinosis and Charcot-Bouchard microaneurysm rupture in deep perforating arteries, causing intracerebral haematoma", "C. Aortic dissection propagating into the carotid arteries, causing cerebral ischaemia", "D. Paradoxical embolism through a patent foramen ovale causing cortical infarction", "E. Venous sinus thrombosis causing venous infarction with haemorrhagic transformation"],
        "correctAnswer": "B",
        "explanation": "Hypertension is the primary risk factor for haemorrhagic stroke (intracerebral haemorrhage — ICH). Chronic hypertension causes hyaline degeneration of small perforating arteries (lipohyalinosis) and formation of Charcot-Bouchard microaneurysms on the deep perforating vessels (lenticulostriate arteries, thalamoperforators). Rupture causes haematoma in deep structures (basal ganglia, thalamus, pons, cerebellum). Unlike ischaemic stroke, thrombolysis is contraindicated — BP control and neurosurgical haematoma evacuation are the treatments."
    },
    {
        "id": "t5-m115", "theme": 5, "topicTag": "hypertension",
        "question": "A 50-year-old man with hypertension and type 2 diabetes has a BP of 145/92 mmHg despite taking amlodipine 10mg. Which ONE of the following is the MOST appropriate next step according to NICE guidelines?",
        "options": ["A. Increase amlodipine to 20mg — the maximum dose has not been reached", "B. Switch amlodipine to a beta-blocker as beta-blockers are better for diabetic patients", "C. Add an ACE inhibitor (e.g. ramipril) — particularly beneficial in diabetic nephropathy", "D. Add a thiazide diuretic but avoid ACE inhibitors in type 2 diabetes", "E. Refer directly to endocrinology for blood pressure management in diabetes"],
        "correctAnswer": "C",
        "explanation": "For a diabetic patient on a CCB whose BP remains uncontrolled, the next step per NICE is to add an ACE inhibitor or ARB. ACE inhibitors have a particularly important role in diabetic patients — they are renoprotective, reducing progression of diabetic nephropathy even at modest blood pressure reductions, and they reduce cardiovascular mortality in this population. The target BP in diabetes is <140/90 mmHg (or <130/80 if microalbuminuria or renal disease). Beta-blockers can mask hypoglycaemic symptoms in insulin-treated patients — not preferred in T2DM."
    },
    # --- PERIPHERAL VASCULAR DISEASE ---
    {
        "id": "t5-m116", "theme": 5, "topicTag": "peripheral-vascular-disease",
        "question": "Which ONE of the following ABPI (ankle-brachial pressure index) values indicates CRITICAL LIMB ISCHAEMIA?",
        "options": ["A. ABPI 0.9–1.2 — normal range; no PAD", "B. ABPI 0.7–0.9 — mild PAD; may have mild claudication", "C. ABPI 0.5–0.7 — moderate PAD; intermittent claudication", "D. ABPI <0.5 — severe PAD; rest pain or critical ischaemia", "E. ABPI >1.3 — non-compressible calcified vessels; common in diabetes"],
        "correctAnswer": "D",
        "explanation": "ABPI categories: >1.2 = non-compressible vessels (calcification — common in diabetes); 0.9–1.2 = normal; 0.7–0.9 = mild PAD; 0.5–0.7 = moderate PAD (claudication); <0.5 = severe PAD — critical limb ischaemia (rest pain, tissue loss, gangrene). ABPI >1.3 indicates calcified, non-compressible tibial arteries — the ABPI is falsely elevated; toe pressures or duplex ultrasound needed for accurate assessment in these patients."
    },
    {
        "id": "t5-m117", "theme": 5, "topicTag": "peripheral-vascular-disease",
        "question": "Which ONE of the following is the MOST common site for an aortic aneurysm?",
        "options": ["A. Ascending aorta — typically associated with Marfan syndrome or syphilitic aortitis", "B. Aortic arch — associated with aortitis and giant cell arteritis", "C. Descending thoracic aorta — typically caused by hypertension", "D. Infra-renal abdominal aorta — most common site; typically atherosclerotic", "E. Iliac bifurcation — most often associated with inflammatory aortitis"],
        "correctAnswer": "D",
        "explanation": "The infrarenal abdominal aorta is the most common site for aortic aneurysm (AAA), accounting for approximately 95% of all aortic aneurysms. The infrarenal aorta is relatively deficient in vasa vasorum (adventitial blood supply), making it more susceptible to ischaemic damage to the adventitia. Risk factors: male sex, age >65, smoking (strongest modifiable risk factor), hypertension, family history. AAA is defined as aortic diameter >3.0 cm; surgery (EVAR or open repair) is recommended at >5.5 cm."
    },
    {
        "id": "t5-m118", "theme": 5, "topicTag": "peripheral-vascular-disease",
        "question": "A 58-year-old man with known peripheral arterial disease presents with a cold, pale, pulseless right leg that developed suddenly 2 hours ago. He has a history of AF. Which ONE of the following is the MOST appropriate management?",
        "options": ["A. Arrange duplex ultrasound for the following day and prescribe analgesia in the interim", "B. Urgent vascular surgical assessment — likely embolic acute limb ischaemia; immediate anticoagulation and surgical embolectomy/thrombolysis", "C. Start a compression bandage to reduce oedema and improve perfusion", "D. Prescribe antibiotics as this may represent an infected diabetic foot", "E. Apply a GTN patch to the affected limb to vasodilate the distal arteries"],
        "correctAnswer": "B",
        "explanation": "Acute limb ischaemia (ALI) is a vascular emergency. The 6 P's: Pain, Pallor, Pulselessness, Paraesthesia, Paralysis (late, with muscle necrosis), Perishing cold. With known AF, this is likely embolic ALI (cardioembolic thrombus from left atrium to peripheral artery). Time window for viable limb: approximately 6 hours. Management: IV unfractionated heparin immediately (anticoagulation); emergency vascular surgery assessment; surgical embolectomy (Fogarty catheter) or thrombolysis depending on location and viability. Irreversible ischaemia (paralysis, rigidity) → amputation."
    },
    {
        "id": "t5-m119", "theme": 5, "topicTag": "peripheral-vascular-disease",
        "question": "A 48-year-old woman has recurrent painful digital ulceration of the fingers bilaterally, precipitated by cold and stress. She describes her fingers turning white, then blue, then red. Which ONE of the following is the MOST likely diagnosis?",
        "options": ["A. Critical limb ischaemia from PAD — requires urgent ABPI assessment", "B. Raynaud's phenomenon — episodic digital vasospasm causing triphasic colour change", "C. Cellulitis — warm, erythematous skin with systemic infection", "D. Embolism from subclavian artery stenosis causing digital ischaemia", "E. Peripheral neuropathy causing cold insensitivity and impaired sensation"],
        "correctAnswer": "B",
        "explanation": "Raynaud's phenomenon is characterised by episodic digital vasospasm triggered by cold or emotional stress, causing the classic triphasic colour change: white (vasospasm → digital pallor), blue (deoxygenation → cyanosis), red (reactive hyperaemia → rubor). It can be primary (idiopathic — Raynaud's disease, young women) or secondary (associated with connective tissue disease — especially systemic sclerosis/CREST syndrome, also SLE, RA). Secondary Raynaud's tends to be more severe and can cause digital ulceration and gangrene. Treatment: keep warm; vasodilators (nifedipine); prostacyclin infusion for severe cases."
    },
    {
        "id": "t5-m120", "theme": 5, "topicTag": "peripheral-vascular-disease",
        "question": "Which ONE of the following is the SINGLE MOST important modifiable risk factor for peripheral arterial disease that should be addressed in all patients?",
        "options": ["A. Hypertension — control with antihypertensives", "B. Hypercholesterolaemia — treat with high-intensity statins", "C. Smoking — cessation is the most important single intervention", "D. Diabetes — tight glycaemic control reduces PAD progression", "E. Obesity — weight loss reduces systemic inflammation"],
        "correctAnswer": "C",
        "explanation": "Smoking is the single most important and most powerful modifiable risk factor for peripheral arterial disease. Smoking significantly accelerates atherosclerosis in the peripheral vasculature, increases blood viscosity, promotes vasoconstriction, and worsens outcomes after revascularisation. Smoking cessation reduces progression of PAD, improves claudication distance, and significantly reduces cardiovascular mortality. All other risk factors are also important and should be addressed, but smoking cessation has the greatest impact."
    },
    # --- ANTICOAGULANTS / ANTIPLATELETS ---
    {
        "id": "t5-m121", "theme": 5, "topicTag": "anticoagulants",
        "question": "A patient on warfarin has an INR of 3.8 (target 2–3). He has no current bleeding and requires an extraction tomorrow. Which ONE of the following is the MOST appropriate action?",
        "options": ["A. Postpone the extraction and prescribe oral vitamin K 5mg to lower the INR immediately", "B. Proceed with the extraction as planned — INR 3.8 is within the safe dental threshold (≤4.0)", "C. Refer to hospital dental service as the INR is above 3.0", "D. Stop warfarin and reschedule when INR is below 2.0", "E. Give IV fresh frozen plasma before proceeding with the extraction"],
        "correctAnswer": "B",
        "explanation": "The safe threshold for dental extractions in warfarin patients is INR ≤4.0. At 3.8, the INR is slightly elevated but remains within the threshold — the extraction should proceed with appropriate local haemostatic measures (pressure, sutures, oxidised cellulose, tranexamic acid 5% mouthwash). Stopping warfarin risks thromboembolism. FFP is reserved for serious haemorrhage. Vitamin K would take 12–24 hours to have effect and would swing the INR into a sub-therapeutic range, risking stroke."
    },
    {
        "id": "t5-m122", "theme": 5, "topicTag": "anticoagulants",
        "question": "Which ONE of the following mechanisms BEST explains why the combination of warfarin and metronidazole is clinically dangerous?",
        "options": ["A. Metronidazole inhibits CYP2C9, reducing warfarin metabolism and significantly raising the INR", "B. Metronidazole competes with warfarin for plasma protein binding, reducing warfarin's anticoagulant effect", "C. Metronidazole induces CYP3A4, accelerating warfarin clearance and reducing the INR", "D. Metronidazole chelates vitamin K in the gut, directly potentiating warfarin's anticoagulant effect", "E. Metronidazole interacts with warfarin's packaging and should not be stored near warfarin tablets"],
        "correctAnswer": "A",
        "explanation": "Warfarin (especially the more potent S-enantiomer) is predominantly metabolised by CYP2C9. Metronidazole is a CYP2C9 inhibitor — it reduces hepatic warfarin metabolism, causing plasma warfarin levels to rise and the INR to increase dramatically (often doubling or tripling within 2–3 days). This can cause life-threatening haemorrhage. Alternative antibiotics should be used whenever possible. If metronidazole is unavoidable, the GP must be informed and the INR checked within 2–3 days of starting."
    },
    {
        "id": "t5-m123", "theme": 5, "topicTag": "anticoagulants",
        "question": "Which ONE of the following is the specific reversal agent for dabigatran in life-threatening haemorrhage?",
        "options": ["A. Vitamin K (phytomenadione) — reverses the effect of all anticoagulants", "B. Protamine sulphate — reverses unfractionated heparin and LMWH", "C. Andexanet alfa — a recombinant factor Xa decoy reversing factor Xa inhibitors", "D. Idarucizumab (Praxbind) — a humanised monoclonal antibody specifically binding and neutralising dabigatran", "E. Fresh frozen plasma — non-specific reversal by providing clotting factors"],
        "correctAnswer": "D",
        "explanation": "Idarucizumab (Praxbind) is the specific reversal agent for dabigatran. It is a humanised monoclonal antibody fragment that binds dabigatran with ~350 times greater affinity than thrombin, completely and rapidly neutralising its anticoagulant effect within minutes. Andexanet alfa reverses factor Xa inhibitors (rivaroxaban, apixaban, edoxaban). Protamine reverses heparin. Vitamin K reverses warfarin (taking 12–24h). FFP provides clotting factors non-specifically for coagulopathy."
    },
    {
        "id": "t5-m124", "theme": 5, "topicTag": "anticoagulants",
        "question": "Which ONE of the following BEST describes the mechanism of action of low molecular weight heparin (LMWH, e.g. enoxaparin)?",
        "options": ["A. It inhibits thrombin (factor IIa) directly without requiring antithrombin III", "B. It binds antithrombin III and primarily enhances inhibition of factor Xa (and to a lesser extent, factor IIa)", "C. It blocks vitamin K-dependent factor synthesis in the liver", "D. It directly inhibits the platelet P2Y12 receptor, preventing ADP-mediated aggregation", "E. It activates tissue plasminogen activator (tPA) to dissolve existing thrombus"],
        "correctAnswer": "B",
        "explanation": "LMWH (enoxaparin, dalteparin, tinzaparin) binds antithrombin III via a specific pentasaccharide sequence, primarily enhancing its inhibition of factor Xa (anti-Xa activity >> anti-IIa activity). This differs from unfractionated heparin (UFH), which has greater anti-IIa activity. Advantages of LMWH: predictable pharmacokinetics (weight-based dosing, no routine monitoring); subcutaneous administration; lower risk of HIT than UFH. Reversal: protamine sulphate (partially reverses LMWH — fully reverses UFH)."
    },
    {
        "id": "t5-m125", "theme": 5, "topicTag": "anticoagulants",
        "question": "Which ONE of the following is the MOST common route of administration and mechanism of action of aspirin as an antiplatelet agent?",
        "options": ["A. Transdermal patch — aspirin inhibits thromboxane A2 synthesis in platelets for 7–10 days (platelet lifespan)", "B. IV infusion — aspirin irreversibly inhibits COX-1 in endothelium, preventing prostacyclin synthesis", "C. Oral tablet — aspirin irreversibly inhibits platelet COX-1, preventing TXA2 synthesis, impairing platelet aggregation for 7–10 days", "D. Sublingual tablet — aspirin blocks ADP receptors on platelets, preventing activation", "E. Oral tablet — aspirin reversibly inhibits COX-2 in platelets, providing temporary anti-inflammatory effects"],
        "correctAnswer": "C",
        "explanation": "Aspirin is taken orally and irreversibly acetylates the active site of cyclooxygenase (COX-1) in platelets. This permanently blocks thromboxane A2 (TXA2) synthesis — TXA2 is a potent platelet aggregator and vasoconstrictor. Because platelets have no nucleus, they cannot synthesise new COX-1. The antiplatelet effect lasts for the entire 7–10 day lifespan of the platelet. Aspirin also inhibits endothelial prostacyclin (PGI2) — an antiaggregatory vasodilator — but endothelial cells can regenerate COX-1, making the net effect antiplatelet. Clopidogrel/ticagrelor block the P2Y12 (ADP) receptor."
    },
    {
        "id": "t5-m126", "theme": 5, "topicTag": "anticoagulants",
        "question": "A patient is on apixaban for AF and requires a full-arch clearance (15 extractions) under general anaesthetic. Which ONE of the following BEST describes the appropriate anticoagulation management?",
        "options": ["A. No change needed — full-arch clearance is equivalent to simple extractions; continue apixaban", "B. Stop apixaban 24–48 hours pre-operatively; LMWH bridging is not needed for AF (unlike prosthetic valves); restart 24–48 hours post-operatively when haemostasis is secure", "C. Stop apixaban 5 days pre-operatively and give full-dose LMWH bridging throughout the perioperative period", "D. Give idarucizumab to reverse apixaban immediately before the procedure, then restart after surgery", "E. Maintain apixaban throughout and plan blood transfusion in advance for anticipated blood loss"],
        "correctAnswer": "B",
        "explanation": "For major oral surgery (extensive extractions under GA), the approach differs from simple extractions. Apixaban should be stopped 24–48 hours pre-operatively (or longer if renal impairment, per prescriber guidance) to reduce surgical haemorrhage risk. LMWH bridging is NOT recommended for non-valvular AF (low thromboembolism risk over 24–48h) — the BRIDGE trial showed bridging in AF patients caused more haemorrhage without reducing thromboembolism. Restart apixaban when haemostasis is secure (typically 24–48h post-op). Idarucizumab reverses dabigatran, not apixaban; andexanet alfa would reverse apixaban but is reserved for emergencies."
    },
    {
        "id": "t5-m127", "theme": 5, "topicTag": "anticoagulants",
        "question": "Tranexamic acid is used as a local haemostatic measure after dental extractions in anticoagulated patients. Which ONE of the following BEST describes its mechanism of action?",
        "options": ["A. It activates platelets by stimulating the GPIIb/IIIa receptor", "B. It inhibits fibrinolysis by competitively blocking lysine binding sites on plasminogen and plasmin, preventing clot dissolution", "C. It directly stimulates thrombin generation, accelerating coagulation", "D. It chelates calcium, reducing the activity of the common coagulation pathway", "E. It inhibits tissue plasminogen activator (tPA) secretion from endothelial cells"],
        "correctAnswer": "B",
        "explanation": "Tranexamic acid (TXA) is an antifibrinolytic agent. It competitively inhibits the lysine binding sites on plasminogen (preventing plasminogen → plasmin activation) and directly inhibits plasmin (the enzyme that cleaves fibrin in the clot). The overall effect is to prevent premature clot dissolution (fibrinolysis), stabilising the fibrin clot at the extraction socket. Used as 5% mouthwash (10mL for 2 minutes, 4× daily for 2 days). The oral mucosa has high fibrinolytic activity — this makes maintaining the clot particularly challenging in this environment."
    },
    # --- DRUGS FOR CVD ---
    {
        "id": "t5-m128", "theme": 5, "topicTag": "drugs-for-cvd",
        "question": "Which ONE of the following BEST describes the mechanism of the dry cough associated with ACE inhibitor therapy?",
        "options": ["A. ACE inhibitors irritate bronchial goblet cells, stimulating excess mucus production", "B. ACE inhibitors prevent angiotensin II formation, reducing bronchodilation", "C. ACE inhibitors inhibit ACE (also known as kininase II), preventing breakdown of bradykinin, which accumulates and stimulates bronchial C-fibres causing cough", "D. ACE inhibitors cross-react with beta-2 receptors in the bronchi, causing mild bronchoconstriction", "E. ACE inhibitors raise potassium levels, which depolarises bronchial smooth muscle and triggers cough"],
        "correctAnswer": "C",
        "explanation": "ACE (angiotensin-converting enzyme) is identical to kininase II, the enzyme responsible for degrading bradykinin. ACE inhibitors block both angiotensin II formation AND bradykinin degradation → bradykinin accumulates → stimulates bradykinin B2 receptors on bronchial C-fibres → persistent dry, tickling cough. The cough is NOT dose-dependent, may occur years after starting the drug, and does not respond to antihistamines or antitussives. Management: switch to an ARB (does not affect bradykinin metabolism)."
    },
    {
        "id": "t5-m129", "theme": 5, "topicTag": "drugs-for-cvd",
        "question": "Which ONE of the following beta-blockers is described as 'cardioselective' and what does this mean in clinical practice?",
        "options": ["A. Propranolol — non-selective; equally blocks beta-1 (cardiac) and beta-2 (bronchial/vascular) receptors", "B. Atenolol (or bisoprolol) — preferentially blocks beta-1 receptors in the heart at low doses; lower risk of bronchospasm", "C. Carvedilol — alpha and beta blocker combined; most selective for cardiac beta-1 receptors", "D. Labetalol — blocks beta-1, beta-2, and alpha-1 receptors equally; used specifically for hypertension in pregnancy", "E. Sotalol — a class III antiarrhythmic that preferentially blocks beta-2 receptors in the ventricle"],
        "correctAnswer": "B",
        "explanation": "Cardioselective beta-blockers (atenolol, bisoprolol, metoprolol) preferentially block beta-1 adrenoceptors (predominant in cardiac muscle) at low therapeutic doses, while relatively sparing beta-2 receptors (bronchial smooth muscle, peripheral vasculature). This means they can be used with caution in mild-moderate asthma or COPD when there is a strong cardiac indication (MI, heart failure, AF) — they are NOT absolutely contraindicated in all asthma patients, but must be used with caution and close monitoring. Propranolol is non-selective (avoid in asthma/COPD)."
    },
    {
        "id": "t5-m130", "theme": 5, "topicTag": "drugs-for-cvd",
        "question": "A patient takes digoxin for AF and heart failure. Which ONE of the following electrolyte abnormalities MOST significantly predisposes to digoxin toxicity?",
        "options": ["A. Hypernatraemia (high sodium) — enhances sodium channel effects of digoxin", "B. Hyperkalaemia (high potassium) — competes with digoxin at the binding site, worsening its effect", "C. Hypokalaemia (low potassium) — potentiates digoxin toxicity by enhancing its binding to Na/K-ATPase", "D. Hypercalcaemia (high calcium) — protects against digoxin toxicity by stabilising the cardiac membrane", "E. Hypomagnesaemia (low magnesium) — the most significant electrolyte effect on digoxin sensitivity"],
        "correctAnswer": "C",
        "explanation": "Digoxin inhibits the Na/K-ATPase pump on cardiac myocytes. Potassium normally competes with digoxin for binding at this site. When potassium is LOW (hypokalaemia), there is less competition → digoxin binds more avidly → enhanced inhibition → toxicity at therapeutic or even sub-therapeutic digoxin levels. Common causes of hypokalaemia in heart failure patients on digoxin: loop diuretics (furosemide) and thiazides. Hypercalcaemia (contrary to option D) also worsens digoxin toxicity — both calcium and digoxin increase intracellular calcium."
    },
    {
        "id": "t5-m131", "theme": 5, "topicTag": "drugs-for-cvd",
        "question": "A patient develops a lichenoid reaction in the oral cavity. Review of their drug history reveals they take atenolol, amlodipine, ramipril, and aspirin. Which ONE of the following drugs is MOST commonly associated with oral lichenoid reactions?",
        "options": ["A. Amlodipine — causes gingival hyperplasia rather than lichenoid reactions", "B. Aspirin — causes chemical burns when placed directly on mucosa but not lichenoid reactions systemically", "C. Ramipril (ACE inhibitor) — dry cough and angioedema are the classic oral/oropharyngeal effects", "D. Atenolol (beta-blocker) — one of the most frequently reported causes of drug-induced oral lichenoid reactions", "E. The combination of atenolol + ramipril is specifically responsible; neither drug alone causes this"],
        "correctAnswer": "D",
        "explanation": "Beta-blockers, particularly atenolol, propranolol, and practolol, are among the most frequently implicated drugs in oral lichenoid reactions. These reactions are clinically and histologically indistinguishable from idiopathic oral lichen planus but resolve when the causative drug is withdrawn. Other common culprits: thiazide diuretics, NSAIDs, gold salts, penicillamine, hydroxychloroquine, and some antihypertensives. Amlodipine causes gingival hyperplasia (not lichenoid reactions)."
    },
    {
        "id": "t5-m132", "theme": 5, "topicTag": "drugs-for-cvd",
        "question": "Which ONE of the following BEST describes the mechanism of action of spironolactone in heart failure?",
        "options": ["A. It inhibits the Na/K-ATPase pump in renal tubular cells, causing potassium retention and sodium excretion", "B. It is a competitive aldosterone antagonist at the mineralocorticoid receptor in the collecting duct; causes natriuresis while retaining potassium", "C. It blocks beta-1 adrenoceptors in the kidney, reducing renin secretion and subsequent aldosterone synthesis", "D. It inhibits ACE in the kidney, reducing angiotensin II and aldosterone production", "E. It is a direct vasodilator that reduces afterload independently of any diuretic effect"],
        "correctAnswer": "B",
        "explanation": "Spironolactone competitively blocks aldosterone at mineralocorticoid receptors in the collecting duct principal cells. Aldosterone normally causes: sodium reabsorption (via ENaC) → water retention → potassium and hydrogen excretion (via ROMK). Blocking this → natriuresis (sodium loss) + water loss → reduced preload. Because potassium excretion is also blocked → hyperkalaemia risk. In heart failure, spironolactone also reduces myocardial fibrosis. Monitor K+ carefully especially combined with ACE inhibitor/ARB."
    },
    {
        "id": "t5-m133", "theme": 5, "topicTag": "drugs-for-cvd",
        "question": "Which ONE of the following correctly describes the indication and mechanism of action of nitrates (e.g. GTN) in angina?",
        "options": ["A. GTN is metabolised to nitric oxide (NO) → activates soluble guanylate cyclase → increases cGMP → smooth muscle relaxation → primarily venous dilation → reduces preload → reduces myocardial oxygen demand", "B. GTN directly blocks L-type calcium channels in coronary arteries, causing vasodilation specifically in atherosclerotic vessels", "C. GTN activates beta-2 receptors in coronary arteries, causing selective coronary vasodilation", "D. GTN inhibits platelet aggregation by blocking GPIIb/IIIa receptors on platelet surfaces", "E. GTN inhibits HMG-CoA reductase, reducing atherosclerotic plaque growth and improving coronary flow long-term"],
        "correctAnswer": "A",
        "explanation": "GTN is an organic nitrate that is metabolised (primarily in vascular smooth muscle by mitochondrial aldehyde dehydrogenase — ALDH2) to release nitric oxide (NO). NO activates soluble guanylate cyclase → increases intracellular cGMP → protein kinase G activation → myosin light chain dephosphorylation → smooth muscle relaxation → vasodilation. GTN predominantly dilates veins (reduces preload and ventricular wall stress → reduced myocardial O2 demand). At higher doses, arterial and coronary dilation occur. Tachyphylaxis (tolerance) develops with prolonged use — nitrate-free interval (6–8 hours/day) prevents this."
    },
    {
        "id": "t5-m134", "theme": 5, "topicTag": "drugs-for-cvd",
        "question": "Nicorandil is prescribed for a patient with refractory angina. Six weeks later, he develops a painful, large, punched-out oral ulcer on his tongue. The ulcer has been present for 3 weeks and is getting larger. Which ONE of the following is the MOST appropriate management?",
        "options": ["A. Prescribe topical corticosteroid (triamcinolone in Orabase) and review in 2 weeks", "B. Perform biopsy immediately to exclude carcinoma and refer to oral medicine", "C. Liaise with the cardiologist about substituting nicorandil with an alternative antianginal; the ulcer is likely nicorandil-induced and should resolve on cessation", "D. Prescribe oral aciclovir for 5 days — this presentation is consistent with herpes simplex virus reactivation", "E. Perform oral swab for culture to exclude Candida infection and prescribe nystatin"],
        "correctAnswer": "C",
        "explanation": "Nicorandil (a potassium channel opener/nitrate combination used for refractory angina) is a well-recognised cause of severe oral ulceration. The ulcers are characteristically large, deep, and punched-out — they closely mimic carcinoma but have clean, non-indurated edges. They are completely unresponsive to topical corticosteroids or other local treatments and only resolve when nicorandil is withdrawn. The dentist should contact the cardiologist to discuss substitution. If the ulcer does not resolve within 4–8 weeks of drug cessation, biopsy to exclude carcinoma should then be performed."
    },
    {
        "id": "t5-m135", "theme": 5, "topicTag": "drugs-for-cvd",
        "question": "A patient on atorvastatin 40mg is prescribed erythromycin for a dental infection. Which ONE of the following BEST describes the risk of this combination?",
        "options": ["A. Erythromycin reduces atorvastatin absorption in the gut — the dose should be doubled", "B. Erythromycin inhibits CYP3A4 → raises plasma atorvastatin levels → increased risk of myopathy and rhabdomyolysis", "C. Erythromycin induces CYP3A4 → accelerates atorvastatin metabolism → reduced cholesterol control", "D. Atorvastatin inhibits erythromycin's antibacterial activity — the infection may not be cleared", "E. The combination is completely safe as atorvastatin is not metabolised by CYP3A4"],
        "correctAnswer": "B",
        "explanation": "Atorvastatin is metabolised by CYP3A4. Erythromycin (and clarithromycin) are potent CYP3A4 inhibitors. Inhibiting CYP3A4 raises atorvastatin plasma concentrations → increased risk of myopathy and rhabdomyolysis. Note: this risk is significantly greater with simvastatin/lovastatin (which are more dependent on CYP3A4 and have no alternative metabolic pathway) than with atorvastatin (which also has some N-dealkylation). Safer alternatives for dental infections in statin patients: amoxicillin (no statin interaction), metronidazole (no significant statin interaction), or azithromycin (less CYP3A4 inhibition than erythromycin/clarithromycin)."
    },
    # ADDITIONAL MIXED TOPICS
    {
        "id": "t5-m136", "theme": 5, "topicTag": "dental-implications-cvd",
        "question": "A patient with a permanent pacemaker is scheduled for a root canal procedure. You plan to use an electric pulp tester. Which ONE of the following is the MOST appropriate consideration?",
        "options": ["A. Electric pulp testers are completely contraindicated in pacemaker patients and must never be used", "B. Electric pulp testers can be used; they generate minimal electromagnetic interference and are generally considered safe, but check device documentation and consider using cold/heat testing instead", "C. Electric pulp testers must be used only in the contralateral arch to the pacemaker", "D. Use the electric pulp tester for no more than 3 seconds per tooth to minimise EMI exposure", "E. Electric pulp testers must only be used under cardiological supervision in patients with pacemakers"],
        "correctAnswer": "B",
        "explanation": "Electric pulp testers produce low levels of electromagnetic interference (EMI). Modern pacemakers (post-1990s) are much better shielded and typically not affected by the small currents used in dental EPTs. Most guidelines consider EPT use acceptable in pacemaker patients, but it is wise to check the patient's device identity card, use cold/heat testing as an alternative where feasible, and avoid placing the tester circuit close to the pacemaker site. Ultrasonic scalers are the more significant concern — keep the working end >15cm from the pacemaker."
    },
    {
        "id": "t5-m137", "theme": 5, "topicTag": "dental-implications-cvd",
        "question": "A patient tells you they are taking clopidogrel 75mg daily following a drug-eluting coronary artery stent placement 8 months ago. They are also on aspirin 75mg. They need 4 extractions. Which ONE of the following is the MOST appropriate approach to their antiplatelet therapy?",
        "options": ["A. Stop clopidogrel 7 days before extractions; continue aspirin only to reduce bleeding risk", "B. Stop both aspirin and clopidogrel 7 days before to ensure normal haemostasis", "C. Continue both clopidogrel and aspirin; perform extractions with local haemostatic measures", "D. Switch clopidogrel to aspirin 300mg for the week of the extractions", "E. Defer extractions until the patient has completed 12 months of DAPT and clopidogrel has been stopped"],
        "correctAnswer": "C",
        "explanation": "Drug-eluting stent patients are on dual antiplatelet therapy (DAPT — clopidogrel + aspirin) for 12 months. Stopping either antiplatelet drug during this period risks acute stent thrombosis (~30–50% mortality). DAPT should never be stopped for routine dental procedures. The correct approach is to continue both drugs, perform extractions with local haemostatic measures (oxidised cellulose, sutures, tranexamic acid mouthwash), and accept slightly increased postoperative bleeding risk, which is always manageable. An elective procedure MIGHT be timed after DAPT completion if non-urgent, but with 4 months remaining, waiting would not be appropriate if the extractions are needed now."
    },
    {
        "id": "t5-m138", "theme": 5, "topicTag": "dental-implications-cvd",
        "question": "Which ONE of the following conditions represents a contraindication to the use of a vasoconstrictor (adrenaline) in the local anaesthetic administered by a dentist?",
        "options": ["A. Well-controlled hypertension on a single antihypertensive medication", "B. Stable angina on atenolol and aspirin, last episode 8 months ago", "C. Unstable angina with chest pain at rest occurring within the past week", "D. Complete surgical revascularisation (CABG) performed 6 months ago with no current symptoms", "E. Dilated cardiomyopathy with EF 38% on optimal medical therapy, fully compensated"],
        "correctAnswer": "C",
        "explanation": "Adrenaline in dental LA is relatively contraindicated (not absolutely) in most cardiac conditions. The key absolute/strong relative contraindications are: unstable angina (myocardium already ischaemic at rest — adrenaline increases myocardial O2 demand acutely), MI within past 3 months, severe uncontrolled hypertension, and uncontrolled arrhythmias. Stable, well-controlled cardiovascular conditions (options A, B, D, E) are NOT contraindications — adrenaline should be used in these patients to ensure adequate anaesthesia, as pain and dental anxiety generate a far greater endogenous catecholamine surge than the small doses in 1–3 cartridges of LA."
    },
    {
        "id": "t5-m139", "theme": 5, "topicTag": "dental-implications-cvd",
        "question": "Which ONE of the following is the recommended minimum time interval between a myocardial infarction and elective (non-urgent) dental treatment?",
        "options": ["A. 2 weeks — when troponin levels have normalised", "B. 6 weeks — when the MI scar has fully fibrosed", "C. 3 months — when the risk of arrhythmia and re-infarction from dental stress is significantly reduced", "D. 12 months — when dual antiplatelet therapy has been completed", "E. 5 years — the high-risk period for secondary MI extends for 5 years post-event"],
        "correctAnswer": "C",
        "explanation": "The recommended deferral period for ELECTIVE (non-urgent) dental treatment after MI is generally 3–6 months, with many sources citing 3 months as the minimum safe interval. During this time: the infarcted myocardium is still healing (scar formation); risk of arrhythmia, re-infarction, and sudden death from sympathetic catecholamine surges (from pain/anxiety during dental treatment) is highest in the first weeks. After 3 months, provided the patient is stable on optimal medical therapy, routine dental treatment can resume with appropriate precautions. Urgent dental treatment (infection, pain) should never be deferred regardless of MI recency."
    },
    {
        "id": "t5-m140", "theme": 5, "topicTag": "dental-implications-cvd",
        "question": "A patient on ramipril for hypertension develops acute, painless, progressive swelling of the tongue and floor of mouth at their dental appointment, without urticaria or apparent allergen exposure. Which ONE of the following is the MOST important IMMEDIATE action?",
        "options": ["A. Give oral chlorphenamine (antihistamine) 4mg and observe for 1 hour", "B. Apply topical adrenaline spray to the oral mucosa to reduce local swelling", "C. Assess the airway immediately — if compromised, give IM adrenaline 500 micrograms in anterolateral thigh; call 999", "D. Administer IV hydrocortisone 200mg and oral prednisolone 50mg and observe", "E. Refer the patient to their GP urgently and advise them to go to A&E if the swelling worsens"],
        "correctAnswer": "C",
        "explanation": "This is ACE inhibitor-induced angioedema — a medical emergency. Tongue and floor of mouth swelling can rapidly progress to complete airway obstruction. Unlike histamine-mediated angioedema, bradykinin-mediated angioedema responds poorly to antihistamines and steroids. Immediate action: (1) Assess and secure the airway — this is the absolute priority; (2) Call 999; (3) IM adrenaline 500 micrograms (1:1000) in the anterolateral thigh if airway is compromised. Adrenaline provides some benefit even in bradykinin-mediated angioedema through its vasoconstrictive effects on local oedema. The patient must go to hospital. Stop ramipril permanently."
    },
    {
        "id": "t5-m141", "theme": 5, "topicTag": "cvd-overview",
        "question": "The QRISK3 tool is used in clinical practice. Which ONE of the following BEST describes its purpose?",
        "options": ["A. It calculates the probability of death from any cause in the next 12 months", "B. It estimates the 10-year risk of cardiovascular disease (MI or stroke) to guide statin prescribing", "C. It determines the appropriate dose of statins based on LDL cholesterol levels alone", "D. It predicts the likelihood of a patient developing heart failure within 5 years", "E. It calculates the CHA2DS2-VASc score for anticoagulation decisions in AF"],
        "correctAnswer": "B",
        "explanation": "QRISK3 (the third iteration of the QRISK algorithm) calculates the 10-year cardiovascular risk (MI or stroke combined) using multiple variables: age, sex, systolic BP and variability, total cholesterol/HDL ratio, smoking, diabetes type, family history, deprivation, BMI, AF, CKD, SLE, severe mental illness, erectile dysfunction, and systolic BP variability. NICE recommends offering high-intensity statin therapy to individuals with QRISK3 ≥10% (primary prevention) and to all patients with established CVD (secondary prevention)."
    },
    {
        "id": "t5-m142", "theme": 5, "topicTag": "ischaemic-heart-disease",
        "question": "A 62-year-old man presents with a new ST-elevation MI. Primary PCI (percutaneous coronary intervention) is the preferred reperfusion strategy. Which ONE of the following door-to-balloon time targets is recommended for primary PCI?",
        "options": ["A. Door-to-balloon time <30 minutes from hospital arrival", "B. Door-to-balloon time <60 minutes from hospital arrival", "C. Door-to-balloon time <90 minutes from hospital arrival (or within 120 minutes from first medical contact)", "D. Door-to-balloon time <3 hours — identical to the thrombolysis window", "E. There is no time-sensitive target for primary PCI — outcome depends only on door-to-TIMI 3 flow"],
        "correctAnswer": "C",
        "explanation": "NICE/ESC guidelines recommend primary PCI should be performed with a door-to-balloon time of <90 minutes from hospital arrival (or ≤120 minutes from first medical contact to wire crossing). PCI is preferred over thrombolysis when it can be performed within this timeframe by an experienced team. 'Time is muscle' — each 30-minute delay in reperfusion increases mortality. If PCI cannot be performed within 120 minutes, systemic thrombolysis (alteplase/tenecteplase) is the alternative, followed by facilitated PCI."
    },
    {
        "id": "t5-m143", "theme": 5, "topicTag": "cardiac-arrhythmias",
        "question": "A patient with Wolff-Parkinson-White (WPW) syndrome presents with a broad complex tachycardia at 220 bpm. Which ONE of the following drugs is MOST DANGEROUS and should be AVOIDED?",
        "options": ["A. Adenosine — safe and recommended as first-line in WPW", "B. IV flecainide — blocks the accessory pathway and is safe in WPW", "C. Verapamil — blocks the AV node, potentially forcing all conduction via the accessory pathway → very fast ventricular rate → VF and cardiac arrest", "D. Amiodarone — the safest antiarrhythmic in all forms of WPW", "E. Digoxin — safe in WPW as it has minimal effect on the accessory pathway"],
        "correctAnswer": "C",
        "explanation": "WPW has an accessory atrioventricular connection (Bundle of Kent) that bypasses the AV node. In AF/atrial flutter with WPW, verapamil (and digoxin) block the AV node → all impulses preferentially conduct via the rapidly conducting accessory pathway → extremely fast ventricular rate (can exceed 300 bpm) → VF and cardiac arrest. This is a potentially fatal effect. The correct management for pre-excited AF in WPW: IV procainamide or flecainide (block the accessory pathway); DC cardioversion if haemodynamically unstable. Adenosine is also contraindicated in pre-excited AF."
    },
    {
        "id": "t5-m144", "theme": 5, "topicTag": "hypertension-stroke",
        "question": "Which ONE of the following is the MOST common type of stroke in the UK (by aetiology)?",
        "options": ["A. Haemorrhagic stroke — subarachnoid haemorrhage — accounts for 60% of strokes", "B. Haemorrhagic stroke — intracerebral haemorrhage — the most common cause overall", "C. Ischaemic stroke — cardioembolic from AF — most common single cause", "D. Ischaemic stroke — accounts for approximately 85% of all strokes; various mechanisms", "E. Venous sinus thrombosis — accounts for 40% in younger patients"],
        "correctAnswer": "D",
        "explanation": "Ischaemic stroke accounts for approximately 85% of all strokes in the UK. The remaining 15% are haemorrhagic (intracerebral haemorrhage ~10%, subarachnoid haemorrhage ~5%). Within ischaemic stroke, the most common aetiology is large artery atherosclerosis (~25%), followed by cardioembolic (~25% — predominantly from AF), and small vessel disease (lacunar — ~20%). AF-related cardioembolic strokes tend to be the most severe and disabling. Venous sinus thrombosis is rare (<1%)."
    },
    {
        "id": "t5-m145", "theme": 5, "topicTag": "valvular-heart-disease",
        "question": "Which ONE of the following BEST describes the pathophysiology of the Carey-Coombs murmur in acute rheumatic fever?",
        "options": ["A. Aortic regurgitation from inflammation of the aortic valve during acute carditis", "B. Mid-diastolic murmur caused by inflammation of the mitral valve leaflets (valvulitis), causing thickening and functional mitral stenosis in acute rheumatic fever", "C. Pansystolic murmur from acute mitral regurgitation during the healing phase of rheumatic fever", "D. Systolic ejection murmur from aortic stenosis developing after repeated episodes of rheumatic fever", "E. Continuous murmur from a patent ductus arteriosus complicating rheumatic fever in children"],
        "correctAnswer": "B",
        "explanation": "The Carey-Coombs murmur is a soft, mid-diastolic murmur heard at the apex in acute rheumatic carditis. It results from acute inflammation and oedema of the mitral valve leaflets, causing thickening that temporarily impairs valve opening — creating a functional (inflammatory) mitral stenosis. It is not permanent — it resolves as the acute inflammation settles. Permanent mitral stenosis develops only after years of repeated rheumatic fever episodes causing progressive commissural fibrosis and valve calcification."
    },
    {
        "id": "t5-m146", "theme": 5, "topicTag": "heart-failure",
        "question": "Which ONE of the following clinical signs is MOST specific for elevated left ventricular filling pressure (left ventricular failure)?",
        "options": ["A. Raised JVP (jugular venous pressure) — reflects right atrial pressure elevation", "B. Third heart sound (S3 gallop) — heard in early diastole; highly specific for elevated LV filling pressure/volume overload", "C. Bilateral pitting ankle oedema — a non-specific sign of fluid retention", "D. Hepatomegaly — reflects right ventricular failure and venous congestion", "E. Kussmaul's sign (JVP rises on inspiration) — specific for constrictive pericarditis"],
        "correctAnswer": "B",
        "explanation": "A third heart sound (S3) occurs in early diastole after the second heart sound (S2), creating a 'Kentucky' cadence (lub-dub-ta). It is caused by rapid ventricular filling causing the ventricular wall to vibrate — it is highly specific for elevated LV end-diastolic pressure (volume overload) and is associated with poor LV function. In younger patients, S3 can be physiological. In patients over 40 with symptoms, an S3 gallop is a strong indicator of heart failure with elevated filling pressures. Raised JVP reflects right atrial pressure. Ankle oedema is non-specific."
    },
    {
        "id": "t5-m147", "theme": 5, "topicTag": "atherosclerosis",
        "question": "Statins (e.g. atorvastatin) reduce cardiovascular risk beyond simply lowering LDL cholesterol. Which ONE of the following 'pleiotropic' (non-lipid) effect of statins has been identified?",
        "options": ["A. Statins directly reverse existing atherosclerotic plaques by removing the lipid core", "B. Statins stabilise vulnerable plaques by reducing macrophage activity and MMP secretion, reducing the risk of plaque rupture", "C. Statins directly inhibit platelet aggregation by blocking GPIIb/IIIa receptors", "D. Statins increase HDL synthesis proportionally to the reduction in LDL they achieve", "E. Statins prevent de novo thrombus formation by inhibiting thrombin directly"],
        "correctAnswer": "B",
        "explanation": "Statins have multiple pleiotropic (lipid-independent) effects: (1) Plaque stabilisation — reduce macrophage content and MMP (matrix metalloproteinase) secretion in plaques → thicker fibrous cap → less prone to rupture; (2) Anti-inflammatory effects — reduce CRP, adhesion molecules (ICAM-1, VCAM-1); (3) Improved endothelial function — upregulate eNOS → more NO production; (4) Antithrombotic effects — reduce platelet activation. These effects partly explain why statins begin reducing cardiovascular events within months of starting, before significant LDL reduction-related structural changes in plaques could occur."
    },
    {
        "id": "t5-m148", "theme": 5, "topicTag": "anticoagulants",
        "question": "A patient with a prosthetic mechanical mitral valve has their warfarin stopped before a major orthopaedic operation. Which ONE of the following is the MOST appropriate anticoagulation management during the perioperative period?",
        "options": ["A. No bridging needed — prosthetic valves can tolerate 5–7 days without anticoagulation safely", "B. Bridge with therapeutic-dose LMWH while warfarin is sub-therapeutic (INR <2), resumed the evening of surgery when haemostasis is secure", "C. Use aspirin monotherapy as anticoagulation cover during the perioperative period", "D. Switch permanently to a DOAC perioperatively as DOACs are safer than warfarin for mechanical valves", "E. Administer IV unfractionated heparin only on the day of surgery, stopping warfarin permanently"],
        "correctAnswer": "B",
        "explanation": "Prosthetic mechanical heart valves carry a very high thromboembolic risk if left without anticoagulation — particularly the mitral position (higher risk than aortic). DOACs are NOT approved for mechanical heart valves (the RE-ALIGN trial showed dabigatran caused more valve thromboses than warfarin). The correct perioperative strategy: stop warfarin 5 days pre-op; when INR falls to <2.0, start therapeutic-dose LMWH (enoxaparin 1mg/kg twice daily SC) as 'bridge'; stop LMWH 24 hours pre-op; restart LMWH post-op evening when haemostasis secured; restart warfarin simultaneously; stop LMWH once INR is therapeutic (≥2.0)."
    },
    {
        "id": "t5-m149", "theme": 5, "topicTag": "drugs-for-cvd",
        "question": "Which ONE of the following BEST describes the mechanism by which thiazide diuretics lower blood pressure in the long term?",
        "options": ["A. Thiazides permanently reduce blood volume by causing irreversible renal tubular damage", "B. Thiazides initially reduce blood volume (diuresis), then long-term vasodilation due to reduced intracellular sodium and calcium in vascular smooth muscle", "C. Thiazides inhibit aldosterone synthesis in the adrenal cortex, preventing fluid retention", "D. Thiazides directly dilate resistance arterioles by blocking alpha-1 adrenoceptors", "E. Thiazides reduce cardiac output by depressing SA node automaticity"],
        "correctAnswer": "B",
        "explanation": "Thiazide (and thiazide-like, e.g. indapamide) diuretics block the Na-Cl cotransporter in the distal convoluted tubule → acute natriuresis and diuresis → initial BP reduction via reduced blood volume. With long-term use (beyond a few weeks), plasma volume returns towards baseline but BP remains reduced. This is because reduced intracellular sodium (via inhibition of NCC and downstream effects) leads to reduced Ca2+ influx via Na/Ca exchangers in vascular smooth muscle → smooth muscle relaxation → vasodilation. This vasodilatory mechanism sustains the long-term antihypertensive effect."
    },
    {
        "id": "t5-m150", "theme": 5, "topicTag": "dental-implications-cvd",
        "question": "A 66-year-old man on ramipril, bisoprolol, and atorvastatin for IHD requires a lower first molar extraction. He reports no angina for 14 months and is fully asymptomatic. Which ONE of the following is the MOST appropriate management plan for his dental appointment?",
        "options": ["A. Refer to hospital as all patients with IHD must be treated in secondary care for extractions", "B. Morning appointment; check current cardiac status; effective LA with adrenaline; short appointment; have O2, GTN, and AED available", "C. Use only adrenaline-free local anaesthetic and prescribe oral diazepam pre-medication for all IHD patients", "D. Request a cardiology clearance letter before any dental procedure for a patient with IHD", "E. Take 2 GTN sprays prophylactically 5 minutes before starting the procedure for all stable IHD patients"],
        "correctAnswer": "B",
        "explanation": "Stable, well-controlled IHD with no symptoms for >3 months is not a contraindication to routine dental treatment in primary care. The correct approach: morning appointment (catecholamines naturally lower in the morning; patient less fatigued); check current symptoms and medications; effective local anaesthesia with appropriate adrenaline (manages pain-induced catecholamine surge — which is more harmful than the LA adrenaline); keep appointment short; ensure emergency drugs (GTN, aspirin, adrenaline, O2) and AED are available. Adrenaline-free LA is NOT routinely required for stable IHD. GTN should not be given prophylactically to all IHD patients — only if requested by the cardiologist or if symptoms develop."
    }
]

data['mockBank'].extend(new_mock)

with open('data/theme-5.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"mockBank total: {len(data['mockBank'])}")
