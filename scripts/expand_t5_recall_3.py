import json

with open('data/theme-5.json', 'r') as f:
    data = json.load(f)

new_recall = [
    {
        "id": "t5-r211",
        "question": "What is the Yellow Card scheme and which CVD drugs are commonly reported on it?",
        "answer": "The Yellow Card scheme (MHRA — Medicines and Healthcare products Regulatory Agency): a voluntary system for reporting suspected adverse drug reactions (ADRs) by healthcare professionals and patients/public. Reports unexpected or serious reactions, even if causation is uncertain.\nCVD drugs frequently reported:\n- ACE inhibitors: cough, angioedema\n- Amiodarone: thyroid disorders, pulmonary fibrosis, hepatotoxicity, skin discolouration\n- Statins: myopathy, rhabdomyolysis, hepatotoxicity\n- Warfarin: bleeding complications, interactions\n- Nicorandil: oral/GI ulceration\n- Clopidogrel: bleeding, TTP (thrombotic thrombocytopenic purpura)\nDental relevance: dentists should report unexpected oral adverse effects of cardiovascular drugs (lichenoid reactions, gingival hyperplasia, angioedema, ulceration) via the Yellow Card scheme."
    },
    {
        "id": "t5-r212",
        "question": "What is the significance of natriuretic peptides (ANP and BNP) in cardiovascular disease?",
        "answer": "Atrial natriuretic peptide (ANP): released from atrial myocytes in response to atrial stretch (volume/pressure overload) → promotes sodium and water excretion (natriuresis and diuresis) + vasodilation; counter-regulatory to RAAS.\nBrain/B-type natriuretic peptide (BNP): released from ventricular myocytes in response to increased wall stress (raised filling pressures) → same effects as ANP.\nNT-proBNP: the inactive N-terminal fragment of proBNP; longer half-life than BNP; used as the routine clinical biomarker.\nClinical uses:\n1. Diagnosis of heart failure: BNP <100 pg/mL rules out HF; BNP >400 pg/mL strongly suggests HF in breathless patient\n2. Prognosis: higher BNP/NT-proBNP = worse outcome\n3. Treatment monitoring: falling BNP indicates response to HF therapy\n4. Used to guide diuretic dosing in HF management clinics"
    },
    {
        "id": "t5-r213",
        "question": "What is the difference between a coronary artery bypass graft (CABG) and percutaneous coronary intervention (PCI)?",
        "answer": "PCI (percutaneous coronary intervention — 'angioplasty + stenting'): catheter inserted via radial or femoral artery under X-ray guidance → balloon inflates at coronary stenosis → stent deployed to keep vessel open. Minimally invasive; quick recovery; local anaesthetic/sedation. Dual antiplatelet therapy (DAPT) required post-stent. Best for: 1–2 vessel disease, suitable anatomy.\nCABG (coronary artery bypass grafting): open-heart surgery; veins (saphenous) or arteries (internal mammary/radial) used to bypass blocked coronary arteries. Longer recovery. Aspirin only (no clopidogrel). Best for: left main stem disease, 3-vessel disease, diabetics (CABG superior long-term), complex anatomy. Survival benefit in left main stem/3-vessel disease compared to PCI.\nDental relevance: CABG patients on warfarin (rarely) or antiplatelet; PCI patients on DAPT — never stop without cardiologist advice."
    },
    {
        "id": "t5-r214",
        "question": "What is the 'vulnerable period' in a heartbeat and how does it relate to arrhythmia risk?",
        "answer": "The vulnerable period (relative refractory period): occurs during the upstroke of the T-wave on ECG — a brief window when only part of the myocardium has repolarised and is excitable again, while the rest is still refractory.\nDanger: an electrical stimulus (e.g. a premature ventricular complex — PVC) landing in this window ('R-on-T phenomenon') encounters a heterogeneous myocardium — some areas can be activated, others cannot → this dispersion of refractoriness creates the perfect substrate for re-entry circuits → can trigger ventricular tachycardia or ventricular fibrillation.\nClinical relevance: DC cardioversion must be synchronised with the QRS complex (avoiding T-wave) — unsynchronised shock could land on T-wave and trigger VF. VF has no defined vulnerable period as all activity is chaotic — defibrillation is unsynchronised."
    },
    {
        "id": "t5-r215",
        "question": "What is a systolic murmur vs diastolic murmur and what are common causes of each?",
        "answer": "Systolic murmur (heard between S1 and S2 — during ventricular contraction/ejection):\n- Ejection systolic murmur (ESM): aortic stenosis (best at right sternal edge, radiates to carotid), pulmonary stenosis, HOCM, aortic sclerosis (no radiation, no gradient)\n- Pansystolic murmur (PSM): mitral regurgitation (apex → axilla), tricuspid regurgitation (LSE), VSD (LSE)\n- Late systolic: mitral valve prolapse (after mid-systolic click)\n\nDiastolic murmur (between S2 and S1 — during ventricular filling — always pathological):\n- Early diastolic: aortic regurgitation (AR — high-pitched, blowing at LSE), pulmonary regurgitation\n- Mid-diastolic: mitral stenosis (low-pitched, rumbling, at apex — heard with patient on left side)"
    },
    {
        "id": "t5-r216",
        "question": "What is complete revascularisation in the context of ACS management?",
        "answer": "In ACS (acute coronary syndrome), the primary PCI targets the 'culprit lesion' — the specific coronary artery responsible for the current presentation (the blocked artery with the ruptured plaque).\nComplete vs incomplete revascularisation:\nComplete: all significant coronary stenoses (>70%) are treated with PCI, not just the culprit vessel. Now preferred — reduces future MACE (major adverse cardiovascular events: MI, death, need for repeat revascularisation) compared to culprit-only PCI.\nIncomplete: only the culprit is treated; other significant lesions left; patient at higher risk of future events.\nContext: many STEMI patients have multi-vessel disease. After the acute STEMI is treated (culprit PCI), the remaining vessels are electively treated within 45 days (COMPLETE trial evidence). Dental relevance: these patients are on DAPT during this period — never stop antiplatelet therapy without cardiology input."
    },
    {
        "id": "t5-r217",
        "question": "What is meant by 'afterload' in the context of heart failure management and which drugs reduce it?",
        "answer": "Afterload: the resistance (pressure) that the left ventricle must overcome to eject blood into the aorta and systemic circulation. Main determinant: peripheral vascular resistance (arteriolar tone).\nIn heart failure: elevated afterload (from RAAS-driven vasoconstriction) means the failing LV must work harder → further reduces stroke volume → worsens cardiac output.\nDrugs that reduce afterload:\n1. ACE inhibitors/ARBs: reduce angiotensin II → vasodilation + reduced aldosterone → lower BP and afterload\n2. Hydralazine: direct arterial vasodilator\n3. Alpha-blockers (doxazosin): block alpha-1 receptors → arterial dilation\n4. Nitrates: predominantly venodilation (reduce preload), but at higher doses also arterial dilation → reduce afterload\n5. Sacubitril/valsartan (Entresto): ARB combined with neprilysin inhibitor → enhances natriuretic peptide vasodilation; newer HF drug improving mortality"
    },
    {
        "id": "t5-r218",
        "question": "What is the mechanism of atrial fibrillation and why does it cause irregular ventricular contraction?",
        "answer": "AF mechanism: multiple chaotic re-entry circuits within both atria fire at 350–600 impulses per minute — no coordinated atrial contraction (the atria 'quiver' instead of contracting). These disorganised impulses bombard the AV node continuously.\nWhy irregular ventricular response: the AV node is the gatekeeper — it responds to atrial impulses in a stochastic (random) fashion based on its refractory period. Some impulses arrive when the AV node is refractory (blocked), others when it has recovered (conducted). This creates a completely random pattern of conduction to the ventricles → irregularly irregular ventricular rate.\nRate: untreated AF typically gives ventricular rate of 100–160 bpm (AV node's intrinsic rate-limiting property protects from conducting every atrial impulse). Rate-control drugs (digoxin, beta-blockers, verapamil) slow AV node conduction → reduce ventricular rate."
    },
    {
        "id": "t5-r219",
        "question": "What are the main causes and consequences of high cardiac output (high-output) heart failure?",
        "answer": "High-output heart failure: the heart is pumping MORE than normal (CO >8 L/min) but still cannot meet the body's excessive metabolic demands → heart failure symptoms despite hyperdynamic circulation.\nCauses (conditions with very high peripheral O2 demand or low SVR):\n1. Anaemia: reduced O2 carrying capacity → compensatory tachycardia and high CO\n2. Hyperthyroidism: increased basal metabolic rate → high demand; also direct chronotropic effect\n3. Pregnancy: 40–50% increase in CO normally; can decompensate in pre-existing heart disease\n4. Arteriovenous (AV) fistula: surgical (dialysis access) or congenital shunting blood directly arterial→venous\n5. Paget's disease of bone: hypervascular bone → functional AV shunting\n6. Severe sepsis (distributive shock)\nTreatment: treat underlying cause; furosemide for fluid overload."
    },
    {
        "id": "t5-r220",
        "question": "What does 'cardiac remodelling' mean in the context of heart failure and what drugs prevent it?",
        "answer": "Cardiac remodelling: progressive structural and functional changes in the heart following injury (MI, pressure overload, volume overload). Changes include:\n- Ventricular dilation (eccentric hypertrophy in volume overload)\n- Wall thinning (loss of myocytes)\n- Shape change: from ellipsoid to spherical (less efficient pump geometry)\n- Fibrosis (replacement of lost myocytes by scar)\n- Molecular: altered gene expression, sarcomeric protein changes\nConsequences: progressive reduction in EF, increasing HF symptoms, arrhythmia risk.\nDrugs that prevent/reverse remodelling:\n1. ACE inhibitors/ARBs: block angiotensin II-mediated hypertrophy and fibrosis\n2. Beta-blockers: reduce catecholamine-driven hypertrophy and myocyte apoptosis\n3. Spironolactone: block aldosterone-driven fibrosis\n4. Sacubitril/valsartan (Entresto): proven to reverse remodelling more effectively than ACE inhibitors alone"
    },
    {
        "id": "t5-r221",
        "question": "What is a myocardial perfusion scan and when is it used?",
        "answer": "Myocardial perfusion scan (MPS/SPECT): a nuclear medicine imaging technique that assesses myocardial blood flow at rest and during stress.\nTechnique: radiotracer (technetium-99m or thallium-201) is injected IV → taken up by myocardial cells proportional to blood flow → gamma camera images taken at rest and after exercise or pharmacological stress (adenosine, dobutamine).\nFindings:\n- Normal perfusion: uniform tracer uptake at rest and stress\n- Reversible defect: reduced uptake on stress, normal at rest → inducible ischaemia (live but ischaemic myocardium — revascularisation will help)\n- Fixed defect: reduced uptake at rest AND stress → scar (previously infarcted — dead myocardium; revascularisation will not help)\nIndications: diagnosis of IHD when coronary angiography not immediately indicated; risk stratification pre-operatively; viability assessment post-MI."
    },
    {
        "id": "t5-r222",
        "question": "What is the clinical significance of a new left bundle branch block (LBBB) in a patient with chest pain?",
        "answer": "New LBBB in the context of chest pain is treated as STEMI equivalent — the patient should be taken directly to the catheterisation laboratory for primary PCI without waiting for enzyme results.\nWhy: LBBB distorts the ECG so profoundly that conventional STEMI criteria (ST elevation in specific leads) cannot be applied. The broad QRS and secondary ST changes ('appropriate ST discordance') mask ST elevation. New LBBB with ischaemic symptoms almost certainly indicates a large anterior MI (often LAD occlusion).\nECG features of LBBB: QRS >120 ms; broad monophasic R in lateral leads (I, aVL, V5–V6); broad S in V1; absent septal Q waves in lateral leads; T-wave discordance (T waves in opposite direction to QRS).\nSgarbossa criteria: can help identify STEMI within LBBB (concordant ST elevation >1 mm or ST elevation ≥5 mm discordant with QRS)."
    },
    {
        "id": "t5-r223",
        "question": "What are the features and management of acute limb ischaemia from an embolism versus in-situ thrombosis?",
        "answer": "Embolism (most common source: cardiac — AF, MI mural thrombus, prosthetic valve):\n- Sudden onset; no prior claudication history; contralateral limb pulses normal\n- No pre-existing PAD; younger patient often\n- Angiography: sharp cut-off with meniscus sign; minimal collaterals\n- Treatment: urgent surgical embolectomy (Fogarty balloon catheter) ± systemic heparinisation\n\nIn-situ thrombosis (on background atherosclerosis):\n- Background of claudication; bilateral disease; pre-existing PAD history\n- Older patient; multiple risk factors\n- Angiography: widespread atherosclerotic disease; multiple occlusions; good collaterals\n- Treatment: thrombolysis (catheter-directed tPA preferred), angioplasty, bypass\n\nBoth: immediate IV heparin; urgent analgesia; limb warming. Fasciotomy needed if compartment syndrome develops after revascularisation (reperfusion oedema)."
    },
    {
        "id": "t5-r224",
        "question": "What are the indications for warfarin versus a DOAC in patients requiring anticoagulation?",
        "answer": "Warfarin preferred:\n- Mechanical prosthetic heart valves (DOACs proven INFERIOR — increased valve thrombosis risk)\n- Moderate-severe mitral stenosis with AF (DOACs not yet fully validated)\n- Antiphospholipid syndrome (especially 'triple positive' — DOACs inferior)\n- Severe renal failure (GFR <15–30 mL/min): DOACs renally cleared; warfarin safer in advanced CKD\n\nDOAC preferred:\n- AF (non-valvular): DOACs superior or non-inferior to warfarin with better safety profile; less monitoring burden\n- VTE (DVT/PE): DOACs first-line; non-inferior to warfarin; no monitoring needed; less drug/food interactions\n- Patients struggling with INR control (labile INR)\n- Patients unable to have regular blood tests\n\nEither:\n- Bioprosthetic valves (after the initial 3-month period)"
    },
    {
        "id": "t5-r225",
        "question": "What is the mechanism of action of nitroglycerin (GTN) at the molecular level?",
        "answer": "GTN (glyceryl trinitrate) → denitrated by mitochondrial aldehyde dehydrogenase (ALDH2) in vascular smooth muscle → releases nitric oxide (NO) → activates soluble guanylate cyclase → converts GTP → cyclic GMP (cGMP) → activates protein kinase G → phosphorylates myosin light chain phosphatase → dephosphorylates myosin → smooth muscle RELAXATION → vasodilation.\nClinical effects:\n- Venodilation (at low doses — main anti-anginal effect): reduces venous return (preload) → reduces cardiac wall stress → lower O2 demand\n- Coronary artery dilation: relieves coronary spasm, dilates large epicardial arteries (does not dilate maximally vasodilated ischaemic arterioles — avoids coronary steal)\n- Arteriodilation (at higher doses): reduces afterload\nTolerance: with continuous use, ALDH2 becomes oxidised (sulfhydryl depletion) → tolerance; requires nitrate-free period."
    },
    {
        "id": "t5-r226",
        "question": "What are the key differences between the four DOACs (dabigatran, rivaroxaban, apixaban, edoxaban)?",
        "answer": "Dabigatran (Pradaxa):\n- Target: direct thrombin (IIa) inhibitor\n- Dosing: twice daily\n- Renal excretion: 80% (most renally dependent — highest risk with renal impairment)\n- Reversal: idarucizumab (Praxbind)\n- GI side effects: dyspepsia (take with food)\n\nRivaroxaban (Xarelto): Factor Xa inhibitor; once daily (with evening meal for AF/VTE); 33% renal excretion\n\nApixaban (Eliquis): Factor Xa inhibitor; twice daily; 27% renal excretion (safest in moderate renal impairment); also used in ACS\n\nEdoxaban (Lixiana): Factor Xa inhibitor; once daily; 50% renal excretion\n\nAll DOACs: reversal with andexanet alfa (Xa inhibitors) or idarucizumab (dabigatran); no routine monitoring needed; fewer drug/food interactions than warfarin; contraindicated in pregnancy/severe renal failure."
    },
    {
        "id": "t5-r227",
        "question": "What is the significance of troponin I vs troponin T in acute MI diagnosis?",
        "answer": "Both cTnI (cardiac troponin I) and cTnT (cardiac troponin T) are regulatory proteins in the cardiac sarcomere. The cardiac isoforms are highly specific to myocardial tissue (unlike CK-MB and myoglobin, which are less specific).\nRise in MI:\n- Begins to rise: 3–6 hours after MI onset\n- Peaks: 24–48 hours\n- Remains elevated: up to 10–14 days (allows retrospective MI diagnosis)\nHigh-sensitivity troponin (hs-cTn): detects even very low levels; allows earlier MI diagnosis (rule-in/rule-out protocols at 0 and 1–3 hours); lower false-negative rate; but slightly lower specificity (minor myocardial injury from non-MI causes — PE, myocarditis, sepsis, renal failure, HF — can cause mild elevation).\ncTnI vs cTnT: similar clinical performance; different assays; cTnT is exclusively cardiac (renal failure can cause false elevation with older assays). Both accepted for MI diagnosis."
    },
    {
        "id": "t5-r228",
        "question": "What is the CHADS2 score and how does it differ from CHA2DS2-VASc?",
        "answer": "CHADS2 (older scoring system):\nC — Congestive HF (1)\nH — Hypertension (1)\nA — Age ≥75 (1)\nD — Diabetes mellitus (1)\nS2 — Stroke/TIA history (2)\nMax: 6 points. Score ≥2 = anticoagulation.\nLimitation: misses many patients at intermediate or low risk who should be anticoagulated.\n\nCHA2DS2-VASc (current, preferred):\nAdds three additional factors: vascular disease (1), age 65–74 (1), female sex (1). Max 9 points.\nAdvantage: better identifies truly low-risk patients (score 0 in males or 1 in females = no treatment needed) versus those who benefit from anticoagulation (score ≥2 in males or ≥3 in females). Reduces unnecessary anticoagulation AND better identifies those at genuine stroke risk.\nBoth validated for non-valvular AF only — patients with mechanical valves or rheumatic mitral stenosis with AF require warfarin regardless of score."
    },
    {
        "id": "t5-r229",
        "question": "What is reperfusion injury in the context of MI management?",
        "answer": "Reperfusion injury: paradoxical myocardial damage that occurs when blood flow is restored (by PCI, thrombolysis, or CABG) to previously ischaemic myocardium.\nMechanisms: sudden restoration of oxygen → burst of reactive oxygen species (ROS/free radicals) → oxidative stress; rapid normalisation of pH → calcium overload (Na+/H+ exchanger → Na+/Ca2+ exchanger overloads cell with Ca2+) → mitochondrial permeability transition pore (mPTP) opens → cell death despite restored blood flow.\nManifestations:\n1. Reperfusion arrhythmias (especially accelerated idioventricular rhythm — 'slow VT' at 60–100 bpm; benign; usually self-terminating)\n2. Myocardial stunning (mechanical dysfunction persisting hours–days after reperfusion; eventually recovers)\n3. Microvascular obstruction ('no-reflow phenomenon') — microemboli block capillaries despite patent epicardial artery\nManagement: minimising ischaemia time is the best strategy (primary PCI as fast as possible)."
    },
    {
        "id": "t5-r230",
        "question": "What drugs should be avoided in patients with known QT prolongation?",
        "answer": "Drugs that prolong the QT interval increase risk of torsade de pointes and VF.\nDrugs to avoid in QT prolongation:\nAntiarrhythmics: amiodarone, sotalol, quinidine (Class Ia), disopyramide\nAntibiotics: erythromycin, clarithromycin, azithromycin, moxifloxacin, metronidazole (mild)\nAntifungals: fluconazole, ketoconazole\nAntihistamines: terfenadine (withdrawn), astemizole (withdrawn)\nAntipsychotics: haloperidol, quetiapine, droperidol\nAntidepressants: tricyclics (TCAs — amitriptyline, imipramine)\nOncology: ondansetron (at high doses)\nDental relevance: erythromycin/clarithromycin are commonly prescribed for dental infections — check patient's medications and cardiac history before prescribing; use amoxicillin or penicillin V when possible in cardiac patients; check www.crediblemeds.org for QT drug interactions."
    },
    {
        "id": "t5-r231",
        "question": "What is the pathophysiology of orthostatic (postural) hypotension and which CVD medications cause it?",
        "answer": "Orthostatic hypotension: fall in systolic BP ≥20 mmHg or diastolic BP ≥10 mmHg within 3 minutes of standing from a lying position. Caused by failure of normal compensatory vasoconstriction on standing (normally: standing → reduced venous return → baroreceptor reflex → sympathetic activation → vasoconstriction + tachycardia → maintains BP).\nCVD drugs causing orthostatic hypotension:\n1. Alpha-blockers (doxazosin, prazosin): prevent reflex vasoconstriction → 'first-dose hypotension'\n2. ACE inhibitors/ARBs: vasodilation\n3. Nitrates: venodilation → reduced venous return\n4. Diuretics: volume depletion → insufficient preload\n5. Beta-blockers: prevent compensatory tachycardia\nDental relevance: raising the dental chair from supine to sitting position can trigger syncope. Allow patient to sit slowly before standing; keep patient seated for 2 minutes after supine treatment."
    },
    {
        "id": "t5-r232",
        "question": "What is the mechanism of action and use of ezetimibe?",
        "answer": "Ezetimibe: selectively inhibits the Niemann-Pick C1-like 1 (NPC1L1) protein in the small intestinal brush border → blocks intestinal absorption of dietary and biliary cholesterol → reduced cholesterol delivery to liver → compensatory upregulation of hepatic LDL receptors → increased LDL clearance from plasma.\nEffect: reduces LDL-C by approximately 15–20% as monotherapy; additive to statin (combination reduces LDL by 50–60%).\nIndications: familial hypercholesterolaemia (add-on to maximal statin), statin intolerance (as monotherapy or with PCSK9 inhibitor), inadequate LDL control on statin alone.\nAdvantages: very well tolerated; no myopathy risk (different mechanism from statins); once daily oral; minimal drug interactions.\nEvidence: IMPROVE-IT trial: ezetimibe + simvastatin vs simvastatin alone after ACS → modest but significant reduction in cardiovascular events (LDL lowering is beneficial regardless of mechanism)."
    },
    {
        "id": "t5-r233",
        "question": "What is the clinical significance of the troponin rise in non-MI conditions?",
        "answer": "Elevated troponin (type 2 MI or non-ischaemic troponin rise) indicates myocardial injury but NOT from plaque rupture/coronary occlusion:\nCauses of non-MI troponin elevation:\n- Pulmonary embolism (RV strain)\n- Myocarditis (viral, autoimmune — hs-troponin often very elevated)\n- Takotsubo cardiomyopathy\n- Cardiac contusion (trauma)\n- Sepsis/critical illness (supply-demand mismatch)\n- Acute heart failure (wall stress)\n- Hypertensive emergency\n- Renal failure (reduced clearance; also cardiac involvement in CKD)\n- Stroke/subarachnoid haemorrhage (catecholamine surge)\n- Defibrillation (electrical injury to myocardium)\nClinical principle: elevated troponin requires clinical interpretation — the pre-test probability and clinical context determine whether it represents an ACS. Rise + fall pattern (dynamic change) more specific for MI than a single static elevated level."
    },
    {
        "id": "t5-r234",
        "question": "What is the role of fibrinolysis in normal haemostasis?",
        "answer": "Fibrinolysis: the process of breaking down (dissolving) the fibrin clot once healing is complete — limits thrombus extension and restores vessel patency.\nMechanism: tissue plasminogen activator (tPA) and urokinase → activate plasminogen → plasmin → cleaves fibrin into fibrin degradation products (FDPs) including D-dimer.\nRegulation:\n- Plasminogen activator inhibitor-1 (PAI-1): inhibits tPA → limits fibrinolysis (raised in metabolic syndrome, obesity → prothrombotic state)\n- Alpha-2 antiplasmin: inhibits plasmin directly\nClinical relevance:\n- D-dimer: fibrin degradation product; elevated in active thrombosis (DVT, PE) and many other conditions (infection, cancer, surgery) — high sensitivity but LOW specificity\n- Thrombolytics (alteplase, streptokinase): pharmacologically activate plasminogen → dissolve pathological thrombi in MI, PE, stroke\n- Tranexamic acid: antifibrinolytic → prevents clot breakdown → used for haemostasis in surgical/dental bleeding"
    },
    {
        "id": "t5-r235",
        "question": "What is meant by 'white coat hypertension' and how should it be managed?",
        "answer": "White coat hypertension (WCH): BP is elevated in the clinic/hospital setting (≥140/90 mmHg) but is normal on ambulatory/home BP monitoring (ABPM: <135/85 mmHg daytime average). Occurs in approximately 15–30% of patients referred with clinic hypertension.\nMechanism: anxiety and sympathetic activation in medical settings → transient adrenaline release → raised HR and BP.\nManagement:\n1. Confirm diagnosis with ABPM or home BP monitoring (HBPM)\n2. Do not start antihypertensive medication based on elevated clinic readings alone\n3. Lifestyle advice: reduce salt, lose weight, increase exercise, reduce alcohol, reduce caffeine\n4. Annual follow-up: WCH confers slightly higher CVD risk than true normotension; approximately 25% develop sustained hypertension within 10 years\nDistinguish from 'masked hypertension' (normal in clinic, elevated on ABPM) — masked hypertension has the same cardiovascular risk as sustained hypertension."
    },
    {
        "id": "t5-r236",
        "question": "What are the dental considerations specific to a patient with Marfan syndrome?",
        "answer": "Marfan syndrome: autosomal dominant connective tissue disorder (fibrillin-1 gene, FBN1 mutation). Affects cardiovascular, ocular, and musculoskeletal systems.\nCardiovascular complications:\n1. Aortic root dilation → aortic regurgitation\n2. Aortic dissection (most serious — leading cause of death in Marfan's)\n3. Mitral valve prolapse + mitral regurgitation\n4. Arrhythmias\nDental considerations:\n1. High-arched palate and dental crowding (malocclusion) are typical features\n2. IE risk: valvular disease (MR/AR) → follow SDCEP/NICE guidance\n3. Anticoagulation: if mechanical valve replacement\n4. Drug interactions: patient may be on beta-blockers (to slow aortic root dilation) — note interactions\n5. Semi-reclined position for procedures: avoid sudden positional changes (risk of aortic rupture is unlikely from dental treatment, but stress minimisation is important)\n6. Consider anxiety and psychosocial impact: tall stature, joint hypermobility, lens dislocation"
    },
    {
        "id": "t5-r237",
        "question": "What is meant by 'myocardial hibernation' and 'myocardial stunning'?",
        "answer": "Both are states of viable but dysfunctional myocardium that can recover if perfusion is restored:\nMyocardial stunning: transient mechanical dysfunction AFTER a brief ischaemic episode (too short to cause infarction) or after reperfusion of an infarcted area, despite restoration of normal blood flow and normal coronary anatomy. Mechanism: oxidative stress from reperfusion injury. Duration: hours to days. WILL recover spontaneously without further intervention.\nMyocardial hibernation: chronic myocardial dysfunction from chronically reduced (but not zero) coronary blood flow — the myocardium is alive but has down-regulated its contractility to match its limited blood supply (protective adaptation). Duration: weeks to months. Will recover ONLY if blood flow is restored (by revascularisation — PCI or CABG). Does NOT recover spontaneously. Detected by: viability imaging (MRI with gadolinium, PET scan, dobutamine stress echo — if segment contracts on low-dose dobutamine, it is hibernating and will recover post-revascularisation)."
    },
    {
        "id": "t5-r238",
        "question": "What are the anti-anginal properties of calcium channel blockers and how do they differ between subclasses?",
        "answer": "All CCBs have anti-anginal properties via vasodilation of coronary and systemic arteries.\nDihydropyridines (amlodipine, nifedipine, felodipine): predominantly vasodilate peripheral and coronary arteries → reduce afterload and coronary vasospasm. Minimal effect on heart rate — can cause reflex tachycardia (nifedipine — less likely with amlodipine due to slow onset). Anti-anginal effect: reduce myocardial O2 demand (reduced afterload) + increase supply (coronary vasodilation). Best for: vasospastic angina, angina combined with hypertension.\nDiltiazem: intermediate — vasodilates + mild rate reduction. Useful when angina coexists with AF/flutter.\nVerapamil: predominantly rate-limiting + coronary vasodilation. Effective anti-anginal. Contraindicated with beta-blockers.\nKey rule for angina: when combining CCB with beta-blocker — use DIHYDROPYRIDINE (amlodipine) ONLY. Never verapamil or diltiazem with beta-blockers (additive bradycardia/heart block)."
    },
    {
        "id": "t5-r239",
        "question": "What are the main complications of uncontrolled atrial fibrillation and how does rate control help?",
        "answer": "Complications of uncontrolled AF (rapid ventricular rate >100 bpm at rest):\n1. Tachycardia-induced cardiomyopathy: sustained rapid ventricular rate (>110 bpm) for weeks to months → dilated cardiomyopathy → systolic heart failure. Potentially reversible with rate control.\n2. Ischaemia: rapid rate → reduced diastolic filling time → reduced coronary perfusion → subendocardial ischaemia; angina in patients with pre-existing CAD\n3. Thromboembolism: poor atrial contraction → left atrial appendage thrombus → stroke (not directly related to rate; risk depends on CHA2DS2-VASc score)\n4. Symptomatic: palpitations, breathlessness, fatigue, reduced exercise tolerance, dizziness\nRate control targets: resting HR <110 bpm (lenient) or <80 bpm (strict — for symptomatic patients). Achieved with: beta-blockers (first line), digoxin, rate-limiting CCBs (diltiazem/verapamil). Note: rate control alone without anticoagulation still leaves stroke risk."
    },
    {
        "id": "t5-r240",
        "question": "What is the mechanism of action of warfarin and how does vitamin K reverse its effect?",
        "answer": "Warfarin mechanism: inhibits vitamin K epoxide reductase → prevents recycling of vitamin K epoxide back to active vitamin K hydroquinone → depletes active vitamin K → cannot gamma-carboxylate glutamate residues of clotting factors II, VII, IX, X (and protein C, S) → non-functional clotting factors produced → anticoagulation. Takes 2–5 days for full effect (factor half-lives must deplete: VII shortest half-life 4–6h; II longest 60–72h).\nVitamin K reversal mechanism: exogenous vitamin K (phytomenadione) bypasses the blocked VKORC enzyme → provides active vitamin K directly → re-enables gamma-carboxylation → new functional clotting factors produced by liver → INR falls over 6–24 hours (depending on dose and route).\nDose: 1–2 mg oral (partial reversal, for over-anticoagulation); 5–10 mg oral (complete reversal, for surgery or serious over-anticoagulation). Higher doses: avoid if patient needs to re-anticoagulate soon (makes warfarin resistance for 1–2 weeks)."
    }
]

data['recallIt'].extend(new_recall)

with open('data/theme-5.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Total recallIt: {len(data['recallIt'])}")
