# Deploy-diffusion

This repository contains scripts for a quick deployment of custom Stable Diffusion models. It is specifically created for **Runpod's aitrepeneur/comfyui:2.3.5** pod template.

### Installation

1. Deploy **aitrepeneur/comfyui:2.3.5** pod in [Runpod.io](https://runpod.io). Make sure to increase pod's disk volumes to run without interferences. Optimal disk space:
* Container disk - 25GB
* Volume disk - 100GB
2. Open the terminal in Jupyter Lab and clone the repository: 
```
git clone https://github.com/matulisd/deploy-diffusion.git
```
3. Change the directory to deploy-diffusion:
```
cd deploy-diffusion
```
4. Start the script:
```
bash start.sh
```
5. When prompted, paste your Hugging Face access token into terminal. Reffer to guide on how to extract Hugging Face user access token [here.](https://huggingface.co/docs/hub/en/security-tokens)

6. Access and update ComfyUI, load the workflows.

### Important links

Quick-start ComfyUI workflows:
* [SD 3.5 workflow (latest)](https://drive.google.com/file/d/1z-1L4gQh9p3XnrWYzIb_k1Or8uvt_flW)
* [SD 3.5 workflow](https://drive.google.com/file/d/1NbvkFbSaQ1MZi-fW-_O7GiKZNsJgoIqm)
* [SD 1.5 workflow](https://drive.google.com/file/d/1ZalcyicANkm1duGJeRtQ1-y_f4vt8xVi)
