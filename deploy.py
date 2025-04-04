import os
import shutil
from huggingface_hub import hf_hub_download
import gdown
from pathlib import Path

COMFYUI_CLIP_DIR = "/workspace/ComfyUI/models/clip"
COMFYUI_UNET_DIR = "/workspace/ComfyUI/models/unet"
COMFYUI_CHECKPOINT_DIR = "/workspace/ComfyUI/models/checkpoints"

SD35_MEDIUM_HF = "stabilityai/stable-diffusion-3.5-medium"
SD15_HF = "sd-legacy/stable-diffusion-v1-5"

SD35_MEDIUM_FILENAME = "sd3.5_medium.safetensors"
SD15_FILENAME = "v1-5-pruned.safetensors"
CLIP_G_FILENAME = "clip_g.safetensors"
CLIP_L_FILENAME = "clip_l.safetensors"
T5XXL_FP16_FILENAME = "t5xxl_fp16.safetensors"

CUSTOM_MODELS = [
    {
        "name": "lusis1-476-steps.safetensors",
        "gdrive_id": "15WNb__YiUVIH7DunjnHvPqqNiVpjzOa_",
        "sd_ver": "3.5"
    },
    {
        "name": "lusis1-272-steps.safetensors",
        "gdrive_id": "121YHKoL8BJtVN54730vkNtm3YnKqfM_d",
        "sd_ver": "3.5"
    },
    {
        "name": "ryt-511-steps.safetensors",
        "gdrive_id": "1EGRJb1zOrV6H1pmFm9C7olUUmIBvw_NZ",
        "sd_ver": "3.5"
    },
    {
        "name": "wwwalantinas001.safetensors",
        "gdrive_id": "1zWfVAv42gV1Mzd2P675WHVjA5M5gJgOv",
        "sd_ver": "1.5"
    }
]

def download_from_gdrive(file_id, dest_path):
    if os.path.isfile(dest_path):
        print(f"✅  File {dest_path} already exists")
    else:
        gdown.download(f"https://drive.google.com/uc?id={file_id}", str(dest_path), quiet=False)
        print(f"✅  Downloaded and saved as {dest_path}")

def download_from_huggingface(repo_id, filename, dest_path, token):
    print(f"🎯  Downloading {filename}..")

    if os.path.isfile(dest_path):
        print(f"✅  File {dest_path} already exists")
    else:
        downloaded = hf_hub_download(
            repo_id=repo_id, 
            filename=filename,
            token=token,
            force_download=True,
            local_dir_use_symlinks=False
        )

        real_file = os.path.realpath(downloaded)

        # Make sure the parent dir exists
        Path(dest_path).parent.mkdir(parents=True, exist_ok=True)

        shutil.copy2(real_file, dest_path)
        print(f"✅  Downloaded and saved as {dest_path}")

def main():
    print("\n\n🔥  Please enter your Hugging Face access token:")
    token = input("> ").strip()

    print("🎯  Setting up Stable Diffusion..")
    download_from_huggingface(SD35_MEDIUM_HF, SD35_MEDIUM_FILENAME, os.path.join(COMFYUI_CHECKPOINT_DIR, SD35_MEDIUM_FILENAME), token)
    download_from_huggingface(SD15_HF, SD15_FILENAME, os.path.join(COMFYUI_CHECKPOINT_DIR, SD15_FILENAME), token)
    
    print("🎯  Downloading text encoders:")
    download_from_huggingface(SD35_MEDIUM_HF, os.path.join("text_encoders", CLIP_G_FILENAME), os.path.join(COMFYUI_CLIP_DIR, CLIP_G_FILENAME), token)
    download_from_huggingface(SD35_MEDIUM_HF, os.path.join("text_encoders", CLIP_L_FILENAME), os.path.join(COMFYUI_CLIP_DIR, CLIP_L_FILENAME), token)
    download_from_huggingface(SD35_MEDIUM_HF, os.path.join("text_encoders", T5XXL_FP16_FILENAME), os.path.join(COMFYUI_CLIP_DIR, T5XXL_FP16_FILENAME), token)

    print("🎯  Dowloading custom models:")
    for model in CUSTOM_MODELS:
        print(f"🎯  Downloading {model['name']}..")
        if model["sd_ver"] == "3.5":
            download_from_gdrive(model["gdrive_id"], os.path.join(COMFYUI_UNET_DIR, model["name"]))
        else:
            download_from_gdrive(model["gdrive_id"], os.path.join(COMFYUI_CHECKPOINT_DIR, model["name"]))

    print("\n\n✅  Setup done, exiting..\n\n")

if __name__ == "__main__":
    main()