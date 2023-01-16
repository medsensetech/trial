import streamlit as st
import pandas as pd

if __name__ == "__main__":
    # setting header, description and citation
    
    
    st.sidebar.markdown('''
    # EH MVP v2.0
    - [Evidence Explorer](#section-1)
    - [Concept Builder](#section-2)
    ''', unsafe_allow_html=True)

    st.header('''
    Evidence Explorer
    ''')
    st.write('''
    Enter your search criteria in the fields below then click on Results to explore the published data available that
most closely matches your selections.
The results would display the services and channels used by similar programs along with the expected adoption
rates and outcomes if you were to design your program similarly.
    ''')
    
    uploaded_file = st.file_uploader("Upload References")
    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        references = pd.read_csv(uploaded_file)
    with st.form('Form1'):
        th_area = st.selectbox('Therapy Area', ['Autoimmune/Immunology','Cardiovascular','Endocrine','Gastrointestinal','Infectious disease','Psychiatry','Nephrology','Neurology','Oncology','Pain','Rare Disease','Respiratory','Rheumatology','Vaccines','Ophthalmology','Haematology','Hepatology','Dermatology','Paediatrics','Obstetrics/Gynaecology','Transplant','Other chronic conditions','Other specify'], key=1)         
        cond = st.selectbox('Condition', ['Acromegaly','Ankylosing spondylitis','Asthma','Crohns disease','Diabetes','Erythema nodosum leprosum','Growth hormone deficiency','Hidradenitis suppurativa','High blood pressure','Idiopathic pulmonary fibrosis','Knee osteoarthritis','Major depressive disorder','Multiple myeloma','Multiple sclerosis','Myelodysplastic syndrome','Neovascular age-related macular degeneration','Neuroendocrine tumours','Obesity','Opioid dependence','Osteoporosis','Ostomy surgery','Prostate cancer','Psoriasis','Psoriatic arthritis','Rheumatoid arthritis','Schizophrenia','Ulcerative colitis','Other chronic conditions','Other specify'], key=2)
        drug = st.selectbox('Drug Name', ['Adalimumab','Aflibercept','Aripiprazole','Bisphosphonate ibandronate','Buprenorphine medicationassisted treatment (B-MAT)','Certolizumab','Denosumab','Dimethyl fumarate ','Fingolimod','Glatiramer acetate','Hypoglycaemic agent (OHA)','Infliximab','Insulin','Interferon beta-1a','Interferon beta-1b','Lenalidomide','Liraglutide','Mesalamine','Mitoxantrone','Natalizumab','Nintedanib','Octreotide','Pirfenidone','Pramlintide','Risedronate','Somatropin','Teriparatide','Telmisartan','Teriflunomide','Thalidomide','Vortioxetine','Other specify'], key=4)
        p_stakeholders = st.selectbox('Program Stakeholders', ['GP','Specialist','Patient','Patient-Carer','Nurse','Pharmacist','AHPs','Other clinical staff, specify','Program-management','Partner organisations','Advocacy group','Other specify'], key=5)
        p_strategy = st.selectbox('Program Strategy', ['Supporting quality use of medicines','Providing patient support at-par with industry standard','Providing patient support that exceeds industry standard','Create a new program to be consistent with current enterprise programs','Address an unmet patient need or barrier','Expansion of existing program','Other specify'], key=6)
        roa = st.selectbox('Route of Administration', ['ID','IV','IVI','NA','Oral','Inhale','Topical','Other specify'], key=7)        
        #references = pd.read_csv('dhairyavayada/trial/dataframe3.csv')
        submit_button = st.form_submit_button('View Results')
        references['Sum'] = pd.Series(dtype='int')
        # if ES_15M_Summary.loc[index, 'Rolling_OLS_Coefficient'] > .08:
        for i, row in references.iterrows():
            sum_roa = 0
            sum_drug = 0
            sum_cond = 0
            sum_th = 0
            if str(references.loc[i, 'Route of Administration']) in str(roa):
                sum_roa = 8
            if str(references.loc[i, 'Molecule']) in str(drug):
                sum_drug = 4
            if str(references.loc[i, 'Condition']) in str(cond):
                sum_cond = 2
            if str(references.loc[i, 'Therapy Area']) in th_area:
                sum_th = 1
            references.loc[i, 'Sum'] = sum_roa + sum_drug + sum_cond + sum_th


        sorted_df = references.sort_values(by=['Sum', 'Participants', 'Adoption', 'Program benefit vs non-program'], ascending=False)


        firsts = sorted_df.groupby('Sr', as_index=False).first()


        firsts = firsts.sort_values(by=['Sum', 'Participants'], ascending=False)



        results = firsts.head(10)

        output = results.drop('Sr', axis=1)
        output = output.drop('Sum', axis=1)

        no_participants = results['Participants'].sum()
        no_programs = results['Condition'].count()

        adoption_rate = results['Adoption'].max()

        program_measure = results['Program Measure']


        prem = results[results['Program Measure'].str.contains('PREM')]
        non_prem = results[~results['Program Measure'].str.contains('PREM')]
        patient_x = prem['Program benefit vs non-program'].max()
        outcome = non_prem['Program benefit vs non-program'].max()

    def remove_dup(x):
        return list(dict.fromkeys(x))
    if submit_button:
        st.write("Based on data from", no_participants, "across ", no_programs, "of programs globally, here are the programs that most closely match your selection \ncriteria.")
        st.write("Best case (from the top 10 programs that most closely match your selection criteria)")
        col1, col2, col3 = st.columns(3)
        col1.metric("Adoption Rate (%)", adoption_rate)
        col2.metric("Patient Experience (%)", patient_x)
        col3.metric("Outcome (%)", outcome)

        st.write("Matches are based on route of administration, condition, therapy area and molecule, in this order.")
        st.write(output)

        
    st.header("Concept Builder")
    
    st.write("Based on selection(s) of program strategy, for your program objective(s) might be recommended below. For strategy around either un-met need or barrier or existing-programs please select any relevant objectives. Also, complete the additional felds below, then press next, to review the potential opportunity for your program concept.")
        

    tag = []
    #print(program_strategy)

    for i in p_strategy:
        if i in ("Supporting quality use of medicines"):
            tag.append("Med")
        elif i in ("Providing patient support at-par with industry standard"):
            tag.append("Low")
        elif i in ("Providing patient support that exceeds industry standard"):
            tag.append("High")
        elif i in ("Create a new program to be consistent with current enterprise programs") or i in ("Expansion of existing program"):
            tag.append("Existing program")
        elif i in ("Address an unmet patient need or barrier"):
            tag.append("Unmet Need")
        else:
            tag.append("Other")
    #print(tag)

    #Step 2: For each program objective, select unique Matched Services (Matrix)

    program_objective = []

    for i in tag:
        if i in "High":
            program_objective.append("Support adherence and persistence")
            program_objective.append("Support complex patient/treatment journey")
            program_objective.append("Best end-to-end experience")
        elif i in "Med":
            program_objective.append("Support end-to-end experience")
            program_objective.append("Support including disease and medicine education")
            program_objective.append("Cross-functional including AHP support")
        elif i in "Low":
            program_objective.append("Disease and medicine education")
        elif i in "Unmet Need":
            program_objective.append("Emotional/psycho-social support")
            program_objective.append("Medication access/financial support")
            program_objective.append("Support carer")
            program_objective.append("HCP support")
        else:
            program_objective.append("Other")

    #print(program_objective)
    program_objective = remove_dup(program_objective)

    #progobj = pd.DataFrame(program_objective)
    #progobj.columns = ['Program Objective']

    matched_service = []

    for i in program_objective:
        if i in 'Support adherence and persistence':
            matched_service.append('Patient Education')
            matched_service.append("Sideeffects/Comorbitity Support")
            matched_service.append("Medicine Usage Support")
            matched_service.append("Medicine Supplies/Logistics")
            matched_service.append("Motivation-Confidence")
        elif i in 'Support complex patient/treatment journey':
            matched_service.append('Patient Education')
            matched_service.append("Sideeffects/Comorbitity Support")
            matched_service.append("Medicine Usage Support")
            matched_service.append("Medicine Supplies/Logistics")
            matched_service.append("Effective HCP Appointments")
            matched_service.append("Motivation-Confidence")
        elif i in 'Best end-to-end experience':
            matched_service.append('Patient Education')
            matched_service.append("Sideeffects/Comorbitity Support")
            matched_service.append("Medicine Usage Support")
            matched_service.append("Medicine Supplies/Logistics")
            matched_service.append("Effective HCP Appointments")
            matched_service.append("Motivation-Confidence")
            matched_service.append("Psychosocial-Emotional")
        elif i in 'Support end-to-end experience':
            matched_service.append('Patient Education')
            matched_service.append("Sideeffects/Comorbitity Support")
            matched_service.append("Medicine Usage Support")
            matched_service.append("Effective HCP Appointments")
            matched_service.append("Motivation-Confidence")
        elif i in 'Support including disease and medicine education':
            matched_service.append('Patient Education')
            matched_service.append("Sideeffects/Comorbitity Support")
            matched_service.append("Medicine Usage Support")
        elif i in 'Disease and medicine education':
            matched_service.append('Patient Education')
        elif i in 'Emotional/psycho-social support':
            matched_service.append("Motivation-Confidence")
            matched_service.append("Psychosocial-Emotional")
        elif i in 'Medication access/financial support':
            matched_service.append("Financial")
        elif i in 'Support carer':
            matched_service.append('Patient Education')
            matched_service.append("Medicine Usage Support")
            matched_service.append("Carer Enablement")
        elif i in 'Cross-functional including AHP support':
            matched_service.append("Sideeffects/Comorbitity Support")
            matched_service.append("Effective HCP Appointments")
        elif i in 'HCP support':
            matched_service.append("HCP-Needs")

    matched_service = remove_dup(matched_service)


    #print(matched_service)




    #Step 3: For each matched service, display patient needs 
    pt_needs = []

    for i in matched_service:
        if i in "Patient Education":
            pt_needs.append("Disease education")
            pt_needs.append("Treatment education")
            pt_needs.append("Side effects education")
        elif i in "Carer Enablement":
            pt_needs.append("Carer enablement")
        elif i in "Effective HCP Appointments":
            pt_needs.append("Effective HCP appointments")
            pt_needs.append("Access to HCPs")
            pt_needs.append("Logistics (e.g. transport)")
        elif i in "Financial":
            pt_needs.append("Financial")
        elif i in "Medicine Supplies/Logistics":
            pt_needs.append("Medicine logistics")
            pt_needs.append("ePharmacy")
            pt_needs.append("Convenience")
        elif i in "Medicine Usage Support":
            pt_needs.append("Reminders (medication, appointments, tests)")
            pt_needs.append("Medicine routine")
            pt_needs.append("Monitoring support")
            pt_needs.append("Access to diagnostics/tests/exams")
            pt_needs.append("Supports treatment initiation")
            pt_needs.append("Self-administration")
        elif i in "Motivation-Confidence":
            pt_needs.append("Motivation")
            pt_needs.append("Supports treatment maintenance / persistence")
        elif i in "Psychosocial-Emotional":
            pt_needs.append("Psychosocial")
            pt_needs.append("Peer to peer networking/community")
        elif i in "Sideeffects/Comorbitity Support":
            pt_needs.append("Co-morbidities/co-meds/medication burden")
    pt_needs = remove_dup(pt_needs)
    #print(pt_needs)
    #ptneeds = pd.DataFrame(pt_needs)
    #ptneeds.columns = ['Patient Needs']

    #Step 4: For each matched service, display HCP needs
    #print(matched_service)
    hcp_needs = []
    for i in matched_service:
        if i in "HCP-Needs":
            hcp_needs.append("Administrative burden")
            hcp_needs.append("HCP training")
            hcp_needs.append("Patient support feedback loop")
        elif i in "Medicine Usage Support":
            hcp_needs.append("Complex therapy management")
        elif i in "Patient Education":
            hcp_needs.append("Time poor to deliver patient education/support")
        elif i in "Effective HCP Appointments":
            hcp_needs.append("Multiple stakeholders in patient journey")
        elif i in "Sideeffects/Comorbitity Support":
            hcp_needs.append("Reassurance of care/support outside of their care")
        elif i in "Psychosocial-Emotional":
            hcp_needs.append("Patient support feedback loop")
        elif i in "HCP-Needs":
            hcp_needs.append("HCP training")
        else:
            hcp_needs.append("Others")


    hcp_needs = remove_dup(hcp_needs)
    #hcp = pd.DataFrame(hcp_needs)
    #print(hcp_needs)
    #hcp.columns = ['HCP Needs']
    #Step 5: Unique values of sub-services and channels 

    matched_serv1 = remove_dup(matched_service)
    #matched_serv = pd.DataFrame(matched_serv1)
    #matched_serv.columns = ['Services']
    #print(matched_serv)

    services = remove_dup(results['Services'])
    serv = pd.DataFrame(services)
    serv.columns = ['Services']

    temp = results[results.Services.isin(matched_serv1)]
    print(temp)

    sub_services = temp['Sub Services']
    #print(sub_services)

    subserv = pd.DataFrame(sub_services)
    #subserv.columns = ['Sub Services']
    #subserv = subserv.drop_duplicates()
    #print(sub_services)

    channels = temp['Channel']
    #print(channels)
    #chnls = pd.DataFrame(channels)
    #chnls.columns = ['Channels']
    #chnls = chnls.drop_duplicates()
    
    
    with st.form('Form2'):
        probj = st.multiselect(
        'Program Objectives',
        ['Support adherence and persistence','Support complex patient/treatment journey','Best end-to-end experience','Support end-to-end experience','Support including disease and medicine education','Cross-functional including AHP support','Disease and medicine education','Emotional/psycho-social support','Medication access/financial support','Support carer','HCP support','Other specify'],
        program_objective)
        
        prsetting = st.selectbox(
        'Program Setting',
        ('New product launch (PBS)','New product launch (private)','Existing product in market','New indication','Other specify'))
        
         adminfreq = st.selectbox(
        'Administration Frequency',
        ('Daily','Weekly','Fortnightly','Monthly','Quarterly','Twice-yearly','Once-yearly','PRN (as required)','Other specify'))
            
        ptneeds = st.multiselect(
        'Patient Needs',
        ['Disease education','Treatment education','Side effects education','Carer enablement','Effective HCP appointments','Access to HCPs','Logistics (e.g. transport)','Financial','Medicine logistics','ePharmacy','Convenience','Reminders (medication, appointments, tests)','Medicine routine','Monitoring support','Access to diagnostics/tests/exams','Supports treatment initiation','Self-administration','Motivation','Supports treatment maintenance / persistence','Psychosocial','Peer to peer networking/community','Co-morbidities/co-meds/medication burden','Other specify'],
        pt_needs)
        
        hcp = st.multiselect(
        'Program Objectives',
        ['Administrative burden','Complex therapy management','Time poor to deliver patient education/support','Multiple stakeholders in patient journey','Reassurance of care/support outside of their care','Patient support feedback loop','HCP training','Other specify'],
        hcp_needs)       
        
        matched_serv = st.multiselect(
        'Services',
        ['Patient Education','Motivation-Confidence','Medicine Usage Support','Medicine Supplies/Logistics','Financial','Psychosocial-Emotional','Side effects/Comorbitity support','HCP-Needs','Effective HCP Appointments','Carer Enablement','Other specify'],
        matched_serv1)
        
        subserv = st.multiselect(
        'Sub-services',
        ['Nurse/AHP assistance','Welcome Pack','Website','Help-line (non-clinical)','App','Partner organisations','Email/SMS/Mail','AHP services','Tools-Kits','Reminders','Telemonitoring','Adherence service','Coaching/Counseling','Individual care plan','Goal Setting','Drug/inj training','Dose support (inc. induction, FDO, titration)','Drug administraion/infusion (home)','Drug administraion/infusion (clinic)','Home Delivery/Order','Disposal','Pharmacy Supply','Patient care coordination','Logistics-travel','Appointment preparation','Patient communities-support','Psychological intervention','e-diary/patient story','Patient-segmentation','Co-pay','Free-supply','Insurance support','PSP-patient feedback','Medicine Usage Support','HCP/AHP training','Effective HCP Appointments','Approval/administrative support','Vouchers','Other specify'],
        sub_services)
               
        chnls = st.multiselect(
        'Channels',
        ['Inperson','Telephone (clinical)','Welcome Pack','Website','Email/SMS/Mail','Telephone (non-clinical)','App','Partner organisations','Third-party tool/software','Print','Digital (other)','Other specify'],
        channels)
        
        submit_button2 = st.form_submit_button('View Results')




        
     

