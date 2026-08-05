from gtts import gTTS

text = "Hello everyone, my name is Satya Mahesh. I am a MERN Stack Developer."

tts = gTTS(text=text, lang="en")
tts.save("voice.mp3")

print("Audio saved successfully")