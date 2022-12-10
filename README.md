## Requirements

```
pip3 install SpeechRecognition
sudo apt install python3-pyaudio
```

## test

```
python3 ./scripts/test.py
```

ros service command

```
# start server
rosrun speech_rec speech_rec.py

# call service
rosservice call /speech_rec True
```
