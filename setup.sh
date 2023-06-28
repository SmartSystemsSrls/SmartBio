# do chmod +x setup.sh
# and then ./script.sh

sudo apt-get update -y
sudo apt install python3-pip -y
sudo apt-get install ffmpeg libsm6 libxext6  -y
sudo apt-get install python3-venv -y
python3 -m ven env
source env/bin/activaye
pip3 install deepface
tmux new-session -d -s face 'source env/bin/activate && python main.py'
tmux new-session -d -s ui 'source env/bin/activate && python app.py'
