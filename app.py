import streamlit as st
import joblib

# -----------------------------
# Load Trained Model
# -----------------------------
model = joblib.load("model/house_price_model.pkl")

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.stApp{
    background-color:#0B0F19;
}

/* Input boxes */
div[data-baseweb="input"]{
    border-radius:10px;
}

/* Button */
.stButton>button{
    width:100%;
    height:55px;
    border-radius:12px;
    border:none;
    background:linear-gradient(90deg,#007CF0,#00DFD8);
    color:white;
    font-size:20px;
    font-weight:bold;
}

.stButton>button:hover{
    background:linear-gradient(90deg,#0066cc,#00bcd4);
    transform:scale(1.02);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------

st.markdown("""
<h1 style='text-align:center;
background: linear-gradient(90deg,#00BFFF,#00FFFF,#0099FF);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;'>

🏠 House Price Prediction

</h1>
""", unsafe_allow_html=True)

st.markdown(
"<h4 style='text-align:center;color:#7FDBFF;'>🤖 AI Powered House Price Estimator</h4>",
unsafe_allow_html=True)

st.divider()

st.subheader("📋 Enter House Details")

# -----------------------------
# Two Columns
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=0,
        max_value=10,
        value=3
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=0.0,
        max_value=10.0,
        value=2.0
    )

    sqft_living = st.number_input(
        "Living Area (sqft)",
        min_value=100,
        value=2000
    )

    sqft_lot = st.number_input(
        "Lot Size (sqft)",
        min_value=100,
        value=8000
    )

    floors = st.number_input(
        "Floors",
        min_value=1.0,
        max_value=5.0,
        value=2.0
    )

    waterfront = st.number_input(
        "Waterfront (0=No,1=Yes)",
        min_value=0,
        max_value=1,
        value=0
    )

with col2:

    view = st.number_input(
        "View (0-4)",
        min_value=0,
        max_value=4,
        value=0
    )

    condition = st.number_input(
        "Condition (1-5)",
        min_value=1,
        max_value=5,
        value=3
    )

    sqft_above = st.number_input(
        "Above Ground Area (sqft)",
        min_value=100,
        value=1800
    )

    sqft_basement = st.number_input(
        "Basement Area (sqft)",
        min_value=0,
        value=200
    )

    yr_built = st.number_input(
        "Year Built",
        min_value=1900,
        max_value=2026,
        value=2000
    )

    yr_renovated = st.number_input(
        "Year Renovated",
        min_value=0,
        max_value=2026,
        value=0
    )

st.divider()

# -----------------------------
# Predict Button
# -----------------------------

left, center, right = st.columns([1,2,1])

with center:

    predict = st.button("🔷 Predict House Price")

# -----------------------------
# Prediction
# -----------------------------

if predict:

    input_data = [[
        bedrooms,
        bathrooms,
        sqft_living,
        sqft_lot,
        floors,
        waterfront,
        view,
        condition,
        sqft_above,
        sqft_basement,
        yr_built,
        yr_renovated
    ]]

    predicted_price = model.predict(input_data)

    st.markdown("---")

    st.markdown(f"""
<div style="
background:linear-gradient(90deg,#007CF0,#00DFD8);
padding:25px;
border-radius:15px;
text-align:center;
box-shadow:0px 0px 20px #00BFFF;
">

<h2 style="color:white;">
💰 Estimated House Price
</h2>

<h1 style="color:white;">
₹ {predicted_price[0]:,.2f}
</h1>

</div>
""", unsafe_allow_html=True)

    st.balloons()

st.divider()

st.markdown(
"""
<p style='text-align:center;color:gray;'>

Made with ❤️ using Streamlit & Scikit-Learn

</p>
""",
unsafe_allow_html=True
)