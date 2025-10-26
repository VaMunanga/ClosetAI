import streamlit as st

# Page Configuration - This MUST be first Streamlit command
st.set_page_config(
    page_title="ClosetAI Dashboard",  # Browser tab title
    page_icon="::",                    # Browser tab icon
    layout="wide"                      # Use full width instead of narrow center
)

# Custom CSS for beautiful styling
st.markdown("""
    <style>
    /* Main title styling */
    .main-title {
        font-size: 5rem; 
        font-weight: bold;
        color: #FF6B9D;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    /* Subtitle styling */
    .subtitle {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Metric card styling */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Outfit card styling */
    .outfit-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border: 2px solid #f0f0f0;
        transition: transform 0.2s;
    }
    
    .outfit-card:hover {
        transform: translateY(-5px);
        border-color: #FF6B9D;
    }
    </style>
""", unsafe_allow_html=True)



# Header Section
st.markdown('<p class="main-title"> ClosetAI Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your Smart Fashion Assistant</p>', unsafe_allow_html=True)



st.divider()  # Visual separator line

# 📊 Statistics Section
st.subheader("📊 Your Wardrobe Stats")

# Create 4 columns for metrics
col1, col2, col3, col4 = st.columns(4)

# 📊 EXPLANATION: st.columns(4) creates 4 equal-width columns
# We can put different content in each column
# This is how you create side-by-side layouts!

with col1:
    st.metric(
        label="Total Items",
        value="42",
        delta="+3 this week",
        delta_color="normal"
    )
    # 📊 EXPLANATION: st.metric() creates a statistic card
    # - label: What you're measuring
    # - value: The main number
    # - delta: Change over time (shows with up/down arrow)
    # - delta_color: "normal" (green=good), "inverse" (red=good), "off" (gray)

with col2:
    st.metric(
        label="Outfits Created",
        value="18",
        delta="+5 this month"
    )

with col3:
    st.metric(
        label="Items Resold",
        value="7",
        delta="+2",
        delta_color="normal"
    )

with col4:
    st.metric(
        label="Savings",
        value="$240",
        delta="+$60"
    )

st.divider()

# 🎯 Recommended Outfits Section
st.subheader("✨ Today's Outfit Recommendations")

# Create tabs for different occasions
tab1, tab2, tab3 = st.tabs(["🏢 Professional", "👟 Casual", "🎉 Night Out"])

# 📊 EXPLANATION: st.tabs() creates tabbed navigation
# Users can click between different sections
# Each tab can have completely different content!

with tab1:
    st.write("**Perfect for:** Office meetings, interviews, presentations")
    
    # Create 3 columns for outfit cards
    outfit_col1, outfit_col2, outfit_col3 = st.columns(3)
    
    with outfit_col1:
        # Container groups elements together
        with st.container():
            st.markdown("#### Outfit 1: Classic Professional")
            st.image("https://via.placeholder.com/300x400/4A90E2/FFFFFF?text=Blue+Blazer", 
                     use_container_width=True)
            # 📊 EXPLANATION: st.image() displays images
            # - use_container_width=True makes it responsive
            # - We're using placeholder images for demo
            
            # Expandable details section
            with st.expander("👔 View Items"):
                st.write("- Navy Blazer")
                st.write("- White Button-up Shirt")
                st.write("- Black Dress Pants")
                st.write("- Black Oxford Shoes")
            # 📊 EXPLANATION: st.expander() creates collapsible section
            # Keeps UI clean but details accessible!
            
            if st.button("Select Outfit", key="outfit1"):
                st.success("✅ Outfit selected!")
                # 📊 EXPLANATION: st.button() creates clickable button
                # key="outfit1" gives it unique ID (important when you have multiple buttons!)
    
    with outfit_col2:
        with st.container():
            st.markdown("#### Outfit 2: Modern Business")
            st.image("https://via.placeholder.com/300x400/E94B3C/FFFFFF?text=Gray+Suit", 
                     use_container_width=True)
            with st.expander("👔 View Items"):
                st.write("- Charcoal Gray Suit")
                st.write("- Light Blue Shirt")
                st.write("- Burgundy Tie")
                st.write("- Brown Loafers")
            if st.button("Select Outfit", key="outfit2"):
                st.success("✅ Outfit selected!")
    
    with outfit_col3:
        with st.container():
            st.markdown("#### Outfit 3: Smart Casual")
            st.image("https://via.placeholder.com/300x400/6A4C93/FFFFFF?text=Business+Casual", 
                     use_container_width=True)
            with st.expander("👔 View Items"):
                st.write("- Beige Chinos")
                st.write("- Navy Polo Shirt")
                st.write("- Brown Belt")
                st.write("- White Sneakers")
            if st.button("Select Outfit", key="outfit3"):
                st.success("✅ Outfit selected!")

