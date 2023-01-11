
if __name__ == "__main__":
    # initialize session state
    if 'color_dict' not in st.session_state:
        st.session_state['color_dict'] = mig.color_map.copy()
    if 'resize_dict' not in st.session_state:
        st.session_state['resize_dict'] = mig.atom_resize.copy()
    if 'reset_color' not in st.session_state:
        st.session_state['reset_color'] = False
    if 'reset_size' not in st.session_state:
        st.session_state['reset_size'] = False
    if 'last_atom_size_but' not in st.session_state:
        st.session_state['last_atom_size_but'] = None
    if 'last_atom_color_but' not in st.session_state:
        st.session_state['last_atom_color_but'] = None
    if 'upload_setting' not in st.session_state:
        st.session_state['upload_setting'] = False
    if 'emoji_dict' not in st.session_state:
        st.session_state['emoji_dict'] = dict()
    if 'update_mol' not in st.session_state:
        st.session_state['update_mol'] = True
    if 'molecules_but' not in st.session_state:
        st.session_state['molecules_but'] = None
    if 'use_emoji' not in st.session_state:
        st.session_state['use_emoji'] = False

    # loading the color, resize and emoji dictionary
    if 'color_dict' in st.session_state:
        new_color = st.session_state['color_dict']
    else:
        st.exception(loading_err)
        print([i for i in st.session_state])
        st.session_state['color_dict'] = mig.color_map.copy()
        new_color = st.session_state['color_dict']
    if 'resize_dict' in st.session_state:
        resize = st.session_state['resize_dict']
    else:
        st.exception(loading_err)
        print([i for i in st.session_state])
        st.session_state['resize_dict'] = mig.atom_resize.copy()
        resize = st.session_state['resize_dict']
    if 'emoji_dict' in st.session_state:
        emoji = st.session_state['emoji_dict']
    else:
        st.exception(loading_err)
        print([i for i in st.session_state])
        st.session_state['emoji_dict'] = dict()
        emoji = st.session_state['emoji_dict']

    # check if the color/resize dictionary have been reset
    if 'atom_color_select' in st.session_state and 'color_picker_but' in st.session_state and st.session_state[
        'reset_color']:
        st.session_state.color_picker_but = new_color[st.session_state.atom_color_select]
        st.session_state['last_atom_color_but'] = None
        st.session_state['reset_color'] = False
    last_atom_color = st.session_state['last_atom_color_but']
    if 'atom_size_select' in st.session_state and 'sizes_percentage_but' in st.session_state and st.session_state[
        'reset_size']:
        st.session_state['last_atom_size_but'] = None
        st.session_state['reset_size'] = False
    last_atom_size = st.session_state['last_atom_size_but']

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

