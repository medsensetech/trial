
if __name__ == "__main__":

    # setting header, description and citation
    st.set_page_config(page_title="Molecule icons")
    st.header('''
    Molecule Icon Generator!
    ''')
    st.write('''
    Generate icons of molecules from SMILES, Name, Cas-number, Inchi, InChIKey, load your molecule file or convert a
    list of SMILES.
    ''')
    st.markdown('''
For more options and information, check out the 
[GitHub repository](https://github.com/lmonari5/molecule-icon-generator.git).\\
[DOI](https://doi.org/10.5281/zenodo.7388429): 10.5281/ZENODO.7388429.
       ''')

    # select the input type
    input_type = st.selectbox("Create your icon by",
                              ['name', 'smiles', 'load file', 'cas_number', 'stdinchi', 'stdinchikey', 'smiles list'],
                              on_change=updatemol,
                              help="""Choose the input info of your molecule. If the app is slow, use SMILES input.""" + smiles_help)
    # default input for each input_type except 'load file'
    def_dict = {'name': 'paracetamol',
                'smiles': "CC(=O)Nc1ccc(cc1)O",
                'cas_number': '103-90-2',
                'stdinchi': 'InChI=1S/C8H9NO2/c1-6(10)9-7-2-4-8(11)5-3-7/h2-5,11H,1H3,(H,9,10)',
                'stdinchikey': 'RZVAJINKPMORJF-UHFFFAOYSA-N'}

