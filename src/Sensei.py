import abstra.dashes as ad
from VoiceRecording_A import start_recording
import threading
from main import start_application
import time
"""
Abstra dashes are the simplest way to build custom user interfaces for your APIs.
"""

gate = [True]
ann = ""

def get_annotation_time(start_time: float):
    seconds = (round((time.time() - start_time)))
    return str(seconds) + '.00s'