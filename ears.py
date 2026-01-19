import pyaudio
import wave
import os
from faster_whisper import WhisperModel

# Configuration
MODEL_SIZE = "base.en" # Use 'tiny.en' for speed, 'medium.en' for accuracy
model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")

def record_audio(filename="input.wav", duration=5):
    """Records audio from the microphone for a fixed duration."""
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    
    print("🎤 Listening...")
    frames = []
    
    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)
        
    print("✅ Processing...")
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def transcribe(filename="input.wav"):
    segments, _ = model.transcribe(filename)
    text = " ".join([segment.text for segment in segments])
    return text.strip()