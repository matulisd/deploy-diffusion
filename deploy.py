import os
import shutil
from huggingface_hub import hf_hub_download
import gdown
from pathlib import Path

COMFYUI_CLIP_DIR = "/workspace/ComfyUI/models/clip"
COMFYUI_UNET_DIR = "/workspace/ComfyUI/models/unet"
COMFYUI_CHECKPOINT_DIR = "/workspace/ComfyUI/models/checkpoints"

SD35_MEDIUM_HF = "stabilityai/stable-diffusion-3.5-medium"
SD3_MEDIUM_HF = "stabilityai/stable-diffusion-3-medium"
SD15_HF = "sd-legacy/stable-diffusion-v1-5"

SD35_MEDIUM_FILENAME = "sd3.5_medium.safetensors"
SD3_MEDIUM_FILENAME = "sd3_medium.safetensors"
SD15_FILENAME = "v1-5-pruned.safetensors"
CLIP_G_FILENAME = "clip_g.safetensors"
CLIP_L_FILENAME = "clip_l.safetensors"
T5XXL_FP16_FILENAME = "t5xxl_fp16.safetensors"

CUSTOM_MODELS = [
    # {
    #     "name": "",
    #     "gdrive_id": "",
    #     "sd_ver": ""
    # },
    # {
    #     "name": "lusis1-476-steps.safetensors",
    #     "gdrive_id": "15WNb__YiUVIH7DunjnHvPqqNiVpjzOa_",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "lusis1-272-steps.safetensors",
    #     "gdrive_id": "121YHKoL8BJtVN54730vkNtm3YnKqfM_d",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "v4l4ntinas-full-250410",
    #     "gdrive_id": "1LkGJgdu2JPcmwPxXv5xGCOub2zOMsd5x",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "v4l4ntinas-230-250410",
    #     "gdrive_id": "1CHpdexJ8zP6ofIVxGBaEskbmyPKJn4Mm",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "wwwalantinas001.safetensors",
    #     "gdrive_id": "1zWfVAv42gV1Mzd2P675WHVjA5M5gJgOv",
    #     "sd_ver": "1.5"
    # },
    # {
    #     "name": "v4l4n-etching-125-0427.safetensors",
    #     "gdrive_id": "10CmvUJmU3jbDGBKfvABVYPyGDye7QONo",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "v4l4n-pencil-75-0427.safetensors",
    #     "gdrive_id": "194jrOj8nLReHwRicxP6hRpS5w5I4UDUS",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "v4l4n-etching-150-0427.safetensors",
    #     "gdrive_id": "1e8xd62SgBKCkf7zKSxYkEm69oidw72a7",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "v4l4n-etching-150-0427.safetensors",
    #     "gdrive_id": "1e8xd62SgBKCkf7zKSxYkEm69oidw72a7",
    #     "sd_ver": "3.5"
    # }
    # ,
    # {
    #     "name": "v4l4n-pencil-20-new-captions.safetensors",
    #     "gdrive_id": "1TkzSzBraXJooWgAKidPCVDygzZ1tsQE6",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "v4l4n-pencil-20ep-standard100",
    #     "gdrive_id": "1YROWcX-4EhdFmFg1cS_HGeNaez5jhTIm",
    #     "sd_ver": "3.5"
    # }
    # {
    #     "name": "w4l4ntinaz-20-0501",
    #     "gdrive_id": "16j_lU_tZwQHoGUc83wGHPrJZjYCVG0Z-",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "w4l4ntinaz-30-0501",
    #     "gdrive_id": "1Fem5gtWysyTRj5i-uURB_3c_dcLgTXty",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "w4l4ntinaz-8000-0505(best-so-far).safetensors",
    #     "gdrive_id": "1LrUowNIp1pmIsX7NkKYsFp8xUPUHO5O-",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "w4l4ntinaz-7200-0517.safetensors",
    #     "gdrive_id": "1MKLmBPh9YrH9jNOh0dGjXyCpo56sMW_Y",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "w4l4ntinaz-9600-0517.safetensors",
    #     "gdrive_id": "1IRVH326gxU4wxvTp244xCKxgDCh1ENx7",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "w4l4ntinaz-12600-0517.safetensors",
    #     "gdrive_id": "1fy7-STSxPDDkZ-sWB9e6WEtiT9n01L3R",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "w4l4ntinaz-16200-0517.safetensors",
    #     "gdrive_id": "1mqVNusjqr1onyKWPTdJ7uveDAzjuyOtt",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "peizazai-2700-0518.safetensors",
    #     "gdrive_id": "1dABXGnkzU-parHmz7aYgEG0u6MFK5ZGe",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "peizazai-3900-0518.safetensors",
    #     "gdrive_id": "1KRwj9NN-sJVAfpge8dotPwUyauM69H9g",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "skull-5600-0518.safetensors",
    #     "gdrive_id": "1QmV-xjR_-A1GIiOPsnM8imMzukeLj5MA",
    #     "sd_ver": "3.5"
    # },
    # {
    #     "name": "skull-7000-0518.safetensors",
    #     "gdrive_id": "1H1ZeCEeBMFByKsK8H_F0374u2irdDGYS",
    #     "sd_ver": "3.5"
    # }
    {
        "name": "etch-0620-5000steps.safetensors",
        "gdrive_id": "1Ly0v6UVzKg6DmlRVG_t_tWsGvhSby7BU",
        "sd_ver": "3.5"
    },
    {
        "name": "etch-0620-7000steps.safetensors",
        "gdrive_id": "1sQsDXYguEn_5kwg901GX18WSn9hEKyl6",
        "sd_ver": "3.5"
    },
    {
        "name": "etch-0620-9000steps.safetensors",
        "gdrive_id": "1hCXzAFMKN9sSRGJgy53p--efnV9QhdFY",
        "sd_ver": "3.5"
    },
    {
        "name": "etch-0620-11000steps.safetensors",
        "gdrive_id": "1bgCRaaVyaysTtpT3F7oL77XTg1JOo8d8",
        "sd_ver": "3.5"
    },
    {
        "name": "crosshatch-0626-3500steps.safetensors",
        "gdrive_id": "1thHDxwAE7C_Zf0PG1Zpej3Z2g8XB-1Ur",
        "sd_ver": "3.5"
    },
    {
        "name": "crosshatch-0626-5500steps.safetensors",
        "gdrive_id": "1Yd05pCM3Jy5Le0wO4LKxhH04y67MzbCh",
        "sd_ver": "3.5"
    },
    {
        "name": "crosshatch-0626-7500steps.safetensors",
        "gdrive_id": "1hW-xShdlKiKUxDUIdLH1RpxxH9Zbkq6y",
        "sd_ver": "3.5"
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
    # download_from_huggingface(SD3_MEDIUM_HF, SD3_MEDIUM_FILENAME, os.path.join(COMFYUI_CHECKPOINT_DIR, SD3_MEDIUM_FILENAME), token)
    # download_from_huggingface(SD15_HF, SD15_FILENAME, os.path.join(COMFYUI_CHECKPOINT_DIR, SD15_FILENAME), token)
    
    print("🎯  Downloading text encoders:")
    download_from_huggingface(SD35_MEDIUM_HF, os.path.join("text_encoders", CLIP_G_FILENAME), os.path.join(COMFYUI_CLIP_DIR, CLIP_G_FILENAME), token)
    download_from_huggingface(SD35_MEDIUM_HF, os.path.join("text_encoders", CLIP_L_FILENAME), os.path.join(COMFYUI_CLIP_DIR, CLIP_L_FILENAME), token)
    download_from_huggingface(SD35_MEDIUM_HF, os.path.join("text_encoders", T5XXL_FP16_FILENAME), os.path.join(COMFYUI_CLIP_DIR, T5XXL_FP16_FILENAME), token)

    print("🎯  Dowloading custom models:")
    for model in CUSTOM_MODELS:
        print(f"🎯  Downloading {model['name']}..")
        if model["sd_ver"] == "3.5":
            download_from_gdrive(model["gdrive_id"], os.path.join(COMFYUI_UNET_DIR, model["name"]))
        elif model["sd_ver"] == "1.5":
            download_from_gdrive(model["gdrive_id"], os.path.join(COMFYUI_CHECKPOINT_DIR, model["name"]))
        else:
            print("🔥 UNSUPORTED SD VERSION")

    print("\n\n✅  Setup done, exiting..\n\n")

if __name__ == "__main__":
    main()
