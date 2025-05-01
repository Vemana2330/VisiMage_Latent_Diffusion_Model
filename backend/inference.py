import torch
from diffusers import StableDiffusionPipeline, UNet2DConditionModel
from safetensors.torch import load_file
import os

# === Paths ===
MODEL_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "model"))
GENERATED_DIR = os.path.join(os.path.dirname(__file__), "generated")
os.makedirs(GENERATED_DIR, exist_ok=True)

# === Load base pipeline (with default tokenizer and text encoder) ===
pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1-base",
    safety_checker=None,
    torch_dtype=torch.float32,
    local_files_only=False
).to("cpu")  # Change to "cuda" if using GPU

# === Load fine-tuned UNet ===
unet = UNet2DConditionModel.from_config(MODEL_DIR)  
unet.load_state_dict(load_file(os.path.join(MODEL_DIR, "diffusion_pytorch_model.safetensors")))
pipe.unet = unet.to("cpu")  # Change to "cuda" if using GPU

# === Generation Function ===
def generate_image(prompt: str, steps: int = 50, scale: float = 8.0) -> str:
    result = pipe(prompt, num_inference_steps=steps, guidance_scale=scale)
    image = result.images[0]

    # Format filename and save
    safe_prompt = prompt.replace(" ", "_").replace(",", "").replace(".", "")[:50]
    filename = f"{safe_prompt}_{steps}_{scale}.png"
    save_path = os.path.join(GENERATED_DIR, filename)
    image.save(save_path)

    return save_path
