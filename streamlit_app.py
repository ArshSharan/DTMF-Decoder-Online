 
# --- DTMF Frequencies ---
DTMF_FREQS = {
    (697, 1209): '1', (697, 1336): '2', (697, 1477): '3', (697, 1633): 'A',
    (770, 1209): '4', (770, 1336): '5', (770, 1477): '6', (770, 1633): 'B',
    (852, 1209): '7', (852, 1336): '8', (852, 1477): '9', (852, 1633): 'C',
    (941, 1209): '*', (941, 1336): '0', (941, 1477): '#', (941, 1633): 'D'
}

LOW_FREQS = [697, 770, 852, 941]
HIGH_FREQS = [1209, 1336, 1477, 1633]

# --- Helper: Map to closest DTMF frequency ---
def closest_freq(value, freq_list, tolerance=20):
    for freq in freq_list:
        if abs(freq - value) <= tolerance:
            return freq
    return None

# --- Page Config ---
st.set_page_config(
    page_title="DTMF DECODER",
    page_icon="🌌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- FUTURISTIC CSS (Next-Level) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;500;700&display=swap');

    :root {
        --primary: #00f0ff;
        --secondary: #ff00ff;
        --dark: #0a0a12;
        --light: #f0f0ff;
        --accent: #7b2dff;
    }

    html, body, [class*="css"] {
        font-family: 'Rajdhani', sans-serif;
        background-color: var(--dark);
        color: var(--light);
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Orbitron', sans-serif;
        color: var(--primary) !important;
        text-shadow: 0 0 15px rgba(0, 240, 255, 0.5);
        letter-spacing: 2px;
    }

    .stApp {
        background-color: var(--dark);
        background-image: radial-gradient(circle at 20% 30%, rgba(123, 45, 255, 0.08) 0%, transparent 30%),
                          radial-gradient(circle at 80% 70%, rgba(0, 240, 255, 0.08) 0%, transparent 30%);
        overflow: hidden;
    }

    /* 🔥 REMOVE all glow effects on hover */
    button, .stButton>button, .stFileUploader>div>div, .stCheckbox>div>div, input, textarea, select {
        outline: none !important;
        box-shadow: none !important;
        transition: none !important;
    }

    /* Button styling */
    .stButton>button {
        border: 2px solid var(--primary) !important;
        background: rgba(10, 10, 20, 0.5) !important;
        color: var(--primary) !important;
        font-family: 'Orbitron', sans-serif !important;
        font-weight: bold !important;
        border-radius: 6px !important;
    }

    /* File uploader */
    .stFileUploader>div>div {
        border: 2px dashed var(--primary) !important;
        background: rgba(10, 10, 20, 0.5) !important;
        color: var(--primary) !important;
        border-radius: 8px !important;
    }

    /* Checkbox and others */
    .stCheckbox>div>div {
        border: 2px solid var(--primary) !important;
        background: rgba(10, 10, 20, 0.5) !important;
    }

    /* Error/success blocks */
    .stSuccess {
        background: rgba(0, 240, 255, 0.08) !important;
        border-left: 4px solid var(--primary) !important;
        border-radius: 0 8px 8px 0 !important;
    }

    .stError {
        background: rgba(255, 0, 100, 0.08) !important;
        border-left: 4px solid #ff0064 !important;
        border-radius: 0 8px 8px 0 !important;
    }

    /* Cyber-terminal block */
    .cyber-terminal {
        background: rgba(0, 0, 0, 0.7);
        border: 1px solid var(--primary);
        border-radius: 8px;
        padding: 20px;
        font-family: 'Courier New', monospace;
        color: var(--primary);
    }

    .ascii-art {
        font-family: 'Courier New', monospace;
        color: var(--primary);
        white-space: pre;
        line-height: 1.2;
    }
    
    *:focus, *:active {
        outline: none !important;
        box-shadow: none !important;
    }

</style>


<script>
// Create floating particles
document.addEventListener('DOMContentLoaded', () => {
    for (let i = 0; i < 30; i++) {
        const particle = document.createElement('div');
        particle.classList.add('particle');
        
        // Random size and position
        const size = Math.random() * 5 + 2;
        particle.style.width = `${size}px`;
        particle.style.height = `${size}px`;
        particle.style.left = `${Math.random() * 100}vw`;
        particle.style.top = `${Math.random() * 100}vh`;
        
        // Random animation delay
        particle.style.animationDelay = `${Math.random() * 15}s`;
        
        document.body.appendChild(particle);
    }
});
</script>
""", unsafe_allow_html=True)

# --- ASCII ART HEADER ---
ascii_art = r"""
   ________  ______  __________ _    ____________  _____ ______
  / ____/\ \/ / __ )/ ____/ __ \ |  / / ____/ __ \/ ___// ____/
 / /      \  / __  / __/ / /_/ / | / / __/ / /_/ /\__ \/ __/   
/ /___    / / /_/ / /___/ _, _/| |/ / /___/ _, _/___/ / /___   
\____/   /_/_____/_____/_/ |_| |___/_____/_/ |_|/____/_____/   

