# 📈 Professional Trading Journal (Google Sheets)

Aplikasi jurnal trading interaktif yang menyimpan data ke Google Sheets.

## 🚀 Fitur
- Form input langsung dari dashboard
- Penyimpanan cloud (Google Sheets)
- Analisis otomatis: total trades, win rate, total PnL
- Tampilan profesional & siap deploy ke Streamlit Cloud

## 🧩 Cara Menjalankan

1. Siapkan file `google_credentials.json` dari Google Cloud Console
2. Upload ke Streamlit Cloud sebagai secret (via `secrets.toml` atau UI)
3. Deploy app ke Streamlit Cloud atau jalankan lokal:
```bash
streamlit run app/main.py
```