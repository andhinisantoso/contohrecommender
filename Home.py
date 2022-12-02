# Importing modules
import pickle # For loading model
import streamlit as st # For web app
import pandas as pd
import difflib

#page config
st.set_page_config(
    page_title="Rekomendasi Wisata Bali by BALINEST",
    page_icon="https://code.iconify.design/2/2.2.1/iconify.min.js",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# Loading data frame
rec_wisata = pickle.load(open('rec_wisata.pkl', 'rb'))
wisata_data = pd.DataFrame(rec_wisata)

# Loading similarity file
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Main heading
st.markdown("<h1 style='text-align: center; color: black;'>REKOMENDASI WISATA BALI</h1>", unsafe_allow_html=True)

input_category = st.text_input('Input kategori wisata yang ingin dikunjungi :')

def recommend(data):
    place_id=data[data.category==place]["ids"].values[0]
    scores=list(enumerate(similarity[place_id]))
    sorted_scores=sorted(scores,key=lambda x:x[1],reverse=True)
    sorted_scores=sorted_scores[0:5]
    place=[data[place[0]==data["ids"]]["place_name"].values[0] for place in sorted_scores]
    
def recommend_ten(place_list):
    first_five=[]
    count=0
    for place in place_list:
        if count > 4:
            break
        count+=1
        first_five.append(place)

    index = place[0]
    image = []
    place_name = []
    category = []
    description = []
    for i in sorted_scores:
        try:
            image.append(wisata_data.iloc[i[0]].image)
            place_name.append(wisata_data.iloc[i[0]].place_name)
            category.append(wisata_data.iloc[i[0]].category)
            description.append(wisata_data.iloc[i[0]].description)
        except:
            pass
    return image, place_name, category, description

if st.button('Search'):
    image,place_name,category,description = recommend(input_category)

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(image[0], width=200, caption=place_name[0])
        with col2:
            st.subheader(place_name[0])
            with st.expander("Kategori"):
                st.write(category[0])
            with st.expander("Deskripsi"):
                st.write(description[0])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(image[1], width=200, caption=place_name[1])
        with col2:
            st.subheader(place_name[1])
            with st.expander("Kategori"):
                st.write(category[1])
            with st.expander("Deskripsi"):
                st.write(description[1])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(image[2], width=200, caption=place_name[2])
        with col2:
            st.subheader(place_name[2])
            with st.expander("Kategori"):
                st.write(category[2])
            with st.expander("Deskripsi"):
                st.write(description[2])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(image[3], width=200, caption=place_name[3])
        with col2:
            st.subheader(place_name[3])
            with st.expander("Kategori"):
                st.write(category[3])
            with st.expander("Deskripsi"):
                st.write(description[3])

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.image(image[4], width=200, caption=place_name[4])
        with col2:
            st.subheader(place_name[4])
            with st.expander("Kategori"):
                st.write(category[4])
            with st.expander("Deskripsi"):
                st.write(description[4])

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
   