import json

with open('data/theme-5.json', 'r') as f:
    data = json.load(f)

new_recall = [
    # CVD ANATOMY & PHYSIOLOGY
    {
        "id": "t5-r17",
        "question": "In order, what is the cardiac conducting system from pacemaker to ventricular muscle?",
        "answer": "SA node (right atrium — sets rate 60–100 bpm) → atrial muscle (produces P wave on ECG) → AV node (delay = PR interval; gives time for atrial contraction to fill ventricles) → Bundle of His → right and left bundle branches → Purkinje fibres → ventricular muscle (produces QRS complex)"
    },
    {
        "id": "t5-r18",
        "question": "Name the three layers of an arterial wall.",
        "answer": "1. Tunica intima — innermost; single layer of endothelial cells; site of atherosclerosis development\n2. Tunica media — middle; smooth muscle and elastic fibres; maintains vessel tone\n3. Tunica adventitia (externa) — outermost; connective tissue; anchors vessel"
    },
    {
        "id": "t5-r19",
        "question": "Name six modifiable risk factors for cardiovascular disease.",
        "answer": "1. Hypertension (most important correctable risk factor; risk doubles every 20/10 mmHg rise)\n2. Hyperlipidaemia (raised LDL, low HDL)\n3. Smoking (carbon monoxide damages endothelium)\n4. Diabetes mellitus\n5. Obesity\n6. Physical inactivity\nAlso: excessive alcohol, poor diet, psychosocial stress"
    },
    {
        "id": "t5-r20",
        "question": "What is cardiac output, and what is the formula for it?",
        "answer": "Cardiac output (CO) = Stroke volume × Heart rate\nNormal at rest: approximately 5 litres/minute (70 mL × 72 bpm)\nIncreases up to 25 L/min during intense exercise via increased heart rate and stroke volume (Starling's law)"
    },
    {
        "id": "t5-r21",
        "question": "What is the difference between preload and afterload, and why do they matter in heart failure?",
        "answer": "Preload: the volume of blood stretching the ventricle at end of diastole (filling pressure). Increased by fluid overload/venous return.\nAfterload: the resistance the heart must overcome to eject blood (arterial resistance). Increased by hypertension/vasoconstriction.\nIn heart failure: increased preload → pulmonary oedema; increased afterload → reduced stroke volume. ACE inhibitors and nitrates reduce both."
    },
    {
        "id": "t5-r22",
        "question": "Why do atherosclerotic plaques preferentially develop at arterial bifurcations?",
        "answer": "At bifurcations, laminar blood flow becomes turbulent and creates low shear stress zones. This damages the endothelium mechanically, promoting LDL infiltration and monocyte adhesion. Common sites: coronary arteries, carotid bifurcation, femoral bifurcation, renal arteries, and the infrarenal aorta."
    },
    {
        "id": "t5-r23",
        "question": "Name the non-modifiable risk factors for cardiovascular disease.",
        "answer": "1. Age (>55 for men, >65 for women)\n2. Male sex (oestrogen is cardioprotective pre-menopause)\n3. Post-menopausal women (lose oestrogen protection)\n4. Ethnicity (South Asian: higher IHD risk; African-Caribbean: higher hypertension/stroke risk)\n5. Family history: first-degree relative with CVD under 55 (men) or 65 (women)\n6. Genetics: familial hypercholesterolaemia, inherited thrombophilias"
    },
    {
        "id": "t5-r24",
        "question": "What are the structural differences between arteries and veins?",
        "answer": "Arteries: thick muscular wall (large tunica media), no valves, high pressure, carry blood away from heart. Lumen relatively small compared to wall thickness.\nVeins: thin wall, have valves (prevent backflow against gravity), low pressure, carry blood to heart. Large lumen relative to wall thickness.\nCapillaries: one cell thick (5 microns), allow gas/nutrient exchange."
    },
    {
        "id": "t5-r25",
        "question": "Which coronary arteries supply which territories of the heart?",
        "answer": "Left anterior descending (LAD) artery: front (anterior wall) of left ventricle and interventricular septum — 'widowmaker'; occlusion causes anterior MI\nCircumflex artery: lateral and posterior walls of left ventricle\nRight coronary artery (RCA): inferior wall of heart, posterior descending artery, SA and AV nodes (most patients)\nRight coronary artery territory MI → inferior MI on ECG (leads II, III, aVF)"
    },
    {
        "id": "t5-r26",
        "question": "What is the renin-angiotensin-aldosterone system (RAAS) and how does it raise blood pressure?",
        "answer": "Low renal perfusion → juxtaglomerular cells release renin → renin cleaves angiotensinogen → angiotensin I → ACE (in lungs) → angiotensin II → binds AT1 receptor → (1) aldosterone secretion from adrenal cortex → Na+/water retention → increased blood volume; (2) direct vasoconstriction → increased peripheral resistance; (3) sympathetic nervous system activation → tachycardia and vasoconstriction.\nACE inhibitors block this at the ACE step."
    },
    # ATHEROSCLEROSIS
    {
        "id": "t5-r27",
        "question": "Describe the four stages of atherosclerosis in order.",
        "answer": "1. Endothelial dysfunction: turbulent flow/risk factors damage endothelium at bifurcations\n2. Fatty streak: monocytes enter intima → differentiate into macrophages → engulf LDL → foam cells (characteristic feature)\n3. Fibrolipid (fibrous) plaque: smooth muscle cells migrate from media → secrete collagen → fibrous cap forms over lipid core; endothelium intact; lumen starts to narrow\n4. Complicated lesion: endothelium stripped → platelets adhere → thrombus; calcification; haemorrhage into plaque; plaque fissure/rupture → embolism"
    },
    {
        "id": "t5-r28",
        "question": "What is a 'vulnerable plaque' and why is it clinically dangerous?",
        "answer": "A vulnerable (unstable) plaque has:\n- Large lipid pool\n- Thin fibrous cap\n- Many inflammatory macrophages (secrete matrix metalloproteinases that degrade the cap)\n- Few smooth muscle cells\nDangerous because it is prone to rupture, exposing the lipid core → platelet activation and thrombosis → acute coronary syndrome or stroke. A stable plaque (thick cap, small lipid pool) is less likely to rupture despite causing greater stenosis."
    },
    {
        "id": "t5-r29",
        "question": "What is diapedesis and what role does it play in atherosclerosis?",
        "answer": "Diapedesis is the passage of cells (especially monocytes/white cells) through the intact vessel wall by squeezing between endothelial cells. In atherosclerosis: endothelial dysfunction → monocytes adhere to damaged endothelium (via adhesion molecules VCAM-1, ICAM-1) → monocytes undergo diapedesis into the intima → differentiate into macrophages (under influence of lymphocyte cytokines) → engulf oxidised LDL → foam cells (fatty streak)"
    },
    {
        "id": "t5-r30",
        "question": "What are lines of Zahn and what do they indicate?",
        "answer": "Lines of Zahn are alternating pale bands (fibrin and platelets) and dark bands (red blood cells) seen histologically in a thrombus that formed in flowing blood during life (ante-mortem thrombus). The alternating layers form as clot builds up in flowing blood. They distinguish a true thrombus from a post-mortem clot (coagulum). Post-mortem clots have a homogeneous 'chicken fat' (yellow) and red jelly appearance without lines of Zahn."
    },
    {
        "id": "t5-r31",
        "question": "What is the role of LDL vs HDL cholesterol in atherosclerosis?",
        "answer": "LDL (low-density lipoprotein): harmful — deposits cholesterol in arterial walls; oxidised LDL in the intima is taken up by macrophages to form foam cells; raised LDL is a major risk factor for atherosclerosis.\nHDL (high-density lipoprotein): protective — 'reverse cholesterol transport'; removes cholesterol from peripheral tissues and arterial walls and transports it to the liver for processing; high HDL is cardioprotective; low HDL is a CVD risk factor.\nTarget: LDL < 2 mmol/L in high-risk patients (statins achieve this)."
    },
    {
        "id": "t5-r32",
        "question": "Name all three components of Virchow's triad with examples of each.",
        "answer": "1. Endothelial damage: hypertension, smoking, atherosclerosis, catheterisation, trauma\n2. Abnormal blood flow: stasis (immobility, AF, venous thrombosis) or turbulence (bifurcations, stenosis)\n3. Hypercoagulability: inherited (Factor V Leiden, protein C/S deficiency, antiphospholipid syndrome), acquired (malignancy, pregnancy, oestrogen therapy, nephrotic syndrome, polycythaemia)\nAll three are more relevant to venous thrombosis; endothelial damage and turbulence are more relevant to arterial thrombosis."
    },
    {
        "id": "t5-r33",
        "question": "What are the risk factors for deep vein thrombosis (DVT)?",
        "answer": "Virchow's triad components:\nStasis: immobility (long-haul flights, surgery, paralysis), congestive heart failure\nHypercoagulability: malignancy (Trousseau's sign), pregnancy, oestrogen (OCP, HRT), inherited thrombophilias, nephrotic syndrome\nEndothelial damage: surgery, trauma, IV catheters\nOther: increasing age, obesity, previous DVT, dehydration, burns\nRisk scoring: Wells score for clinical probability before investigation"
    },
    {
        "id": "t5-r34",
        "question": "What is a paradoxical embolism?",
        "answer": "A paradoxical embolism is a venous thrombus that crosses from the right to the left circulation through a patent foramen ovale (PFO) or other septal defect, becoming a systemic arterial embolus. This can cause stroke or peripheral limb ischaemia in young patients without typical arterial risk factors. Approximately 25% of the population have a PFO. Cryptogenic (unexplained) stroke in young patients should prompt investigation for PFO with bubble echocardiography."
    },
    {
        "id": "t5-r35",
        "question": "What is haemopericardium and at what time point after MI is it most dangerous?",
        "answer": "Haemopericardium = blood in the pericardial sac, usually from rupture of the necrotic ventricular wall following MI. Greatest risk: 4–6 days post-MI, when the infarcted myocardium is at its softest (maximum coagulative necrosis, before fibrosis). Blood fills the pericardial space → cardiac tamponade (compress heart → prevent filling → fall in cardiac output) → cardiogenic shock and sudden death. Treatment: urgent pericardiocentesis or surgical drainage."
    },
    # IHD/ANGINA/MI
    {
        "id": "t5-r36",
        "question": "What is the difference between stable angina, unstable angina, and acute MI in terms of pathophysiology and symptoms?",
        "answer": "Stable angina: fixed atherosclerotic stenosis → reversible ischaemia on exertion; pain <5 min; resolves with rest/GTN; no troponin rise.\nUnstable angina: plaque disruption → partial occlusion → ischaemia at rest or minimal exertion; pain >20 min; no troponin rise (no necrosis).\nAcute MI: complete coronary occlusion → irreversible necrosis; pain at rest, severe, >20 min; troponin elevated (myocyte death releases it into bloodstream); ECG: ST changes."
    },
    {
        "id": "t5-r37",
        "question": "What is troponin and why is it the key biomarker in MI?",
        "answer": "Troponin (troponin I and troponin T) is a regulatory protein in cardiac muscle fibres. It is highly specific to cardiac muscle (cTnI and cTnT isoforms unique to myocardium). When myocardial cells die (infarction), troponin leaks into the bloodstream. Levels rise within 3–6 hours of MI onset, peak at 24–48 hours, and remain elevated for up to 2 weeks. High sensitivity troponin assays allow earlier diagnosis. Serial measurements (at 0 and 3 hours) are used in emergency diagnosis."
    },
    {
        "id": "t5-r38",
        "question": "What is the difference between STEMI and NSTEMI?",
        "answer": "STEMI (ST-Elevation MI): complete occlusion of coronary artery → transmural (full thickness) infarction → ST elevation on ECG → emergency PCI (percutaneous coronary intervention) within 90 minutes ('door-to-balloon time') is treatment.\nNSTEMI (Non-ST-Elevation MI): partial occlusion → subendocardial infarction → ST depression or T-wave changes (no ST elevation) → positive troponin → managed medically initially then early angiography. Both involve troponin rise (unlike unstable angina)."
    },
    {
        "id": "t5-r39",
        "question": "What is the MONCA mnemonic for immediate MI management and what does each letter stand for?",
        "answer": "M — Morphine (IV, for pain and anxiety — also reduces catecholamine release)\nO — Oxygen (15L/min via non-rebreathe mask if SaO2 <94%; NOT if normoxic — hyperoxia is harmful post-MI)\nN — Nitrates (GTN sublingually — vasodilates, reduces preload)\nC — Call 999\nA — Aspirin 300mg chewed (irreversible COX inhibitor → antiplatelet → limits clot extension)\nAlso: clopidogrel (dual antiplatelet), anticoagulation (heparin/LMWH), and primary PCI."
    },
    {
        "id": "t5-r40",
        "question": "How does GTN (glyceryl trinitrate) spray work to relieve angina?",
        "answer": "GTN is a nitrate prodrug → metabolised to nitric oxide (NO) → activates guanylate cyclase in vascular smooth muscle → ↑cGMP → smooth muscle relaxation → vasodilation.\nEffects: (1) Venodilation → reduces preload (less blood returning to heart) → reduced O2 demand; (2) coronary artery dilation → improves myocardial blood supply; (3) arteriodilation (at higher doses) → reduces afterload.\nDose: 2 puffs sublingually; repeat after 3–5 min if needed. Adverse effects: headache (meningeal vasodilation), flushing, hypotension. Nitrate tolerance requires 'nitrate-free period' (usually overnight)."
    },
    {
        "id": "t5-r41",
        "question": "What drug classes are used for chronic stable angina and their mechanisms?",
        "answer": "1. Nitrates (GTN, isosorbide mononitrate) — NO donor → vasodilation → reduced preload + coronary dilation\n2. Beta-blockers (atenolol, bisoprolol) — reduce heart rate and contractility → reduced O2 demand\n3. Calcium channel blockers — dihydropyridines (amlodipine): vasodilate; rate-limiting (verapamil, diltiazem): slow HR + vasodilate\n4. Nicorandil — K+ channel opener + nitrate → vasodilation; causes oral ulceration\n5. Ivabradine — If channel blocker → reduces HR only (no effect on contractility); useful if beta-blockers not tolerated\n6. Ranolazine — inhibits late Na+ current → reduces myocardial oxygen demand without affecting HR or BP"
    },
    {
        "id": "t5-r42",
        "question": "When should elective dental treatment be deferred after an MI?",
        "answer": "Elective dental treatment should be deferred for at least 3–6 months after MI. During this period: the patient is at high risk of re-infarction; the autonomic nervous system is unstable; arrhythmia risk is high; and the patient may still be on new anticoagulant/antiplatelet regimens.\nAfter 3–6 months (with cardiologist clearance if needed): routine treatment can proceed with: morning appointments, effective LA, minimal adrenaline, BP/ECG monitoring, GTN available."
    },
    {
        "id": "t5-r43",
        "question": "What is the time course of macroscopic changes in an MI?",
        "answer": "0–6 hours: no macroscopic change (but ECG changes present; troponin rises)\n6–24 hours: slight pallor\n24–48 hours: pallor with central yellow and haemorrhagic rim\n3–5 days: pale, grey, soft (maximum softening → risk of rupture → haemopericardium)\n1–2 weeks: grey, firm\nWeeks to months: fibrosis → white scar replaces necrotic tissue (myocyte cannot regenerate)"
    },
    {
        "id": "t5-r44",
        "question": "How do you manage an acute angina attack that occurs during dental treatment?",
        "answer": "1. Stop treatment immediately; remain calm\n2. Sit patient upright (or in comfortable position — do not lie flat)\n3. Administer patient's own GTN spray: 2 puffs sublingually\n4. Wait 3–5 minutes\n5. If unresolved: repeat GTN (2 more puffs)\n6. If still unresolved after second dose: treat as MI — call 999; give 100% O2 15L/min; administer aspirin 300mg chewed; prepare to start CPR\n7. Monitor pulse, respiration, and consciousness throughout\nDo NOT administer GTN if patient is on phosphodiesterase-5 inhibitors (sildenafil) — fatal hypotension risk"
    },
    {
        "id": "t5-r45",
        "question": "What is the 'nitrate-free period' and why is it needed?",
        "answer": "Nitrate tolerance develops with continuous nitrate exposure: the enzyme converting organic nitrates to NO becomes depleted (sulfhydryl group depletion), and counter-regulatory neurohormonal mechanisms are activated. This reduces efficacy within 24–48 hours of continuous therapy.\nTo prevent tolerance: a nitrate-free period of 8–12 hours per day is built into dosing (e.g. isosorbide mononitrate taken at 8am and 2pm, not at night). GTN spray used intermittently does not develop tolerance. Asymmetric dosing is used for long-acting preparations."
    },
    # VALVULAR DISEASE / IE
    {
        "id": "t5-r46",
        "question": "What are the major Duke criteria for diagnosing infective endocarditis?",
        "answer": "Major criteria (2 sufficient for definite IE):\n1. Positive blood cultures: two separate cultures with typical IE organisms (viridans streptococci, S. aureus, HACEK); or persistently positive cultures with other organisms\n2. Evidence of endocardial involvement on echocardiography: oscillating mass (vegetation) on valve; periannular abscess; new partial dehiscence of prosthetic valve; or new valvular regurgitation on echo\n(Definite IE = 2 major; or 1 major + 3 minor; or 5 minor)"
    },
    {
        "id": "t5-r47",
        "question": "What are the minor Duke criteria for infective endocarditis?",
        "answer": "Minor criteria:\n1. Predisposing factor: cardiac condition or intravenous drug use\n2. Fever >38°C\n3. Vascular phenomena: arterial emboli, septic pulmonary infarcts, mycotic aneurysm, intracranial haemorrhage, conjunctival haemorrhages, Janeway lesions\n4. Immunological phenomena: glomerulonephritis, Osler's nodes, Roth spots, positive rheumatoid factor\n5. Microbiological evidence: positive blood culture not meeting a major criterion\nDiagnosis: 2 major; or 1 major + 3 minor; or 5 minor = definite IE"
    },
    {
        "id": "t5-r48",
        "question": "Describe the pathogenesis of rheumatic fever leading to valvular heart disease.",
        "answer": "Group A Streptococcal pharyngitis → immune response produces antibodies against streptococcal M protein → molecular mimicry: antibodies cross-react with cardiac proteins (myosin, valvular proteins) → autoimmune inflammation of heart valves (Aschoff bodies histologically) → repeated episodes cause progressive valve scarring, thickening, fibrosis, and calcification → mitral stenosis (most common) or regurgitation. Rare now in UK due to penicillin treatment of strep throat. Still common in developing countries."
    },
    {
        "id": "t5-r49",
        "question": "What is the difference between tissue and mechanical prosthetic heart valves?",
        "answer": "Tissue (bioprosthetic) valves: made from porcine or bovine pericardium. Advantages: do NOT require long-term anticoagulation (aspirin only for 3 months post-op). Disadvantages: wear out over 10–15 years; need re-replacement. Used in: elderly patients, those who cannot tolerate anticoagulation.\nMechanical valves: metal (tilting disc or bileaflet). Advantages: last lifelong. Disadvantages: require LIFELONG warfarin anticoagulation (INR 2.5–4). Risk: IE, thromboembolism if anticoagulation inadequate. Used in: younger patients."
    },
    {
        "id": "t5-r50",
        "question": "Give three arguments against routine antibiotic prophylaxis for IE before dental procedures.",
        "answer": "1. No consistent evidence of causal link between dental procedures and IE — bacteraemia from dental procedures is transient and similar to daily toothbrushing\n2. Cumulative bacteraemia from daily toothbrushing (365×/year) is far greater than a single dental procedure\n3. Risk of antibiotic adverse effects (anaphylaxis, C. difficile colitis) may exceed the risk of preventing IE\n4. Only a small fraction of IE cases are attributable to dental bacteraemia; most arise spontaneously\n5. Poor evidence of efficacy from animal models — human RCTs impossible"
    },
    {
        "id": "t5-r51",
        "question": "Which patients does SDCEP consider 'high risk' for infective endocarditis?",
        "answer": "High risk (SDCEP):\n1. Previous infective endocarditis (highest risk)\n2. Prosthetic heart valves or prosthetic material used for cardiac valve repair\n3. Cyanotic congenital heart disease (unrepaired or with palliative shunt)\n4. Repaired congenital heart disease with prosthetic material — first 6 months post-repair, or lifelong if residual shunt/regurgitation at site of prosthetic material\n\nModerate risk: rheumatic fever with valve damage, native valve disease, unrepaired non-cyanotic congenital defects"
    },
    {
        "id": "t5-r52",
        "question": "What is TAVI (Transcatheter Aortic Valve Implantation) and who is it used for?",
        "answer": "TAVI is a catheter-based (keyhole) procedure for replacing a diseased aortic valve without open-heart surgery. A bioprosthetic valve mounted on a stent is compressed onto a catheter, inserted via the femoral artery (or directly through the chest in trans-apical approach), guided to the aortic valve position, and deployed by balloon inflation — pushing aside the diseased valve and anchoring in position.\nUsed for: aortic stenosis in high surgical risk or inoperable patients (elderly, multiple comorbidities). Transcatheter edge-to-edge repair (MitraClip) is analogous for mitral regurgitation."
    },
    # HEART FAILURE
    {
        "id": "t5-r53",
        "question": "What is the NYHA classification of heart failure severity?",
        "answer": "Class I: No limitation — ordinary physical activity does not cause symptoms\nClass II: Slight limitation — comfortable at rest; symptoms on moderate exertion (climbing stairs, walking on level)\nClass III: Marked limitation — comfortable at rest; symptoms on minimal exertion (walking short distances)\nClass IV: Unable to carry on any physical activity without discomfort; symptoms at rest; bed- or chair-bound\nRelevant to dental management: NYHA III/IV require special precautions (positioning, shorter appointments, avoid supine position)"
    },
    {
        "id": "t5-r54",
        "question": "What is BNP (B-type natriuretic peptide) and what is its clinical significance?",
        "answer": "BNP (B-type/Brain natriuretic peptide) and NT-proBNP are peptides released by ventricular myocytes in response to increased wall stretch (raised filling pressures). They promote natriuresis (sodium excretion) and vasodilation.\nClinical use: diagnostic biomarker for heart failure. Elevated BNP helps distinguish cardiac from respiratory cause of breathlessness. BNP is also used to monitor treatment response.\nNormal BNP: <100 pg/mL (unlikely heart failure). Elevated: >400 pg/mL (high probability). Also used in prognosis — higher BNP = worse outcome."
    },
    {
        "id": "t5-r55",
        "question": "What is orthopnoea and why does it occur in left-sided heart failure?",
        "answer": "Orthopnoea = breathlessness on lying flat (requires multiple pillows to sleep comfortably). Occurs because: when supine, fluid from the lower limbs redistributes (hydrostatic pressure removed) → venous return to the heart increases → rises pulmonary blood volume → worsens pulmonary oedema → dyspnoea.\nParoxysmal nocturnal dyspnoea: patient wakes from sleep acutely breathless 1–2 hours after lying down (fluid redistribution process takes time). Relieved by sitting upright. Dental implication: patients with orthopnoea cannot tolerate the supine dental chair position."
    },
    {
        "id": "t5-r56",
        "question": "What is the mechanism of action of furosemide and what are its electrolyte side effects?",
        "answer": "Mechanism: furosemide (frusemide) is a loop diuretic that inhibits the Na+/K+/2Cl− co-transporter in the thick ascending limb of the loop of Henle → prevents reabsorption of sodium and water → 10-fold increase in urine output (most potent diuretic class).\nSide effects:\n- Hypokalaemia (most important — risk of arrhythmias; requires K+ monitoring/supplementation)\n- Hyponatraemia\n- Hypomagnesaemia\n- Metabolic alkalosis\n- Ototoxicity (especially with rapid IV administration or high doses)\n- Gout (increases uric acid)\n- Dehydration/hypovolaemia"
    },
    {
        "id": "t5-r57",
        "question": "What is the mechanism of spironolactone and its two main adverse effects?",
        "answer": "Spironolactone: competitive aldosterone antagonist. Blocks aldosterone receptors in the collecting duct → prevents sodium reabsorption and potassium excretion (potassium-sparing diuretic). Also a pro-drug (active metabolite canrenone).\nBenefits in heart failure: reduces fluid overload; improves survival (RALES trial — 30% mortality reduction).\nAdverse effects:\n1. Hyperkalaemia — dangerous; can cause fatal arrhythmias; avoid with ACE inhibitors + high potassium diet; monitor regularly\n2. Gynaecomastia (and breast pain/impotence in men) — due to anti-androgen effects of spironolactone structure. Eplerenone (selective mineralocorticoid antagonist) causes less gynaecomastia."
    },
    {
        "id": "t5-r58",
        "question": "What are the signs and symptoms of digoxin toxicity?",
        "answer": "Digoxin has a narrow therapeutic index (therapeutic: 1–2 ng/mL; toxic: >2 ng/mL). Risk is increased in hypokalaemia (K+ competes with digoxin at Na/K-ATPase).\nSigns/symptoms of toxicity:\n- GI: nausea, vomiting, anorexia, diarrhoea\n- Neurological: confusion, headache, fatigue, weakness\n- Visual: xanthopsia (yellow-green tinge to vision), halos around lights, blurred vision\n- Cardiac: bradycardia, heart block, atrial tachycardia with AV block, premature ventricular beats, VF\nManagement: stop digoxin; correct hypokalaemia; digoxin-specific antibody fragments (Digibind) for severe toxicity"
    },
    {
        "id": "t5-r59",
        "question": "Why must beta-blockers be used only in STABLE, not ACUTE, heart failure?",
        "answer": "In stable chronic heart failure: beta-blockers reduce sympathetic over-stimulation of the failing heart → reduce myocardial damage and arrhythmias → improve survival (carvedilol, bisoprolol proven to reduce mortality by ~30%).\nIn acute/decompensated heart failure: the failing heart depends on sympathetic stimulation (tachycardia, increased contractility) to maintain cardiac output. Beta-blockers suddenly remove this compensatory drive → cardiac output falls → clinical deterioration, pulmonary oedema, hypotension. Therefore: NEVER start beta-blockers in acutely decompensated heart failure. Only introduce once patient is stable and euvolaemic."
    },
    {
        "id": "t5-r60",
        "question": "What is Cor Pulmonale and how does it develop?",
        "answer": "Cor Pulmonale = right ventricular failure (RVF) caused by pulmonary hypertension secondary to chronic lung disease (most commonly COPD).\nPathophysiology: chronic lung disease → chronic hypoxia → hypoxic pulmonary vasoconstriction (the lung shunts blood away from poorly ventilated areas) → chronically raised pulmonary vascular resistance → right ventricle must pump against high afterload → right ventricular hypertrophy → eventually right ventricular failure.\nFeatures: peripheral oedema, raised JVP, hepatomegaly, right parasternal heave. Cor Pulmonale differs from right heart failure caused by left heart disease."
    },
    # ARRHYTHMIAS
    {
        "id": "t5-r61",
        "question": "Summarise the Vaughan Williams classification of antiarrhythmic drugs with one example for each class.",
        "answer": "Class I — Sodium channel blockers: slow conduction; used for ventricular arrhythmias\n  Ia: quinidine, procainamide (prolong action potential)\n  Ib: lidocaine, mexiletine (shorten action potential)\n  Ic: flecainide (minimal effect on action potential duration)\nClass II — Beta-blockers (e.g. atenolol, metoprolol): reduce automaticity of SA node; used for AF rate control, SVT\nClass III — Potassium channel blockers (e.g. amiodarone, sotalol): prolong action potential; used for VF, AF rhythm control\nClass IV — Calcium channel blockers (e.g. verapamil, diltiazem): slow AV node conduction; used for SVT"
    },
    {
        "id": "t5-r62",
        "question": "What is the mechanism of action and main adverse effects of amiodarone?",
        "answer": "Mechanism: Class III antiarrhythmic — potassium channel blocker → prolongs the cardiac action potential duration and refractory period → prevents re-entry arrhythmias; also has Class I, II, and IV effects.\nFirst-line for: ventricular fibrillation (VF) resuscitation, haemodynamically unstable VT.\nAdverse effects (extensive because amiodarone is highly lipophilic and accumulates in tissues):\n- Thyroid: hypo- or hyperthyroidism (contains 37% iodine)\n- Pulmonary fibrosis (most serious; dose-dependent)\n- Peripheral neuropathy\n- Hepatitis (LFT monitoring needed)\n- Irreversible blue-grey skin discolouration (photosensitivity)\n- Corneal microdeposits\n- Pro-arrhythmic (can cause torsade de pointes)\nVery long half-life (40–55 days)"
    },
    {
        "id": "t5-r63",
        "question": "What is adenosine used for and how does it work?",
        "answer": "Adenosine is used to terminate acute supraventricular tachycardia (SVT), particularly those involving the AV node (e.g. AVNRT — AV nodal re-entry tachycardia, AVRT). It is also a diagnostic tool to reveal underlying atrial rhythm in tachycardias.\nMechanism: activates A1 adenosine receptors → opens K+ channels in the AV node → hyperpolarises the node → transiently blocks AV node conduction (seconds) → terminates re-entry circuits.\nAdministration: rapid IV bolus (6mg, then 12mg if needed). Very short half-life (<10 seconds). Adverse effects: transient flushing, chest tightness, brief asystole, bronchospasm (contraindicated in asthma)."
    },
    {
        "id": "t5-r64",
        "question": "What is complete (third degree) heart block and how is it managed?",
        "answer": "Complete heart block (3rd degree): no impulses conducted from atria to ventricles through the AV node. Atria and ventricles beat independently (AV dissociation). Ventricular escape rhythm: 20–40 bpm (inherently slow, unstable, prone to asystole). \nCauses: MI (inferior), digoxin toxicity, fibrosis of conduction system, Lyme disease, cardiac surgery.\nSymptoms: syncope (Stokes-Adams attacks), breathlessness, fatigue, sudden death.\nManagement: if haemodynamically compromised: atropine (IV) or temporary transcutaneous pacing immediately; followed by permanent pacemaker implantation (PPM)."
    },
    {
        "id": "t5-r65",
        "question": "What is the risk of dental electromagnetic equipment for patients with pacemakers or ICDs?",
        "answer": "Older pacemakers were susceptible to electromagnetic interference (EMI) from dental equipment, which could cause pacemaker inhibition or reset. Modern pacemakers (post-2000) have better shielding and are generally safe.\nHighest-risk dental equipment: ultrasonic scalers, electrosurgery/diathermy units, pulp testers, and older piezo devices.\nSafest equipment: conventional dental drills, suction, X-rays, curing lights (all safe).\nManagement: check manufacturer pacemaker card; keep electrosurgery >15cm from device; if uncertain, avoid ultrasonic scalers and use alternative methods. ICD patients: same general principles."
    },
    {
        "id": "t5-r66",
        "question": "What is the CHA2DS2-VASc score and how is it used?",
        "answer": "CHA2DS2-VASc calculates stroke risk in atrial fibrillation to guide anticoagulation decisions:\nC — Congestive heart failure (1)\nH — Hypertension (1)\nA2 — Age ≥75 (2 points)\nD — Diabetes mellitus (1)\nS2 — Stroke/TIA history (2 points — most important)\nV — Vascular disease (IHD, PAD, aortic plaque) (1)\nA — Age 65–74 (1)\nSc — Sex category: female (1)\nScore ≥2 in males or ≥3 in females: anticoagulation recommended (warfarin or DOAC). Score 1 in males: consider anticoagulation. Score 0: no treatment needed."
    },
    {
        "id": "t5-r67",
        "question": "What is rate control vs rhythm control in atrial fibrillation?",
        "answer": "Rate control: reduce the ventricular rate to normal (60–100 bpm at rest) without trying to restore sinus rhythm. Drugs: beta-blockers (bisoprolol), digoxin, rate-limiting CCBs (diltiazem, verapamil). Often used in elderly patients or those with persistent AF.\nRhythm control: restore and maintain sinus rhythm. Methods: chemical cardioversion (amiodarone, flecainide), electrical DC cardioversion, catheter ablation. Used when rate control fails to control symptoms or in younger patients.\nAnticoagulation: required for both strategies (if CHA2DS2-VASc ≥2) regardless of rhythm status."
    },
    # HYPERTENSION
    {
        "id": "t5-r68",
        "question": "What is ambulatory blood pressure monitoring (ABPM) and why is it used?",
        "answer": "ABPM: a portable device automatically records BP at regular intervals (usually every 30 minutes) over 24 hours as the patient goes about normal activities. NICE recommends ABPM as the gold standard for confirming hypertension diagnosis.\nWhy: avoids 'white coat hypertension' (elevated BP in clinic due to anxiety); detects 'masked hypertension' (normal in clinic, high at home); reveals nocturnal hypertension (non-dipping pattern associated with end-organ damage). ABPM threshold: daytime average ≥135/85 mmHg = Stage 1 hypertension (vs clinic ≥140/90)."
    },
    {
        "id": "t5-r69",
        "question": "What are the adverse effects of ACE inhibitors relevant to dentistry?",
        "answer": "1. Dry cough (bradykinin accumulation — 10–15% of patients; reason to switch to ARB)\n2. Angioedema (swelling of lips, tongue, larynx — potentially life-threatening airway emergency; rare but well-documented; can occur years after starting drug; treat with adrenaline IM, antihistamine, corticosteroid)\n3. Hyperkalaemia (reduce K+ excretion — dangerous if combined with spironolactone or potassium-sparing diuretics)\n4. Postural hypotension (vasodilation — patients may feel dizzy on sitting up after dental chair)\n5. Altered taste (captopril — sulphydryl group; metallic taste)\n6. Burning mouth syndrome (rarely reported)"
    },
    {
        "id": "t5-r70",
        "question": "What is the FAST acronym for stroke recognition?",
        "answer": "F — Face: asymmetry, drooping, unilateral weakness; ask patient to smile\nA — Arms: weakness; ask patient to raise both arms — one drifts downward\nS — Speech: slurred, inappropriate words, unable to speak or understand\nT — Time: note time of onset; call 999 immediately\nImportance of time: ischaemic stroke treated with thrombolysis (alteplase) if within 4.5 hours; 'Time is brain' — approximately 1.9 million neurons die per minute of ischaemia. Door-to-needle time targets: thrombolysis within 60 minutes of hospital arrival."
    },
    {
        "id": "t5-r71",
        "question": "What is the difference between a TIA and a stroke in terms of definition and management?",
        "answer": "TIA (Transient Ischaemic Attack): focal neurological deficit due to vascular cause that resolves completely within 24 hours (by definition). Modern definition: resolves within 1 hour with no diffusion restriction on MRI.\nStroke: neurological deficit lasting >24 hours (or causing death) due to vascular cause — either ischaemic (85%) or haemorrhagic (15%).\nManagement of TIA: ABCD2 score (Age, BP, Clinical features, Duration, Diabetes) guides urgency. High-risk TIA: aspirin 300mg immediately; specialist review within 24 hours; antiplatelet, statin, antihypertensive. TIA has 10–15% stroke risk within 3 months."
    },
    # PVD
    {
        "id": "t5-r72",
        "question": "What is the ankle-brachial pressure index (ABPI) and how is it interpreted?",
        "answer": "ABPI = systolic BP at ankle ÷ systolic BP at arm (brachial artery). Measured with a handheld Doppler probe.\nInterpretation:\n>1.3: falsely elevated — calcified, incompressible arteries (common in diabetes, elderly); unreliable\n0.9–1.3: normal\n0.7–0.9: mild PAD — claudication\n0.5–0.7: moderate PAD — claudication, consider revascularisation\n<0.5: severe PAD — critical ischaemia likely; Doppler pressure in foot <50 mmHg indicates critical ischaemia\n<0.3: limb at immediate risk of loss"
    },
    {
        "id": "t5-r73",
        "question": "List the six Ps of acute limb ischaemia.",
        "answer": "1. Pain — severe, sudden onset\n2. Pallor — cold, pale leg (white → blue → mottled)\n3. Pulselessness — absent distal pulses\n4. Paraesthesiae — numbness, tingling (ischaemia of sensory nerves)\n5. Paralysis — loss of motor function (ischaemia of motor nerves)\n6. Perishingly cold (poikilothermia) — limb assumes ambient temperature\nIrreversible nerve and muscle damage occurs after 4–6 hours. Emergency management: IV heparin immediately, urgent analgesia, surgical embolectomy or bypass. Causes: thrombosis in situ (more common), arterial embolism (usually from AF or cardiac thrombus)."
    },
    {
        "id": "t5-r74",
        "question": "What is aortic dissection, what causes it, and how does it present?",
        "answer": "Aortic dissection: a tear in the aortic intima allows blood to enter and track within the tunica media, creating a false lumen alongside the true lumen.\nCauses: hypertension (most common — medial degeneration); connective tissue disorders (Marfan's syndrome — fibrillin-1 mutation; Ehlers-Danlos); trauma (road traffic accidents); coarctation; pregnancy (third trimester).\nPresentation: sudden, severe, tearing or ripping chest pain radiating to the back/scapulae (different character from angina); unequal blood pressures in both arms; pulse deficit; hypertension or hypotension; aortic regurgitation murmur.\nManagement: emergency BP control (IV labetalol), surgical repair (Type A — involving ascending aorta) or stenting (Type B)."
    },
    {
        "id": "t5-r75",
        "question": "What is a berry aneurysm and what is its classic complication?",
        "answer": "Berry (saccular) aneurysm: a sac-like outpouching of an arterial wall, typically at bifurcations of the circle of Willis (most common: junction of anterior communicating artery and anterior cerebral artery; posterior communicating artery is second most common). Associated with polycystic kidney disease, coarctation of aorta, connective tissue disorders.\nComplication: rupture → subarachnoid haemorrhage (SAH). Classic presentation: sudden severe 'thunderclap headache' ('worst headache of my life'), photophobia, meningism (neck stiffness, Kernig's sign). Diagnosis: CT head (blood in subarachnoid space) → lumbar puncture if CT negative (xanthochromia). Management: neurosurgical clipping or endovascular coiling."
    },
    # ANTICOAGULANTS
    {
        "id": "t5-r76",
        "question": "How does heparin work and how is it reversed?",
        "answer": "Mechanism: heparin enhances the activity of antithrombin III (a natural anticoagulant) by 1000-fold → antithrombin III inactivates thrombin (factor IIa) and factor Xa → immediate anticoagulation. Unfractionated heparin (UFH) inhibits both thrombin and Xa. LMWH (dalteparin, enoxaparin) preferentially inhibits factor Xa.\nMonitoring: UFH monitored by APTT (activated partial thromboplastin time); LMWH does not need routine monitoring (predictable dose response).\nReversal: protamine sulphate neutralises UFH rapidly (but only partially reverses LMWH). Dose: 1mg protamine per 100 units of heparin administered in last 2–3 hours."
    },
    {
        "id": "t5-r77",
        "question": "What is the difference between unfractionated heparin (UFH) and low molecular weight heparin (LMWH)?",
        "answer": "UFH: large molecule; IV or SC; inhibits thrombin AND factor Xa; monitored by APTT; short half-life (1–2 hrs); fully reversible with protamine; risk of heparin-induced thrombocytopenia (HIT); used in hospital, renal failure, when rapid reversal needed.\nLMWH (dalteparin, enoxaparin, tinzaparin): fragments of heparin; SC injection once or twice daily; predominantly inhibit factor Xa; predictable pharmacokinetics → no routine monitoring; less HIT risk; longer half-life (4–6 hrs); renally excreted (contraindicated in severe renal failure); partially reversed by protamine; easier outpatient use."
    },
    {
        "id": "t5-r78",
        "question": "What is the mechanism of warfarin and which clotting factors does it inhibit?",
        "answer": "Warfarin: vitamin K antagonist — inhibits hepatic vitamin K epoxide reductase enzyme → prevents recycling of vitamin K back to its active form → depletes vitamin K-dependent clotting factors.\nFactors inhibited: II (prothrombin), VII, IX, X (mnemonic: 1972 — these were discovered in 1972) and protein C and protein S (anticoagulants — important: early in warfarin therapy, protein C falls first → brief hypercoagulable state → reason for heparin overlap when starting warfarin).\nMonitoring: INR (International Normalised Ratio — standardises PT ratio; normal = ~1; therapeutic = 2–3 for most; 2.5–3.5 for mechanical valves).\nHalf-life: 35–37 hours; 98% protein-bound."
    },
    {
        "id": "t5-r79",
        "question": "What is the mechanism of action of clopidogrel and what is its dental significance?",
        "answer": "Clopidogrel: prodrug (requires hepatic CYP2C19 activation to active thiol metabolite) → irreversible antagonist of P2Y12 ADP receptor on platelets → prevents ADP-induced platelet aggregation.\nOnset: 3–7 days for full effect. Duration: irreversible for platelet lifespan (7–10 days).\nDental significance: increases bleeding risk (like aspirin). For routine extractions: continue clopidogrel — do NOT stop (risk of in-stent thrombosis in coronary stent patients can be fatal). Use local haemostatic measures. If on dual antiplatelet (aspirin + clopidogrel after PCI): both must be continued — stopping either increases coronary stent thrombosis risk significantly."
    },
    {
        "id": "t5-r80",
        "question": "What are the reversal agents for the four main DOACs?",
        "answer": "DOACs and reversal:\n1. Dabigatran (thrombin inhibitor) → reversed by idarucizumab (Praxbind — humanised antibody fragment; binds dabigatran with very high affinity; approved 2015)\n2. Rivaroxaban / apixaban / edoxaban (factor Xa inhibitors) → reversed by andexanet alfa (FXa decoy protein; approved 2019); also coagulation factor concentrates (PCC — 4-factor prothrombin complex concentrate) can be used in emergencies\nFor non-emergency procedures: no reversal agent needed; time the procedure according to DOAC half-life and renal function (usually skip one dose or treat in morning before dose). Activated charcoal if within 2 hours of ingestion."
    },
    # CVD DRUGS / DENTAL IMPLICATIONS
    {
        "id": "t5-r81",
        "question": "What drugs can cause gingival hyperplasia and what is the management?",
        "answer": "Drugs causing gingival overgrowth:\n1. Calcium channel blockers — dihydropyridines: nifedipine (most common), amlodipine (less common)\n2. Ciclosporin (calcineurin inhibitor/immunosuppressant — post-organ transplant)\n3. Phenytoin (anti-epileptic)\nPathophysiology: increased collagen synthesis by fibroblasts; reduced collagen degradation; poor oral hygiene exacerbates severity.\nManagement: intensive oral hygiene instruction (reduces severity); referral to periodontist; liaison with physician about drug substitution (e.g. switch from nifedipine to amlodipine or to a different antihypertensive class — some improvement but may not fully resolve); surgical gingivectomy as last resort if functional impairment."
    },
    {
        "id": "t5-r82",
        "question": "What are the oral manifestations of drugs used in cardiovascular disease?",
        "answer": "Gingival hyperplasia: calcium channel blockers (dihydropyridines — nifedipine, amlodipine)\nXerostomia: beta-blockers, ACE inhibitors, diuretics, CCBs\nOral ulceration: nicorandil (severe, non-healing, can be extensive)\nLichenoid reactions: beta-blockers, diuretics, ACE inhibitors, thiazide diuretics, NSAIDs, statins\nAngioedema (tongue/lip swelling): ACE inhibitors — emergency!\nAltered taste: captopril (metallic taste), atorvastatin\nIncreased tooth demineralisation: beta-blockers (reduce salivary flow + alter saliva composition)\nBurning mouth syndrome: ACE inhibitors (occasionally)\nPeriodontal disease (bidirectional relationship): CVD shares inflammatory pathways with periodontitis"
    },
    {
        "id": "t5-r83",
        "question": "Why are morning appointments preferred for patients with significant cardiovascular disease?",
        "answer": "Cortisol (endogenous steroid) peaks in the morning, providing natural cardiovascular protection and better stress tolerance. Most adverse cardiac events (MI, sudden cardiac death, stroke, arrhythmias) peak in the early to mid-morning (6am–noon) due to morning sympathetic surge, platelet aggregability, and catecholamine levels.\nFor dental patients with CVD: morning appointments → patient arrives at their most physiologically robust; afternoon/evening appointments coincide with fatigue and can be harder to manage. Shorter appointments reduce stress. Effective LA is critical — pain and anxiety cause equal catecholamine surges to the physical stress of surgery."
    },
    {
        "id": "t5-r84",
        "question": "In which cardiovascular conditions are vasoconstrictors (adrenaline) in LA relatively or absolutely contraindicated?",
        "answer": "Absolutely contraindicated or use minimum amount:\n- Uncontrolled severe hypertension (systolic >200 or diastolic >115 mmHg)\n- Unstable angina or recent MI (<3 months)\n- Uncontrolled cardiac arrhythmias\n- Severe uncontrolled heart failure\n- Phaeochromocytoma (catecholamine-secreting tumour — risks hypertensive crisis)\n- Patients on MAOIs or tricyclic antidepressants (potentiate adrenaline)\n\nRelatively contraindicated (use minimal amounts with aspiration and slow injection):\n- Controlled hypertension\n- Well-controlled heart failure\n- Non-selective beta-blockers (theoretical risk of hypertension from unopposed alpha stimulation — usually safe in practice)"
    },
    {
        "id": "t5-r85",
        "question": "What post-operative analgesia is safest in patients with heart failure, and what should be avoided?",
        "answer": "Safe:\n- Paracetamol (first-line — no cardiovascular effects; safe up to 1g QDS in normal hepatic function)\n- Codeine/dihydrocodeine (weak opioids — second-line; monitor for constipation)\n\nAVOID:\n- NSAIDs (ibuprofen, diclofenac, naproxen, COX-2 inhibitors): cause sodium and water retention (worsen oedema and heart failure); reduce renal perfusion (especially dangerous with ACE inhibitors — 'triple whammy': ACE inhibitor + diuretic + NSAID → acute renal failure); increase blood pressure; increase cardiovascular event risk\n- Aspirin at analgesic doses (325mg+) — same prostaglandin-mediated effects on kidney and fluid balance"
    },
    {
        "id": "t5-r86",
        "question": "What is the periodontal–cardiovascular disease link?",
        "answer": "Bidirectional inflammatory relationship between periodontitis and CVD:\nEvidence: multiple meta-analyses show 1.5–2× increased CVD risk in patients with periodontal disease, independent of shared risk factors (smoking, diabetes).\nProposed mechanisms:\n1. Bacteraemia: periodontal bacteria (Porphyromonas gingivalis, Tannerella forsythia) enter bloodstream → adhere to atherosclerotic plaques → promote platelet aggregation and thrombus formation\n2. Systemic inflammation: raised CRP, IL-6, TNF-alpha from chronic periodontal infection → promotes endothelial dysfunction and atherosclerosis progression\nClinical relevance: treating periodontal disease may reduce systemic CRP and improve endothelial function. Regular dental review is part of CVD prevention."
    },
    {
        "id": "t5-r87",
        "question": "How should you position a patient with significant left-sided heart failure in the dental chair?",
        "answer": "DO NOT place in supine (fully flat) position. Orthopnoea means the patient cannot lie flat without becoming breathless.\nPosition: semi-reclined or upright (at least 30–45° from horizontal; ideally treat in the position the patient can breathe most comfortably). Ask the patient before starting ('How many pillows do you sleep on?').\nRationale: supine position increases venous return to the heart → increases pulmonary blood volume → worsens pulmonary oedema → acute breathlessness. Sitting up uses gravity to shift fluid to dependent areas (legs) away from lungs.\nOther considerations: shorter appointments; supplemental oxygen may be needed; avoid respiratory-depressant drugs (sedatives, opioids)."
    },
    {
        "id": "t5-r88",
        "question": "What is the mechanism and management of ACE inhibitor angioedema?",
        "answer": "Mechanism: ACE inhibitors prevent degradation of bradykinin → bradykinin accumulates → activates B2 receptors → increased vascular permeability → angioedema (deep dermal/submucosal swelling).\nPresentation: sudden onset swelling of lips, tongue, soft palate, uvula, larynx — can cause fatal airway obstruction. May occur at any time (even years after starting drug). Not dose-dependent.\nManagement (it is a medical emergency):\n1. STOP the ACE inhibitor (switch to ARB — ARBs don't cause bradykinin accumulation)\n2. Adrenaline IM 500 micrograms (1:1000) if anaphylaxis or airway threatened\n3. IV chlorphenamine (antihistamine)\n4. IV hydrocortisone\n5. Call emergency services; secure airway\nFrequency: occurs in 0.1–0.5% of users; more common in patients of African origin"
    },
    {
        "id": "t5-r89",
        "question": "What is dual antiplatelet therapy (DAPT) and when is it used?",
        "answer": "DAPT = combination of aspirin + a P2Y12 inhibitor (clopidogrel, ticagrelor, or prasugrel). Used for:\n1. Acute coronary syndrome (ACS — STEMI, NSTEMI, unstable angina): DAPT for 12 months post-event\n2. Following coronary artery stenting (PCI): DAPT for 1–12 months depending on stent type (bare metal vs drug-eluting) and bleeding risk — prevents in-stent thrombosis\n3. Following CABG: aspirin alone usually sufficient\nDental relevance: NEVER stop DAPT without cardiologist advice — premature discontinuation causes acute stent thrombosis risk (mortality ~30–50% if it occurs). For dental extractions: continue DAPT, use local haemostatic measures."
    },
    {
        "id": "t5-r90",
        "question": "What drugs can cause lichenoid reactions in the mouth and what does this look like?",
        "answer": "Drug-induced lichenoid reactions (OLP-like appearance): white striae (Wickham's striae), erosions, erythematous areas — clinically and histologically similar to oral lichen planus.\nCommon causative drugs:\n- Beta-blockers (propranolol, atenolol)\n- Thiazide/thiazide-like diuretics (hydrochlorothiazide, indapamide)\n- ACE inhibitors (captopril, lisinopril)\n- NSAIDs (ibuprofen, aspirin)\n- Statins (atorvastatin, simvastatin)\n- Oral hypoglycaemics (metformin, sulfonylureas)\n- Gold salts, penicillamine, quinidine, antimalarials\nManagement: identify and stop offending drug (if possible, with prescriber); topical corticosteroids for symptomatic lesions; usually resolves within weeks to months of stopping drug."
    },
    {
        "id": "t5-r91",
        "question": "What is the role of statins in cardiovascular disease and what are their dental implications?",
        "answer": "Statins (atorvastatin, simvastatin, rosuvastatin): inhibit HMG-CoA reductase → reduce hepatic cholesterol synthesis → upregulate LDL receptors → lower LDL-C by 30–50%; anti-inflammatory and plaque-stabilising effects beyond lipid-lowering.\nIndications: primary/secondary CVD prevention, familial hypercholesterolaemia, diabetes with CVD risk.\nTarget: LDL <1.8 mmol/L in high-risk patients.\nDental implications:\n- Lichenoid reactions (rare)\n- Altered taste (atorvastatin — metallic or bitter)\n- Some statins interact with clarithromycin (CYP3A4 inhibitor → raise simvastatin levels → myopathy risk): use azithromycin instead, or omit statin temporarily; atorvastatin less problematic"
    },
    {
        "id": "t5-r92",
        "question": "What is the difference between rate and rhythm control for AF, and which drugs are used for each?",
        "answer": "Rate control (slow ventricular rate; atria still in AF):\n- Beta-blockers (bisoprolol, atenolol) — first line\n- Rate-limiting CCBs (diltiazem, verapamil) — second line if beta-blocker contraindicated\n- Digoxin — in sedentary/elderly patients; less effective on exercise\n- Combination: digoxin + beta-blocker if needed\n\nRhythm control (restore sinus rhythm):\n- Flecainide (Class Ic) — if no structural heart disease\n- Amiodarone (Class III) — if structural heart disease or flecainide contraindicated\n- DC cardioversion (electrical) — most effective for acute restoration\n- Catheter ablation (pulmonary vein isolation) — curative in selected patients with paroxysmal AF"
    },
    {
        "id": "t5-r93",
        "question": "What are the differences between primary and secondary prevention of CVD in terms of pharmacological management?",
        "answer": "Primary prevention (reducing risk in people WITHOUT established CVD):\n- Antihypertensives if BP ≥140/90\n- Statins if 10-year CVD risk ≥10% (QRISK calculator)\n- Low-dose aspirin: NO LONGER recommended routinely in primary prevention (bleeding risk outweighs benefit in those without CVD)\n- Lifestyle: smoking cessation, exercise, diet, weight loss\n\nSecondary prevention (after established CVD — MI, angina, stroke, PAD):\n- Aspirin 75mg daily (antiplatelet)\n- Statin (high intensity — atorvastatin 80mg)\n- ACE inhibitor (for post-MI, heart failure, diabetics)\n- Beta-blocker (post-MI to reduce reinfarction and sudden death)\n- RAAS blockade + antihypertensives to target BP <130/80"
    },
    {
        "id": "t5-r94",
        "question": "What is infective endocarditis prophylaxis with antibiotics and what is the regimen if it WERE used?",
        "answer": "Current UK practice (NICE 2016): routine antibiotic prophylaxis NOT recommended before dental procedures for any patient.\nHistorical regimen (still used in some countries; may be used in specific high-risk cases at clinician's discretion):\nAmoxicillin 3g single oral dose 1 hour before procedure\nOR if penicillin-allergic: clindamycin 600mg oral 1 hour before\nSDCEP guidance allows for patient-specific risk assessment in high-risk individuals. The most important prevention remains optimal oral hygiene — reducing the daily bacteraemia from tooth brushing is far more important than pre-procedure prophylaxis."
    },
    {
        "id": "t5-r95",
        "question": "What is hypertensive urgency vs emergency, and how does each present?",
        "answer": "Hypertensive urgency: severely elevated BP (typically >180/110 mmHg) WITHOUT evidence of acute end-organ damage. Symptoms: headache, flushing, anxiety. Management: gradual BP reduction over 24–48 hours with oral antihypertensives; not a medical emergency requiring immediate IV treatment.\nHypertensive emergency (crisis): severely elevated BP WITH acute end-organ damage:\n- Hypertensive encephalopathy (severe headache, confusion, seizures)\n- Acute left ventricular failure\n- Aortic dissection\n- Hypertensive nephropathy\n- Retinal changes (haemorrhages, papilloedema)\nManagement: IV labetalol (or nicardipine, sodium nitroprusside) in monitored setting; reduce MAP by 20–25% over 1–2 hours (too rapid → watershed infarction)."
    },
    {
        "id": "t5-r96",
        "question": "What are the antiplatelet effects of aspirin and what are the specific dosing regimens used in dentistry?",
        "answer": "Aspirin mechanism: irreversibly acetylates COX-1 → blocks thromboxane A2 synthesis → antiplatelet effect lasting 7–10 days (platelet lifespan).\nDosing:\n- Prophylactic (anti-thrombotic): 75–100mg daily\n- Acute MI: 300mg immediately (load), then 75mg daily\n- Dental: do NOT stop low-dose aspirin before extractions; risk of cardiac event outweighs bleeding risk; local haemostasis sufficient\nContraindications in dentistry:\n- NEVER prescribe aspirin under age 12 (Reye's syndrome — hepatic encephalopathy)\n- Avoid if active peptic ulcer, haemophilia, or recent GI/intracranial haemorrhage\n- Do NOT add NSAIDs to a patient already on aspirin (GI bleeding risk)"
    },
    {
        "id": "t5-r97",
        "question": "What is the INR monitoring system for warfarin and what are the therapeutic ranges for different conditions?",
        "answer": "INR (International Normalised Ratio): standardises prothrombin time (PT) across laboratories using an internationally standardised thromboplastin reagent.\nNormal INR (no anticoagulation): ~1.0\nTherapeutic ranges:\n- VTE treatment/prevention, AF: 2.0–3.0\n- Mechanical prosthetic heart valves (mitral): 3.0–4.0\n- Mechanical aortic valves (lower risk): 2.5–3.5\nDental threshold:\n- INR ≤4.0: proceed with dental procedure using local haemostasis\n- INR >4.0: postpone elective procedure; contact GP/haematologist\n- Check INR within 72 hours pre-procedure (ideally same day); INR can fluctuate"
    },
    {
        "id": "t5-r98",
        "question": "What is the role of tranexamic acid in dental haemostasis and how is it used?",
        "answer": "Tranexamic acid: antifibrinolytic drug — synthetic lysine analogue → competitively inhibits plasminogen binding to fibrin → prevents conversion of plasminogen to plasmin → prevents clot dissolution (fibrinolysis) → stabilises clot once formed.\nOral haemostasis use:\n- 5% tranexamic acid mouthwash: 10mL for 2 minutes 4 times daily for 2 days post-extraction\n- Does NOT raise INR (unlike systemic antifibrinolytics at high doses)\n- Safe to use in anticoagulated patients alongside local measures\n- Also available as IV/oral tablet for systemic use (trauma, surgery, menorrhagia)\nAlong with: oxidised cellulose (Surgicel), gelatin sponge (Gelfoam), resorbable collagen, figure-of-eight sutures."
    },
    {
        "id": "t5-r99",
        "question": "What is the management of a patient taking a DOAC who needs an urgent dental extraction?",
        "answer": "For most routine dental extractions (1–3 simple teeth) on DOACs:\n1. Do NOT stop the DOAC\n2. Check renal function (all DOACs are renally cleared; impaired renal function prolongs drug effect)\n3. Timing: for once-daily DOACs: ideally treat 12–18 hours after last dose (before next dose). For twice-daily DOACs: treat 6–8 hours after last dose.\n4. Use local haemostatic measures: oxidised cellulose, sutures, tranexamic acid mouthwash 5% 4× daily for 2 days\n5. Monitor for 30 minutes post-procedure before discharge\nFor major oral surgery: consult with prescribing physician; consider temporary DOAC interruption (1–2 days for high bleeding risk); reversal agents rarely needed in elective cases."
    },
    {
        "id": "t5-r100",
        "question": "What is Conn's syndrome and how does it cause hypertension?",
        "answer": "Conn's syndrome = primary hyperaldosteronism: autonomous, non-RAAS-dependent excess aldosterone secretion, usually from a unilateral adrenal adenoma (75%) or bilateral adrenal hyperplasia (25%).\nMechanism: excess aldosterone → acts on collecting duct mineralocorticoid receptors → retains Na+ (and water) → expands circulating volume → hypertension. Simultaneously: K+ is excreted → hypokalaemia (weakness, cramps, polyuria).\nDiagnosis: raised aldosterone-to-renin ratio (ARR); adrenal CT; adrenal vein sampling to lateralise.\nManagement: unilateral adenoma → adrenalectomy (curative); bilateral hyperplasia → spironolactone (aldosterone antagonist). Account for ~5–10% of all hypertension."
    }
]

data['recallIt'].extend(new_recall)

with open('data/theme-5.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Total recallIt: {len(data['recallIt'])}")
