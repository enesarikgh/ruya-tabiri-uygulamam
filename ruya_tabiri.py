import streamlit as st
import google.generativeai as genai
import os

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="İslami Rüya Tabiri ve Rehberi",
    page_icon="🌙",
    layout="centered"
)

# --- GİZLİ ANAHTARI ALMA ---
try:
    # Senin 'Secrets' kısmına kaydettiğin şifreyi çeker
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("Sistem hatası: API Anahtarı bulunamadı. Lütfen site sahibiyle iletişime geçin.")
    st.stop()

# --- KENAR ÇUBUĞU ---
with st.sidebar:
    st.header("🌙 Hakkımızda")
    st.info("Bu yapay zeka asistanı, İslami kaynakları tarayarak rüyalarınızı analiz eder.")
    st.markdown("---")
    st.markdown("""
    ### 📌 Bilmeniz Gerekenler
    * **Rahmani Rüya:** Müjdedir, anlatılır.
    * **Şeytani Rüya:** Korkutucudur, anlatılmaz.
    * **Nefsani Rüya:** Bilinçaltıdır, yorumlanmaz.
    """)

# --- ANA EKRAN ---
st.title("🌙 İslami Rüya Rehberi")
st.write("Rüyanızı aşağıya yazın, Rahmani mi yoksa Şeytani mi olduğunu ve manasını öğrenin.")

# --- YAPAY ZEKA TALİMATI ---
system_instruction = """
GÖREVİN:
Sen İslami hassasiyetlere sahip, güvenilir bir Rüya Rehberi ve Eğitmenisin.

KURALLAR:
1. RAHMANİ (SADIK) RÜYALAR: Allah'tan gelen müjdelerdir. Hayra yor, sembolleri açıkla, ümit ver.
2. ŞEYTANİ VE KORKUNÇ RÜYALAR: ASLA YORUMLAMA. Kullanıcıya "Bu rüya şeytani veya psikolojik kökenli görünüyor. Peygamber Efendimiz'in tavsiyesi üzerine bu tür rüyalar anlatılmaz ve yorumlanmaz. Allah'a sığın ve unut" de.
3. NEFSANİ (BİLİNÇALTI): Günlük olayların yansımasıdır. Yorumlanmaz.

ÜSLUP:
- Besmele veya selam ile başla.
- Asla kesin konuşma, "Allah en doğrusunu bilir" de.
- Nazik, eğitici ve ferahlatıcı ol.
"""

# --- KULLANICI GİRİŞİ ---
user_dream = st.text_area("Rüyanızı buraya yazın:", height=150, placeholder="Örn: Rüyamda temiz bir suda yüzdüğümü gördüm...")

if st.button("Rüyamı Yorumla"):
    if not user_dream:
        st.warning("Lütfen boş bırakmayınız, rüyanızı yazınız.")
    else:
        try:
            # LİSTEDE GÖRDÜĞÜMÜZ MODELİ KULLANIYORUZ:
            model = genai.GenerativeModel(
               model_name="gemini-flash-latest",
                system_instruction=system_instruction
            )
            
            with st.spinner("Rüyanız İslami kaynaklara göre taranıyor..."):
                response = model.generate_content(user_dream)
                
            st.success("Yorum Hazır:")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")


