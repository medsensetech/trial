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
        st.selectbox('Therapy Area', ['Vanilla', 'Chocolate'], key=1)
        st.selectbox('Condition', ['Vanilla', 'Chocolate'], key=1)
        st.selectbox('Therapy Area', ['Vanilla', 'Chocolate'], key=1)
        st.selectbox('Drug Name', ['Vanilla', 'Chocolate'], key=1)
        st.selectbox('Program Stakeholders', ['Vanilla', 'Chocolate'], key=1)
        st.selectbox('Program Strategy', ['Vanilla', 'Chocolate'], key=1)
        st.selectbox('Route of Administration', ['Vanilla', 'Chocolate'], key=1)        
        submit_button = st.form_submit_button('Submit 1')

form = st.form(key='my_form')
form.text_input(label='Enter some text')
submit_button = form.form_submit_button(label='Submit')
