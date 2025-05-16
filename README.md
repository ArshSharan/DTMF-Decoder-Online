# DTMF Tone Analyzer

A futuristic, hacker-themed web app that decodes **DTMF (Dual-Tone Multi-Frequency)** signals from `.wav` audio files using signal processing techniques in Python. This project is built using **Streamlit** and designed to be both educational and visually captivating.


##  What is DTMF?

DTMF (Dual-Tone Multi-Frequency) is the signal generated when you press the keys on a telephone keypad. Each key generates a unique combination of two frequencies: one from a **low-frequency group** and one from a **high-frequency group**.

For example:
- Pressing "5" emits tones at **770 Hz and 1336 Hz**.
- Pressing "#" emits tones at **941 Hz and 1477 Hz**.

This app identifies those frequency pairs and decodes the digits or symbols pressed.


## ✨ Features

- 🎧 **Upload `.wav` Files**  
  Upload any `.wav` file containing DTMF tones.

- ⚙️ **Accurate Signal Decoding**  
  Uses **Fast Fourier Transform (FFT)** to extract and decode tone frequencies.

- 📟 **Terminal-Style Output**  
  Decrypted tone sequence is displayed in a custom-styled cyber-terminal.

- 📊 **Optional Spectrum Analysis**  
  Visualize the full frequency spectrum of the audio signal.

- 🎨 **Hacker-Themed UI**  
  Styled with neon aesthetics, Orbitron fonts, and futuristic gradients.


##  How It Works (Beginner Friendly)

1. The app reads the uploaded `.wav` file using `scipy.io.wavfile`.
2. It slices the audio into short 50ms segments.
3. Each segment is windowed with a **Hamming function** to reduce spectral leakage.
4. It performs **FFT (Fast Fourier Transform)** on each segment to extract frequency components.
5. It identifies the two **strongest frequency peaks** and maps them to the nearest DTMF pair.
6. If the pair matches a valid DTMF combination, the corresponding key (like `5`, `#`, `A`) is appended to the output.

---

## Educational Tip

Want to explore further? Try:
- [ ] Recording your own DTMF tones with a mobile dial pad.

- [ ] Adjusting the FFT window size for better time resolution.

- [ ] Exploring noise filtering or spectrograms.
