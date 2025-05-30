# app.py
import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Alzheimer's Apps",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk styling dengan kompatibilitas dark mode
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Global Styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #6A0DAD 0%, #8A2BE2 50%, #9370DB 100%) !important;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #6A0DAD 0%, #8A2BE2 50%, #9370DB 100%) !important;
    }
    
    /* Custom App Header */
    .app-header {
        background: linear-gradient(135deg, #6A0DAD 0%, #8A2BE2 25%, #9370DB 50%, #DDA0DD 75%, #E6E6FA 100%);
        padding: 2rem 3rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(106, 13, 173, 0.3);
        text-align: center;
        border: 2px solid rgba(106, 13, 173, 0.2);
    }
    
    .app-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: #FFFFFF !important;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
        -webkit-text-stroke: 1px rgba(255,255,255,0.1);
    }
    
    .app-subtitle {
        font-family: 'Poppins', sans-serif;
        font-size: 1.2rem;
        color: #FFFFFF !important;
        font-weight: 400;
        margin-top: 0;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.3);
    }
    
    /* Card Styling dengan kontras yang lebih baik */
    .info-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8F8FF 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(106, 13, 173, 0.15);
        margin: 1rem 0;
        border: 2px solid rgba(106, 13, 173, 0.2);
        color: #2E2E2E !important;
    }
    
    .info-card p {
        color: #2E2E2E !important;
        font-weight: 500;
    }
    
    .feature-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8F8FF 100%);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 5px 15px rgba(106, 13, 173, 0.1);
        margin: 1rem 0;
        border-left: 4px solid #8A2BE2;
        border: 2px solid rgba(106, 13, 173, 0.15);
        transition: transform 0.3s ease;
        color: #2E2E2E !important;
    }
    
    .feature-card p {
        color: #444444 !important;
        font-weight: 400;
    }
    
    .feature-card h3, .feature-card h4 {
        color: #6A0DAD !important;
        font-weight: 600;
    }
    
    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(106, 13, 173, 0.2);
    }
    
    /* Custom Headers dengan kontras lebih baik */
    .section-header {
        font-family: 'Poppins', sans-serif;
        color: #6A0DAD !important;
        font-weight: 700;
        font-size: 2rem;
        margin: 2rem 0 1rem 0;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(106, 13, 173, 0.1);
    }
    
    .subsection-header {
        font-family: 'Poppins', sans-serif;
        color: #8A2BE2 !important;
        font-weight: 600;
        font-size: 1.5rem;
        margin: 1.5rem 0 1rem 0;
        text-shadow: 1px 1px 2px rgba(138, 43, 226, 0.1);
    }
    
    /* Form Styling dengan background yang solid */
    .stForm {
        background: #FFFFFF !important;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(106, 13, 173, 0.1);
        border: 2px solid rgba(106, 13, 173, 0.2);
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #6A0DAD 0%, #8A2BE2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.75rem 2rem !important;
        font-family: 'Poppins', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 5px 15px rgba(106, 13, 173, 0.3) !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(106, 13, 173, 0.4) !important;
        background: linear-gradient(135deg, #5A0B9D 0%, #7A1BD2 100%) !important;
    }
    
    /* Success/Alert Styling */
    .stAlert {
        border-radius: 10px !important;
        border: 2px solid rgba(106, 13, 173, 0.3) !important;
    }
    
    /* Navigation Menu Styling */
    .nav-menu {
        background: linear-gradient(135deg, #6A0DAD 0%, #8A2BE2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border: 2px solid rgba(255, 255, 255, 0.1);
    }
    
    .nav-title {
        font-family: 'Poppins', sans-serif;
        color: #FFFFFF !important;
        font-weight: 600;
        font-size: 1.3rem;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.3);
    }
    
    /* Metrics Styling dengan background solid */
    .metric-container {
        background: linear-gradient(135deg, #FFFFFF 0%, #F0E6FF 100%);
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(106, 13, 173, 0.1);
        border: 2px solid rgba(106, 13, 173, 0.15);
    }
    
    .metric-container h2 {
        color: #6A0DAD !important;
        margin: 0 !important;
        font-weight: 700 !important;
        text-shadow: 1px 1px 2px rgba(106, 13, 173, 0.1);
    }
    
    .metric-container p {
        margin: 0 !important;
        color: #5A0B9D !important;
        font-weight: 500 !important;
    }
    
    /* Custom Text Colors dengan kontras yang lebih baik */
    .purple-text {
        color: #6A0DAD !important;
        font-weight: 600 !important;
    }
    
    .light-purple-text {
        color: #8A2BE2 !important;
        font-weight: 500 !important;
    }
    
    /* Perbaikan untuk teks di dalam list */
    .info-card ul li {
        color: #2E2E2E !important;
        font-weight: 400;
        margin-bottom: 0.5rem;
    }
    
    .info-card strong {
        color: #6A0DAD !important;
        font-weight: 600;
    }
    
    .info-card h4 {
        color: #6A0DAD !important;
        font-weight: 600;
    }
    
    /* Perbaikan untuk input form labels */
    .stSelectbox label, .stSlider label, .stRadio label {
        color: #2E2E2E !important;
        font-weight: 500 !important;
    }
    
    /* Styling untuk markdown dalam form */
    .stForm p, .stForm strong {
        color: #2E2E2E !important;
        font-weight: 500;
    }
    
    /* Footer styling */
    .footer-text {
        color: #6A0DAD !important;
        font-weight: 500;
    }
    
    .footer-text small {
        color: #8A2BE2 !important;
    }
    
    /* Perbaikan untuk hasil prediksi */
    .prediction-result {
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .prediction-positive {
        color: #d32f2f !important;
    }
    
    .prediction-negative {
        color: #2e7d32 !important;
    }
</style>
""", unsafe_allow_html=True)

# Header Aplikasi
st.markdown("""
<div class="app-header">
    <h1 class="app-title">🧠 Alzheimer's Apps</h1>
    <p class="app-subtitle">Advanced Detection & Analysis System</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("""
    <div class="nav-menu">
        <div class="nav-title">Navigation Menu</div>
    </div>
    """, unsafe_allow_html=True)
    
    page = st.selectbox(
        "",
        ["🏠 Beranda", "🔬 Identifikasi Alzheimer", "📚 Informasi Tambahan"],
        format_func=lambda x: x
    )

# Main Content berdasarkan pilihan menu
if page == "🏠 Beranda":
    st.markdown('<h2 class="section-header">Selamat Datang di Alzheimer\'s Apps</h2>', unsafe_allow_html=True)
    
    # Welcome Card
    st.markdown("""
    <div class="info-card">
        <p style="font-size: 1.1rem; text-align: center; margin-bottom: 0;">
            Platform canggih untuk deteksi dini dan analisis penyakit Alzheimer menggunakan 
            teknologi Machine Learning terdepan.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Features Overview
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3 style="color: #6A0DAD; text-align: center;">🔬 Deteksi Akurat</h3>
            <p style="text-align: center;">Menggunakan algoritma XGBoost dan Random Forest untuk prediksi yang presisi</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3 style="color: #6A0DAD; text-align: center;">⚡ Hasil Cepat</h3>
            <p style="text-align: center;">Analisis komprehensif dalam hitungan detik dengan interface yang user-friendly</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3 style="color: #6A0DAD; text-align: center;">📊 Data Lengkap</h3>
            <p style="text-align: center;">Evaluasi berdasarkan 31 parameter klinis dan gaya hidup</p>
        </div>
        """, unsafe_allow_html=True)

# Features Explanation Section
    st.markdown('<h2 class="section-header">📝 Penjelasan Fitur Input</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <p style="font-size: 1.1rem; text-align: center; margin-bottom: 1rem;">
            Sistem kami menganalisis <strong>32 parameter</strong> yang terbagi dalam 5 kategori utama 
            untuk memberikan prediksi Alzheimer yang akurat dan komprehensif.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create expandable sections for each category
    with st.expander("👥 **Demographic Details** - Detail Demografis", expanded=False):
        st.markdown("""
        <div class="feature-card">
            <h4>Parameter Demografis Pasien</h4>
            <ul>
                <li><strong>Age (Usia):</strong> Rentang usia pasien dari 60-90 tahun. Usia adalah faktor risiko utama Alzheimer.</li>
                <li><strong>Gender (Jenis Kelamin):</strong> 
                    <ul>
                        <li>0 = Pria (Male)</li>
                        <li>1 = Wanita (Female)</li>
                    </ul>
                </li>
                <li><strong>Ethnicity (Etnis):</strong>
                    <ul>
                        <li>0 = Kaukasia (Caucasian)</li>
                        <li>1 = Afrika Amerika (African American)</li>
                        <li>2 = Asia (Asian)</li>
                        <li>3 = Lainnya (Other)</li>
                    </ul>
                </li>
                <li><strong>Education Level (Tingkat Pendidikan):</strong>
                    <ul>
                        <li>0 = Tidak Sekolah (None)</li>
                        <li>1 = SMA (High School)</li>
                        <li>2 = Sarjana (Bachelor's)</li>
                        <li>3 = Pendidikan Tinggi (Higher)</li>
                    </ul>
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("🏃‍♂️ **Lifestyle Factors** - Faktor Gaya Hidup", expanded=False):
        st.markdown("""
        <div class="feature-card">
            <h4>Parameter Gaya Hidup dan Kebiasaan</h4>
            <ul>
                <li><strong>BMI (Body Mass Index):</strong> Indeks massa tubuh dengan rentang 15-40. Obesitas dapat meningkatkan risiko Alzheimer.</li>
                <li><strong>Smoking (Merokok):</strong> 
                    <ul>
                        <li>0 = Tidak Merokok</li>
                        <li>1 = Merokok</li>
                    </ul>
                </li>
                <li><strong>Alcohol Consumption (Konsumsi Alkohol):</strong> Konsumsi alkohol mingguan dalam unit (0-20). Konsumsi berlebihan dapat mempengaruhi kognitif.</li>
                <li><strong>Physical Activity (Aktivitas Fisik):</strong> Aktivitas fisik mingguan dalam jam (0-10). Olahraga teratur dapat mengurangi risiko Alzheimer.</li>
                <li><strong>Diet Quality (Kualitas Diet):</strong> Skor kualitas diet (0-10). Diet sehat dapat melindungi fungsi otak.</li>
                <li><strong>Sleep Quality (Kualitas Tidur):</strong> Skor kualitas tidur (4-10). Tidur yang buruk dikaitkan dengan penurunan kognitif.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("🏥 **Medical History** - Riwayat Medis", expanded=False):
        st.markdown("""
        <div class="feature-card">
            <h4>Riwayat Penyakit dan Kondisi Medis</h4>
            <ul>
                <li><strong>Family History Alzheimers (Riwayat Keluarga):</strong> 
                    <ul>
                        <li>0 = Tidak Ada Riwayat Keluarga</li>
                        <li>1 = Ada Riwayat Keluarga Alzheimer</li>
                    </ul>
                </li>
                <li><strong>Cardiovascular Disease (Penyakit Kardiovaskular):</strong> 
                    <ul>
                        <li>0 = Tidak Ada</li>
                        <li>1 = Ada Penyakit Jantung</li>
                    </ul>
                </li>
                <li><strong>Diabetes:</strong> 
                    <ul>
                        <li>0 = Tidak Diabetes</li>
                        <li>1 = Menderita Diabetes</li>
                    </ul>
                </li>
                <li><strong>Depression (Depresi):</strong> 
                    <ul>
                        <li>0 = Tidak Depresi</li>
                        <li>1 = Mengalami Depresi</li>
                    </ul>
                </li>
                <li><strong>Head Injury (Cedera Kepala):</strong> 
                    <ul>
                        <li>0 = Tidak Ada Riwayat</li>
                        <li>1 = Ada Riwayat Cedera Kepala</li>
                    </ul>
                </li>
                <li><strong>Hypertension (Hipertensi):</strong> 
                    <ul>
                        <li>0 = Tekanan Darah Normal</li>
                        <li>1 = Hipertensi</li>
                    </ul>
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("🩺 **Clinical Measurements** - Pengukuran Klinis", expanded=False):
        st.markdown("""
        <div class="feature-card">
            <h4>Parameter Laboratorium dan Vital Signs</h4>
            <ul>
                <li><strong>Systolic BP (Tekanan Darah Sistolik):</strong> Tekanan darah sistolik (90-180 mmHg). Tekanan tinggi dapat merusak pembuluh darah otak.</li>
                <li><strong>Diastolic BP (Tekanan Darah Diastolik):</strong> Tekanan darah diastolik (60-120 mmHg).</li>
                <li><strong>Cholesterol Total (Kolesterol Total):</strong> Kadar kolesterol total (150-300 mg/dL). Kolesterol tinggi dapat mempengaruhi aliran darah ke otak.</li>
                <li><strong>Cholesterol LDL (Kolesterol Jahat):</strong> Kadar LDL (50-200 mg/dL). LDL tinggi dikaitkan dengan risiko Alzheimer.</li>
                <li><strong>Cholesterol HDL (Kolesterol Baik):</strong> Kadar HDL (20-100 mg/dL). HDL tinggi dapat melindungi otak.</li>
                <li><strong>Cholesterol Triglycerides (Trigliserida):</strong> Kadar trigliserida (50-400 mg/dL).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("🧠 **Cognitive & Functional Assessments** - Penilaian Kognitif dan Fungsional", expanded=False):
        st.markdown("""
        <div class="feature-card">
            <h4>Tes Kognitif dan Penilaian Fungsional</h4>
            <ul>
                <li><strong>MMSE (Mini-Mental State Examination):</strong> Skor tes kognitif (0-30). Skor rendah menunjukkan gangguan kognitif.</li>
                <li><strong>Functional Assessment (Penilaian Fungsional):</strong> Skor kemampuan fungsional (0-10). Skor rendah menunjukkan gangguan yang lebih besar.</li>
                <li><strong>Memory Complaints (Keluhan Memori):</strong> 
                    <ul>
                        <li>0 = Tidak Ada Keluhan</li>
                        <li>1 = Ada Keluhan Memori</li>
                    </ul>
                </li>
                <li><strong>Behavioral Problems (Masalah Perilaku):</strong> 
                    <ul>
                        <li>0 = Tidak Ada Masalah</li>
                        <li>1 = Ada Masalah Perilaku</li>
                    </ul>
                </li>
                <li><strong>ADL (Activities of Daily Living):</strong> Skor kemampuan aktivitas harian (0-10). Skor rendah menunjukkan ketergantungan yang lebih besar.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("⚠️ **Symptoms** - Gejala Klinis", expanded=False):
        st.markdown("""
        <div class="feature-card">
            <h4>Gejala dan Tanda Klinis Alzheimer</h4>
            <ul>
                <li><strong>Confusion (Kebingungan):</strong> 
                    <ul>
                        <li>0 = Tidak Mengalami Kebingungan</li>
                        <li>1 = Mengalami Kebingungan</li>
                    </ul>
                </li>
                <li><strong>Disorientation (Disorientasi):</strong> 
                    <ul>
                        <li>0 = Orientasi Normal</li>
                        <li>1 = Mengalami Disorientasi (waktu, tempat, orang)</li>
                    </ul>
                </li>
                <li><strong>Personality Changes (Perubahan Kepribadian):</strong> 
                    <ul>
                        <li>0 = Kepribadian Stabil</li>
                        <li>1 = Mengalami Perubahan Kepribadian</li>
                    </ul>
                </li>
                <li><strong>Difficulty Completing Tasks (Kesulitan Menyelesaikan Tugas):</strong> 
                    <ul>
                        <li>0 = Dapat Menyelesaikan Tugas Normal</li>
                        <li>1 = Kesulitan Menyelesaikan Tugas Sehari-hari</li>
                    </ul>
                </li>
                <li><strong>Forgetfulness (Kelupaan):</strong> 
                    <ul>
                        <li>0 = Memori Normal</li>
                        <li>1 = Mengalami Kelupaan yang Signifikan</li>
                    </ul>
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Summary card
    st.markdown("""
    <div class="info-card">
        <h4 style="color: #6A0DAD; text-align: center;">🎯 Mengapa Fitur-Fitur Ini Penting?</h4>
        <p style="text-align: center;">
            Setiap fitur telah dipilih berdasarkan penelitian medis yang menunjukkan korelasi 
            dengan perkembangan Alzheimer. Kombinasi dari 31 parameter ini memberikan 
            gambaran holistik tentang kondisi pasien dan memungkinkan prediksi yang lebih akurat.
        </p>
        <p style="text-align: center; font-weight: 600; color: #8A2BE2;">
            Semakin lengkap dan akurat data yang dimasukkan, semakin tepat hasil prediksi yang diberikan.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
 #Data Visualization Section
    st.markdown('<h2 class="section-header">📈 Visualisasi Data Alzheimer</h2>', unsafe_allow_html=True)
    
    # Load and display dataset
    try:
        import pandas as pd
        import numpy as np
        import plotly.express as px
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
        
        # Load dataset
        df = pd.read_csv('alzheimers_disease_data.csv')


        
        # Dataset Overview Card
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #6A0DAD; margin-bottom: 1rem;">📋 Dataset Overview</h4>
            <p><strong>Dataset:</strong> alzheimers_disease_data.csv</p>
            <p><strong>Total Records:</strong> {} samples</p>
            <p><strong>Features:</strong> {} variables</p>
            <p><strong>Target Variable:</strong> Diagnosis (Alzheimer's vs Non-Alzheimer's)</p>
        </div>
        """.format(len(df), len(df.columns)), unsafe_allow_html=True)
        
        # Tabs for different visualizations
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Data Overview", "📈 Distribusi", "🔍 Korelasi", "📋 Raw Data"])
        
        with tab1:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                total_patients = len(df)
                st.markdown(f"""
                <div class="metric-container">
                    <h2>{total_patients:,}</h2>
                    <p>Total Pasien</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                if 'Diagnosis' in df.columns:
                    alzheimer_cases = len(df[df['Diagnosis'] == 1])
                else:
                    alzheimer_cases = "N/A"
                st.markdown(f"""
                <div class="metric-container">
                    <h2>{alzheimer_cases}</h2>
                    <p>Kasus Alzheimer</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                if 'Diagnosis' in df.columns:
                    normal_cases = len(df[df['Diagnosis'] == 0])
                else:
                    normal_cases = "N/A"
                st.markdown(f"""
                <div class="metric-container">
                    <h2>{normal_cases}</h2>
                    <p>Kasus Normal</p>
                </div>
                """, unsafe_allow_html=True)
            
            # Distribution of Diagnosis
            if 'Diagnosis' in df.columns:
                fig_pie = px.pie(
                    values=df['Diagnosis'].value_counts().values,
                    names=['Normal', 'Alzheimer'],
                    title="Distribusi Diagnosis",
                    color_discrete_sequence=['#9370DB', '#6A0DAD']
                )
                fig_pie.update_layout(
                    title_font_size=16,
                    title_font_color='#6A0DAD',
                    font=dict(size=12),
                    showlegend=True,
                    height=400
                )
                st.plotly_chart(fig_pie, use_container_width=True)
        
        with tab2:
            # Age and Gender Distribution
            if 'Age' in df.columns:
                col1, col2 = st.columns(2)
                
                with col1:
                    fig_age = px.histogram(
                        df, x='Age', 
                        title="Distribusi Usia Pasien",
                        color_discrete_sequence=['#8A2BE2']
                    )
                    fig_age.update_layout(
                        title_font_color='#6A0DAD',
                        xaxis_title="Usia",
                        yaxis_title="Jumlah Pasien"
                    )
                    st.plotly_chart(fig_age, use_container_width=True)
                
                with col2:
                    if 'Gender' in df.columns:
                        fig_gender = px.bar(
                            x=df['Gender'].value_counts().index,
                            y=df['Gender'].value_counts().values,
                            title="Distribusi Jenis Kelamin",
                            color_discrete_sequence=['#9370DB']
                        )
                        fig_gender.update_layout(
                            title_font_color='#6A0DAD',
                            xaxis_title="Jenis Kelamin",
                            yaxis_title="Jumlah Pasien"
                        )
                        st.plotly_chart(fig_gender, use_container_width=True)
            
            # Lifestyle factors
            lifestyle_cols = ['PhysicalActivity', 'DietQuality', 'SleepQuality', 'BMI']
            available_lifestyle = [col for col in lifestyle_cols if col in df.columns]
            
            if available_lifestyle:
                fig_lifestyle = make_subplots(
                    rows=2, cols=2,
                    subplot_titles=available_lifestyle
                )
                
                for i, col in enumerate(available_lifestyle[:4]):
                    row = (i // 2) + 1
                    col_pos = (i % 2) + 1
                    
                    fig_lifestyle.add_trace(
                        go.Histogram(x=df[col], name=col, marker_color='#8A2BE2'),
                        row=row, col=col_pos
                    )
                
                fig_lifestyle.update_layout(
                    title_text="Distribusi Faktor Gaya Hidup",
                    title_font_color='#6A0DAD',
                    height=500,
                    showlegend=False
                )
                st.plotly_chart(fig_lifestyle, use_container_width=True)
        
        with tab3:
            # --- Heatmap Korelasi dari Gambar ---
            st.markdown('<h4 class="subsection-header" style="font-size: 1.3rem; margin: 2rem 0 1rem 0;">📊 Matriks Korelasi</h4>', unsafe_allow_html=True)

            # Memanggil gambar heatmap yang sudah ada
            st.image("assets/heatmap.png", caption="Matriks Korelasi Antar Variabel")

            # Anda bisa menambahkan penjelasan singkat di sini jika diperlukan
            st.markdown("""
                <p>
                Visualisasi di atas menunjukkan matriks korelasi antar variabel.
                Angka-angka dalam heatmap merepresentasikan kekuatan dan arah hubungan linier antar pasangan variabel.
                </p>
            """, unsafe_allow_html=True)
            
            # --- Feature Importance Visualization ---
            st.markdown('<h4 class="subsection-header" style="font-size: 1.3rem; margin: 2rem 0 1rem 0;">⭐ Tingkat Kepentingan Fitur</h4>', unsafe_allow_html=True)

            # Definisikan kembali numeric_cols di sini
            numeric_cols = df.select_dtypes(include=[np.number]).columns

            if 'Diagnosis' in df.columns:
                if 'Diagnosis' in numeric_cols:
                    feature_importance = abs(df[numeric_cols].corrwith(df['Diagnosis'])).sort_values(ascending=True)
                else:
                    df['Diagnosis_numeric'] = df['Diagnosis'].astype(int)
                    feature_importance = abs(df[numeric_cols].corrwith(df['Diagnosis_numeric'])).sort_values(ascending=True)


                fig_importance = px.bar(
                    x=feature_importance.values,
                    y=feature_importance.index,
                    orientation='h',
                    title="Tingkat Kepentingan Fitur (Korelasi Absolut dengan Diagnosis)", # Perbarui judul sedikit
                    color_discrete_sequence=['#6A0DAD']
                )
                fig_importance.update_layout(
                    title_font_color='#6A0DAD',
                    xaxis_title="Korelasi Absolut",
                    yaxis_title="Fitur",
                    height=600
                )
                st.plotly_chart(fig_importance, use_container_width=True)
            else:
                st.warning("Kolom 'Diagnosis' tidak ditemukan dalam data. Visualisasi Tingkat Kepentingan Fitur tidak dapat ditampilkan.")
        
        with tab4:
            st.markdown("""
            <div class="info-card">
                <h4 style="color: #6A0DAD;">📋 Data Mentah - alzheimers_disease_data.csv</h4>
                <p>Berikut adalah tampilan data mentah dari dataset yang digunakan untuk analisis:</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Display raw data with pagination
            st.dataframe(
                df, 
                use_container_width=True,
                height=400
            )
            
            # Data summary
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                <div class="feature-card">
                    <h4>📊 Statistik Deskriptif</h4>
                </div>
                """, unsafe_allow_html=True)
                st.dataframe(df.describe(), use_container_width=True)
            
            with col2:
                st.markdown("""
                <div class="feature-card">
                    <h4>ℹ️ Informasi Dataset</h4>
                </div>
                """, unsafe_allow_html=True)
                
                # Dataset info
                info_data = {
                    'Kolom': df.columns.tolist(),
                    'Tipe Data': [str(dtype) for dtype in df.dtypes],
                    'Missing Values': [df[col].isnull().sum() for col in df.columns]
                }
                info_df = pd.DataFrame(info_data)
                st.dataframe(info_df, use_container_width=True)
    
    except FileNotFoundError:
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #d32f2f;">⚠️ Dataset Tidak Ditemukan</h4>
            <p>File 'alzheimers_disease_data.csv' tidak ditemukan. Pastikan file dataset sudah diupload ke direktori yang sama dengan aplikasi.</p>
            <p><strong>Langkah-langkah:</strong></p>
            <ul>
                <li>Upload file 'alzheimers_disease_data.csv' ke direktori aplikasi</li>
                <li>Pastikan nama file sesuai dengan yang diharapkan</li>
                <li>Refresh halaman setelah file diupload</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    except Exception as e:
        st.markdown(f"""
        <div class="info-card">
            <h4 style="color: #d32f2f;">❌ Error Loading Data</h4>
            <p>Terjadi kesalahan saat memuat data: {str(e)}</p>
        </div>
        """, unsafe_allow_html=True)
    

elif page == "🔬 Identifikasi Alzheimer":
    # Import required libraries
    import joblib
    import numpy as np
    import pandas as pd
    
    st.markdown('<h2 class="section-header">Identifikasi Penyakit Alzheimer</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <p style="text-align: center; font-size: 1.1rem;">
            Silakan lengkapi formulir berikut untuk melakukan analisis risiko Alzheimer berdasarkan data klinis dan gaya hidup.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load models
    try:
        with open("xgb_model.pkl", "rb") as file:
            xgb_model = joblib.load(file)
        with open("rf_model.pkl", "rb") as file:
            rf_model = joblib.load(file)
        models_loaded = True
    except FileNotFoundError:
        st.warning("⚠️ Model files tidak ditemukan. Menggunakan simulasi untuk demo.")
        models_loaded = False
    
    # Fungsi prediksi label
    def interpret_prediction(pred):
        return "Alzheimer" if pred == 1 else "Tidak Alzheimer"
    
    # Mapping options
    ethnicity_options = {
        "Caucasian": 0,
        "African American": 1,
        "Asian": 2,
        "Other": 3
    }
    
    education_options = {
        "None": 0,
        "High School": 1,
        "Bachelor's": 2,
        "Higher": 3
    }
    
    # Main Form
    with st.form("alzheimer_form"):
        st.markdown('<h3 class="subsection-header">📋 Data Pasien</h3>', unsafe_allow_html=True)
        
        # Demographics Section
        st.markdown("**👤 Informasi Demografis**")
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.slider("Usia", 60, 90, 75)
            gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
        
        with col2:
            ethnicity_label = st.selectbox("Etnis", list(ethnicity_options.keys()))
            ethnicity = ethnicity_options[ethnicity_label]
            education_label = st.selectbox("Tingkat Pendidikan", list(education_options.keys()))
            education = education_options[education_label]
        
        st.markdown("---")
        
        # Lifestyle Section
        st.markdown("**🏃‍♂️ Gaya Hidup**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            bmi = st.slider("BMI", 15.0, 40.0, 25.0)
            smoking = st.radio("Merokok?", ["Tidak", "Ya"])
        
        with col2:
            alcohol = st.slider("Konsumsi Alkohol (unit/minggu)", 0, 20, 5)
            activity = st.slider("Aktivitas Fisik (jam/minggu)", 0, 10, 3)
        
        with col3:
            diet = st.slider("Kualitas Diet (0-10)", 0, 10, 7)
            sleep = st.slider("Kualitas Tidur (4-10)", 4, 10, 7)
        
        st.markdown("---")
        
        # Medical History Section
        st.markdown("**🏥 Riwayat Medis**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            family_history = st.radio("Riwayat Alzheimer Keluarga", ["Tidak", "Ya"])
            cvd = st.radio("Penyakit Kardiovaskular", ["Tidak", "Ya"])
        
        with col2:
            diabetes = st.radio("Diabetes", ["Tidak", "Ya"])
            depression = st.radio("Depresi", ["Tidak", "Ya"])
        
        with col3:
            head_injury = st.radio("Cedera Kepala", ["Tidak", "Ya"])
            hypertension = st.radio("Hipertensi", ["Tidak", "Ya"])
        
        st.markdown("---")
        
        # Clinical Measurements
        st.markdown("**🩺 Pengukuran Klinis**")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            sbp = st.slider("Tekanan Darah Sistolik", 90, 180, 120)
            dbp = st.slider("Tekanan Darah Diastolik", 60, 120, 80)
        
        with col2:
            chol_total = st.slider("Kolesterol Total", 150, 300, 200)
            chol_ldl = st.slider("Kolesterol LDL", 50, 200, 100)
        
        with col3:
            trig = st.slider("Trigliserida", 50, 400, 150)
            chol_hdl = st.slider("Kolesterol HDL", 20, 100, 50)

        
        st.markdown("---")
        
        # Cognitive Assessment
        st.markdown("**🧠 Asesmen Kognitif & Fungsional**")
        col1, col2 = st.columns(2)
        
        with col1:
            mmse = st.slider("Skor MMSE", 0, 30, 25)
            func_assess = st.slider("Skor Fungsional", 0, 10, 8)
            adl = st.slider("Skor ADL", 0, 10, 8)
        
        with col2:
            memory_complaints = st.radio("Keluhan Memori", ["Tidak", "Ya"])
            behavioral = st.radio("Masalah Perilaku", ["Tidak", "Ya"])
        
        st.markdown("---")
        
        # Clinical Symptoms
        st.markdown("**⚕️ Gejala Klinis**")
        col1, col2 = st.columns(2)
        
        with col1:
            confusion = st.radio("Kebingungan", ["Tidak", "Ya"])
            disorientation = st.radio("Disorientasi", ["Tidak", "Ya"])
            personality = st.radio("Perubahan Kepribadian", ["Tidak", "Ya"])
        
        with col2:
            tasks = st.radio("Kesulitan Menyelesaikan Tugas", ["Tidak", "Ya"])
            forgetful = st.radio("Sering Lupa", ["Tidak", "Ya"])
        
        st.markdown("---")
        
        # Submit Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            submitted = st.form_submit_button("🔍 Analisis Sekarang", use_container_width=True)
        
        if submitted:
            # Prepare input data (sesuai dengan kode asli)
            input_data = np.array([
                age,
                0 if gender == "Laki-laki" else 1,
                ethnicity,
                education,
                bmi,
                0 if smoking == "Tidak" else 1,
                alcohol,
                activity,
                diet,
                sleep,
                0 if family_history == "Tidak" else 1,
                0 if cvd == "Tidak" else 1,
                0 if diabetes == "Tidak" else 1,
                0 if depression == "Tidak" else 1,
                0 if head_injury == "Tidak" else 1,
                0 if hypertension == "Tidak" else 1,
                sbp, dbp, chol_total, chol_ldl, chol_hdl, trig,
                mmse, func_assess,
                0 if memory_complaints == "Tidak" else 1,
                0 if behavioral == "Tidak" else 1,
                adl,
                0 if confusion == "Tidak" else 1,
                0 if disorientation == "Tidak" else 1,
                0 if personality == "Tidak" else 1,
                0 if tasks == "Tidak" else 1,
                0 if forgetful == "Tidak" else 1
            ]).reshape(1, -1)
            
            # Prediksi menggunakan model (sesuai logika asli)
            if models_loaded:
                xgb_pred = xgb_model.predict(input_data)[0]
                rf_pred = rf_model.predict(input_data)[0]
            else:
                # Simulasi untuk demo jika model tidak tersedia
                import random
                xgb_pred = random.choice([0, 1])
                rf_pred = random.choice([0, 1])
            
            st.markdown("---")
            st.markdown('<h3 class="subsection-header">📊 Hasil Analisis</h3>', unsafe_allow_html=True)

            # Tampilkan hasil sesuai format asli dengan styling yang lebih baik
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"""
                <div class="feature-card">
                    <h4 style="color: #6A0DAD; text-align: center; margin-bottom: 1rem;">XGBoost Model</h4>
                    <p class="prediction-result {'prediction-positive' if xgb_pred == 1 else 'prediction-negative'}" style="text-align: center; margin: 0 0 1rem 0;">
                        📌 {interpret_prediction(xgb_pred)}
                    </p>
                    <div style="background: rgba(106, 13, 173, 0.1); padding: 0.8rem; border-radius: 8px; text-align: center;">
                        <p style="margin: 0; color: #6A0DAD; font-weight: 600; font-size: 0.9rem;">Akurasi Overall: 93%</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class="feature-card">
                    <h4 style="color: #6A0DAD; text-align: center; margin-bottom: 1rem;">Random Forest Model</h4>
                    <p class="prediction-result {'prediction-positive' if rf_pred == 1 else 'prediction-negative'}" style="text-align: center; margin: 0 0 1rem 0;">
                        📌 {interpret_prediction(rf_pred)}
                    </p>
                    <div style="background: rgba(106, 13, 173, 0.1); padding: 0.8rem; border-radius: 8px; text-align: center;">
                        <p style="margin: 0; color: #6A0DAD; font-weight: 600; font-size: 0.9rem;">Akurasi Overall: 91%</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # Performance Metrics Section
            st.markdown('<h4 class="subsection-header" style="font-size: 1.3rem; margin: 2rem 0 1rem 0;">📈 Performa Model</h4>', unsafe_allow_html=True)

            # Create performance metrics in a more detailed format with Predict 0 and Predict 1
            perf_col1, perf_col2 = st.columns(2)

            with perf_col1:
                st.markdown("""
                <div class="metric-container">
                    <h4 style="color: #6A0DAD; margin-bottom: 1rem;">XGBoost Performance</h4>
                    <div style="background: rgba(46, 125, 50, 0.1); padding: 0.8rem; border-radius: 8px; margin-bottom: 1rem;">
                        <p style="margin: 0 0 0.5rem 0; color: #2e7d32; font-weight: 600; text-align: center; font-size: 0.95rem;">Predict 0 (Normal)</p>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">Akurasi:</span>
                            <span style="color: #2e7d32; font-weight: 700; font-size: 0.9rem;">93%</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">Precision:</span>
                            <span style="color: #2e7d32; font-weight: 700; font-size: 0.9rem;">90%</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">Recall:</span>
                            <span style="color: #2e7d32; font-weight: 700; font-size: 0.9rem;">95%</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">F1-Score:</span>
                            <span style="color: #2e7d32; font-weight: 700; font-size: 0.9rem;">93%</span>
                        </div>
                    </div>
                    <div style="background: rgba(211, 47, 47, 0.1); padding: 0.8rem; border-radius: 8px;">
                        <p style="margin: 0 0 0.5rem 0; color: #d32f2f; font-weight: 600; text-align: center; font-size: 0.95rem;">Predict 1 (Alzheimer)</p>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">Akurasi:</span>
                            <span style="color: #d32f2f; font-weight: 700; font-size: 0.9rem;">93%</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">Precision:</span>
                            <span style="color: #d32f2f; font-weight: 700; font-size: 0.9rem;">95%</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">Recall:</span>
                            <span style="color: #d32f2f; font-weight: 700; font-size: 0.9rem;">90%</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">F1-Score:</span>
                            <span style="color: #d32f2f; font-weight: 700; font-size: 0.9rem;">92%</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            with perf_col2:
                st.markdown("""
                <div class="metric-container">
                    <h4 style="color: #6A0DAD; margin-bottom: 1rem;">Random Forest Performance</h4>
                    <div style="background: rgba(46, 125, 50, 0.1); padding: 0.8rem; border-radius: 8px; margin-bottom: 1rem;">
                        <p style="margin: 0 0 0.5rem 0; color: #2e7d32; font-weight: 600; text-align: center; font-size: 0.95rem;">Predict 0 (Normal)</p>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">Akurasi:</span>
                            <span style="color: #2e7d32; font-weight: 700; font-size: 0.9rem;">91%</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">Precision:</span>
                            <span style="color: #2e7d32; font-weight: 700; font-size: 0.9rem;">88%</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">Recall:</span>
                            <span style="color: #2e7d32; font-weight: 700; font-size: 0.9rem;">96%</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">F1-Score:</span>
                            <span style="color: #2e7d32; font-weight: 700; font-size: 0.9rem;">92%</span>
                        </div>
                    </div>
                    <div style="background: rgba(211, 47, 47, 0.1); padding: 0.8rem; border-radius: 8px;">
                        <p style="margin: 0 0 0.5rem 0; color: #d32f2f; font-weight: 600; text-align: center; font-size: 0.95rem;">Predict 1 (Alzheimer)</p>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">Akurasi:</span>
                            <span style="color: #d32f2f; font-weight: 700; font-size: 0.9rem;">91%</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">Precision:</span>
                            <span style="color: #d32f2f; font-weight: 700; font-size: 0.9rem;">96%</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.3rem;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">Recall:</span>
                            <span style="color: #d32f2f; font-weight: 700; font-size: 0.9rem;">86%</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span style="color: #2E2E2E; font-weight: 500; font-size: 0.9rem;">F1-Score:</span>
                            <span style="color: #d32f2f; font-weight: 700; font-size: 0.9rem;">91%</span>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # Explanation of Predict 0 and Predict 1
            st.markdown("""
            <div class="info-card" style="background: linear-gradient(135deg, #E8F5E8 0%, #F3E5F5 100%); border: 2px solid rgba(106, 13, 173, 0.3);">
                <h4 style="color: #6A0DAD; margin-bottom: 1rem; text-align: center;">🔍 Penjelasan Predict 0 dan Predict 1</h4>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
                    <div style="background: rgba(46, 125, 50, 0.1); padding: 1rem; border-radius: 10px; border-left: 4px solid #2e7d32;">
                        <h5 style="margin: 0 0 0.5rem 0; color: #2e7d32; font-weight: 600;">🟢 Predict 0 (Normal)</h5>
                        <p style="margin: 0; color: #2E2E2E; font-size: 0.9rem; line-height: 1.4;">
                            Prediksi untuk pasien yang <strong>tidak memiliki Alzheimer</strong>. 
                            Nilai ini menunjukkan seberapa baik model dalam mengidentifikasi kondisi normal/sehat.
                        </p>
                    </div>
                    <div style="background: rgba(211, 47, 47, 0.1); padding: 1rem; border-radius: 10px; border-left: 4px solid #d32f2f;">
                        <h5 style="margin: 0 0 0.5rem 0; color: #d32f2f; font-weight: 600;">🔴 Predict 1 (Alzheimer)</h5>
                        <p style="margin: 0; color: #2E2E2E; font-size: 0.9rem; line-height: 1.4;">
                            Prediksi untuk pasien yang <strong>terindikasi memiliki Alzheimer</strong>. 
                            Nilai ini menunjukkan seberapa baik model dalam mendeteksi kondisi Alzheimer.
                        </p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Model Comparison
            st.markdown("""
            <div class="info-card" style="background: linear-gradient(135deg, #F0E6FF 0%, #E6E6FA 100%); border: 2px solid rgba(106, 13, 173, 0.3);">
                <h4 style="color: #6A0DAD; margin-bottom: 1rem; text-align: center;">🏆 Perbandingan Model</h4>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                    <div style="text-align: center;">
                        <p style="margin: 0 0 0.5rem 0; color: #6A0DAD; font-weight: 600; font-size: 1.1rem;">🥇 Terbaik Keseluruhan</p>
                        <p style="margin: 0; color: #2E2E2E; font-weight: 500;">XGBoost</p>
                        <p style="margin: 0; color: #2e7d32; font-size: 0.9rem;">(Keseimbangan performa lebih baik)</p>
                    </div>
                    <div style="text-align: center;">
                        <p style="margin: 0 0 0.5rem 0; color: #6A0DAD; font-weight: 600; font-size: 1.1rem;">🌟 Keunggulan Lain</p>
                        <p style="margin: 0; color: #2E2E2E; font-weight: 500;">Random Forest</p>
                        <p style="margin: 0; color: #d32f2f; font-size: 0.9rem;">(Precision 96% untuk Predict 1 - Alzheimer)</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Additional information
            st.markdown("""
            <div class="info-card">
                <h4 style="color: #6A0DAD; margin-bottom: 1rem;">ℹ️ Catatan Penting</h4>
                <p style="margin-bottom: 0.5rem;"><strong>•</strong> Hasil ini adalah prediksi berdasarkan model machine learning dan bukan diagnosis medis definitif</p>
                <p style="margin-bottom: 0.5rem;"><strong>•</strong> Konsultasikan dengan dokter spesialis untuk diagnosis dan penanganan yang tepat</p>
                <p style="margin-bottom: 0;"><strong>•</strong> Model ini memiliki akurasi tinggi namun tetap memerlukan validasi klinis</p>
            </div>
            """, unsafe_allow_html=True)

elif page == "📚 Informasi Tambahan":
    st.markdown('<h2 class="section-header">Informasi Tambahan</h2>', unsafe_allow_html=True)

    # About Alzheimer's
    st.markdown('<h3 class="subsection-header">Tentang Penyakit Alzheimer</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <p style="text-align: justify; line-height: 1.6;">
            Penyakit Alzheimer adalah bentuk demensia yang paling umum, menyebabkan masalah dengan memori, 
            pemikiran, dan perilaku. Gejala biasanya berkembang secara perlahan dan memburuk dari waktu ke waktu, 
            hingga cukup parah sehingga mengganggu tugas sehari-hari. Deteksi dini sangat penting untuk 
            penanganan yang tepat dan perencanaan perawatan yang optimal.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tips Section
    st.markdown('<h3 class="subsection-header">💡 Tips Pencegahan Alzheimer</h3>', unsafe_allow_html=True)
    
    tips_data = [
        ("🧠", "Stimulasi Mental", "Lakukan aktivitas yang menantang otak seperti teka-teki, membaca, atau mempelajari hal baru"),
        ("🏃‍♂️", "Olahraga Teratur", "Aktivitas fisik minimal 150 menit per minggu dapat meningkatkan kesehatan otak"),
        ("🥗", "Pola Makan Sehat", "Konsumsi makanan kaya omega-3, antioksidan, dan kurangi makanan olahan"),
        ("😴", "Tidur Berkualitas", "Tidur 7-9 jam per malam untuk proses detoksifikasi otak yang optimal"),
        ("👥", "Interaksi Sosial", "Pertahankan hubungan sosial yang aktif dan bermakna dengan orang sekitar khususnya keluarga"),
        ("🚭", "Hindari Rokok & Alkohol", "Berhenti merokok dan batasi konsumsi alkohol untuk kesehatan otak")
    ]
    
    for i in range(0, len(tips_data), 2):
        col1, col2 = st.columns(2)
        
        with col1:
            icon, title, desc = tips_data[i]
            st.markdown(f"""
            <div class="feature-card">
                <h4 style="color: #6A0DAD; margin-bottom: 0.5rem;">{icon} {title}</h4>
                <p style="margin: 0; line-height: 1.5; color: #444444;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
        
        if i + 1 < len(tips_data):
            with col2:
                icon, title, desc = tips_data[i + 1]
                st.markdown(f"""
                <div class="feature-card">
                    <h4 style="color: #6A0DAD; margin-bottom: 0.5rem;">{icon} {title}</h4>
                    <p style="margin: 0; line-height: 1.5; color: #444444;">{desc}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Facts Section
    st.markdown('<h3 class="subsection-header">🔍 Fakta Menarik</h3>', unsafe_allow_html=True)
    
    facts = [
        "Otak manusia dewasa terdiri dari sekitar 86 miliar neuron",
        "Penyakit Alzheimer dapat dimulai 10-20 tahun sebelum gejala muncul",
        "Wanita memiliki risiko 2 kali lebih besar terkena Alzheimer dibanding pria",
        "Bilingual dapat menunda onset demensia hingga 4-5 tahun",
        "Musik dapat membantu mengaktifkan area otak yang terkait dengan memori",
        "Stres kronis dapat meningkatkan risiko penyakit Alzheimer"
    ]
    
    for i, fact in enumerate(facts, 1):
        st.markdown(f"""
        <div class="info-card">
            <p style="margin: 0; font-size: 1.1rem;"><strong style="color: #8A2BE2;">Fakta {i}:</strong> {fact}</p>
        </div>
        """, unsafe_allow_html=True)

    # Statistics
    st.markdown('<h3 class="subsection-header">Statistik Penyakit Alzheimer</h3>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-container">
            <h2>55M+</h2>
            <p>Penderita Worldwide</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-container">
            <h2>60-70%</h2>
            <p>Kasus Demensia</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-container">
            <h2>65+</h2>
            <p>Usia Risiko Tinggi</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-container">
            <h2>$1.1T</h2>
            <p>Biaya Global/Tahun</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Warning Signals
    st.markdown('<h3 class="subsection-header">⚠️ Tanda Peringatan Dini</h3>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-card">
        <h4 style="color: #6A0DAD; margin-bottom: 1rem;">Segera konsultasi dengan dokter jika mengalami:</h4>
        <ul style="line-height: 1.6;">
            <li>Kehilangan memori yang mengganggu aktivitas sehari-hari</li>
            <li>Kesulitan merencanakan atau menyelesaikan tugas yang familiar</li>
            <li>Kebingungan dengan waktu atau tempat</li>
            <li>Kesulitan memahami gambar visual dan hubungan spasial</li>
            <li>Masalah dengan kata-kata dalam berbicara atau menulis</li>
            <li>Menaruh barang di tempat yang salah dan kehilangan kemampuan untuk menelusuri kembali</li>
            <li>Penurunan atau penilaian yang buruk</li>
            <li>Menarik diri dari pekerjaan atau aktivitas sosial</li>
            <li>Perubahan mood dan kepribadian</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem;" class="footer-text">
    <p style="margin: 0; font-family: 'Poppins', sans-serif;">
        <strong>Alzheimer's Apps</strong> - Developed for early detection and awareness<br>
        <small>© 2025 Naufal Ramadhan | For educational and screening purposes only</small>
    </p>
</div>
""", unsafe_allow_html=True)