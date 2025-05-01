import streamlit as st
from PIL import Image
import requests
import os

# === Streamlit Page Setup ===
st.set_page_config(
    page_title="VisiMage",
    layout="wide",
    page_icon="🧠",
    initial_sidebar_state="collapsed"
)

# === Sidebar Navigation ===
page = st.sidebar.radio("Go to", ["🏠 Home", "🎨 Generate Image"])

# === Landing Page ===
if page == "🏠 Home":
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Centered Logo
    logo = Image.open("Images/Logo/VisiMage_Logo.png")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        st.image(logo, use_container_width=True)

    # Headline
    st.markdown(
        """
        <h1 style='text-align: center; font-size: 3.5rem; font-weight: bold;'>Turn text to <span style='color:#3b82f6;'>image</span>, in seconds.</h1>
        <p style='text-align: center; font-size: 1.25rem; color: gray;'>
            Unleash your creativity with AI — just describe your vision, and let the magic happen.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # How It Works
    st.markdown("""
    <h3 style='font-size: 1.75rem;'>🔍 How It Works</h3>
    <ol style='font-size: 1.15rem; line-height: 1.8;'>
      <li><strong>Describe Your Vision:</strong> Type a prompt (e.g., <em>"Masked ninja in Hidden Leaf Village attire"</em>)</li>
      <li><strong>Watch the Magic:</strong> Our AI model converts your prompt into an image</li>
      <li><strong>Download & Share:</strong> Save or share your artwork instantly</li>
    </ol>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Examples
    st.markdown("### ✨ Generated Examples")
    examples_dir = "Images/Generated_Images_VisiMage"
    example_files = sorted([f for f in os.listdir(examples_dir) if f.endswith(".png")])[:5]

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            image_path = os.path.join(examples_dir, example_files[idx])
            st.image(image_path, caption=f"Ex{idx+1}", use_container_width=True)

# === Generate Image Page ===
elif page == "🎨 Generate Image":
    st.title("🎨 Generate Image")

    st.markdown("Fill out the details below to generate a unique image using AI:")

    # Input Form
    with st.form("image_form"):
        prompt = st.text_input("Prompt", placeholder="e.g., a futuristic city skyline at night")
        steps = st.slider("Steps", min_value=10, max_value=100, value=50)
        scale = st.slider("Scale", min_value=1.0, max_value=20.0, value=7.5)
        submitted = st.form_submit_button("Generate")

    # Submit to FastAPI
    if submitted:
        if prompt.strip() == "":
            st.warning("⚠️ Please enter a prompt.")
        else:
            with st.spinner("Generating image... ⏳"):
                try:
                    response = requests.post(
                        "http://localhost:8000/generate",
                        json={"prompt": prompt, "steps": steps, "scale": scale}
                    )
                    data = response.json()

                    if "url" in data:
                        st.success("✅ Image generated!")
                        image_url = f"http://localhost:8000{data['url']}"
                        st.image(image_url, width=512)
                        st.markdown(f"[📥 Download Image]({image_url})", unsafe_allow_html=True)
                    else:
                        st.error("❌ Failed to generate image.")
                except Exception as e:
                    st.error(f"🚨 Error: {e}")
