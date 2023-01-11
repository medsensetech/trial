import streamlit as st
import pandas as pd

if __name__ == "__main__":
    # setting header, description and citation
    st.set_page_config(page_title="Molecule icons")
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
        st.write(references)

   
    with st.form('Form1'):
        th_area = st.selectbox('Therapy Area', ['Autoimmune/Immunology','Cardiovascular','Endocrine','Gastrointestinal','Infectious disease','Psychiatry','Nephrology','Neurology','Oncology','Pain','Rare Disease','Respiratory','Rheumatology','Vaccines','Ophthalmology','Haematology','Hepatology','Dermatology','Paediatrics','Obstetrics/Gynaecology','Transplant','Other chronic conditions','Other specify'], key=1)         
        cond = st.selectbox('Condition', ['Acromegaly','Ankylosing spondylitis','Asthma','Crohns disease','Diabetes','Erythema nodosum leprosum','Growth hormone deficiency','Hidradenitis suppurativa','High blood pressure','Idiopathic pulmonary fibrosis','Knee osteoarthritis','Major depressive disorder','Multiple myeloma','Multiple sclerosis','Myelodysplastic syndrome','Neovascular age-related macular degeneration','Neuroendocrine tumours','Obesity','Opioid dependence','Osteoporosis','Ostomy surgery','Prostate cancer','Psoriasis','Psoriatic arthritis','Rheumatoid arthritis','Schizophrenia','Ulcerative colitis','Other chronic conditions','Other specify'], key=2)
        drug = st.selectbox('Drug Name', ['Adalimumab','Aflibercept','Aripiprazole','Bisphosphonate ibandronate','Buprenorphine medicationassisted treatment (B-MAT)','Certolizumab','Denosumab','Dimethyl fumarate ','Fingolimod','Glatiramer acetate','Hypoglycaemic agent (OHA)','Infliximab','Insulin','Interferon beta-1a','Interferon beta-1b','Lenalidomide','Liraglutide','Mesalamine','Mitoxantrone','Natalizumab','Nintedanib','Octreotide','Pirfenidone','Pramlintide','Risedronate','Somatropin','Teriparatide','Telmisartan','Teriflunomide','Thalidomide','Vortioxetine','Other specify'], key=4)
        p_stakeholders = st.selectbox('Program Stakeholders', ['GP','Specialist','Patient','Patient-Carer','Nurse','Pharmacist','AHPs','Other clinical staff, specify','Program-management','Partner organisations','Advocacy group','Other specify'], key=5)
        p_strategy = st.selectbox('Program Strategy', ['Supporting quality use of medicines','Providing patient support at-par with industry standard','Providing patient support that exceeds industry standard','Create a new program to be consistent with current enterprise programs','Address an unmet patient need or barrier','Expansion of existing program','Other specify'], key=6)
        roa = st.selectbox('Route of Administration', ['ID','IV','IVI','NA','Oral','Inhale','Topical','Other specify'], key=7)        
        #references = pd.read_csv('dhairyavayada/trial/dataframe3.csv')
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



        result = firsts.head(10)

        output = result.drop('Sr', axis=1)
        output = output.drop('Sum', axis=1)

        no_participants = results['Participants'].sum()
        no_programs = results['Condition'].count()

        adoption_rate = results['Adoption'].max()/100

        program_measure = results['Program Measure']


        prem = results[results['Program Measure'].str.contains('PREM')]
        non_prem = results[~results['Program Measure'].str.contains('PREM')]
        patient_x = prem['Program benefit vs non-program'].max()/100
        outcome = non_prem['Program benefit vs non-program'].max()/100

    def remove_dup(x):
        return list(dict.fromkeys(x))
    submit_button = st.form_submit_button('View Results')

    st.write("Based on data from", no_participants, "across ", no_programs, "of programs globally, here are the programs that most closely match your selection \ncriteria.")
    st.write("Matches are based on route of administration, condition, therapy area and molecule, in this order.")

