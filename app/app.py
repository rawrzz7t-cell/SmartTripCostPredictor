import streamlit as st
from predict import predict_price

st.markdown("""
<style>

/* Main */
.main {
    background-color: #f5f7fa;
}

/* Tombol */
.stButton>button{
    width:100%;
    height:55px;
    border-radius:10px;
    background:#0d6efd;
    color:white;
    font-size:20px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#0b5ed7;
    color:white;
}

/* Metric */
[data-testid="stMetric"]{
    border-radius:12px;
    border:1px solid #dddddd;
    padding:20px;
    background:white;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Smart Trip Cost Predictor",
    page_icon="🚖",
    layout="wide"
)

st.title("🚖 Smart Trip Cost Predictor")

st.caption("Prediksi tarif perjalanan menggunakan Artificial Neural Network")

st.write("")

st.divider()

st.subheader("📋 Input Data Perjalanan")

# Membuat 2 kolom
col1, col2 = st.columns(2)

# ==========================
# KOLOM KIRI
# ==========================
with col1:

    distance = st.number_input(
        "📍 Trip Distance (km)",
        min_value=0.0,
        value=5.0
    )

    passenger = st.number_input(
        "👥 Passenger Count",
        min_value=1,
        value=1
    )

    duration = st.number_input(
        "⏱ Trip Duration",
        min_value=1.0,
        value=20.0
    )

    base_fare = st.number_input(
        "💵 Base Fare",
        min_value=0.0,
        value=5.0
    )

    per_km = st.number_input(
        "🚗 Per KM Rate",
        min_value=0.0,
        value=2.0
    )

    per_minute = st.number_input(
        "⏰ Per Minute Rate",
        min_value=0.0,
        value=0.5
    )

# ==========================
# KOLOM KANAN
# ==========================
with col2:

    # Time of Day
    time_options = {
        "Morning": 0,
        "Afternoon": 1,
        "Evening": 2,
        "Night": 3
    }

    selected_time = st.selectbox(
        "Time of Day",
        list(time_options.keys())
    )

    time = time_options[selected_time]

    # Day of Week
    day_options = {
        "Weekday": 0,
        "Weekend": 1
    }

    selected_day = st.selectbox(
        "Day of Week",
        list(day_options.keys())
    )

    day = day_options[selected_day]

    # Traffic
    traffic_options = {
        "Low": 0,
        "Medium": 1,
        "High": 2
    }

    selected_traffic = st.selectbox(
        "Traffic Conditions",
        list(traffic_options.keys())
    )

    traffic = traffic_options[selected_traffic]

    # Weather
    weather_options = {
        "Clear": 0,
        "Rain": 1,
        "Fog": 2
    }

    selected_weather = st.selectbox(
        "Weather",
        list(weather_options.keys())
    )

    weather = weather_options[selected_weather]

st.divider()

# Tombol (belum dipakai)
if st.button("🚖 Predict Fare"):

    # Susun data sesuai urutan fitur saat training
    input_data = [
        distance,
        time,
        day,
        passenger,
        traffic,
        weather,
        base_fare,
        per_km,
        per_minute,
        duration
    ]

    # Prediksi tarif
    hasil = predict_price(input_data)

    ##st.write("Hasil dari model :", hasil)

    kurs = 17900
    hasil_rupiah = hasil * kurs

    ##st.write("Hasil dalam Rupiah :", hasil_rupiah)

    # Tampilkan hasil
    st.divider()

    st.subheader("💰 Estimated Fare")

    st.write(f"## 💰 Estimasi Tarif")
    st.write(f"### Rp {hasil_rupiah:,.0f}")
        
    st.caption("Konversi menggunakan kurs 1 USD = Rp17.900")