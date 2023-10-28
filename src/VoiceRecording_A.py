from pvrecorder import PvRecorder
import wave
import struct
import time
import threading




def start_recording(gate: list, filename: str):
    recorder = PvRecorder(frame_length = 1024)
    audio = []
    # Start recording
    recorder.start()
    print ('Recording Started!')


    try:
        while recorder.is_recording and gate[0]:
            frame = recorder.read()
            # process audio frame
            audio.extend(frame)

        print ('Recording Stopped!')
        recorder.stop()
        
        with wave.open(f'static\{filename}.wav', 'w') as f:
            f.setparams((1, 2, 16000, 1024, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(audio), *audio))

    finally:
        recorder.delete()
        f.close()