"""

# --- MAIN UI ---
st.markdown(f"""
<div style="text-align: center; margin-bottom: 30px;">
    <div class="ascii-art" style="color: var(--primary); font-size: 10px; opacity: 0.8;">{ascii_art}</div>
    <h1 class="glow" style="margin-top: -10px; font-size: 3em;">DTMF DECODER</h1>
    <p style="color: var(--light); letter-spacing: 2px;">DTMF AUDIO FREQUENCY ANALYSIS</p>
    <div style="height: 2px; background: linear-gradient(90deg, transparent, var(--primary), transparent); margin: 10px auto; width: 50%;"></div>
</div>
""", unsafe_allow_html=True)

# --- FILE UPLOADER (Futuristic) ---
with stylable_container(
    key="uploader",
    css_styles="""
        {
            border: 2px dashed var(--primary);
            border-radius: 8px;
            padding: 40px;
            text-align: center;
            background: rgba(10, 10, 20, 0.5);
            margin-bottom: 30px;
            transition: all 0.3s ease;
        }
    """,
):
    uploaded_file = st.file_uploader("UPLOAD WAV FILE", type=["wav"], label_visibility="collapsed")

# --- PROCESSING ---
if uploaded_file:
    with st.spinner('DECRYPTING SIGNAL...'):
        # Simulate processing delay for dramatic effect
        time.sleep(1.5)
        
        rate, data = wav.read(uploaded_file)
        
        # Stereo to mono
        if len(data.shape) == 2:
            data = data.mean(axis=1)
        
        # Display file info in a sleek card
        with stylable_container(
            key="file_info",
            css_styles="""
                {
                    border-left: 4px solid var(--primary);
                    padding: 15px 20px;
                    background: rgba(0, 0, 0, 0.5);
                    margin-bottom: 20px;
                    border-radius: 0 8px 8px 0;
                }
            """,
        ):
            st.success(f"**SAMPLE RATE:** `{rate} Hz` | **DURATION:** `{len(data) / rate:.2f} sec`")
        
        window_size = int(rate * 0.05)  # 50ms
        step_size = int(window_size * 0.5)
        
        decoded_sequence = ""
        last_key = None
        
        for i in range(0, len(data) - window_size, step_size):
            segment = data[i:i+window_size] * np.hamming(window_size)
            spectrum = np.abs(fft(segment))
            freqs = np.fft.fftfreq(len(segment), 1 / rate)
            
            # Keep only positive frequencies
            mask = freqs > 0
            freqs = freqs[mask]
            spectrum = spectrum[mask]
            
            # Get 2 dominant frequencies
            peak_indices = spectrum.argsort()[-2:]
            dom_freqs = sorted([round(freqs[idx]) for idx in peak_indices])
            
            low = closest_freq(dom_freqs[0], LOW_FREQS)
            high = closest_freq(dom_freqs[1], HIGH_FREQS)
            
            if low and high:
                key = DTMF_FREQS.get((low, high))
                if key and key != last_key:
                    decoded_sequence += key
                    last_key = key
    
    # --- RESULTS (Terminal-Style) ---
    if decoded_sequence:
        st.markdown("""
        <div style="margin: 30px 0;">
            <h3 style="color: var(--secondary); text-align: center;">DECRYPTED SEQUENCE</h3>
            <div class="cyber-terminal" style="font-size: 24px; text-align: center; padding: 30px;">
                <span style="color: var(--secondary);">>> </span>
                <span style="color: var(--primary); font-weight: bold;">{0}</span>
            </div>
        </div>
        """.format(decoded_sequence), unsafe_allow_html=True)
    else:
        st.error("DECODING FAILED. ENSURE CLEAR DTMF TONES ARE PRESENT.")
    
    # --- 3D SPECTRUM VISUALIZATION ---
    if st.checkbox("SHOW FREQUENCY SPECTRUM", value=False):
        full_spectrum = np.abs(fft(data))
        freqs = np.fft.fftfreq(len(data), 1 / rate)
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(freqs[:len(freqs)//2], full_spectrum[:len(freqs)//2], 
                color='#00f0ff', linewidth=1.5, alpha=0.8)
        
        # Fill under curve for hologram effect
        ax.fill_between(freqs[:len(freqs)//2], full_spectrum[:len(freqs)//2], 
                       color='#00f0ff', alpha=0.1)
        
        ax.set_title("FREQUENCY SPECTRUM ANALYSIS", color='#00f0ff', pad=20, fontsize=14, fontweight='bold')
        ax.set_xlabel("FREQUENCY (Hz)", color='#00f0ff', fontsize=12)
        ax.set_ylabel("AMPLITUDE", color='#00f0ff', fontsize=12)
        
        ax.set_facecolor('#0a0a12')
        fig.patch.set_facecolor('#0a0a12')
        ax.tick_params(colors='#00f0ff')
        
        # Grid styling
        ax.grid(color='#00f0ff', alpha=0.1, linestyle='--')
        
        # Glow effect on lines
        for spine in ax.spines.values():
            spine.set_edgecolor('#00f0ff')
            spine.set_alpha(0.5)
        
        st.pyplot(fig)

# --- FOOTER (Cyberpunk Style) ---
st.markdown("""
<div style="text-align: center; margin-top: 50px; color: var(--light); font-size: 0.8em; opacity: 0.7;">
    <div style="height: 1px; background: linear-gradient(90deg, transparent, var(--primary), transparent); margin: 20px auto; width: 30%;"></div>
    NEURAL DECODER v3.0 | [SYSTEM: ONLINE] | [CPU: 87%] | [MEM: 64%]
</div>
""", unsafe_allow_html=True)