# SmartBio

Steps to setup

git clone https://github.com/SmartSystemsSrls/SmartBio.git

cd SmartBio

chmod +x setup.sh

./setup.sh




_________________________________________________________________________________________________________________

1. cd SmartBio
this takes you to your github folder

then run
tmux new-session -d -s face 'source env/bin/activate && python main.py'
tmux new-session -d -s ui 'source env/bin/activate && python app.py'

this wil start both the face detection and the ui server
