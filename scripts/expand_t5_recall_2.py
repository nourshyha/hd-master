import json

with open('data/theme-5.json', 'r') as f:
    data = json.load(f)

new_recall = [
    # ATHEROSCLEROSIS (continued)
    {
        "id": "t5-r101",
        "question": "What is the difference between a thrombus and an embolus?",
        "answer": "Thrombus: a solid clot formed in a living blood vessel or heart from blood constituents. Attached to the vessel wall. Contains platelets, fibrin, and red cells arranged in lines of Zahn (in arteries/cardiac thrombi). Can be arterial (white, platelet-rich) or venous (red, fibrin-rich).\nEmbolus: a mass of material (usually a detached thrombus) carried in the bloodstream from its site of origin to lodge elsewhere. 'Something travels somewhere'. Most common: thromboemboli. Others: fat, air, bone marrow, amniotic fluid, tumour, foreign material."
    },
    {
        "id": "t5-r102",
        "question": "What is the difference between atherosclerosis and arteriosclerosis?",
        "answer": "Arteriosclerosis: generic term for hardening and loss of elasticity of arteries with ageing. Three types: atherosclerosis, Mönckeberg's medial calcific sclerosis, arteriolosclerosis.\nAtherosclerosis: specific type — focal accumulation of lipid (atheroma) in the intima of large/medium arteries (aorta, coronary, carotid, femoral). The most clinically important form.\nMönckeberg's: calcification of the tunica media in medium arteries (no luminal narrowing; common in elderly, diabetics; gives 'tramline' calcification on X-ray).\nArteriolosclerosis: hyaline or hyperplastic thickening of small arterioles; causes concentric narrowing; associated with hypertension and diabetes."
    },
    {
        "id": "t5-r103",
        "question": "What are the consequences of atherosclerosis in different arterial territories?",
        "answer": "Coronary arteries: stable angina (partial stenosis → reversible ischaemia), acute MI (complete occlusion → infarction), sudden cardiac death, heart failure\nCarotid/cerebral arteries: TIA, ischaemic stroke, vascular dementia\nRenal arteries: renal artery stenosis → renovascular hypertension, ischaemic nephropathy\nMesenteric arteries: intestinal angina (post-prandial abdominal pain), mesenteric infarction (bowel ischaemia)\nFemoral/popliteal arteries: intermittent claudication, critical ischaemia, gangrene, amputation\nAorta: aortic aneurysm (especially infrarenal), aortic occlusion"
    },
    {
        "id": "t5-r104",
        "question": "What are cholesterol clefts and where are they seen histologically?",
        "answer": "Cholesterol clefts are needle-shaped clear spaces (clefts) seen in histological sections of advanced atherosclerotic plaques. They represent sites where cholesterol crystals were dissolved out during tissue processing. The cholesterol was deposited in the lipid-rich necrotic core of a fibrolipid plaque. Their presence indicates an advanced, complicated plaque. They are a feature of the atheromatous core — not the early fatty streak (which is characterised by foam cells). Cholesterol crystals can also be seen in cholesterol emboli in small vessels."
    },
    # IHD / MI / ANGINA (continued)
    {
        "id": "t5-r105",
        "question": "What is prinzmetal (variant) angina and how does it differ from stable angina?",
        "answer": "Prinzmetal (variant) angina: chest pain at rest caused by coronary artery SPASM (not fixed atherosclerotic stenosis). Typically occurs at night or early morning. ECG shows transient ST elevation (unlike stable angina which shows depression). Coronary arteries may look normal on angiography.\nTreatment: calcium channel blockers (preferred) and nitrates to relieve and prevent spasm. Beta-blockers are CONTRAINDICATED (may worsen spasm via unopposed alpha-mediated vasoconstriction).\nContrast with stable angina: exertional; ECG ST depression; fixed plaque; responds to beta-blockers."
    },
    {
        "id": "t5-r106",
        "question": "What is the left anterior descending (LAD) artery and why is it called the 'widowmaker'?",
        "answer": "The LAD is a branch of the left main coronary artery that runs down the anterior interventricular groove, supplying the anterior wall of the left ventricle, the interventricular septum, and the apex of the heart. It supplies approximately 40–50% of total myocardial mass.\nCalled 'widowmaker' because: occlusion of the LAD causes a large anterior MI (most commonly presenting as STEMI with ST elevation in V1–V4). This can rapidly cause cardiogenic shock, arrhythmia, and death. Prompt revascularisation (primary PCI) is critical."
    },
    {
        "id": "t5-r107",
        "question": "What ECG changes are seen in acute STEMI and how do they evolve over time?",
        "answer": "Hyperacute (minutes): tall, peaked T-waves (earliest change, often missed)\nAcute (minutes-hours): ST segment elevation in leads overlying the infarct territory; reciprocal ST depression in opposing leads\nEvolution (hours-days): ST elevation persists; T-wave inversion develops; Q-waves form (>0.04s wide, >25% of R-wave height — signify transmural necrosis — permanent)\nChronic: persistent Q-waves; T-waves may normalise; ST usually returns to baseline. Persistent ST elevation >3 months suggests left ventricular aneurysm."
    },
    {
        "id": "t5-r108",
        "question": "What is the mechanism of cardiac resynchronisation therapy (CRT) and when is it used?",
        "answer": "CRT (biventricular pacemaker): a special pacemaker that stimulates BOTH ventricles simultaneously (via leads in right ventricle + coronary sinus/lateral wall of left ventricle). Resynchronises the ventricular contraction in patients with left bundle branch block (LBBB) — where the left ventricle contracts late and out of phase with the right → wasted contraction.\nIndications: heart failure with NYHA class III–IV; ejection fraction <35%; QRS duration >120ms (usually LBBB). Benefits: improves symptoms, exercise tolerance, ejection fraction, and reduces mortality.\nCRT-D: combined CRT + ICD (implantable cardioverter-defibrillator) for simultaneous resynchronisation and defibrillation capability."
    },
    # VALVULAR DISEASE / IE (continued)
    {
        "id": "t5-r109",
        "question": "What is the clinical triad of aortic stenosis?",
        "answer": "The classic triad of severe aortic stenosis:\n1. Angina — reduced coronary perfusion (thickened ventricular wall compresses coronary ostia); median survival after onset: 5 years\n2. Syncope (dizziness/fainting) — inadequate cardiac output on exertion; peripheral vessels dilate but CO cannot increase; median survival: 3 years\n3. Breathlessness/heart failure — compensatory mechanisms fail; median survival: 1–2 years\nOther signs: slow-rising carotid pulse, ejection systolic murmur (right sternal edge radiating to carotid), heaving apex beat, narrow pulse pressure. Valve replacement indicated when symptomatic."
    },
    {
        "id": "t5-r110",
        "question": "What is the 'vegetation' seen in infective endocarditis histologically?",
        "answer": "A vegetation is an irregular, friable (crumbly) mass adherent to the heart valve leaflet — most often on the low-pressure side (atrial side of mitral/tricuspid valves; ventricular side of aortic/pulmonary valves). It consists of a layered structure of: bacteria + fibrin + platelets + white cells. The bacteria are embedded deep within the fibrin matrix — this protects them from antibiotics and the immune system, requiring prolonged intravenous antibiotic therapy (4–6 weeks). Vegetations can fragment → septic emboli → end-organ infarction."
    },
    {
        "id": "t5-r111",
        "question": "What is mitral valve prolapse (MVP) and is it a risk factor for infective endocarditis?",
        "answer": "MVP: one or both mitral valve leaflets prolapse (bulge) backwards into the left atrium during systole due to redundant leaflet tissue and chordae tendineae. Very common (2–3% of population). Usually asymptomatic; detected as mid-systolic click + late systolic murmur on auscultation.\nIE risk: MVP with mitral regurgitation (especially with leaflet thickening) is considered a moderate-risk factor for IE by SDCEP. MVP without MR has a very low risk and was dropped from NICE high-risk categories in 2008.\nDental relevance: no routine antibiotic prophylaxis recommended (per NICE) for MVP patients, even with MR. Advise excellent oral hygiene."
    },
    {
        "id": "t5-r112",
        "question": "What are the echocardiographic features of infective endocarditis?",
        "answer": "Transthoracic echo (TTE): first-line; detects vegetations >2mm. May miss small vegetations (sensitivity ~75%).\nTransoesophageal echo (TOE): more sensitive (>90%); used if TTE negative but suspicion remains; better for posterior structures (mitral valve, prosthetic valves, aortic root abscess).\nFindings:\n- Vegetations: oscillating echogenic masses on valves\n- Perivalvular abscess (especially aortic root — surgical emergency)\n- New valvular regurgitation (major Duke criterion)\n- Fistulae between cardiac chambers\n- Valve perforation or destruction\nRepeat echo at 7 days if clinical suspicion persists despite negative initial echo."
    },
    # HEART FAILURE (continued)
    {
        "id": "t5-r113",
        "question": "What is systolic vs diastolic heart failure (HFrEF vs HFpEF)?",
        "answer": "Systolic heart failure (HFrEF — Heart Failure with Reduced Ejection Fraction, EF <40%): the ventricle cannot contract adequately → reduced stroke volume → reduced cardiac output. Cause: ischaemic heart disease, dilated cardiomyopathy. Treatment: ACE inhibitors/ARBs, beta-blockers, spironolactone, diuretics — all proven to improve mortality.\nDiastolic heart failure (HFpEF — Heart Failure with Preserved Ejection Fraction, EF >50%): ventricle is stiff, cannot relax adequately → poor filling → reduced stroke volume. Causes: hypertension (LV hypertrophy), hypertrophic cardiomyopathy, aging. Treatment: largely symptom-based (diuretics, rate control, BP control); no proven mortality benefit from standard HF drugs."
    },
    {
        "id": "t5-r114",
        "question": "What are the neurohormonal compensatory mechanisms in heart failure and why are they ultimately harmful?",
        "answer": "Initially compensatory but long-term harmful:\n1. Sympathetic activation: ↑heart rate + ↑contractility (maintain CO) → but chronic stimulation: tachycardia increases O2 demand; catecholamines are directly cardiotoxic → fibrosis; peripheral vasoconstriction ↑ afterload → worsens heart failure.\n2. RAAS activation: aldosterone → Na+/water retention → expanded blood volume (raises preload, maintains BP) → but: fluid overload → oedema, pulmonary congestion; vasoconstriction ↑ afterload.\n3. ANP/BNP release: counter-regulatory — promote natriuresis and vasodilation (beneficial but overwhelmed).\nDrug targets: ACE inhibitors (block RAAS), beta-blockers (block sympathetic), spironolactone (block aldosterone) — all improve survival by blocking these harmful mechanisms."
    },
    {
        "id": "t5-r115",
        "question": "What is dilated cardiomyopathy and what causes it?",
        "answer": "Dilated cardiomyopathy (DCM): dilation of one or both ventricles with impaired systolic function (reduced EF). The commonest cardiomyopathy.\nCauses:\n- Idiopathic (most common — ~50%)\n- Genetic/familial (30–40% — autosomal dominant; genes: titin, lamin A/C, dystrophin)\n- Alcohol excess (toxic effect on myocytes + beriberi)\n- Viral myocarditis (Coxsackie B, HIV, parvovirus B19)\n- Peripartum (within last month of pregnancy to 5 months postpartum)\n- Drug toxicity: doxorubicin (anthracycline chemotherapy), trastuzumab, cocaine\n- Thyroid disease (hypo- and hyperthyroidism)\n- Haemochromatosis\nPresentation: progressive heart failure symptoms, atrial/ventricular arrhythmias, embolic events."
    },
    {
        "id": "t5-r116",
        "question": "What drug is used for acute decompensated heart failure with fluid overload, and what dose is used?",
        "answer": "Furosemide (loop diuretic): first-line for acute pulmonary oedema/decompensated heart failure.\nIV furosemide 40–80mg (faster onset than oral; oral furosemide absorbed poorly in oedematous gut). Up to 500mg IV in refractory cases.\nOther acute heart failure management: (1) oxygen (high flow if hypoxic); (2) sit upright (reduce pulmonary venous return); (3) IV nitrates (if SBP >100 mmHg — vasodilate, reduce preload); (4) IV morphine (historical — reduces anxiety/dyspnoea, now controversial — may worsen outcomes); (5) CPAP/NIV for respiratory failure; (6) treat underlying cause (e.g. cardioversion for AF, revascularise MI)."
    },
    # ARRHYTHMIAS (continued)
    {
        "id": "t5-r117",
        "question": "What is torsade de pointes and what drugs cause it?",
        "answer": "Torsade de pointes ('twisting of points'): a form of polymorphic ventricular tachycardia associated with a prolonged QT interval on ECG. The QRS complexes appear to twist around the baseline. Can degenerate into VF and cause sudden death.\nCauses of long QT syndrome:\nCongenital: Romano-Ward (autosomal dominant, no deafness), Jervell-Lange-Nielsen (autosomal recessive, congenital deafness)\nAcquired — drugs that prolong QT interval:\n- Class III antiarrhythmics: amiodarone, sotalol\n- Macrolide antibiotics: erythromycin, clarithromycin, azithromycin\n- Fluoroquinolones: ciprofloxacin, moxifloxacin\n- Antifungals: fluconazole, ketoconazole\n- Antihistamines: terfenadine (withdrawn)\n- Antipsychotics: haloperidol, quetiapine\n- Hypokalaemia, hypomagnesaemia\nManagement: IV magnesium sulphate; remove causative drug; cardioversion if haemodynamically unstable."
    },
    {
        "id": "t5-r118",
        "question": "What is Wolff-Parkinson-White (WPW) syndrome?",
        "answer": "WPW: a congenital accessory electrical pathway (Bundle of Kent) that bypasses the AV node → pre-excitation of the ventricles before the normal AV node pathway. ECG features: short PR interval (<120ms), delta wave (slurred upstroke of QRS), broad QRS.\nProblems: (1) Re-entry tachycardia (AVRT) — the impulse travels down the AV node and returns via the accessory pathway (or vice versa) → SVT; (2) Atrial fibrillation conducted rapidly via the accessory pathway (bypasses AV node rate-limiting) → ventricular rates >300 bpm → VF → sudden cardiac death.\nManagement: radiofrequency catheter ablation of the accessory pathway (curative). AVOID digoxin and verapamil in WPW + AF (both can paradoxically speed up conduction through the accessory pathway → fatal arrhythmia)."
    },
    {
        "id": "t5-r119",
        "question": "How does atrial flutter differ from AF on ECG and clinically?",
        "answer": "Atrial flutter: organised atrial activity at ~300 bpm creating a 'sawtooth' (flutter wave) pattern on ECG (best seen in leads II, III, aVF). Ventricular rate typically 150 bpm (2:1 block) or 100 bpm (3:1 block) — the AV node cannot conduct every flutter wave. Regular ventricular rhythm.\nAF: completely disorganised atrial activity — no distinct P waves; irregular fibrillatory baseline (350–600 bpm); irregularly irregular ventricular response.\nClinically: both cause palpitations, stroke risk, can lead to heart failure. Both treated similarly (rate control, rhythm control, anticoagulation). Flutter is more amenable to radiofrequency ablation (ablation of the cavotricuspid isthmus is curative in ~95%)."
    },
    {
        "id": "t5-r120",
        "question": "What is first, second, and third degree heart block?",
        "answer": "1st degree: prolonged PR interval (>200ms = >5 small squares) — all impulses conducted but delayed at AV node. Benign. No treatment.\n2nd degree: some impulses not conducted from atria to ventricles.\n- Mobitz I (Wenckebach): progressively lengthening PR until a beat is dropped → cycles. Usually benign; occurs at AV node level.\n- Mobitz II: sudden non-conducted P-waves without prior PR prolongation. More dangerous; occurs at bundle branch level; risk of progression to complete block → pacemaker.\n3rd degree (complete): no AV conduction; atria and ventricles beat independently. Ventricular escape rate 20–40 bpm. Causes: inferior MI (usually reversible), fibrosis, digoxin toxicity. Treatment: urgent pacing."
    },
    # HYPERTENSION / STROKE (continued)
    {
        "id": "t5-r121",
        "question": "What is phaeochromocytoma and how does it cause hypertension?",
        "answer": "Phaeochromocytoma: a catecholamine-secreting tumour arising from the adrenal medulla (90%) or extra-adrenal chromaffin tissue (10% — called paraganglioma). Part of the 'rule of 10s': 10% malignant, 10% bilateral, 10% extra-adrenal, 10% familial (MEN2, VHL, NF1).\nMechanism: excess adrenaline and noradrenaline → vasoconstriction + raised heart rate → paroxysmal or sustained hypertension.\nPresentation: episodes of severe headache, palpitations, sweating, pallor, anxiety (the 5 Ps: Pressor episodes, Pain in head, Perspiration, Palpitations, Pallor).\nDiagnosis: 24-hour urinary catecholamines and metanephrines; plasma metanephrines; CT/MRI adrenal glands.\nTreatment: alpha-blockade FIRST (phenoxybenzamine), then beta-blockade; surgical resection. NEVER give beta-blockers first → unopposed alpha stimulation → hypertensive crisis."
    },
    {
        "id": "t5-r122",
        "question": "What are the renal causes of secondary hypertension?",
        "answer": "Secondary hypertension (10% of all hypertension). Renal causes (most common overall cause of secondary hypertension):\n1. Renovascular disease: renal artery stenosis (atherosclerotic — older smokers; fibromuscular dysplasia — young women) → reduced renal perfusion → RAAS activation → hypertension. Diagnosed by Doppler ultrasound, CT/MR angiography. Treatment: angioplasty + stenting; ACE inhibitors (but CONTRAINDICATED in bilateral RAS).\n2. Parenchymal renal disease: chronic kidney disease (CKD), glomerulonephritis, polycystic kidney disease, diabetic nephropathy → fluid overload + RAAS activation → hypertension.\n3. Renal tumour secreting renin (rare)"
    },
    {
        "id": "t5-r123",
        "question": "What is malignant hypertension and how does it present?",
        "answer": "Malignant (accelerated) hypertension: severe hypertension (typically diastolic >120–130 mmHg) with characteristic fundal changes (grade III/IV hypertensive retinopathy — flame haemorrhages, cotton wool spots; papilloedema in grade IV). Medical emergency.\nMechanism: extremely high pressure → damage to arteriolar walls → fibrinoid necrosis of vessel walls → end-organ ischaemia.\nFeatures:\n- Headache, visual disturbance, encephalopathy\n- Acute kidney injury (fibrinoid necrosis of renal arterioles)\n- Pulmonary oedema\n- Retinal haemorrhages, papilloedema (bilateral disc swelling)\nManagement: IV antihypertensives (labetalol, nicardipine); controlled BP reduction (not too rapid — risk of watershed infarction); target: reduce MAP by 20–25% over 1–2 hours."
    },
    {
        "id": "t5-r124",
        "question": "What is a lacunar infarct and what causes it?",
        "answer": "Lacunar infarct: small (<1.5cm) ischaemic stroke in the deep brain structures (internal capsule, basal ganglia, thalamus, pons, cerebellum), caused by occlusion of small penetrating arteries (lipohyalinosis — hyaline degeneration of small vessel walls caused by chronic hypertension and/or diabetes).\nClinical syndromes: pure motor stroke (most common — internal capsule), pure sensory stroke, ataxic hemiparesis, dysarthria-clumsy hand.\nFeatures: no cortical signs (no aphasia, no visual field defects, no loss of consciousness), gradual onset possible, often no identifiable embolic source.\nManagement: antiplatelet therapy, aggressive hypertension and diabetes control. Better prognosis than large cortical infarcts."
    },
    {
        "id": "t5-r125",
        "question": "What are the differences between ischaemic and haemorrhagic stroke in terms of causes, imaging, and management?",
        "answer": "Ischaemic stroke (85%): thrombosis or embolism (most from AF, cardiac thrombus, carotid plaque) → cerebral infarction. CT: normal initially, then hypodensity (dark area). Management: aspirin 300mg (if not haemorrhagic); thrombolysis (alteplase) within 4.5 hours of onset if no contraindications; thrombectomy for large vessel occlusions within 6–24 hours.\nHaemorrhagic stroke (15%): rupture of blood vessel into brain parenchyma (intracerebral haemorrhage) or subarachnoid space. Most common cause: hypertension. CT: hyperdensity (bright white blood). Management: reversal of anticoagulation (if applicable); surgical evacuation for some cerebellar haemorrhages; NO thrombolysis; BP lowering. Prognosis: generally worse than ischaemic stroke."
    },
    # PVD (continued)
    {
        "id": "t5-r126",
        "question": "What is Raynaud's phenomenon and how is it distinguished from Raynaud's disease?",
        "answer": "Raynaud's phenomenon: episodic vasospasm of digital arteries in response to cold or stress → colour changes: white (ischaemia) → blue (cyanosis) → red (reactive hyperaemia). Classic triphasic: white → blue → red.\nRaynaud's disease (primary): no underlying cause; young women; bilateral, symmetric; rarely progresses to tissue damage. Managed with lifestyle (avoid cold, gloves) and nifedipine (CCB — vasodilation).\nRaynaud's phenomenon (secondary): associated with underlying disease — autoimmune (systemic sclerosis, SLE, rheumatoid arthritis), thoracic outlet syndrome, vibration (hand-arm vibration syndrome — VWF), drugs (beta-blockers worsen Raynaud's — avoid), cervical rib. More severe; asymmetric; digital ulcers possible."
    },
    {
        "id": "t5-r127",
        "question": "What is coarctation of the aorta and what are its features?",
        "answer": "Coarctation of the aorta: congenital narrowing of the descending aorta, typically just distal to the origin of the left subclavian artery at the level of the ductus arteriosus (juxtaductal position).\nAssociations: Turner's syndrome (45,XO), bicuspid aortic valve (50%), berry aneurysms.\nFeatures:\n- Hypertension in upper limbs; reduced/delayed pulses in lower limbs ('radiofemoral delay')\n- Lower limb claudication\n- Chest X-ray: 'notching' of ribs (collateral intercostal arteries erode undersurface of ribs), '3 sign' (pre- and post-stenotic dilation of aorta)\nManagement: surgical correction or endovascular stenting. Untreated → premature death from heart failure, dissection, ruptured aneurysm."
    },
    {
        "id": "t5-r128",
        "question": "What is a saddle embolus and where does it typically lodge?",
        "answer": "A saddle embolus is a large thromboembolism that straddles a major arterial bifurcation — typically the bifurcation of the main pulmonary artery (saddle pulmonary embolism). It occludes both the left and right pulmonary artery branches.\nConsequences: massive pulmonary embolism → acute right heart failure → obstructive shock → rapid haemodynamic collapse. Mortality is very high (up to 30%).\nPresentation: sudden collapse, severe hypoxia, right heart strain on ECG (S1Q3T3 pattern, right bundle branch block, sinus tachycardia), hypotension.\nManagement: immediate systemic thrombolysis (alteplase); surgical embolectomy or catheter-directed therapy if thrombolysis contraindicated. IVC filter if anticoagulation contraindicated."
    },
    # ANTICOAGULANTS (continued)
    {
        "id": "t5-r129",
        "question": "What is heparin-induced thrombocytopenia (HIT) and why is it dangerous?",
        "answer": "HIT: paradoxical immune reaction to heparin that causes dangerous thrombosis despite low platelet count.\nType 1 HIT (non-immune): mild, transient thrombocytopenia in first 2 days; not clinically significant; platelet count recovers with continued heparin.\nType 2 HIT (immune-mediated): occurs 5–14 days after starting heparin. IgG antibodies form against heparin-platelet factor 4 (PF4) complex → immune complex activates platelets → platelet consumption (count falls >50%) + widespread thrombosis (venous and arterial).\nManagement: STOP all heparin immediately (including LMWH, heparin flushes). Switch to alternative anticoagulant (argatroban, danaparoid, fondaparinux, or DOAC). NEVER use warfarin in acute HIT (initial fall of protein C can worsen thrombosis)."
    },
    {
        "id": "t5-r130",
        "question": "What is the difference between dipyridamole and clopidogrel as antiplatelet agents?",
        "answer": "Dipyridamole: inhibits platelet phosphodiesterase → ↑ cyclic AMP → reduced platelet activation; also inhibits adenosine reuptake. Relatively weak antiplatelet. Combined with aspirin in modified-release form (Aggrenox) — used for secondary prevention after TIA/stroke (superior to aspirin alone for stroke prevention). Also used with warfarin in patients with prosthetic heart valves. Contraindicated in unstable angina (vasodilates coronary arteries → can precipitate ischaemia via coronary steal).\nClopidogrel: irreversible P2Y12 ADP receptor blocker. Stronger antiplatelet. Used: ACS, post-PCI (DAPT), PAD, alternative to aspirin in aspirin-intolerant patients. Prodrug: hepatic activation by CYP2C19 (poor metabolisers: reduced effect — PPI omeprazole inhibits CYP2C19)."
    },
    {
        "id": "t5-r131",
        "question": "What are the dental management considerations for a patient who has a coronary artery stent?",
        "answer": "Key issue: patients with stents are on antiplatelet therapy (usually DAPT: aspirin + clopidogrel/ticagrelor). Timing is critical:\n- Bare metal stent (BMS): DAPT for minimum 1 month post-stenting\n- Drug-eluting stent (DES): DAPT for minimum 12 months post-stenting (longer re-endothelialisation time)\nDental management:\n1. Do NOT stop DAPT — in-stent thrombosis risk is approximately 30–50% mortality\n2. Elective surgery: delay if possible until DAPT course is complete\n3. Urgent surgery on DAPT: discuss with cardiologist; continue DAPT; use local haemostatic measures\n4. Aspirin monotherapy after DAPT: continue; never stop before dental surgery\n5. Inform patient of bleeding risk; use local measures (sutures, tranexamic acid, pressure)"
    },
    {
        "id": "t5-r132",
        "question": "What is the coagulation cascade and which factors are in the intrinsic vs extrinsic pathway?",
        "answer": "Extrinsic pathway (triggered by tissue damage): tissue factor (TF) + Factor VII → activated Factor X → common pathway. Monitored by PT/INR.\nIntrinsic pathway (triggered by contact with damaged endothelium): Factor XII → XI → IX → VIII → activated Factor X → common pathway. Monitored by APTT.\nCommon pathway: Factor X + Factor V → prothrombin (Factor II) activator complex → prothrombin → thrombin → fibrinogen (Factor I) → fibrin → clot. Factor XIII cross-links fibrin.\nVitamin K-dependent factors: II, VII, IX, X (plus protein C and S). Warfarin inhibits all of these.\nHeparin: activates antithrombin III → inactivates thrombin (IIa) and Xa."
    },
    {
        "id": "t5-r133",
        "question": "What drug interactions raise the INR in patients taking warfarin that are relevant in dental practice?",
        "answer": "RAISE INR (increase bleeding risk) — drugs to avoid:\n1. Miconazole oral gel — most dangerous; CYP2C9 inhibitor; even topical form raises INR 5–10× → use NYSTATIN instead\n2. Fluconazole — potent CYP2C9/CYP3A4 inhibitor; single dose can significantly raise INR\n3. Metronidazole — CYP2C9 inhibitor + direct anticoagulant properties; commonly prescribed in dentistry — AVOID with warfarin\n4. Erythromycin / Clarithromycin — CYP3A4 inhibitors; raise INR significantly\n5. Amoxicillin — minor; disrupts gut flora producing vitamin K; modest INR rise\n6. NSAIDs — displace warfarin from protein binding + impair platelet function\nSAFE antibiotics: cefalexin, clindamycin (minimal interaction)"
    },
    {
        "id": "t5-r134",
        "question": "What is thrombolysis and when is it used in cardiovascular disease?",
        "answer": "Thrombolysis: pharmacological dissolution of existing blood clots using plasminogen activators.\nDrugs: alteplase (recombinant tPA — tissue plasminogen activator), streptokinase, reteplase, tenecteplase.\nMechanism: convert plasminogen → plasmin → digest fibrin in the clot.\nIndications:\n1. Acute STEMI: if primary PCI unavailable within 120 minutes; give within 12 hours of symptom onset; alteplase/tenecteplase preferred\n2. Massive pulmonary embolism: systemic alteplase if haemodynamically unstable\n3. Acute ischaemic stroke: alteplase within 4.5 hours of onset (if no contraindications)\nContraindications: active bleeding, recent major surgery/trauma (<10 days), stroke in last 3 months, severe hypertension, intracranial pathology"
    },
    # DENTAL IMPLICATIONS (continued)
    {
        "id": "t5-r135",
        "question": "What cardiovascular assessment should be performed before a dental procedure in a patient with significant heart disease?",
        "answer": "History:\n- Nature and severity of cardiac condition; last cardiologist review\n- Symptoms: chest pain at rest or minimal exertion (unstable angina), breathlessness lying flat (orthopnoea), ankle swelling, recent palpitations, syncope\n- Current medications (anticoagulants, antiplatelets, antihypertensives, anti-anginals)\n- Cardiac devices (pacemaker, ICD — card with model number)\n- Recent hospitalisations/procedures (recent MI, cardiac surgery)\nExamination:\n- BP (both arms), pulse rate and rhythm\n- Respiratory rate, oxygen saturation\n- Look for ankle oedema, raised JVP, cyanosis\nConsider: ECG monitoring in high-risk patients; pulse oximetry during treatment; consult cardiologist if significant concerns"
    },
    {
        "id": "t5-r136",
        "question": "What is the 'rule of halves' and how does it apply to hypertension in clinical practice?",
        "answer": "The 'rule of halves' (traditional observation in population studies):\n- Of all people with hypertension: only half are aware of it\n- Of those aware: only half are receiving treatment\n- Of those treated: only half have their BP adequately controlled\nThis explains why hypertension remains a leading cause of preventable stroke and MI — many patients are undiagnosed or undertreated. Dental relevance: patients may present with undetected hypertension. Routine BP measurement in dental practice can identify undiagnosed hypertension. If BP ≥180/110: defer non-urgent treatment; refer to GP urgently. If 140–180 systolic: note in records, inform GP, proceed with care."
    },
    {
        "id": "t5-r137",
        "question": "What are the side effects of beta-blockers relevant to dentistry?",
        "answer": "Oral/dental relevance:\n1. Xerostomia (dry mouth) — reduced salivary flow → dental caries risk, candidiasis, difficulty with dentures\n2. Increased tooth demineralisation — altered saliva composition\n3. Lichenoid reactions (rare) — white striae in oral mucosa, erosions\n\nSystemic concerns for dental management:\n4. Bronchospasm — non-selective beta-blockers (propranolol) contraindicated in asthma; if patient has asthma + beta-blocker, caution with LA adrenaline (theoretical bronchospasm, usually minor)\n5. Blunted hypoglycaemia awareness in diabetics — masks tachycardia warning sign of hypoglycaemia\n6. Bradycardia — pre-existing bradycardia may worsen with dental anxiety response\n7. Fatigue, cold extremities, vivid dreams"
    },
    {
        "id": "t5-r138",
        "question": "What specific considerations apply to the use of local anaesthetic in a patient taking non-selective beta-blockers?",
        "answer": "Non-selective beta-blockers (propranolol, nadolol, timolol): block both beta-1 and beta-2 receptors. Risk with adrenaline in LA: inadvertent intravascular injection of adrenaline → alpha-receptor stimulation causes vasoconstriction (BP rises) → with beta-2 receptor blocked, the normal reflex vasodilation cannot occur → unopposed alpha effect → significant hypertensive surge + reflex bradycardia.\nClinically: with careful aspiration technique and 1:80,000 or 1:100,000 adrenaline at normal doses (2–3 cartridges), this interaction is rarely significant.\nPractice: aspirate before injection; inject slowly; limit total adrenaline; monitor BP and pulse. In severe uncontrolled hypertension on non-selective beta-blocker: consider adrenaline-free LA (prilocaine with felypressin — Citanest)."
    },
    {
        "id": "t5-r139",
        "question": "What is the difference between felypressin and adrenaline as vasoconstrictors in local anaesthetic?",
        "answer": "Adrenaline (epinephrine): sympathomimetic; alpha + beta agonist → potent vasoconstriction (alpha-1) + cardiac stimulation (beta-1) + vasodilation in muscle (beta-2). Prolongs LA duration and depth. Concentration: 1:80,000 (12.5 micrograms/mL) in prilocaine 3% or articaine 4%; 1:100,000 (10 mcg/mL) in lidocaine 2%.\nFelypressin (octapressin): synthetic vasopressin analogue; acts on V1 vascular receptors → smooth muscle contraction → vasoconstriction WITHOUT cardiac effects. Used with prilocaine 3%. Safer in: cardiovascular disease patients, phaeochromocytoma, patients on MAOIs/TCAs. Contraindicated in: pregnancy (uterotonic effect). Duration slightly shorter than adrenaline."
    },
    {
        "id": "t5-r140",
        "question": "What are the key messages about preventing cardiovascular complications in the dental surgery?",
        "answer": "1. Take thorough medical history — identify undiagnosed/uncontrolled CVD\n2. Measure BP — defer treatment if severe hypertension (>180/110)\n3. Effective pain control — pain = catecholamine surge = cardiac stress. Use sufficient LA.\n4. Anxiety control — consider conscious sedation for anxious patients with CVD\n5. Morning appointments; shorter sessions\n6. Semi-reclined position for heart failure patients (cannot lie flat)\n7. GTN spray always available\n8. Know emergency protocols: angina, MI, cardiac arrest\n9. Do NOT stop anticoagulants/antiplatelets without consultation\n10. Avoid NSAID analgesics in heart failure and anticoagulated patients\n11. Avoid drug interactions: miconazole + warfarin; metronidazole + warfarin; clarithromycin raises QT"
    },
    # ADDITIONAL HIGH-YIELD TOPICS
    {
        "id": "t5-r141",
        "question": "What is the mechanism and use of ivabradine?",
        "answer": "Ivabradine: selective inhibitor of the I_f (funny/hyperpolarisation-activated cation) channel in the SA node → reduces spontaneous depolarisation rate of SA node → REDUCES HEART RATE ONLY (no effect on contractility, blood pressure, or AV conduction).\nAdvantages over beta-blockers: can be used in patients who cannot tolerate beta-blockers (e.g. asthma, severe COPD, peripheral arterial disease).\nIndications: chronic stable angina (in sinus rhythm, HR >70 bpm, when beta-blockers are insufficient or contraindicated); symptomatic heart failure with EF <35% and HR >70 bpm in sinus rhythm.\nSide effects: bradycardia, visual symptoms ('phosphenes' — light flashes due to retinal I_f channels), atrial fibrillation."
    },
    {
        "id": "t5-r142",
        "question": "What is ranolazine and how does it differ from other anti-anginal drugs?",
        "answer": "Ranolazine: inhibits the late (sustained) sodium current (I_Na-late) in cardiac myocytes → less sodium enters → less calcium overload (via the Na/Ca exchanger) → reduces myocardial oxygen demand without affecting heart rate or blood pressure.\nAdvantage: can be added to other anti-anginal drugs without further lowering HR or BP — useful when HR is already controlled but angina persists. Does not cause significant haemodynamic effects.\nIndications: chronic stable angina as add-on therapy when standard anti-anginals are insufficient.\nSide effects: QT prolongation (risk of torsade de pointes), nausea, dizziness, constipation. Inhibits CYP3A4 → multiple drug interactions. Avoid with strong CYP3A4 inhibitors (clarithromycin raises levels)."
    },
    {
        "id": "t5-r143",
        "question": "What is the mechanism of action of digoxin and what is its therapeutic use?",
        "answer": "Digoxin (cardiac glycoside): inhibits Na+/K+-ATPase pump on cardiac myocytes → intracellular Na+ rises → Na+/Ca2+ exchanger pumps less Na+ in and less Ca2+ out → intracellular Ca2+ rises → stronger contraction (positive inotrope).\nParasympathomimetic (vagolytic) effects: slows AV node conduction → reduces ventricular rate in AF; useful for rate control in AF.\nIndications: heart failure with AF (rate control); heart failure in sinus rhythm (mainly symptom improvement, no mortality benefit in sinus rhythm, unlike ACE inhibitors/beta-blockers).\nMonitoring: plasma digoxin level 6–8 hours post-dose (therapeutic: 0.5–2 ng/mL). Hypokalaemia greatly increases toxicity risk (K+ competes with digoxin at Na/K-ATPase)."
    },
    {
        "id": "t5-r144",
        "question": "What are the major risk factors for stroke and how does AF contribute?",
        "answer": "Major stroke risk factors:\n- Hypertension (most important modifiable risk factor — causes both ischaemic and haemorrhagic stroke)\n- Atrial fibrillation (5× increased stroke risk; causes cardioembolic ischaemic stroke from left atrial thrombus)\n- Carotid artery stenosis (>70% symptomatic stenosis → >15% annual stroke risk without endarterectomy)\n- Previous TIA or stroke (highest risk: 10–15% of TIAs → stroke within 90 days)\n- Diabetes mellitus (vascular disease acceleration)\n- Smoking, hypercholesterolaemia, obesity\n- Hypercoagulable states (antiphospholipid syndrome, malignancy)\nAF contribution: loss of atrial contraction → blood pools in left atrial appendage → thrombus formation → embolism to cerebral circulation → stroke. AF-related strokes: typically larger and more disabling than other causes."
    },
    {
        "id": "t5-r145",
        "question": "What is infective endocarditis prophylaxis in the context of non-dental procedures?",
        "answer": "IE prophylaxis beyond dentistry:\n- Genitourinary/gastrointestinal procedures: antibiotic prophylaxis NOT recommended (NICE/AHA) — insufficient evidence\n- Body piercing/tattooing: high-risk patients (previous IE, prosthetic valves) should be strongly advised AGAINST body piercing/tattooing — the bacteraemia from contaminated equipment (non-sterile needles) carries significant IE risk; inform patients\n- IVDU (IV drug abuse): highest-risk situation for right-sided IE (Staphylococcus aureus); no specific prophylaxis; harm reduction strategies (clean needles) are the intervention\n- Respiratory tract instrumentation: no routine prophylaxis\nKey message: good oral hygiene, skin hygiene, and avoidance of high-risk practices are the mainstays of IE prevention."
    },
    {
        "id": "t5-r146",
        "question": "What causes atrial fibrillation and what are the main underlying conditions?",
        "answer": "AF causes (mnemonic: PIRATES):\nP — Pulmonary: PE, pneumonia, COPD\nI — Ischaemic heart disease/Infarction\nR — Rheumatic heart disease (mitral stenosis — most common valvular cause of AF)\nA — Anaemia, Anaesthetic complication\nT — Thyrotoxicosis (hyperthyroidism — key cause to exclude; even subclinical hyperthyroidism can cause AF)\nE — Electrolytes (hypokalaemia, hypomagnesaemia)\nS — Sepsis, Stroke, Sick sinus syndrome\nAlso: hypertension, alcohol excess ('holiday heart'), cardiac surgery, cardiomyopathy, idiopathic/lone AF (structurally normal heart, usually younger patients).\nThyroid function tests are mandatory in all new AF diagnoses."
    },
    {
        "id": "t5-r147",
        "question": "What is the difference between stable and unstable heart failure and why does this matter for drug therapy?",
        "answer": "Stable heart failure: chronic compensated state — patient not acutely short of breath at rest; no new oedema; stable weight; haemodynamically stable. In this state:\n- Beta-blockers CAN be introduced and up-titrated (long-term mortality benefit)\n- ACE inhibitors and spironolactone are continued/adjusted\n- Target: highest tolerated dose of ACE inhibitor and beta-blocker\nUnstable/decompensated heart failure: acutely breathless, wet rales, new oedema, hypoxia, haemodynamic compromise. In this state:\n- Beta-blockers should NOT be started or increased (may worsen acute decompensation)\n- IV furosemide for diuresis\n- May need to halve or stop beta-blocker temporarily\n- IV nitrates, inotropes (dobutamine) if severe\nDental relevance: patient in decompensated HF cannot safely have elective dental treatment — treat emergencies only."
    },
    {
        "id": "t5-r148",
        "question": "What is the most common cause of death in patients with peripheral arterial disease?",
        "answer": "The most common cause of death in patients with PAD is myocardial infarction, not limb loss. This is because PAD is a systemic atherosclerotic disease — patients with leg artery disease almost certainly have coronary artery disease as well.\nStatistics:\n- 20% of PAD patients die from MI within 5 years of diagnosis\n- Amputation is required in only ~3%\n- Annual major cardiovascular event rate (MI, stroke, death): ~5–7%\nThis explains why PAD management focuses on:\n1. Reducing cardiovascular risk (statins, antihypertensives, smoking cessation, antiplatelet therapy)\n2. Not just treating the legs\nAll PAD patients should be on: aspirin or clopidogrel + statin + antihypertensive; and aggressive lifestyle modification."
    },
    {
        "id": "t5-r149",
        "question": "What is 'takotsubo' (stress) cardiomyopathy?",
        "answer": "Takotsubo (apical ballooning syndrome, 'broken heart syndrome'): transient left ventricular dysfunction — the apex of the LV balloons out and the base contracts normally during systole (mimics the Japanese octopus trap 'tako-tsubo' shape on ventriculography).\nTrigger: intense emotional or physical stress (bereavement, medical procedure, natural disaster) → massive catecholamine surge → coronary artery spasm or direct myocardial toxicity.\nPatients: predominantly post-menopausal women (oestrogen protection lost).\nPresentation: acute chest pain + ECG changes (ST elevation, T-wave inversion) + elevated troponin — mimics STEMI but coronary angiography shows NO culpable coronary artery disease.\nPrognosis: usually full recovery in 4–8 weeks. Rarely fatal.\nDental relevance: a highly emotional dental appointment could theoretically trigger this."
    },
    {
        "id": "t5-r150",
        "question": "What is hypertrophic cardiomyopathy (HCM) and why does it cause sudden death?",
        "answer": "HCM: autosomal dominant genetic disorder of sarcomeric proteins (most commonly beta-myosin heavy chain or myosin-binding protein C mutations) → inappropriate and asymmetric hypertrophy of the LV myocardium, particularly the interventricular septum.\nFeatures:\n- Diastolic dysfunction (stiff LV cannot fill properly)\n- LV outflow tract obstruction (LVOTO) in ~25% — dynamic obstruction worsens with dehydration/vasodilation/tachycardia\n- Mitral regurgitation (anterior mitral leaflet pulled into LVOTO — SAM: systolic anterior motion)\nSudden death cause: ventricular arrhythmias (VF) from chaotic disorganised myofibril arrangement (myofibre disarray histologically). Leading cause of sudden cardiac death in young athletes (<35 years). Management: ICD implantation for high-risk patients; avoid dehydration, competitive sport."
    },
    # ADDITIONAL PHARMACOLOGY
    {
        "id": "t5-r151",
        "question": "What are calcium channel blockers and how do their three subclasses differ?",
        "answer": "All block voltage-gated L-type calcium channels → less Ca2+ enters cells.\nThree subclasses:\n1. Dihydropyridines (amlodipine, nifedipine, felodipine): act predominantly on vascular smooth muscle → vasodilation → lower BP; minimal cardiac conduction effect. Use: hypertension, angina (vasodilatory). Side effects: gingival hyperplasia, flushing, peripheral oedema, reflex tachycardia.\n2. Benzothiazines (diltiazem): mixed cardiac and vascular effects → moderate rate slowing + vasodilation. Use: AF rate control, angina, some hypertension. Side effects: bradycardia, constipation.\n3. Phenylalkylamines (verapamil): predominant cardiac effect → slows SA and AV nodes (rate control). Use: SVT, AF rate control, some angina. Side effects: severe bradycardia, heart block, constipation, heart failure exacerbation. NEVER combine with beta-blockers (cardiac arrest risk)."
    },
    {
        "id": "t5-r152",
        "question": "What is the mechanism of action of ACE inhibitors and ARBs, and how do they differ in side effects?",
        "answer": "ACE inhibitors (lisinopril, ramipril, enalapril): inhibit angiotensin-converting enzyme → prevent Ang I → Ang II conversion → reduce aldosterone, vasoconstriction, and sympathetic activation. Also block bradykinin degradation → bradykinin accumulates → cough (in 10–15%).\nARBs (losartan, candesartan, valsartan): directly block AT1 angiotensin receptors → same downstream effects as ACE inhibitors (reduce aldosterone, vasodilate). Do NOT affect bradykinin → NO cough.\nBoth contraindicated: bilateral renal artery stenosis, pregnancy, hyperkalaemia.\nBoth can cause: angioedema (ARBs rare but can cross-react in ACE inhibitor-induced angioedema; some patients develop angioedema on both — this is important clinically).\nKey: ARB is the substitute when ACE inhibitor cough is intolerable."
    },
    {
        "id": "t5-r153",
        "question": "What is the mechanism and main uses of furosemide (frusemide) compared with thiazide diuretics?",
        "answer": "Furosemide (loop diuretic): inhibits Na+/K+/2Cl− cotransporter (NKCC2) in the thick ascending limb of loop of Henle → most potent diuretic (10-fold urine increase). Rapid onset (30 min oral, 5 min IV). Used: acute pulmonary oedema, decompensated heart failure, resistant hypertension. Hypokalaemia, hyponatraemia, ototoxicity, gout, hypomagnesaemia.\nThiazide/thiazide-like (bendroflumethiazide, indapamide, hydrochlorothiazide): inhibit Na+/Cl− cotransporter (NCC) in the distal convoluted tubule → moderate diuresis. Slower onset. Used: hypertension (first-line), mild oedema. Side effects: hypokalaemia, hyponatraemia, hyperuricaemia (gout), hyperglycaemia, hyperlipidaemia, hypercalcaemia. Ineffective in GFR <30 mL/min (switch to loop diuretic)."
    },
    {
        "id": "t5-r154",
        "question": "What is the mechanism of action of statins and which drug interactions are clinically important?",
        "answer": "Statins (atorvastatin, simvastatin, rosuvastatin, pravastatin): competitive inhibitors of HMG-CoA reductase (the rate-limiting enzyme in cholesterol biosynthesis in the liver) → reduced hepatic cholesterol production → upregulation of LDL receptors → increased LDL uptake from plasma → LDL-C lowered by 30–50%. Also: anti-inflammatory, plaque-stabilising effects.\nDrug interactions:\n- Simvastatin/lovastatin metabolised by CYP3A4: clarithromycin, erythromycin, diltiazem, verapamil, antifungals (ketoconazole) raise statin levels → myopathy/rhabdomyolysis risk\n- Fibrates (gemfibrozil) + statins → myopathy risk\n- Warfarin + atorvastatin → modest INR rise (monitor)\nSafe to use: atorvastatin (dental antibiotics: use azithromycin instead of clarithromycin in statin patients; cefalexin is safe)"
    },
    {
        "id": "t5-r155",
        "question": "What are the electrocardiographic features of atrial fibrillation?",
        "answer": "ECG features of AF:\n1. Absent P waves (replaced by irregular fibrillatory baseline — 'f' waves — at 350–600 bpm; best seen in V1 and limb leads)\n2. Irregularly irregular R-R intervals — the most characteristic feature (the ventricular response is completely irregular due to random conduction through the AV node)\n3. Narrow QRS complexes (unless aberrant conduction or bundle branch block)\n4. Ventricular rate: typically 100–160 bpm if untreated (AV node limits rate)\n5. No clear relationship between atrial and ventricular activity\nDistinguish from: atrial flutter (regular sawtooth flutter waves at ~300 bpm; regular or regularly irregular ventricular rate with fixed AV block e.g. 2:1, 3:1)"
    },
    {
        "id": "t5-r156",
        "question": "What is familial hypercholesterolaemia and how is it diagnosed?",
        "answer": "Familial hypercholesterolaemia (FH): autosomal dominant genetic condition causing severely elevated LDL cholesterol from birth (LDL typically >5 mmol/L). Most common: mutations in LDL receptor gene (LDLR), apolipoprotein B (APOB), or PCSK9. Affects 1 in 250 people (commonest serious inherited metabolic disorder).\nClinical signs:\n- Xanthomas (cholesterol deposits in tendons — Achilles, extensor tendons of hand)\n- Xanthelasma (periorbital yellow plaques)\n- Corneal arcus (white/grey ring at corneal periphery — more significant under 45)\n- Premature cardiovascular disease (<55 in men, <65 in women)\nDiagnosis: Simon Broome criteria (clinical + genetic); cascade testing of first-degree relatives.\nManagement: high-intensity statin from early life; add ezetimibe; PCSK9 inhibitors (alirocumab, evolocumab) for very high-risk."
    },
    {
        "id": "t5-r157",
        "question": "What is a pulmonary embolism (PE) and how does it present?",
        "answer": "PE: obstruction of a pulmonary artery or branch by a thrombus (usually from DVT). Reduces pulmonary blood flow → ventilation-perfusion (V/Q) mismatch → hypoxia; right heart strain.\nClassification: massive (haemodynamically unstable, obstructive shock), submassive (right heart strain but stable), low-risk.\nPresentation:\n- Pleuritic chest pain (sharp, worse on breathing; from pleural irritation)\n- Breathlessness (sudden onset)\n- Haemoptysis (blood-stained sputum)\n- Tachycardia, tachypnoea\n- Hypoxia on pulse oximetry\n- Signs of DVT (swollen calf)\nInvestigation: D-dimer (if low pre-test probability and negative → PE excluded); CT pulmonary angiography (CTPA — gold standard); V/Q scan.\nECG: sinus tachycardia (most common); S1Q3T3 pattern (classic but uncommon); RBBB."
    },
    {
        "id": "t5-r158",
        "question": "What are the haemodynamic effects of aortic stenosis on the heart?",
        "answer": "Aortic stenosis → progressively narrowed aortic valve orifice → increased resistance to LV outflow.\nCompensation: LV hypertrophies concentrically (wall thickens without cavity dilation — pressure overload response) → maintains cardiac output at rest but reduces diastolic compliance.\nDecompensation (when compensation fails):\n1. Fixed cardiac output → cannot increase CO on exertion → syncope, dizziness\n2. Coronary blood flow impaired (LV wall thickened → compresses coronary ostia; high LV end-diastolic pressure reduces diastolic coronary perfusion) → angina\n3. Eventually LV fails → dilates → pulmonary oedema → heart failure\nNatural history: long asymptomatic period → once symptomatic (angina, syncope, heart failure): rapid deterioration without valve replacement. Median survival from: angina = 5 years; syncope = 3 years; heart failure = 1–2 years."
    },
    {
        "id": "t5-r159",
        "question": "What is mitral stenosis and what are its haemodynamic consequences?",
        "answer": "Mitral stenosis: narrowing of the mitral valve orifice (normal area 4–6 cm²; critical stenosis <1 cm²) → obstruction to LV filling.\nCauses: rheumatic fever (most common worldwide), congenital, carcinoid syndrome, mucopolysaccharidoses.\nHaemodynamics: impaired LV filling → low cardiac output → blood dams back in left atrium → raised left atrial pressure → raised pulmonary venous pressure → pulmonary oedema.\nConsequences:\n- Left atrial dilation → AF (very common — ~40% of MS patients)\n- Pulmonary hypertension → right heart failure (Cor Pulmonale)\n- Systemic emboli (AF + dilated LA → thrombus → stroke)\nSymptoms: breathlessness on exertion, haemoptysis (from pulmonary congestion), palpitations (AF), embolic stroke.\nDiagnosis: echo (gradient across mitral valve, valve area). Treatment: mitral valvuloplasty or valve replacement."
    },
    {
        "id": "t5-r160",
        "question": "What is the Wells score for DVT and how is it used?",
        "answer": "The Wells score estimates the clinical pre-test probability of DVT:\nScore 1 point each for:\n- Active cancer (treatment within 6 months)\n- Paralysis/paresis/plaster cast of leg\n- Bedridden >3 days or major surgery within 12 weeks\n- Localised tenderness along deep vein system\n- Entire leg swollen\n- Calf swelling >3cm compared to asymptomatic leg\n- Pitting oedema confined to symptomatic leg\n- Collateral superficial veins\n- Previous DVT\nMinus 2 points: alternative diagnosis at least as likely as DVT\n\nInterpretation:\nScore ≥2: high probability → directly to compression duplex ultrasound\nScore 0–1: low probability → D-dimer first; if positive → ultrasound; if negative → DVT excluded"
    },
    {
        "id": "t5-r161",
        "question": "What are the clinical features of right-sided heart failure?",
        "answer": "Right-sided heart failure (RHF): blood dams back in the systemic venous system.\nSigns and symptoms:\n- Peripheral oedema: pitting oedema of ankles and legs (gravity-dependent); sacral oedema in bedbound patients\n- Raised jugular venous pressure (JVP): visible pulsation in jugular veins >3cm above sternal angle\n- Hepatomegaly: hepatic congestion → right upper quadrant discomfort; pulsatile liver in tricuspid regurgitation\n- Ascites: severe RHF → portal hypertension-like picture\n- Fatigue, poor exercise tolerance\n- Nausea, anorexia (bowel oedema)\n- Pleural effusions (bilateral in biventricular failure; right-sided in isolated RHF)\n- Weight gain (fluid retention)\nCauses: LVF (most common cause of RVF), cor pulmonale, right ventricular MI, pulmonary hypertension, tricuspid valve disease."
    },
    {
        "id": "t5-r162",
        "question": "What is the ABCD² score for TIA risk stratification?",
        "answer": "ABCD² score predicts short-term stroke risk after a TIA:\nA — Age: ≥60 years (1 point)\nB — Blood pressure: systolic ≥140 OR diastolic ≥90 (1 point)\nC — Clinical features: unilateral weakness (2 points); speech disturbance without weakness (1 point)\nD — Duration: ≥60 minutes (2 points); 10–59 minutes (1 point)\nD — Diabetes mellitus: present (1 point)\n\nTotal: 0–7 points\nHigh risk (≥4): refer as emergency ('TIA clinic within 24 hours'); approximately 8% stroke risk at 2 days\nLow risk (0–3): specialist assessment within 7 days\nAll high-risk TIA: aspirin 300mg immediately; statin; BP control; anticoagulate if AF identified"
    },
    {
        "id": "t5-r163",
        "question": "What is the link between periodontal disease and infective endocarditis?",
        "answer": "Connection: both the oral flora and IE share key organisms — oral streptococci (S. sanguis, S. mutans, S. oralis) are part of normal dental plaque and cause subacute bacterial endocarditis.\nBacteraemia: dental procedures (extractions, scaling) and even routine tooth brushing release these organisms into the bloodstream. In most people this is harmless, but in those with damaged/prosthetic valves, bacteria can adhere to valve surfaces and establish infection.\nPrevention: the strongest evidence-based intervention is excellent oral hygiene — reducing dental plaque reduces the frequency and magnitude of bacteraemia from daily activities far more effectively than pre-procedural antibiotic prophylaxis.\nClinical message: regular dental review, effective plaque control, and prompt treatment of periodontal disease are the highest-value IE prevention strategies."
    },
    {
        "id": "t5-r164",
        "question": "What is the difference between acute and subacute infective endocarditis in terms of causative organisms and clinical course?",
        "answer": "Acute IE: virulent organisms on previously NORMAL valves; rapid progression over days to weeks; high mortality.\n- Organism: Staphylococcus aureus (most common; also MRSA)\n- Features: high fever (>39°C), septic emboli, rapid valve destruction, septic shock\n- Mortality: 25–47%\nSubacute IE: less virulent organisms on DAMAGED/ABNORMAL valves; indolent course over weeks to months.\n- Organisms: Streptococcus viridans (oral streptococci — most common in dental context), HACEK organisms, Enterococcus faecalis\n- Features: low-grade fever, fatigue, weight loss, sweats, malaise; peripheral stigmata (Osler's nodes, Janeway lesions) develop over time\n- Mortality: lower (10–20% with treatment)"
    },
    {
        "id": "t5-r165",
        "question": "What is HOCM (hypertrophic obstructive cardiomyopathy) and what are its dental implications?",
        "answer": "HOCM: a form of hypertrophic cardiomyopathy where the thickened septum causes dynamic left ventricular outflow tract obstruction during systole, worsened by: reduced preload (dehydration, hypovolaemia, vasodilation), tachycardia, increased contractility.\nSymptoms: dyspnoea, angina, syncope (especially on exertion), palpitations, sudden death.\nMurmur: ejection systolic murmur at LSE, increases with Valsalva (reduces preload) and decreases on squatting (increases preload).\nDental implications:\n- Adequate hydration before procedure (maintain preload)\n- Effective LA (avoid pain/anxiety → tachycardia that worsens LVOTO)\n- Avoid tachycardia-inducing agents (excessive adrenaline)\n- May need IE prophylaxis assessment (significant LVOTO with MR)\n- Avoid vasodilators\n- Check for ICD/pacemaker (if implanted)"
    },
    {
        "id": "t5-r166",
        "question": "What is a Berry aneurysm versus a fusiform aneurysm?",
        "answer": "Berry (saccular) aneurysm: sac-like outpouching from ONE wall of an artery, typically at a bifurcation. Found in cerebral circulation (circle of Willis). Associated with polycystic kidney disease, Marfan's, coarctation. Thin wall susceptible to rupture → subarachnoid haemorrhage.\nFusiform aneurysm: entire circumference of the artery is dilated (no sac — the artery bulges outward symmetrically). Caused by atherosclerosis and hypertension. Common in the abdominal aorta (AAA). Rarely rupture suddenly; gradually expand; repaired at >5.5cm.\nKey difference: Berry = focal sac at bifurcation (often cerebral), high rupture risk at relatively small size; Fusiform = diffuse dilation of entire segment (often aorta), larger before rupture risk exceeds surgical risk."
    },
    {
        "id": "t5-r167",
        "question": "What is a VSD (ventricular septal defect) and what is its relevance to infective endocarditis?",
        "answer": "VSD: congenital defect (hole) in the interventricular septum. Most common congenital heart defect.\nHaemodynamics: left-to-right shunt (LV pressure > RV pressure) → increased blood flow through lungs → pulmonary hypertension if large and untreated (Eisenmenger syndrome: shunt eventually reverses → cyanosis).\nIE relevance: high-velocity jet through VSD damages the RV endocardium at the site of impact (jet lesion) → predisposes to IE, specifically on the RV wall. VSDs are a congenital IE risk factor.\nDental management: moderate-risk category for IE. Antibiotic prophylaxis is debated (NICE: not routinely recommended). Small, isolated muscular VSDs may close spontaneously. Large VSDs require surgical or catheter-based closure.\nOther congenital defects with IE risk: patent ductus arteriosus, tetralogy of Fallot, bicuspid aortic valve."
    },
    {
        "id": "t5-r168",
        "question": "What is cardiac tamponade and how is it recognised?",
        "answer": "Cardiac tamponade: compression of the heart by fluid (blood, effusion) in the pericardial sac → impairs cardiac filling → falls in cardiac output → haemodynamic collapse.\nCauses: haemopericardium (MI rupture, aortic dissection, trauma), pericarditis, malignancy, iatrogenic (post-cardiac surgery/catheterisation).\nBeck's triad:\n1. Hypotension (low CO)\n2. Raised JVP (obstructed venous return)\n3. Muffled/quiet heart sounds (fluid cushions heart)\nOther signs: pulsus paradoxus (BP falls >10 mmHg on inspiration — increased RV filling on inspiration compresses LV); electrical alternans on ECG (swinging heart in pericardial fluid).\nManagement: emergency pericardiocentesis (needle drainage via subxiphoid approach); surgical drainage if blood clot."
    },
    {
        "id": "t5-r169",
        "question": "What is the most important initial investigation and management step in suspected acute MI in the dental surgery?",
        "answer": "Initial investigation: 12-lead ECG is the single most important initial investigation (identifies STEMI with ST elevation → requires immediate primary PCI; differentiates STEMI from NSTEMI, arrhythmia, pericarditis).\nIn dental surgery scenario:\n1. Call 999 (first and most important)\n2. Administer aspirin 300mg CHEWED (not swallowed whole — chewing speeds absorption)\n3. Give supplemental oxygen IF SpO2 < 94% (do NOT give oxygen routinely if normoxic — hyperoxia post-MI may be harmful)\n4. GTN spray if systolic BP >90 mmHg (do NOT if patient took phosphodiesterase-5 inhibitor in last 24 hours)\n5. Lie patient flat (unless pulmonary oedema — then sit up); reassure; monitor pulse\n6. Be prepared to start CPR and use AED if cardiac arrest occurs"
    },
    {
        "id": "t5-r170",
        "question": "What is the significance of splinter haemorrhages in infective endocarditis?",
        "answer": "Splinter haemorrhages: longitudinal dark red/brown streaks under the fingernails or toenails, running in the direction of nail growth (parallel to long axis of nail).\nCauses:\n1. Infective endocarditis (septic microemboli in nail bed capillaries) — clinically significant when MULTIPLE (>4–5) and proximal (near the proximal nail fold)\n2. Trauma (most common cause overall — usually ONE or TWO, distal location, fading from the distal end)\n3. Vasculitis, anti-phospholipid syndrome, septicaemia, renal disease\nIn IE context: part of the peripheral vasculitic manifestations (also: Osler's nodes, Janeway lesions, Roth spots, petechiae). More than 8 splinter haemorrhages in a febrile patient should raise strong suspicion for IE.\nMinor Duke criterion: 'vascular phenomena' includes splinter haemorrhages."
    },
    {
        "id": "t5-r171",
        "question": "What is the difference between cardiac ischaemia and cardiac infarction at the cellular level?",
        "answer": "Ischaemia (reversible injury): insufficient O2 delivery → anaerobic glycolysis → ATP falls → pump failure → cell swelling (cytotoxic oedema) → ionic imbalance (Na+/Ca2+ overload). At this stage: if blood flow is restored (reperfusion), the myocyte RECOVERS completely (no permanent damage). ECG: transient ST changes. No troponin rise.\nInfarction (irreversible injury): sustained ischaemia beyond the point of no return (approximately 20–40 minutes in vulnerable territory) → mitochondrial dysfunction → membrane disruption → cell death (coagulative necrosis → inflammatory infiltrate → macrophage removal → fibrosis). Troponin leaks from necrotic cells → elevated in blood. ECG: persistent ST changes, Q-wave formation. Scar replaces dead myocardium (myocytes cannot regenerate)."
    },
    {
        "id": "t5-r172",
        "question": "What are the causes and clinical features of pericarditis?",
        "answer": "Pericarditis: inflammation of the pericardium.\nCauses: viral (most common — Coxsackie B, echovirus, influenza; often post-viral); bacterial (Staphylococcus, TB — uncommon in immunocompetent); post-MI (Dressler's syndrome: 2–6 weeks after MI — autoimmune; also acute pericarditis within 24 hours of transmural MI); uraemia (renal failure); malignancy; autoimmune (SLE, RA).\nSymptoms: pleuritic chest pain (sharp, stabbing; worse on lying flat, inspiration; relieved by sitting forward — pathognomonic), fever, malaise.\nSigns: pericardial friction rub (scratching/grating sound in synchrony with heartbeat); ECG: saddle-shaped ST elevation in multiple leads (diffuse, no reciprocal changes — unlike MI).\nTreatment: aspirin or ibuprofen + colchicine (reduces recurrence)."
    },
    {
        "id": "t5-r173",
        "question": "What is the role of the implantable cardioverter defibrillator (ICD) and who needs one?",
        "answer": "ICD: a device implanted subcutaneously with leads in the heart that continuously monitors rhythm and can: (1) detect and treat ventricular fibrillation or pulseless VT with an internal shock (defibrillation); (2) detect and overdrive-pace ventricular tachycardia; (3) act as a pacemaker for bradyarrhythmias.\nIndications:\nPrimary prevention: high risk of sudden cardiac death without previous episode. EF <35% despite optimal medical therapy ≥3 months; some inherited channelopathies (LQTS, Brugada, HCM); previous sustained VT without haemodynamic compromise.\nSecondary prevention: survived cardiac arrest from VF/VT; sustained VT with haemodynamic compromise.\nDental consideration: ICD shock therapy may rarely be triggered by electromagnetic interference from some dental equipment. Carry ICD identification card; contact cardiologist if uncertain about specific equipment."
    },
    {
        "id": "t5-r174",
        "question": "What are the clinical features that distinguish a myocardial infarction from an angina attack in the dental chair?",
        "answer": "Feature comparison:\nAngina in dental chair:\n- Known cardiac history, similar pain to usual attacks\n- Onset with treatment (stress/pain)\n- Resolves with GTN within 3–5 minutes\n- Pain character: typical tightness, may be mild-moderate\n- Patient usually not acutely unwell\n\nMI in dental chair:\n- Pain may be more severe and crushing\n- NOT relieved by GTN after two doses (5 min apart)\n- May occur at rest or with minimal stimulation\n- Associated features: profound sweating, pallor, nausea, vomiting, breathlessness\n- Patient looks acutely unwell; may become confused\n- If GTN has not worked after two doses → treat as MI; call 999; give aspirin 300mg chewed"
    },
    {
        "id": "t5-r175",
        "question": "What is the clinical significance of a new murmur in a febrile patient?",
        "answer": "A new or changing heart murmur in a febrile patient should be considered infective endocarditis until proven otherwise.\nPathophysiology: IE vegetations on valve leaflets distort valvular closure → new regurgitant murmur (most commonly — IE causes regurgitation by preventing valve closure or by perforating leaflets). Less commonly: large vegetations can cause stenotic murmur.\nImportance: new murmur + fever = major clinical sign of IE (a major Duke criterion requires echocardiographic evidence, but new murmur on auscultation combined with fever and positive blood cultures strongly supports the diagnosis).\nManagement: blood cultures × 3 before starting antibiotics; transthoracic echo; consult cardiology/infectious diseases. IV antibiotics for 4–6 weeks (penicillin + gentamicin for streptococcal; flucloxacillin + gentamicin for staphylococcal)."
    },
    {
        "id": "t5-r176",
        "question": "What is the difference between a shunt left-to-right versus right-to-left in congenital heart disease?",
        "answer": "Left-to-right shunt (acyanotic): oxygenated blood shunts back to pulmonary circulation → increased pulmonary blood flow. Examples: ASD, VSD, PDA.\nConsequences: increased pulmonary blood flow → pulmonary hypertension → RV hypertrophy. Initially acyanotic ('pink baby'). If uncorrected: Eisenmenger syndrome — pulmonary hypertension becomes severe → RV pressure exceeds LV → shunt REVERSES (right-to-left) → deoxygenated blood enters systemic circulation → cyanosis (now a cyanotic condition). Eisenmenger syndrome is irreversible — surgical correction no longer possible.\nRight-to-left shunt (cyanotic): deoxygenated blood enters systemic circulation directly → cyanosis from birth. Examples: tetralogy of Fallot (most common), transposition of the great arteries, tricuspid atresia."
    },
    {
        "id": "t5-r177",
        "question": "What is Tetralogy of Fallot and what are its four components?",
        "answer": "Tetralogy of Fallot: most common CYANOTIC congenital heart defect.\nFour components (mnemonic: PROVE):\n1. Pulmonary stenosis (right ventricular outflow tract obstruction) — the key abnormality\n2. Right ventricular hypertrophy (consequence of obstruction)\n3. Overriding aorta (aorta sits astride the VSD, receiving blood from both ventricles)\n4. VSD (ventricular septal defect — communication between the two ventricles)\nPhysiology: RV pressure > LV → right-to-left shunt at VSD → deoxygenated blood enters aorta → cyanosis ('blue baby').\n'Tet spells': episodes of severe hypoxia → infants squat (increases afterload, reduces shunt) to relieve symptoms.\nManagement: surgical correction usually in first year of life. IE risk: significant → higher risk category."
    },
    {
        "id": "t5-r178",
        "question": "What is ankle oedema and how do you distinguish cardiac from non-cardiac causes?",
        "answer": "Ankle oedema: pitting oedema (leaves a pit when pressed) of the ankles and lower legs. Bilateral usually suggests systemic cause.\nCardiac causes (right heart failure): bilateral pitting oedema; raised JVP (key distinguishing sign); hepatomegaly; breathlessness; history of IHD/valvular disease. BNP elevated.\nOther causes:\n- Hypoalbuminaemia (nephrotic syndrome, liver disease, malnutrition) — bilateral; JVP normal\n- Venous insufficiency (varicose veins, DVT) — usually unilateral or asymmetric; no raised JVP; skin changes (lipodermatosclerosis, haemosiderin)\n- Lymphoedema — non-pitting; firm; history of cancer treatment, filariasis\n- Drug-induced: CCBs (amlodipine — very common, not cardiac failure; pitting, symmetrical; no JVP elevation)\n- Dependency oedema: immobility; disappears overnight with leg elevation"
    },
    {
        "id": "t5-r179",
        "question": "What is meant by 'cardiac output reserve' and how is it relevant to dental treatment?",
        "answer": "Cardiac output reserve: the ability of the heart to increase its output above resting levels in response to physiological demands (exercise, stress, infection). Measured as the difference between maximum possible CO and resting CO.\nHealthy heart: can increase CO from 5 L/min at rest to 20–25 L/min during maximal exercise (CO reserve of ~15–20 L/min).\nFailing heart: resting CO is maintained only through compensatory mechanisms (tachycardia, neurohormonal activation); CO reserve is markedly reduced — cannot increase adequately on demand.\nDental relevance: a patient with severely impaired cardiac output reserve cannot safely cope with the added cardiovascular stress of a painful, anxiety-provoking dental procedure. This is why: effective LA (eliminate pain), anxiety management, shorter appointments, and morning scheduling are critical for patients with significant heart failure."
    },
    {
        "id": "t5-r180",
        "question": "What are the differences between the three main types of shock relevant to cardiology?",
        "answer": "Cardiogenic shock: the heart cannot pump adequately → low cardiac output → hypotension + signs of poor perfusion (cold, clammy, oliguric, confused). Causes: massive MI, acute heart failure, severe arrhythmia, tension pneumothorax, cardiac tamponade. Raised JVP, pulmonary oedema. Treatment: inotropes (dobutamine), intra-aortic balloon pump, revascularisation.\nDistributive shock: widespread vasodilation → low SVR → hypotension despite normal/high CO. Causes: septic shock (most common), anaphylaxis, neurogenic. Warm, flushed, raised CO.\nObstructive shock: mechanical obstruction to blood flow. Causes: massive PE (pulmonary artery obstruction), cardiac tamponade (pericardial compression). Raised JVP + hypotension. Treatment: relieve obstruction (thrombolysis for PE, pericardiocentesis for tamponade)."
    },
    # ADDITIONAL DENTAL CVD OVERLAP
    {
        "id": "t5-r181",
        "question": "What is defibrillation and what are the two shockable rhythms?",
        "answer": "Defibrillation: delivery of a high-energy electrical shock to the heart to terminate a lethal arrhythmia by simultaneously depolarising all cardiac myocytes, allowing the SA node to resume normal pacemaker function.\nShockable rhythms:\n1. Ventricular fibrillation (VF): disorganised electrical activity; no coordinated contraction; no cardiac output → cardiac arrest\n2. Pulseless ventricular tachycardia (pVT): organised but rapid ventricular activity (usually >150 bpm) without effective contraction or pulses → cardiac arrest\nNon-shockable rhythms (CPR + adrenaline only — defibrillation useless):\n- Asystole: no electrical activity ('flat line')\n- Pulseless electrical activity (PEA): organised ECG activity but no cardiac output (treat 4 Hs and 4 Ts)\nAED: automated external defibrillator — analyses rhythm and advises shock or no shock."
    },
    {
        "id": "t5-r182",
        "question": "What are the 4 Hs and 4 Ts of reversible causes in cardiac arrest (PEA/asystole)?",
        "answer": "In pulseless electrical activity (PEA) or asystole, survival depends on identifying and treating reversible causes:\n4 Hs:\n1. Hypoxia — ensure adequate ventilation; high-flow O2\n2. Hypovolaemia — give IV fluids; stop bleeding\n3. Hypothermia — warm the patient (check temperature)\n4. Hypo/Hyperkalaemia and other metabolic disorders — check bloods; treat electrolyte disturbances; sodium bicarbonate for acidosis\n4 Ts:\n1. Tension pneumothorax — needle decompression (2nd ICS, MCL); then chest drain\n2. Tamponade (cardiac) — pericardiocentesis\n3. Toxins/drugs — antidotes (naloxone for opioids, atropine for organophosphates)\n4. Thrombosis (coronary or pulmonary) — thrombolysis; primary PCI"
    },
    {
        "id": "t5-r183",
        "question": "What is the ankle pressure (Doppler) threshold below which critical ischaemia of the lower limb is diagnosed?",
        "answer": "Critical ischaemia (also called critical limb ischaemia or CLI) is diagnosed when:\n- Ankle systolic pressure (measured by handheld Doppler) is <50 mmHg\n- OR Toe pressure <30 mmHg\n- Clinical features: rest pain (in toes/forefoot at night, relieved by hanging foot down), tissue loss (non-healing ulceration, gangrene)\nABPI in critical ischaemia is usually <0.5 (but ABPI may be falsely elevated in diabetics/heavily calcified vessels → use toe pressures instead).\nRisk: without revascularisation, 70% need amputation within 1 year.\nCompare: claudication = symptoms on walking only; rest pain = constant ischaemia at rest = critical ischaemia."
    },
    {
        "id": "t5-r184",
        "question": "What is the INR check timing and logistics for a dental patient on warfarin?",
        "answer": "Key rule: check INR within 72 hours before the dental procedure. Ideally check on the day of the procedure.\nWhy 72 hours: INR can fluctuate significantly day-to-day due to dietary changes (vitamin K intake), intercurrent illness, or drug interactions. An INR result older than 72 hours may not reflect the current state.\nLogistics:\n1. Contact patient's GP surgery or anticoagulant clinic to get the INR result\n2. If INR ≤4.0: proceed with dental procedure using local haemostatic measures\n3. If INR >4.0: defer elective treatment; contact GP/haematologist for warfarin dose adjustment; reschedule\n4. Document INR value and date in patient's dental notes\n5. Advise patient to contact their GP if they feel unusually drowsy or bleeding excessively after procedure"
    },
    {
        "id": "t5-r185",
        "question": "What is meant by 'target organ damage' in hypertension?",
        "answer": "Target organ damage (TOD): structural or functional damage to specific organs from sustained hypertension:\n1. Heart: LV hypertrophy (hypertensive heart disease → diastolic dysfunction → heart failure); coronary artery disease; MI; atrial fibrillation\n2. Brain: stroke (haemorrhagic and ischaemic); TIA; hypertensive encephalopathy; vascular dementia\n3. Kidneys: hypertensive nephrosclerosis → CKD; proteinuria; glomerular damage\n4. Eyes: hypertensive retinopathy (grades I–IV); Keith-Wagener-Barker classification; papilloedema (grade IV = hypertensive emergency)\n5. Aorta/large vessels: aortic aneurysm; aortic dissection; peripheral arterial disease\nPresence of TOD indicates stage 2 hypertension requiring immediate treatment regardless of BP reading and upgrades cardiovascular risk to 'very high'."
    },
    {
        "id": "t5-r186",
        "question": "What is the mechanism by which mitral regurgitation leads to cardiac failure?",
        "answer": "Mitral regurgitation (MR): backflow of blood from LV → LA during systole (LV cannot fully eject blood forward into aorta — some leaks back).\nAcute MR (e.g. from papillary muscle rupture post-MI, IE vegetation perforation): sudden volume overload of LA (unprepared, non-dilated) → rapidly rising pulmonary venous pressure → acute pulmonary oedema → haemodynamic emergency.\nChronic MR: LA and LV gradually dilate to accommodate regurgitant volume (eccentric hypertrophy — volume overload pattern). Initially compensated. Over years: LV contractility fails → forward CO falls → heart failure. Also: atrial dilation → AF → further loss of atrial contribution to LV filling → worsening CO.\nTreatment: surgical repair (preferred) or replacement before LV function irreversibly deteriorates (EF <60% is a trigger for surgery)."
    },
    {
        "id": "t5-r187",
        "question": "What is the significance of the ankle-brachial pressure index (ABPI) in diabetic patients?",
        "answer": "In diabetic patients, the ABPI is UNRELIABLE and often FALSELY ELEVATED (>1.3 or even >1.5).\nReason: diabetic peripheral neuropathy causes calcium deposition in the media of small arteries (Mönckeberg's medial sclerosis) → calcified, incompressible vessel walls → the cuff pressure required to occlude the vessel (and thus the measured ankle pressure) is artefactually high, because the calcified vessel doesn't fully compress.\nConsequence: a 'normal' or even supranormal ABPI in a diabetic doesn't exclude PAD — the patient may have severe atherosclerotic disease despite an ABPI >1.0.\nAlternative investigations in diabetics: toe pressures (digital arteries are less often calcified), pulse wave velocity, duplex ultrasound, CT/MR angiography."
    },
    {
        "id": "t5-r188",
        "question": "What is meant by 'transient' vs 'permanent' AF?",
        "answer": "Classification of AF by duration:\nParoxysmal AF: episodes that self-terminate within 7 days (usually <48 hours); recurrent but spontaneously convert to sinus rhythm. May still need anticoagulation if CHA2DS2-VASc score indicates risk.\nPersistent AF: lasts >7 days; does NOT self-terminate; requires electrical or pharmacological cardioversion to restore sinus rhythm.\nLongstanding persistent AF: AF lasting >1 year when a rhythm control strategy is being considered.\nPermanent AF: a joint decision between patient and physician to no longer pursue rhythm control; rate control and anticoagulation are the management goals. The term implies acceptance of AF as the chronic rhythm.\nNote: anticoagulation is required in all types of AF if CHA2DS2-VASc ≥2 in males or ≥3 in females."
    },
    {
        "id": "t5-r189",
        "question": "What is the role of aldosterone in heart failure and why does spironolactone help?",
        "answer": "In heart failure: RAAS is chronically activated → aldosterone levels are persistently elevated → aldosterone acts on distal nephron → Na+ retention and K+ excretion → further fluid overload → worsening oedema. Additionally: aldosterone has direct pro-fibrotic effects on the myocardium and blood vessels → cardiac remodelling → worsening ventricular function.\nSpironolactone: competitively blocks aldosterone receptors → prevents Na+ retention → natriuresis and diuresis; prevents myocardial fibrosis; reduces afterload; preserves K+.\nEvidence: RALES trial (1999): spironolactone 25mg added to standard therapy → 30% reduction in all-cause mortality in severe HF (EF <35%).\nEplerenone: more selective aldosterone antagonist; less gynaecomastia; used post-MI with EF <40%."
    },
    {
        "id": "t5-r190",
        "question": "How should a patient with an ICD (implantable cardioverter defibrillator) be managed in the dental surgery?",
        "answer": "Key principles:\n1. Obtain ICD identification card — note device manufacturer, model; check last follow-up\n2. Ask about recent device-related events (shocks, symptoms of arrhythmia)\n3. Electromagnetic interference (EMI) risk: generally LOW with modern dental equipment for ICDs; the concern is primarily with ultrasonic scalers, electrosurgery units, and pulp testers\n4. Ultrasonic scalers: some older ICDs may be inhibited (pacemaker function) by EMI — use alternative scalers (manual or sonic); keep distance >15cm from device if using ultrasonics\n5. Electrosurgery: AVOID if possible; bipolar electrosurgery is safer than monopolar\n6. Restorative equipment and curing lights: SAFE\n7. If ICD fires during procedure: stop immediately; check patient consciousness; call emergency services; begin CPR if needed\n8. Inform cardiologist of any planned complex procedures"
    },
    {
        "id": "t5-r191",
        "question": "What is the significance of the PR interval and QRS duration on ECG in cardiovascular disease?",
        "answer": "PR interval (normal: 120–200 ms = 3–5 small squares):\n- Short PR (<120 ms): WPW syndrome (accessory pathway), LGL syndrome\n- Long PR (>200 ms): first-degree heart block (increased AV node delay — benign alone; may indicate underlying disease or drug effect — beta-blockers, digoxin, verapamil)\n- Variable PR: second-degree heart block (Wenckebach or Mobitz II)\n- No relationship between P and QRS: third-degree (complete) heart block\n\nQRS duration (normal: 80–120 ms = 2–3 small squares):\n- Broad QRS (>120 ms): bundle branch block (LBBB or RBBB), ventricular origin rhythm (VT, accelerated idioventricular), hyperkalaemia, class I antiarrhythmics, WPW\n- Very broad QRS + rate >150 bpm: consider VT until proven otherwise"
    },
    {
        "id": "t5-r192",
        "question": "What are the dental implications of a patient with a prosthetic (replacement) heart valve?",
        "answer": "1. Anticoagulation: mechanical valves require lifelong warfarin (INR 2.5–4); check INR within 72 hours; proceed if ≤4; never stop warfarin without cardiology input\n2. IE risk: prosthetic valves are high-risk for IE (SDCEP high-risk category). NICE does not recommend routine antibiotic prophylaxis, but meticulous oral hygiene is essential; counsel patient on IE symptoms\n3. Antibiotic considerations: if antibiotics are needed for dental infection, avoid metronidazole and erythromycin/clarithromycin (raise INR).\n4. Drug interactions: nystatin (not azole antifungals) for oral candidiasis. Paracetamol for analgesia (avoid NSAIDs).\n5. Inform cardiologist of planned complex dental procedures\n6. Document valve type (tissue vs mechanical), position, and date of implant in notes\n7. Seek haematologist advice if INR consistently unstable"
    },
    {
        "id": "t5-r193",
        "question": "What is hypertensive retinopathy and how is it classified?",
        "answer": "Hypertensive retinopathy: changes in retinal blood vessels from high blood pressure, detected on fundoscopy.\nKeith-Wagener-Barker classification:\nGrade I: generalised arteriolar narrowing (silver-wire appearance) — may be normal variant in elderly\nGrade II: arteriovenous nipping (AV crossing changes — arteriole compresses vein at crossing point) + copper-wire arteries\nGrade III: Grade II changes + flame haemorrhages (nerve fibre layer bleeds) + cotton wool spots (retinal infarcts from arteriolar occlusion) + hard exudates (lipid deposits)\nGrade IV: Grade III changes + papilloedema (optic disc swelling from raised intracranial/intraocular pressure) = MALIGNANT HYPERTENSION — medical emergency\nRelevance: dentists may perform retinal examination via telemedicine screening; grade III/IV findings should prompt urgent referral."
    },
    {
        "id": "t5-r194",
        "question": "What is renal artery stenosis and how does it relate to hypertension and dental management?",
        "answer": "Renal artery stenosis (RAS): narrowing of the renal artery → reduced renal perfusion → activation of RAAS → hypertension (renovascular hypertension). The most common cause of secondary hypertension.\nTypes:\n1. Atherosclerotic RAS: elderly, smokers, often bilateral; common with generalised vascular disease\n2. Fibromuscular dysplasia: young women; bead-like appearance on angiogram; non-atherosclerotic\nDiagnosis: Doppler ultrasound (elevated peak systolic velocity in renal artery), CT/MR angiography.\nDental management implications:\n1. ACE inhibitors/ARBs are contraindicated in bilateral RAS (cause acute renal failure by blocking efferent arteriolar tone)\n2. NSAIDs also impair renal perfusion — avoid in RAS\n3. Patients may have CKD → check electrolytes, bleeding tendency\n4. Hypertension may be resistant to treatment (multiple antihypertensives)"
    },
    {
        "id": "t5-r195",
        "question": "What are the main differences between heparin and warfarin in clinical use?",
        "answer": "Heparin:\n- Route: injection only (SC or IV)\n- Onset: immediate\n- Mechanism: activates antithrombin III → inhibits thrombin and factor Xa\n- Monitoring: APTT (UFH); anti-Xa level (LMWH)\n- Reversal: protamine sulphate\n- Use: acute thrombosis (DVT, PE, ACS, haemodialysis); bridging when warfarin stopped\n- Crosses placenta: no → safe in pregnancy (preferred anticoagulant)\n- HIT: risk with UFH\n\nWarfarin:\n- Route: oral\n- Onset: delayed (2–5 days for full effect; factor VII falls first but lasting anticoagulation takes longer)\n- Mechanism: vitamin K antagonist → depletes factors II, VII, IX, X\n- Monitoring: INR\n- Reversal: vitamin K (takes 6–12 hours); fresh frozen plasma/PCC for immediate reversal\n- Use: chronic anticoagulation (AF, VTE, mechanical valves)\n- Crosses placenta: yes → teratogenic, contraindicated in pregnancy"
    },
    {
        "id": "t5-r196",
        "question": "What is PCSK9 and what are PCSK9 inhibitors used for?",
        "answer": "PCSK9 (proprotein convertase subtilisin-kexin type 9): an enzyme produced by the liver that degrades LDL receptors on hepatocytes → fewer LDL receptors → less LDL cleared from blood → raised LDL levels.\nPCSK9 inhibitors (alirocumab, evolocumab): monoclonal antibodies that bind and inhibit PCSK9 → more LDL receptors persist on liver surface → dramatically reduce LDL (by 50–60% on top of statin therapy).\nIndications:\n- Familial hypercholesterolaemia (heterozygous or homozygous) where statins insufficient\n- High cardiovascular risk with LDL not at target despite maximally tolerated statin + ezetimibe\n- Statin intolerance\nAdministration: subcutaneous injection every 2–4 weeks. Very well tolerated. Given alongside statins typically."
    },
    {
        "id": "t5-r197",
        "question": "How does myocardial ischaemia cause arrhythmias?",
        "answer": "Ischaemia creates conditions that predispose to arrhythmias:\n1. Reduced ATP → failure of ion pumps → cellular depolarisation → resting membrane potential rises towards threshold → spontaneous depolarisation (automaticity)\n2. Inhomogeneous repolarisation: ischaemic and non-ischaemic zones recover at different rates → dispersion of refractoriness → re-entry circuits (the anatomical substrate for VF and VT)\n3. Hyperkalaemia (K+ leaks from ischaemic cells) → raises resting potential → further depolarisation\n4. Acidosis and catecholamine release → further arrhythmia promotion\nMost dangerous time: first 24–48 hours post-MI (particularly first 30 minutes — most sudden cardiac deaths occur at this time from VF).\nPrevention: revascularisation (restores normal repolarisation); beta-blockers (reduce catecholamine-mediated arrhythmia); amiodarone/lidocaine for VF."
    },
    {
        "id": "t5-r198",
        "question": "What are the risk factors specifically associated with ventricular fibrillation?",
        "answer": "VF is the most common cause of sudden cardiac death:\nAcute causes (correctable):\n- Acute MI / myocardial ischaemia (plaque rupture → severe ischaemia → re-entry VF)\n- Electrolyte imbalances: hypokalaemia, hypomagnesaemia (both reduce defibrillation threshold)\n- Drug-induced: drugs that prolong QT interval (amiodarone, class Ia/III drugs, clarithromycin) → torsade de pointes → VF\n\nChronic predisposing conditions:\n- Reduced ejection fraction (<35%) from any cause\n- Previous MI with scar (anatomical re-entry substrate)\n- Hypertrophic cardiomyopathy\n- Brugada syndrome (SCN5A mutation)\n- Long QT syndrome (congenital)\n- Wolff-Parkinson-White (rapid conduction → VF)\nManagement: ICD for high-risk patients; treat reversible causes"
    },
    {
        "id": "t5-r199",
        "question": "What is an anticoagulant 'bridging' strategy and when is it used?",
        "answer": "Bridging: when a patient on long-term oral anticoagulation (warfarin) needs surgery requiring temporary warfarin cessation, LMWH is used to 'bridge' the anticoagulation gap.\nRationale: warfarin has a long half-life (35–37 hours) and takes 5 days to stop working fully → patient needs surgery with INR in normal range → warfarin stopped 5 days pre-op → LMWH started to cover the gap → LMWH stopped 12–24 hours before surgery (short half-life) → surgery performed → warfarin restarted post-op → LMWH continued until INR therapeutic again.\nUsed for: high-risk patients (mechanical heart valves, VTE within 3 months, AF with previous stroke).\nNOT needed for: dental extractions (warfarin continued without interruption if INR ≤4); low-risk patients."
    },
    {
        "id": "t5-r200",
        "question": "What is the typical blood pressure threshold for deferring routine dental treatment?",
        "answer": "Blood pressure thresholds for dental treatment (based on SDCEP/BCS guidelines):\nBelow 160/100 mmHg: routine dental treatment can proceed; inform GP if hypertension not known/managed\n160–180 / 100–110 mmHg: refer/liaise with GP; may treat dental emergency; advise lifestyle modification; re-check BP at each visit\n180–200 / 110–115 mmHg: defer elective treatment; refer to GP urgently; treat dental emergency only (pain, acute infection) with minimisation of adrenaline; consider sedation for anxious patients\nAbove 200/115 mmHg: only treat absolute dental emergencies; emergency medical referral; call 999 if hypertensive emergency signs present (encephalopathy, visual disturbance, acute LVF)\nNote: a single elevated reading requires confirmation — check BP in both arms; white coat effect is common."
    },
    {
        "id": "t5-r201",
        "question": "What is an echocardiogram and what are the different types used in cardiac investigation?",
        "answer": "Echocardiogram (echo): ultrasound imaging of the heart to assess structure and function.\nTypes:\nTransthoracic echo (TTE): probe on chest wall; non-invasive; first-line; limited image quality in obese/emphysematous patients. Assesses: LV function (EF), valve anatomy, wall motion, pericardial effusion, congenital defects.\nTransoesophageal echo (TOE): probe swallowed into oesophagus (requires sedation); excellent posterior heart views. Used: suspected IE (more sensitive), prosthetic valve assessment, LA thrombus (before cardioversion), aortic dissection.\nStress echo: echo performed during exercise or pharmacological stress (dobutamine) — assesses for inducible ischaemia.\nDoppler echo: measures blood flow velocities — calculates pressure gradients across valves (essential for stenosis grading).\n3D echo: volumetric reconstruction; better EF measurement, mitral valve assessment."
    },
    {
        "id": "t5-r202",
        "question": "What is the mechanism by which nicorandil causes oral ulceration and how is it managed?",
        "answer": "Nicorandil: potassium channel opener + nitrate component → vasodilation. Mechanism of oral ulceration: poorly understood; probably involves direct mucosal toxicity related to the nitrate component or local vascular changes (microvascular ischaemia of mucosa) → breakdown of mucosal integrity → severe, non-healing ulceration.\nClinical features: large (can be several centimetres), deep, very painful oral ulcers that fail to heal despite standard treatment. May also cause perianal and GI ulceration. Often initially misdiagnosed as traumatic or aphthous.\nManagement:\n1. Identify nicorandil as the cause (drug history is crucial)\n2. Refer to GP/cardiologist for drug substitution (nicorandil replaced with alternative antianginal — isosorbide mononitrate, amlodipine, ivabradine)\n3. Ulcers heal within 4–8 weeks of drug cessation\n4. Symptomatic: topical anaesthetic, antiseptic (chlorhexidine), benzydamine mouthwash"
    },
    {
        "id": "t5-r203",
        "question": "What is the mechanism of action of beta-blockers and why are non-selective beta-blockers contraindicated in asthma?",
        "answer": "Beta-adrenoceptor antagonists:\n- Beta-1 receptors (heart): reduce heart rate (SA node) and contractility → reduced cardiac output and BP; reduce renin release from kidney → lower RAAS activity\n- Beta-2 receptors (bronchi, peripheral vessels, uterus): bronchodilation and vasodilation are blocked → bronchoconstriction and vasoconstriction\nCardioselective (Beta-1 selective): atenolol, bisoprolol, metoprolol → mainly heart effects at standard doses; less bronchospasm risk (but NOT completely safe in severe asthma)\nNon-selective (Beta-1 + Beta-2): propranolol, labetalol, carvedilol → block bronchodilation → can cause severe, life-threatening bronchospasm in asthma/COPD patients → CONTRAINDICATED in asthma\nDental: careful with adrenaline in LA for patients on non-selective beta-blockers (theoretical hypertension risk from unopposed alpha stimulation)"
    },
    {
        "id": "t5-r204",
        "question": "What are the main types of stroke complication and what is the post-stroke dental management?",
        "answer": "Stroke complications relevant to dentistry:\n1. Motor deficits: hemiparesis/hemiplegia → difficulty sitting, transfers, maintaining oral hygiene\n2. Dysphagia: impaired swallowing → aspiration risk; avoid impression materials that could be aspirated; use high-volume suction\n3. Cognitive impairment/vascular dementia: reduced capacity to consent; shorter appointments; carer involvement\n4. Aphasia: communication difficulties → use pictures, simple language, closed questions\n5. Medications: anticoagulants (warfarin/DOAC) or antiplatelets (aspirin + clopidogrel) — manage as per standard guidelines\nPost-stroke dental management:\n- Defer elective treatment for 3–6 months post-stroke (risk of recurrence highest in early period)\n- Morning appointments; shorter sessions\n- Careful monitoring of BP\n- Liaise with stroke team regarding anticoagulation and procedure risk"
    },
    {
        "id": "t5-r205",
        "question": "What is the difference between primary and secondary pulmonary hypertension?",
        "answer": "Pulmonary arterial hypertension (PAH): mean pulmonary arterial pressure >25 mmHg at rest.\nPrimary (idiopathic) PAH: no identifiable cause. Rare; predominantly young women; progressive obliterative arteriopathy in pulmonary vessels. BMPR2 gene mutation in 70% of familial cases. Rapidly fatal without treatment. Treatment: vasodilators (sildenafil, bosentan, prostacyclin analogues).\nSecondary pulmonary hypertension (far more common): due to identifiable underlying disease:\n- Left heart disease (most common): elevated pulmonary venous pressure from LV failure → back-pressure\n- Chronic lung disease: hypoxic pulmonary vasoconstriction (COPD, interstitial lung disease) → Cor Pulmonale\n- Chronic thromboembolic disease: unresolved pulmonary emboli → organised clot obstructs pulmonary vasculature\n- Connective tissue disease (systemic sclerosis, SLE)\nManagement: treat underlying cause."
    },
    {
        "id": "t5-r206",
        "question": "What is the TIMI risk score and when would it be used?",
        "answer": "TIMI (Thrombolysis in Myocardial Infarction) risk score: a clinical risk assessment tool to predict the 14-day risk of death, MI, or urgent revascularisation in patients with unstable angina (UA) or NSTEMI.\nComponents (7 variables, 1 point each):\n1. Age ≥65\n2. ≥3 CAD risk factors (family history, hypertension, hyperlipidaemia, DM, smoking)\n3. Prior coronary stenosis ≥50%\n4. ST-segment deviation on presenting ECG\n5. ≥2 anginal events in prior 24 hours\n6. Use of aspirin in prior 7 days\n7. Elevated serum cardiac markers (troponin/CK-MB)\nScore 0–2: low risk; Score 3–4: intermediate; Score 5–7: high risk → early invasive strategy (angiography ± revascularisation within 24 hours).\nNot typically a dental exam topic but may appear in context of patient history."
    },
    {
        "id": "t5-r207",
        "question": "What are the features of constrictive pericarditis and how does it differ from cardiac tamponade?",
        "answer": "Constrictive pericarditis: chronic pericardial scarring/thickening (from previous pericarditis, TB, cardiac surgery, radiotherapy) → rigid pericardium encases the heart → restricts diastolic filling of all chambers.\nFeatures: raised JVP (Kussmaul's sign: JVP RISES on inspiration — opposite of normal); pericardial knock (early diastolic sound); oedema, ascites, hepatomegaly (hepatic congestion).\nDistinct from tamponade:\n- Tamponade: acute (fluid in pericardial sac); pulsus paradoxus prominent; echo shows swinging heart in fluid; JVP rises on inspiration (Kussmaul's positive only in constriction usually)\n- Constrictive pericarditis: chronic; calcified pericardium on X-ray/CT; small heart on echo; treated surgically (pericardiectomy)\nBoth: raised JVP, oedema, reduced cardiac output — but different causes and treatments."
    },
    {
        "id": "t5-r208",
        "question": "What is Brugada syndrome and why is it clinically important?",
        "answer": "Brugada syndrome: an inherited (autosomal dominant; SCN5A gene — sodium channel mutation) channelopathy with a structurally normal heart. Causes a characteristic ECG pattern (coved/saddleback ST elevation in V1–V3) and predisposes to ventricular arrhythmias (VF) and sudden cardiac death, particularly during sleep/rest (vagally mediated, at night).\nEpidemiology: more common in South-East Asian males (Thailand/Japan — 'Pokkuri' sudden nocturnal death syndrome). First or second most common cause of sudden cardiac death in people under 40 without structural heart disease.\nDrug triggers: sodium channel blockers (Class Ia, Ic drugs, tricyclic antidepressants), fever, cocaine.\nManagement: ICD is the only proven therapy for high-risk patients. Avoid causative drugs. Antipyretics promptly for any fever.\nDental note: local anaesthetics (sodium channel blockers) — lidocaine at dental doses generally considered safe, but caution in confirmed Brugada."
    },
    {
        "id": "t5-r209",
        "question": "What is the clinical significance of an elevated JVP (jugular venous pressure)?",
        "answer": "JVP: reflects right atrial pressure — a window into the central venous pressure (CVP). Normal: JVP observed pulsation ≤3–4 cm above the sternal angle (right atrium) with the patient reclining at 45°. If visible when patient is upright (90°), it is markedly elevated.\nElevated JVP indicates:\n1. Right heart failure — most common cause (blood dams in venous system)\n2. Cardiac tamponade — pericardial fluid prevents RV filling\n3. Constrictive pericarditis\n4. Pulmonary hypertension / cor pulmonale\n5. Superior vena cava obstruction (SVC syndrome — mediastinal tumour/malignancy; the JVP is raised but non-pulsatile with no waveform)\n6. Tricuspid stenosis or regurgitation\n7. Fluid overload (aggressive IV fluid administration)\nNot elevated in isolated left heart failure (pressure rise is on left side → pulmonary oedema, not raised JVP)."
    },
    {
        "id": "t5-r210",
        "question": "Summarise the dental management considerations for the top five CVD conditions.",
        "answer": "1. Hypertension: check BP before treatment; defer if >200/115; avoid adrenaline excess if very high BP; warn of ACE inhibitor angioedema/gingival hyperplasia (CCBs)\n2. Ischaemic heart disease/recent MI: defer elective 3–6 months post-MI; effective LA; GTN available; morning appointments; adrenaline safe in mild-moderate IHD\n3. Heart failure: semi-reclined position (no lying flat); avoid NSAIDs; check INR if on warfarin; morning appointments\n4. Atrial fibrillation: check INR/ask about DOAC; continue anticoagulation; treat infection promptly; avoid metronidazole with warfarin\n5. Valvular disease/prosthetic valve: check INR (warfarin); do not stop anticoagulation; nystatin not miconazole for thrush; excellent OH advice; tell patient to report fever/malaise (IE); inform of no routine antibiotic prophylaxis needed per NICE but maximise OH"
    }
]

data['recallIt'].extend(new_recall)

with open('data/theme-5.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Total recallIt: {len(data['recallIt'])}")
