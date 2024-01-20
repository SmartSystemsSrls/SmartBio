import cv2
from deepface import DeepFace
from uuid import getnode as get_mac
import requests
import base64
import time
from datetime import datetime, timezone
import json

mac = get_mac()

def convert(obj, image):
  x = obj["region"]["x"]
  y = obj["region"]["y"]
  x2 = x + obj["region"]["w"]
  y2 = y + obj["region"]["h"]

  # cv2_imshow(frame4[y:y2,x:x2])
  img =  image[y:y2,x:x2]
  obj["image"] = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()
  obj["mac"] = mac
  obj["device"] = device_name
  obj["camera"] = "/".join(rtsp_video.split("/")[-2:])
  obj["datetime_utc"] = str(datetime.now(timezone.utc))
  obj["full_image"] =  base64.b64encode(cv2.imencode('.jpg', show_img(image, obj))[1]).decode()
  return obj

def save_obj(url, data):
  requests.post(url, json=data)

def show_img(img, obj):
  cv2.rectangle(img, (obj['region']['x'],obj['region']['y']), (obj['region']['x'] + obj['region']['w'],obj['region']['y'] + obj['region']['h']), (0,255,0), 3)
  return cv2.resize(img, (0, 0), fx = 0.3, fy = 0.3)

loaded_config = {}

def process_config(config):
    rtsp_video = config["rtsp_video"]
    send_url = config["send_url"]
    device_name = config["device_name"]
    try:
      cap = cv2.VideoCapture(rtsp_video)
      ret, frame = cap.read()
      try:
        objs = DeepFace.analyze(img_path = frame,
                actions = ['age', 'gender', 'race', 'emotion'], detector_backend = 'retinaface'
        )
        print("Face(s) detected")
        print(objs)
        objs_with_metadata = [convert(obj, frame) for obj in objs]
        # print(objs_with_metadata)
        save_obj(send_url, objs)
        print("save completed")
      except Exception as e:
        print(e)
    except Exception as e2:
      print("could not read video")
      print(e2)

while(True):
  print("Checking for " + str(datetime.now(timezone.utc)))
  try:
    configs = json.load(open('config.json'))
    if(loaded_config != configs):
      loaded_config = configs
      print("loaded config:", configs)
    for config in configs:
      process_config(config)
  except Exception as e3:
    print("could not load config, it should be a file named config.json with rtsp_video, send_url and device_name")
    print(e3)
  time.sleep(2)

