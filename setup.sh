# do chmod +x setup.sh
# and then ./setup.sh

sudo apt-get update -y
sudo apt install python3-pip -y
sudo apt-get install ffmpeg libsm6 libxext6  -y
sudo apt-get install python3-venv -y
sudo apt install python3-wheel -y
python3 -m venv env
source env/bin/activate
pip3 install --upgrade pip
pip3 install wheel
pip3 install deepface
pip3 install flask
tmux new-session -d -s face 'source env/bin/activate && python main.py'
tmux new-session -d -s ui 'source env/bin/activate && python app.py
