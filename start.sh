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
python deploy.py