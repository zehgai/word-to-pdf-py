import os
from docx2pdf import convert

def convert_word_to_pdf():
    input_file = input("Word dosyası adı (örn: belge.docx): ")
    
    if not os.path.exists(input_file):
        print("❌ Dosya bulunamadı!")
        return

    # Çıktı ismini otomatik oluştur (belge.docx -> belge.pdf)
    output_file = input_file.replace(".docx", ".pdf")

    try:
        print("🔄 Dönüştürülüyor...")
        convert(input_file, output_file)
        print(f"✅ Tamamlandı: {output_file}")
    except Exception as e:
        print(f"⚠️ Hata: {e}")

if __name__ == "__main__":
    convert_word_to_pdf()
