import os
import shutil
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

# def download_from_huggingface(repo_id, filename, dest_path, token):
#     downloaded = hf_hub_download(
#         repo_id=repo_id, 
#         filename=filename,
#         token=token
#         )

#     if os.path.exists(os.path.join(dest_path, filename)):
#         print(f"🎯  {os.path.join(dest_path, filename)} already exists -> deleting..")
#         os.remove(dest_path)

#     # real_file = os.path.realpath(downloaded)
    
#     Path(dest_path).parent.mkdir(parents=True, exist_ok=True)
#     shutil.move(downloaded, dest_path)
#     # shutil.copy2(real_file, dest_path)

def download_from_huggingface(repo_id, filename, dest_path, token):
    downloaded = hf_hub_download(
        repo_id=repo_id, 
        filename=filename,
        token=token
    )

    # Make sure the parent dir exists
    Path(dest_path).parent.mkdir(parents=True, exist_ok=True)

    # Remove existing file or symlink
    if os.path.isfile(dest_path) or os.path.islink(dest_path):
        print(f"🎯  {dest_path} already exists -> deleting..")
        os.remove(dest_path)

    # Use the real file, not symlink
    real_file = os.path.realpath(downloaded)
    shutil.copy2(real_file, dest_path)
    print(f"     ✅  Downloaded and saved to {dest_path}")


def main():
    print("\n\n\n🔥  Please enter your Hugging Face access token:")
    token = input("> ").strip()

    print("🎯  Setting up Stable Diffusion..")
    print("     🎯  Downloading base stable diffusion 3.5 medium model..")
    download_from_huggingface(SD35_MEDIUM_HF, SD35_MEDIUM_FILENAME, COMFYUI_CHECKPOINT_DIR, token)
    
    print("🎯  Downloading text encoders:")
    print(f"     🎯  Downloading {CLIP_G_FILENAME}")
    download_from_huggingface(SD35_MEDIUM_HF, os.path.join("text_encoders", CLIP_G_FILENAME), COMFYUI_CLIP_DIR, token)
    print(f"     🎯  Downloading {CLIP_L_FILENAME}")
    download_from_huggingface(SD35_MEDIUM_HF, os.path.join("text_encoders", CLIP_L_FILENAME), COMFYUI_CLIP_DIR, token)
    print(f"     🎯  Downloading {T5XXL_FP16_FILENAME}")
    download_from_huggingface(SD35_MEDIUM_HF, os.path.join("text_encoders", T5XXL_FP16_FILENAME), COMFYUI_CLIP_DIR, token)

    print("🎯  Dowloading custom models:")
    print("     🎯  Downloading lusis1-476steps..")
    download_from_gdrive(LUSIS_476_ID, os.path.join(COMFYUI_UNET_DIR, "lusis1-476steps.safetensors"))
    print("     🎯  Downloading lusis1-272steps..")
    download_from_gdrive(LUSIS_272_ID, os.path.join(COMFYUI_UNET_DIR, "lusis1-272steps.safetensors"))

if __name__ == "__main__":
    main()