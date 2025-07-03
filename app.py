import streamlit as st
from recommender import recommend
from recommender import get_movie_details
st.set_page_config(page_title="Movie Recommender", layout ="centered")
st.title("Movie Recommender")
st.write("Enter a movie title to get similar recommendations.")
if 'rec_count' not in st.session_state:
    st.session_state.rec_count = 5
if 'last_movie' not in st.session_state:
    st.session_state.last_movie = ""
if 'trigger_recommend' not in st.session_state:
    st.session_state.trigger_recommend = False
user_input = st.text_input("Movie Title")
if user_input != st.session_state.last_movie:
    st.session_state.rec_count = 5
    st.session_state.last_movie = user_input
    st.session_state.trigger_recommend = False
if st.button("Recommend"):
    if user_input.strip() == "":
        st.warning("Please enter a movie title.")
        st.session_state.trigger_recommend = False
    else:
        st.session_state.trigger_recommend = True
if st.session_state.trigger_recommend:
    results = recommend(user_input, count = st.session_state.rec_count)
    if isinstance(results, list):
        st.success("Here are your recommendations:")
        for movie in results:
            details = get_movie_details(movie)
            if details:
                imdb_url = f"https://www.imdb.com/title/{details['imdb_id']}/"
                col1, col2 = st.columns([1, 3])

                with col1:
                    st.image(details['poster'], width=120)

                with col2:
                    st.markdown(f"### 🎬 [{details['title']}]({imdb_url})", unsafe_allow_html=True)
                    st.write(f"⭐ **IMDb Rating:** {details['rating']}")
                    if details["plot"]:
                        st.write(f"📝 {details['plot']}")      
                st.markdown("---")
            else:
                st.write(f"🎬 {movie}")
                st.write("Details not found.")
                st.markdown("---")
        if st.button("Show more recommendations"):
            st.session_state.rec_count += 5
            st.rerun()
    else:
        st.error(results)