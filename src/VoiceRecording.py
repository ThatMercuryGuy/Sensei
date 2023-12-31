from pvrecorder import PvRecorder
import wave
import struct
import time
import threading



class StopRecordingException(Exception):
    "Exception Thrown When Recording Has to Stop"
    pass

def ThrowStopRecordingException():
    raise StopRecordingException

def start_recording():
    recorder = PvRecorder(frame_length = 1024)
    audio = []
    # Start recording
    recorder.start()
    print ('Recording Started!')


    try:
        while recorder.is_recording:
            frame = recorder.read()
            # process audio frame
            audio.extend(frame)

    except StopRecordingException or KeyboardInterrupt:
        print ('Recording Stopped!')
        recorder.stop()
        filename = time.ctime().replace(':', '.')
        with wave.open(f'{filename}.wav', 'w') as f:
            f.setparams((1, 2, 16000, 1024, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(audio), *audio))

    finally:
        recorder.delete()
        f.close()
        return filename