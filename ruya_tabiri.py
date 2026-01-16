import streamlit as st
import google.generativeai as genai
import os

st.title("🔍 Model Dedektifi")

# 1. Kütüphane Versiyonunu Göster
try:
    st.write(f"📦 Yüklü Kütüphane Versiyonu: **{genai.__version__}**")
except:
    st.error("Kütüphane versiyonu okunamadı.")

# 2. Modelleri Listele
st.write("📋 **Sunucuda Kullanılabilir Modeller:**")

try:
    # Anahtarı çek
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Modelleri listele
    models = list(genai.list_models())
    
    found_any = False
    for m in models:
        # Sadece generateContent destekleyenleri gösterelim
        if 'generateContent' in m.supported_generation_methods:
            st.code(m.name) # Model ismini ekrana bas
            found_any = True
            
    if not found_any:
        st.warning("Hiçbir metin modeli bulunamadı. API Anahtarınız kısıtlı olabilir.")

except Exception as e:
    st.error(f"HATA OLUŞTU: {e}")
    st.info("Lütfen API Anahtarınızın 'Secrets' kısmında doğru kayıtlı olduğundan emin olun.")

