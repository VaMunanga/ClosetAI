import streamlit as st

# 🧥 Title and intro
st.title("👗 Closet AI - Your Smart Fashion Assistant")
st.subheader("Organize, Recommend, and Redefine Your Closet")

# 🧍 User Section
st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Go to", ["Add Clothes", "View Closet", "Recommendations"])

if page == "Add Clothes":
    st.header("Add New Clothes 👕")
    name = st.text_input("Clothing name")
    color = st.selectbox("Color", ["Red", "Blue", "Black", "White", "Other"])
    image = st.file_uploader("Upload clothing image", type=["jpg", "png"])
    if st.button("Add to Closet"):
        st.success(f"{name} ({color}) added successfully!")

elif page == "View Closet":
    st.header("👚 Your Closet")
    st.info("You’ll soon be able to view and manage your wardrobe here!")

elif page == "Recommendations":
    st.header("✨ Outfit Recommendations")
    st.info("AI styling coming soon!")
