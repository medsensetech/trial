import streamlit as st

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
   
    with st.form('Form1'):
        st.selectbox('Therapy Area', ['Autoimmune/Immunology','Cardiovascular','Endocrine','Gastrointestinal','Infectious disease','Psychiatry','Nephrology','Neurology','Oncology','Pain','Rare Disease','Respiratory','Rheumatology','Vaccines','Ophthalmology','Haematology','Hepatology','Dermatology','Paediatrics','Obstetrics/Gynaecology','Transplant','Other chronic conditions','Other specify'], key=1)         
        st.selectbox('Condition', ['Acromegaly','Ankylosing spondylitis','Asthma','Crohns disease','Diabetes','Erythema nodosum leprosum','Growth hormone deficiency','Hidradenitis suppurativa','High blood pressure','Idiopathic pulmonary fibrosis','Knee osteoarthritis','Major depressive disorder','Multiple myeloma','Multiple sclerosis','Myelodysplastic syndrome','Neovascular age-related macular degeneration','Neuroendocrine tumours','Obesity','Opioid dependence','Osteoporosis','Ostomy surgery','Prostate cancer','Psoriasis','Psoriatic arthritis','Rheumatoid arthritis','Schizophrenia','Ulcerative colitis','Other chronic conditions','Other specify'], key=2)
        st.selectbox('Drug Name', ['Adalimumab','Aflibercept','Aripiprazole','Bisphosphonate ibandronate','Buprenorphine medicationassisted treatment (B-MAT)','Certolizumab','Denosumab','Dimethyl fumarate ','Fingolimod','Glatiramer acetate','Hypoglycaemic agent (OHA)','Infliximab','Insulin','Interferon beta-1a','Interferon beta-1b','Lenalidomide','Liraglutide','Mesalamine','Mitoxantrone','Natalizumab','Nintedanib','Octreotide','Pirfenidone','Pramlintide','Risedronate','Somatropin','Teriparatide','Telmisartan','Teriflunomide','Thalidomide','Vortioxetine','Other specify'], key=4)
        st.selectbox('Program Stakeholders', ['GP','Specialist','Patient','Patient-Carer','Nurse','Pharmacist','AHPs','Other clinical staff, specify','Program-management','Partner organisations','Advocacy group','Other specify'], key=5)
        st.selectbox('Program Strategy', ['Supporting quality use of medicines','Providing patient support at-par with industry standard','Providing patient support that exceeds industry standard','Create a new program to be consistent with current enterprise programs','Address an unmet patient need or barrier','Expansion of existing program','Other specify'], key=6)
        st.selectbox('Route of Administration', ['ID','IV','IVI','NA','Oral','Inhale','Topical','Other specify'], key=7)        
        submit_button = st.form_submit_button('View Results')

