import streamlit as st
import pandas as pd
import joblib
import streamlit as st

st.title("Bilgisayar Fiyatı Tahmin Uygulaması")
ekran_boyutlari=pd.read_excel("C:\\Users\\Gözde\\Desktop\\data\\Ekran_Boyutu.xlsx")
isletim_sistemi=pd.read_excel("C:\\Users\\Gözde\\Desktop\\data\\Isletim_Sistemi.xlsx")
cozunurluk=pd.read_excel("C:\\Users\\Gözde\\Desktop\\data\\Cozunurluk.xlsx")

r2_ridge_model = joblib.load('C:\\Users\\Gözde\\r2_dt.pkl')



def ekran_boyutu_index(ekranlar):
    try:
        selected_row = ekran_boyutlari[ekran_boyutlari["Ekran_Boyutu"] == ekranlar].iloc[0]
        index = selected_row.name
        return index
    except IndexError:
        st.sidebar.error(f"{ekranlar} ekran boyutu bulunamadı!")
        return None

  


def isletim_sistemi_index(isletimler):
    try:
        selected_row = isletim_sistemi[isletim_sistemi["Isletim_Sistemi"] == isletimler].iloc[0]
        index = selected_row.name
        return index
    except IndexError:
        st.sidebar.error(f"{isletimler} işletim sistemi bulunamadı!")
        return None


def cozunurluk_index(cozunurlukler):
    try:
        selected_row = cozunurluk[cozunurluk["Cozunurluk"] == cozunurlukler].iloc[0]
        index = selected_row.name
        return index
    except IndexError:
        st.sidebar.error(f"{cozunurlukler} çözünürlük bulunamadı!")
        return None


ekran_Boyutu = ["küçük ekran", "orta ekran", "büyük ekran"]
Garanti_Suresi = ["1", "2","3"]
Ram = ["8", "32", "16", "4", "64", "128", "12", "48", "24", "36", "18", "1", "6", "2", "40"]
SSD_Kapasitesi = ["256", "512", "1", "0", "128", "240", "8", "500", "2", "64", "4", "32", "120", "480"]
isletim_Sistemi = ["Free Dos", "Windows", "Mac Os","Linux", "Ubuntu", "Windows 11","Android",
 "Chrome OS"]
Cozunurluk = ["1920 x 1080","3024 x 1964","2560 x 1600","1280 x 800","1366 x 768",
 "1920 x 1200","2880 x 1800","3840 x 2160","2160 x 1440","2880 x 1620",
 "4480 x 2520","3840 x 2400","2560 x 1440","2240 x 1400","1440 x 900",
 "2560 x 1664","2550 x 1600","1600 x 900","3072 x 1920","5120 x 2880",
 "1920 x 1280","2256 x 1504","4096 x 2160"]



st.sidebar.header("Girdiler")

ekran_Boyutu = st.sidebar.selectbox("Ekran Boyutu Seçiniz", ekran_Boyutu)
Garanti_Suresi = st.sidebar.selectbox("Garanti Süresi Seçiniz",Garanti_Suresi)
Ram= st.sidebar.selectbox("Ram Boyutu Seçiniz",Ram)
SSD_Kapasitesi = st.sidebar.selectbox("SSD Kapasitesi Seçiniz", SSD_Kapasitesi)
isletim_Sistemi = st.sidebar.selectbox("İşletim Sistemi Seçiniz", isletim_Sistemi)
Cozunurluk = st.sidebar.selectbox("Çözünürlük Seçiniz", Cozunurluk)


def create_prediction_value(ekranlar, garanti_suresi, ram_sistem_bellegi, ssd_kapasitesi, isletimler, cozunurlukler):
    res = pd.DataFrame(data={
        'Ekran_Boyutu': [ekranlar],
        'Garanti_Suresi': [garanti_suresi],
        'Ram_(Sistem Bellegi)': [ram_sistem_bellegi],
        'SSD_Kapasitesi': [ssd_kapasitesi],
        'Isletim_Sistemi': [isletimler],
        'Cozunurluk': [cozunurlukler]
    })
    return res

if st.sidebar.button("Bilgisayar Fiyatını Tahmin Et"):

    predict_value=create_prediction_value(ekran_boyutu_index(ekran_Boyutu),Garanti_Suresi,Ram,
               SSD_Kapasitesi, isletim_sistemi_index(isletim_Sistemi),cozunurluk_index(Cozunurluk))
    

    def predict_models(res):
        return "Ridge Result: "+str(int(r2_ridge_model.predict(res))).strip('[]')+" TL"
   
    

    st.header("Tahmin Edilen Fiyat")
    st.write(predict_models(predict_value))
   