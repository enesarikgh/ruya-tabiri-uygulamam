import streamlit as st
import google.generativeai as genai

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="İslami Rüya Tabiri ve Rehberi",
    page_icon="🌙",
    layout="centered"
)

# --- KENAR ÇUBUĞU (API KEY GİRİŞİ) ---
with st.sidebar:
    st.header("⚙️ Ayarlar")
    st.info("Bu uygulama Google Gemini AI altyapısını kullanır.")
    api_key = st.text_input("Google API Anahtarınızı Buraya Girin:", type="password")
    st.markdown("---")
    st.markdown("""
    ### 📌 Rüya Adabı
    * **Güzel rüya:** Allah'tandır, hamd edilir ve sevilene anlatılır.
    * **Kötü rüya:** Şeytandandır, Allah'a sığınılır ve kimseye anlatılmaz.
    """)

# --- ANA BAŞLIK VE GİRİŞ ---
st.title("🌙 İslami Rüya Rehberi")
st.write("""
Hoşgeldiniz. Bu platform, rüyalarınızı **İslami hassasiyetlere** ve **sahih kaynaklara** göre analiz eder.
Lütfen rüyanızı aşağıya yazın. Sistemimiz rüyanın türünü (Rahmani, Şeytani veya Bilinçaltı) tespit edip size rehberlik edecektir.
""")

# --- SİSTEM TALİMATI (SENİN HAZIRLADIĞIN ZEKA) ---
system_instruction = """
GÖREVİN:
Sen İslami hassasiyetlere sahip, güvenilir bir Rüya Rehberi ve Eğitmenisin.

KURALLAR:
1. RAHMANİ (SADIK) RÜYALAR: Allah'tan gelen müjdelerdir. Hayra yor, sembolleri açıkla, ümit ver.
2. ŞEYTANİ VE KORKUNÇ RÜYALAR: ASLA YORUMLAMA. Kullanıcıya "Bu rüya şeytani veya psikolojik kökenli görünüyor. Peygamber Efendimiz'in tavsiyesi üzerine bu tür rüyalar anlatılmaz ve yorumlanmaz. Allah'a sığın ve unut" de.
3. NEFSANİ (BİLİNÇALTI): Günlük olayların yansımasıdır. Yorumlanmaz, kullanıcının kafasına takmamasını söyle.

ÜSLUP:
- Besmele veya selam ile başla.
- Asla kesin konuşma, "Allah en doğrusunu bilir" de.
- Nazik, eğitici ve ferahlatıcı ol.
"""

# --- KULLANICI ARAYÜZÜ ---
user_dream = st.text_area("Rüyanızı detaylıca anlatın:", height=150, placeholder="Örn: Rüyamda yemyeşil bir bahçede...")

if st.button("Rüyamı Yorumla"):
    if not api_key:
        st.error("Lütfen önce sol taraftan Google API Anahtarınızı giriniz.")
    elif not user_dream:
        st.warning("Lütfen bir rüya yazınız.")
    else:
        try:
            # Yapay Zeka Ayarları
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                system_instruction=system_instruction
            )
            
            with st.spinner("Rüyanız İslami kaynaklara göre analiz ediliyor..."):
                response = model.generate_content(user_dream)
                
            # Sonucu Göster
            st.success("Analiz Tamamlandı")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")
            st.info("Lütfen API anahtarınızın doğru olduğundan emin olun.")

# --- ALT BİLGİ ---
st.markdown("---")
st.caption("⚠️ Uyarı: Bu sistem yapay zeka desteklidir. Rüyalar gaybın kesin habercisi değildir. En doğrusunu Allah bilir.")