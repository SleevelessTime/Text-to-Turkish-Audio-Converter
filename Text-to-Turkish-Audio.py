############################################################################################
# Project: Text-to-Turkish-Audio Converter (PDF, DOCX, TXT to MP3)
# Author: Oğuzhan Cem Yücel
# Version: 1.0
# Date: 2025-05-08
# Description:
#   Converts written content (PDF, DOCX, TXT) into natural-sounding Turkish speech.
#   Features include duration estimation, progress feedback, and auto-naming.
############################################################################################

import sys
import os
import time
from gtts import gTTS
import PyPDF2
from docx import Document
from tqdm import tqdm
import mimetypes

def oku_pdf(dosya_yolu):
    metin = ""
    with open(dosya_yolu, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for sayfa in reader.pages:
            sayfa_metni = sayfa.extract_text()
            if sayfa_metni:
                metin += sayfa_metni + "\n"
    return metin

def oku_txt(dosya_yolu):
    with open(dosya_yolu, 'r', encoding='utf-8') as file:
        return file.read()

def oku_docx(dosya_yolu):
    doc = Document(dosya_yolu)
    metin = '\n'.join([p.text for p in doc.paragraphs])
    return metin

def metni_al(dosya_yolu):
    uzanti = os.path.splitext(dosya_yolu)[1].lower()
    if uzanti == '.pdf':
        return oku_pdf(dosya_yolu)
    elif uzanti == '.txt':
        return oku_txt(dosya_yolu)
    elif uzanti == '.docx':
        return oku_docx(dosya_yolu)
    else:
        raise ValueError(f"Desteklenmeyen dosya türü: {uzanti}")

def tahmini_sure(metin):
    kelime_sayisi = len(metin.split())
    dakika = kelime_sayisi / 81.1  # Ortalama 81 kelime/dk
    return round(dakika, 2)

def dosya_adi_olustur(giris_dosyasi):
    ad = os.path.splitext(os.path.basename(giris_dosyasi))[0]
    return ad + ".mp3"

def seslendir_ve_kaydet(metin, cikti_dosyasi):
    tts = gTTS(text=metin, lang='tr')
    tts.save(cikti_dosyasi)

def ilerleme_cubugu(sure_sn):
    for _ in tqdm(range(100), desc="Ses dosyası oluşturuluyor", ncols=70):
        time.sleep(sure_sn / 100)  # sembolik bekleme (istenirse kaldırılabilir)

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python dosya_seslendir.py <dosya_adı>")
        return

    dosya_yolu = sys.argv[1]

    if not os.path.exists(dosya_yolu):
        print(f"[!] Dosya bulunamadı: {dosya_yolu}")
        return

    try:
        print(f"[*] Dosya okunuyor: {dosya_yolu}")
        metin = metni_al(dosya_yolu)

        if not metin.strip():
            print("[!] Dosya boş veya içerik okunamadı.")
            return

        cikti_dosyasi = dosya_adi_olustur(dosya_yolu)
        sure = tahmini_sure(metin)

        print(f"[*] Tahmini ses süresi: {sure} dakika")
        print(f"[*] Türkçe seslendiriliyor ve '{cikti_dosyasi}' olarak kaydediliyor...")

        ilerleme_cubugu(sure * 1)

        seslendir_ve_kaydet(metin, cikti_dosyasi)

        print(f"[✓] MP3 başarıyla oluşturuldu: {cikti_dosyasi}")

    except Exception as e:
        print(f"[X] Hata oluştu: {str(e)}")

if __name__ == "__main__":
    main()
