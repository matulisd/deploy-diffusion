#!/bin/bash
set -e

cat <<'EOF'
                                                           
                 ░▓▓█▒                                           
                 ▒███▓                   ▒██▓▒                   
                  ▒▓▓░                  ░██▓                     
                  ▒██▓░               ▓█▓▓▒                      
                  ██▓▒▒▒           ░▓█▓▓▓█░                      
                ▒▓▒██▓▒▒▒░░     ▒▓███▓▒▓█▒                       
                ▒███████▓▓▓██████████▓▒▒▒                        
                ██▓█████████████████████▓                        
               ▒███████████████████████▓                        
               ░████████████████████████▒                        
               ▒█████████████████████████▓                       
               ▒███████████████████████▓▓▒                       
               ██████████████████████████▓                       
               ▓█████████████████████████▓                        
              ▒█████▓█▓▓▓▓▓███▓▒▒▒▒███▓▓▓▒                       
          ▒█████▓██▓████▓▒▒▓██▓▒▒▓▓██▓░▓█▒                       
       ░▓███████▓█▓▓▓▓▒▒░▒▓▓▓▒▒░░▒▒░░▒█▓                         
   ▒███████████▓▒█▓▒▒▒░   ▒▒▓██░     ░░                          
█████████████████▒░▓█▓░░      ░▓█▒░                              
██████████████████▓███▓░         ▒░                              
████████████████████████▒ ░      ▒▒░░                            
████████████████████████▓▒▓▒     ▓▓▒▒░                           
███████████████████████████▓▓▒▒ ░▒▓░                             
█████████████████████████████▓██▓▒                               
████████████████████████████████▓▒                               
█████████████████████████████▓▓▓▓▓░                              

EOF

if [ -d "/workspace/deploy-diffusion/venv" ]; then
    echo "🎯  Virtual environment already exists. Activating.."
    source /workspace/deploy-diffusion/venv/bin/activate
else
    echo "🎯  Creating virtual environment..."
    python -m venv venv

    echo "🎯  Activating virtual environment..."
    source /workspace/deploy-diffusion/venv/bin/activate

    echo "🎯  Installing dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
fi

echo "🎯  Running deployment script..."
cd /workspace/deploy-diffusion
python deploy.py

echo "🎯  Updating ComfyUI..."
cd /workspace/ComfyUI
git stash
git pull origin master
source /workspace/ComfyUI/venv/bin/activate
pip install -r requirements.txt
python main.py 