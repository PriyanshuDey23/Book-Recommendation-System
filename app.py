import pickle
import  streamlit as st
import numpy as np


# Launch my webpage in my local host

st.header("Book Recommender System")

# Load the artifacts

model=pickle.load(open('artifacts\\model\\model.pkl','rb'))
book_name=pickle.load(open('artifacts\\book_name\\book_name.pkl','rb'))
book_pivot=pickle.load(open('artifacts\\book_pivot\\book_pivot.pkl','rb'))
final_rating=pickle.load(open('artifacts\\final_rating\\final_rating.pkl','rb'))


# Fetch the poster
def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []


    # Books name through indexing in pivot
    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    # Get the title
    for name in book_name[0]: 
        ids = np.where(final_rating['title'] == name)[0][0] # Get the index
        ids_index.append(ids) 

    # image url
    for idx in ids_index:
        url = final_rating.iloc[idx]['img_url']
        poster_url.append(url)

    return poster_url




# Function for recommending the books, return recommend book and poster url
def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6 )

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            books_list.append(j)
    return books_list , poster_url   




# Create selecting box  in which all the book name will be present
selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    book_name
)



# recommended books
if st.button('Show Recommendation'):
    recommended_books,poster_url = recommend_book(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5) # 5 books columns
    # Not taking 0 index because i donot want to recommend the same book
    with col1:
        st.text(recommended_books[1]) # Headline
        st.image(poster_url[1]) # Url
    with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2])

    with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommended_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommended_books[5])
        st.image(poster_url[5])
