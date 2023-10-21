from faster_whisper import WhisperModel

def transcribe(filename: str):

    model_size = "medium"

    # Run on GPU with FP16
    model = WhisperModel(model_size, device="cuda", compute_type="float16")

    segments, info = model.transcribe(f'{filename}.wav', beam_size=5)
    f = open (f'{filename}.txt', 'a')
    for segment in segments:
        f.write("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text) + '\n')

    f.close()