with tab2:
    st.write("**Perfect for:** Weekend errands, coffee dates, relaxing")
    
    casual_col1, casual_col2, casual_col3 = st.columns(3)
    
    with casual_col1:
        with st.container():
            st.markdown("#### Outfit 4: Weekend Comfort")
            st.image("https://via.placeholder.com/300x400/52B788/FFFFFF?text=Casual+Jeans", 
                     use_container_width=True)
            with st.expander("👕 View Items"):
                st.write("- Blue Jeans")
                st.write("- White T-Shirt")
                st.write("- Denim Jacket")
                st.write("- White Sneakers")
            if st.button("Select Outfit", key="outfit4"):
                st.success("✅ Outfit selected!")
    
    with casual_col2:
        with st.container():
            st.markdown("#### Outfit 5: Athletic Style")
            st.image("https://via.placeholder.com/300x400/FF6B6B/FFFFFF?text=Sporty+Look", 
                     use_container_width=True)
            with st.expander("👕 View Items"):
                st.write("- Black Joggers")
                st.write("- Gray Hoodie")
                st.write("- Running Shoes")
                st.write("- Baseball Cap")
            if st.button("Select Outfit", key="outfit5"):
                st.success("✅ Outfit selected!")
    
    with casual_col3:
        with st.container():
            st.markdown("#### Outfit 6: Relaxed Vibe")
            st.image("https://via.placeholder.com/300x400/4ECDC4/FFFFFF?text=Chill+Mode", 
                     use_container_width=True)
            with st.expander("👕 View Items"):
                st.write("- Khaki Shorts")
                st.write("- Striped Polo")
                st.write("- Canvas Shoes")
                st.write("- Sunglasses")
            if st.button("Select Outfit", key="outfit6"):
                st.success("✅ Outfit selected!")

with tab3:
    st.write("**Perfect for:** Dinners, parties, special events")
    
    night_col1, night_col2, night_col3 = st.columns(3)
    
    with night_col1:
        with st.container():
            st.markdown("#### Outfit 7: Elegant Evening")
            st.image("https://via.placeholder.com/300x400/8B5CF6/FFFFFF?text=Evening+Wear", 
                     use_container_width=True)
            with st.expander("✨ View Items"):
                st.write("- Black Dress Shirt")
                st.write("- Dark Jeans")
                st.write("- Black Blazer")
                st.write("- Leather Shoes")
            if st.button("Select Outfit", key="outfit7"):
                st.success("✅ Outfit selected!")
    
    with night_col2:
        with st.container():
            st.markdown("#### Outfit 8: Club Ready")
            st.image("https://via.placeholder.com/300x400/EC4899/FFFFFF?text=Party+Style", 
                     use_container_width=True)
            with st.expander("✨ View Items"):
                st.write("- Slim Black Pants")
                st.write("- Patterned Shirt")
                st.write("- Chelsea Boots")
                st.write("- Watch")
            if st.button("Select Outfit", key="outfit8"):
                st.success("✅ Outfit selected!")
    
    with night_col3:
        with st.container():
            st.markdown("#### Outfit 9: Date Night")
            st.image("https://via.placeholder.com/300x400/F59E0B/FFFFFF?text=Date+Night", 
                     use_container_width=True)
            with st.expander("✨ View Items"):
                st.write("- Navy Sweater")
                st.write("- Gray Slacks")
                st.write("- Brown Shoes")
                st.write("- Cologne")
            if st.button("Select Outfit", key="outfit9"):
                st.success("✅ Outfit selected!")

st.divider()

#Quick Actions Section
st.subheader("⚡ Quick Actions")

action_col1, action_col2, action_col3, action_col4 = st.columns(4)

with action_col1:
    if st.button("📸 Add New Item", use_container_width=True):
        st.info("Navigate to Add Clothes page!")

with action_col2:
    if st.button("🔄 Shuffle Recommendations", use_container_width=True):
        st.success("New recommendations coming!")

with action_col3:
    if st.button("💰 Check Resale Value", use_container_width=True):
        st.info("Resale feature coming soon!")

with action_col4:
    if st.button("📊 View Analytics", use_container_width=True):
        st.info("Analytics feature coming soon!")


# Footer Section
st.divider()
st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <p>Built with ❤️ using Streamlit | ClosetAI v1.0</p>
        <p>Your personal fashion AI assistant</p>
    </div>
""", unsafe_allow_html=True)