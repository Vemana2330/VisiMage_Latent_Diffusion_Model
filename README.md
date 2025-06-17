# VisiMage_Latent_Diffusion_Model

## Technologies Used

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![Stable Diffusion](https://img.shields.io/badge/Stable_Diffusion_v2.1-FFBF00?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/CompVis/stable-diffusion-v-2-1)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFBF00?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/datasets/lambdalabs/naruto-blip-captions)
[![VAE](https://img.shields.io/badge/VAE_Encoder--Decoder-4CAF50?style=for-the-badge&logo=autodesk&logoColor=white)](https://arxiv.org/abs/1312.6114)
[![U-Net](https://img.shields.io/badge/U--Net-4B8BBE?style=for-the-badge&logo=tensorflow&logoColor=white)](https://arxiv.org/abs/1505.04597)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pillow](https://img.shields.io/badge/Pillow-316192?style=for-the-badge&logo=python&logoColor=white)](https://python-pillow.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-000000?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![VS Code](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/)

## Overview

VisiMage is a full-stack generative AI system that transforms natural language prompts into high-quality anime-style images using a fine-tuned Stable Diffusion model. By training only the U-Net component on a Naruto-themed image-caption dataset and integrating Streamlit and FastAPI, the system delivers an interactive and customizable text-to-image experience.

## Problem Statement

While generative AI models like Stable Diffusion can create stunning visuals, adapting them to specific artistic styles requires significant computational resources and complex tuning. Most existing systems lack fine-grained control and style personalization, limiting creative expression for users who want tailored outputs from minimal textual input.

## Dataset

- Name: [Naruto BLIP-Captions Dataset](https://huggingface.co/datasets/lambdalabs/naruto-blip-captions)
- Source: LambdaLabs via Hugging Face
- Size: 4,965 image–caption pairs
- Format:
  - image: Naruto-style anime image
  - caption: Auto-generated using BLIP (Bootstrapped Language-Image Pretraining)
- The dataset was used to fine-tune the U-Net module of Stable Diffusion, enabling the generation of anime-style images conditioned on natural language prompts.
 
## Project Goals
- Develop a full-stack generative AI system for text-to-image synthesis using Stable Diffusion
- Fine-tune only the U-Net component on a custom Naruto-style dataset while keeping CLIP and VAE encoders frozen
- Design a modular architecture with separate frontend (Streamlit) and backend (FastAPI) layers
- Provide user control over inference parameters such as guidance scale and number of steps
- Enable prompt-based generation of high-quality, stylized images in real-time through a web interface
- Demonstrate the creative potential of domain-specific fine-tuning in diffusion-based models

## Architecture Diagram
<img width="612" alt="image" src="https://github.com/user-attachments/assets/f34b4aef-aa20-4846-998b-038a56f26259" />

## Application UI
![Visimage_Project](https://github.com/user-attachments/assets/92aba796-a3b8-4bf6-90d6-fd2bae85fad3)


## Outputs

| Bill Gates with a Hoodie | Six Women in a Spacecraft |
| :-: | :-: |
| <img src="https://github.com/user-attachments/assets/476c34ae-230a-4fa0-9239-e1c8912b1218" width="500" height="300"/> | <img src="https://github.com/user-attachments/assets/d902461b-9ca3-4c72-9819-cae773edd3c1" width="500" height="300"/> |

| A Cat Wears a Yellow Hat | A Girl Wears Red Skirt |
| :-: | :-: |
| <img src="https://github.com/user-attachments/assets/de5676ea-0e3b-4a1b-8a73-ff2146986b9e" width="500" height="300"/> | <img src="https://github.com/user-attachments/assets/a76f427b-a6ba-418e-828f-2919f3e4d9f2" width="500" height="300"/> |


## Directory Structure
```
VisiMage/
├── backend/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── inference.py              # Inference logic for Stable Diffusion
│   ├── main.py                   # FastAPI backend entry point
│   ├── PromptRequest.py          # Pydantic model for request validation
│   └── generated/                # Folder to save generated output images
├── frontend/
│   ├── __pycache__/
│   ├── .streamlit/
│   │   └── config.toml           # Streamlit UI configuration
│   ├── app.py                    # Streamlit web UI
│   ├── assets/                   # Contains static assets and logo
│   └── generated_images/         # Stores displayed images for UI
├── model/
│   └── diffusion_pytorch_model.safetensors  # Fine-tuned U-Net weights
├── diffusion_clean.ipynb         # Notebook used for fine-tuning
├── requirements.txt              # Required Python packages
└── README.md                     # Project documentation
```

## Fine Tuning

The Stable Diffusion v2.1 model was fine-tuned using the Naruto BLIP-captioned dataset to specialize the model for anime-style image generation. During training:
- Only the U-Net component was updated; both the CLIP encoder and VAE modules were kept frozen to preserve generalization and reduce computational cost.
- Training was performed for 80 epochs using the AdamW optimizer and Mean Squared Error (MSE) loss.
- Captions were embedded via CLIP and used to condition the U-Net in denoising noisy image latents.
- The result is a stylized diffusion model capable of generating high-fidelity Naruto-themed visuals from natural language prompts.

## Application Workflow

1. **Landing Page:** Displays the logo, system overview, usage instructions, and example outputs.
2. **Prompt Input:** User enters a text prompt and selects parameters: inference steps and guidance scale.
3. **Request Submission:** Frontend sends the prompt and parameters to the backend via POST request.
4. **Image Generation:** Backend uses the fine-tuned U-Net model to generate an image based on the prompt.
5. **Image Storage:** Generated image is saved in the generated/ folder.
6. **Image Display:** Image is served via FastAPI static route and displayed in the frontend.
7. **Prompt Iteration:** User can modify the prompt or parameters and generate new images.

## Prerequisites

- Python: Version 3.8 or higher must be installed.
- API Keys: Add required keys to .env files.
- Hugging Face Account.
- Basic Knowledge:
  - Stable Diffusion architecture and U-Net fine-tuning
  - Streamlit for UI modification
  - FastAPI for backend routing and inference handling
  - PyTorch for model loading and inference
 
## How to run this Application Locally

1. Clone the Repository
```
git clone https://github.com/Vemana2330/VisiMage_Latent_Diffusion_Model.git
cd VisiMage_Latent_Diffusion_Model
```
2.Authenticate with Hugging Face Token in Notebook (Before Fine-Tuning):
```
from huggingface_hub import login
from getpass import getpass

# Prompt for Hugging Face token securely
hf_token = getpass("Enter your Hugging Face token: ")

# Login to Hugging Face
if hf_token:
    login(token=hf_token)
else:
    print("No token entered. Please try again.")
```
3. Create and Activate a Virtual Environment
```
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
4. Install Required Packages
```
pip install -r backend/requirements.txt
pip install -r frontend/requirements.txt
```
5. Start FastApi Backend
```
cd backend
uvicorn main:app --reload --port 8000
```
5. Start Streamlit Frontend
```
cd frontend
streamlit run app.py --server.port 8501
```
6. Access the Application
  - Frontend (Streamlit): http://localhost:8501
  - Backend (FastAPI Docs): http://localhost:8000/docs
7. Generate an Image
  - Enter a text prompt on the Streamlit UI like "Bill Gates with a hoodie"
  - Adjust parameters like guidance scale and inference steps.
  - Submit the prompt to view the generated image.

## References

- [Stable Diffusion v2.1 – Hugging Face](https://huggingface.co/stabilityai/stable-diffusion-2-1)  
- [Naruto BLIP-Captions Dataset – Hugging Face](https://huggingface.co/datasets/lambdalabs/naruto-blip-captions)  
- [CLIP Model – OpenAI](https://github.com/openai/CLIP)  
- [BLIP: Bootstrapping Language-Image Pretraining](https://github.com/salesforce/BLIP)  
- [U-Net Architecture](https://arxiv.org/abs/1505.04597)  
- [Variational Autoencoder (VAE)](https://arxiv.org/abs/1312.6114)  
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [FastAPI Documentation](https://fastapi.tiangolo.com/)  
- [PyTorch Documentation](https://pytorch.org/docs/)  
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)  
- [Google Colab](https://colab.research.google.com/)  
- [Docker Documentation](https://docs.docker.com/)  
