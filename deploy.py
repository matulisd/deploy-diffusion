import os
from huggingface_hub import hf_hub_download
import gdown
from pathlib import Path

COMFYUI_CLIP_DIR = "/workspace/ComfyUI/models/clip"
COMFYUI_UNET_DIR = "/workspace/ComfyUI/models/unet"
COMFYUI_CHECKPOINT_DIR = "/workspace/ComfyUI/models/checkpoints"

SD35_MEDIUM_HF = "stabilityai/stable-diffusion-3.5-medium"

SD35_MEDIUM_FILENAME = "sd3.5_medium.safetensors"
CLIP_G_FILENAME = "clip_g.safetensors"
CLIP_L_FILENAME = "clip_l.safetensors"
T5XXL_FP16_FILENAME = "t5xxl_fp16.safetensors"



LUSIS_476_ID = "15WNb__YiUVIH7DunjnHvPqqNiVpjzOa_"
LUSIS_272_ID = "121YHKoL8BJtVN54730vkNtm3YnKqfM_d"

def download_from_gdrive(file_id, dest_path):
    gdown.download(f"https://drive.google.com/uc?id={file_id}", str(dest_path), quiet=False)

def download_from_huggingface(repo_id, filename, dest_path):
    downloaded = hf_hub_download(repo_id=repo_id, filename=filename)
    Path(dest_path).parent.mkdir(parents=True, exist_ok=True)
    os.rename(downloaded, dest_path)

def main():
    print("Setting up Stable Diffusion..")

    download_from_huggingface(SD35_MEDIUM_HF, SD35_MEDIUM_FILENAME, COMFYUI_CHECKPOINT_DIR)
    
    print("Downloading text encoders:")
    print(f"Downloading {CLIP_G_FILENAME}")
    download_from_huggingface(SD35_MEDIUM_HF, CLIP_G_FILENAME, COMFYUI_CLIP_DIR)
    print(f"Downloading {CLIP_L_FILENAME}")
    download_from_huggingface(SD35_MEDIUM_HF, CLIP_L_FILENAME, COMFYUI_CLIP_DIR)
    print(f"Downloading {T5XXL_FP16_FILENAME}")
    download_from_huggingface(SD35_MEDIUM_HF, T5XXL_FP16_FILENAME, COMFYUI_CLIP_DIR)

    print("Dowloading custom models:")
    print("Downloading lusis1-476steps..")
    download_from_gdrive(LUSIS_476_ID, COMFYUI_UNET_DIR / "lusis1-476steps.safetensors")
    print("Downloading lusis1-272steps..")
    download_from_gdrive(LUSIS_272_ID, COMFYUI_UNET_DIR / "lusis1-272steps.safetensors")

if __name__ == "__main__":
    main()