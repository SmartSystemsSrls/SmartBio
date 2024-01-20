#!/bin/sh
cd
cd SmartBio
tmux new-session -d -s face 'source env/bin/activate && python main.py'
tmux new-session -d -s ui 'source env/bin/activate && python app.py'
