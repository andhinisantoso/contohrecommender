import  streamlit as st
import pickle
import pandas as pd

#page config
st.set_page_config(
    page_title="Rekomendasi Wisata Bali by BALINEST",
    page_icon="https://code.iconify.design/2/2.2.1/iconify.min.js",
    layout="centered",
    initial_sidebar_state="collapsed"
)

rec_wisata = pickle.load(open('rec_wisata.pkl','rb'))
wisata = pd.DataFrame(rec_wisata)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Rekomendasi Wisata Bali by BALINEST')

def recommend(data):
    wisata_index = wisata[wisata['category'] == data].index[0]
    distances = similarity[wisata_index]
    wisata_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_wisata = []
    recommended_wisata_image = []
    recommended_wisata_category = []
    recommended_wisata_description = []

    for i in wisata_list:
        recommended_wisata.append(wisata.iloc[i[0]].place_name)
        recommended_wisata_image.append(wisata.iloc[i[0]].image)
        recommended_wisata_category.append(wisata.iloc[i[0]].category)
        recommended_wisata_description.append(wisata.iloc[i[0]].description)
        
    return recommended_wisata, recommended_wisata_image, recommended_wisata_category, recommended_wisata_description

selected_wisata_category = st.selectbox(
    "Pilih kategori wisata yang ingin dikunjungi :",
    ('alam', 'agrowisata', 'belanja', 'pantai', 'religius')
)

if st.button('Tampilkan Rekomendasi'):
    recommended_wisata, recommended_wisata_image, recommended_wisata_category, recommended_wisata_description = recommend(selected_wisata_category)

    #display with the columns
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_wisata_image[0], width=200, caption=recommended_wisata[0])
        with col2:
            st.subheader(recommended_wisata[0])
            with st.expander("Kategori"):
                st.write(recommended_wisata_category[0])
            with st.expander("Deskripsi"):
                st.write(recommended_wisata_description[0])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_wisata_image[1], width=200, caption=recommended_wisata[1])
        with col2:
            st.subheader(recommended_wisata[1])
            with st.expander("Kategori"):
                st.write(recommended_wisata_category[1])
            with st.expander("Deskripsi"):
                st.write(recommended_wisata_description[1])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_wisata_image[2], width=200, caption=recommended_wisata[2])
        with col2:
            st.subheader(recommended_wisata[2])
            with st.expander("Kategori"):
                st.write(recommended_wisata_category[2])
            with st.expander("Deskripsi"):
                st.write(recommended_wisata_description[2])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_wisata_image[3], width=200, caption=recommended_wisata[3])
        with col2:
            st.subheader(recommended_wisata[3])
            with st.expander("Kategori"):
                st.write(recommended_wisata_category[3])
            with st.expander("Deskripsi"):
                st.write(recommended_wisata_description[3])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(recommended_wisata_image[4], width=200, caption=recommended_wisata[4])
        with col2:
            st.subheader(recommended_wisata[4])
            with st.expander("Kategori"):
                st.write(recommended_wisata_category[4])
            with st.expander("Deskripsi"):
                st.write(recommended_wisata_description[4])