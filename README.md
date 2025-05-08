# Text-to-Turkish-Audio Converter

This project converts written content from files (PDF, DOCX, TXT) into natural-sounding Turkish speech. It estimates the duration of the audio, provides progress feedback, and automatically generates an output filename for the MP3 audio.

---

## Features
- **Supported Input Formats**: PDF, DOCX, TXT.
- **Natural Turkish Speech**: Converts text to speech using `gTTS` (Google Text-to-Speech) in Turkish.
- **Progress Bar**: Displays conversion progress with an interactive progress bar.
- **Estimated Duration**: Calculates and displays the approximate duration of the generated audio.
- **Auto-Generated Output Name**: Automatically names the output MP3 file based on the input file name.

---

## Requirements

Install the following Python packages before running the script:

```bash
pip install gtts PyPDF2 python-docx tqdm
```

---

## Usage

Run the script from the command line with the path to the input file as an argument:

```bash
python dosya_seslendir.py <dosya_adı>
```

### Example:
```bash
python dosya_seslendir.py metin.pdf
```

---

## How It Works

1. **Input File Validation**: The script checks if the file exists and whether its format is supported.
2. **Text Extraction**:
   - PDF: Extracts text from PDF pages using `PyPDF2`.
   - DOCX: Extracts text from Word documents using `python-docx`.
   - TXT: Reads plain text files.
3. **Text-to-Speech Conversion**: Converts the extracted text into Turkish speech using `gTTS`.
4. **Progress Feedback**: Displays a progress bar while generating the audio file.
5. **Output**: Saves the generated audio as an MP3 file with an auto-generated name (based on input file name).

---

## Output Example

For an input file named `metin.pdf`, the script will generate:

- `metin.mp3`

---

## Functions

### `oku_pdf(dosya_yolu)`
- Reads and extracts text from a PDF file.

### `oku_txt(dosya_yolu)`
- Reads content from a plain text file.

### `oku_docx(dosya_yolu)`
- Reads and extracts text from a DOCX file.

### `metni_al(dosya_yolu)`
- Detects the file type and extracts text accordingly.

### `tahmini_sure(metin)`
- Estimates the duration of the audio in minutes based on an average reading speed of 81 words per minute.

### `dosya_adi_olustur(giris_dosyasi)`
- Generates an output filename by appending `.mp3` to the input file's name.

### `seslendir_ve_kaydet(metin, cikti_dosyasi)`
- Converts text to Turkish speech and saves it as an MP3 file.

### `ilerleme_cubugu(sure_sn)`
- Displays a progress bar during the audio generation process.

---

## Error Handling

- **File Not Found**: Displays an error message if the input file does not exist.
- **Unsupported File Type**: Displays an error message if the file type is not PDF, DOCX, or TXT.
- **Empty or Unreadable Content**: Handles cases where the input file has no readable content.
- **General Exceptions**: Catches and displays any other errors encountered during execution.

---

## Example Output

```bash
[*] Dosya okunuyor: metin.pdf
[*] Tahmini ses süresi: 2.45 dakika
[*] Türkçe seslendiriliyor ve 'metin.mp3' olarak kaydediliyor...
Ses dosyası oluşturuluyor: 100%|█████████████████████████████████████████| 100/100 [00:02<00:00, 39.20it/s]
[✓] MP3 başarıyla oluşturuldu: metin.mp3
```

---

## Notes

- The average reading speed is taken as **81 words per minute** for Turkish.
- Progress bar delay is symbolic and can be adjusted or removed in the `ilerleme_cubugu` function.

---

## Author

- **Oğuzhan Cem Yücel**
- **Version**: 1.0
- **Date**: 2025-05-08
