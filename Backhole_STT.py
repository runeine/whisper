import whisper
import sounddevice as sd
import numpy as np
import queue
import threading

model = whisper.load_model("base")  # Load the Whisper model
samplerate = 16000  # Sample rate for the audio input
block_duration = 5  # seconds
q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(indata.copy())

def audio_to_text():
    # device index를 확인하려면 다음 코드를 주석 해제하고 실행하세요.
    #print(sd.query_devices())
    print("Recording audio...")
    # input 채널에 맞게 device index 설정
    with sd.InputStream(samplerate=samplerate, channels=2, callback=callback,device=2):
        #input("BlackHole 입력 신호를 테스트 중입니다. Jabra에서 소리를 내고 엔터를 누르세요.\n")
        
        while True:
            audio_block_s = []
            duration = 0
            while duration < block_duration:
                block = q.get()
                audio_block_s.append(block)
                duration += len(block) / samplerate
            audio = np.concatenate(audio_block_s, axis=0)
            
                
            # 스테레오(2채널) → 모노(1채널) 변환
            if audio.ndim > 1 and audio.shape[1] == 2:
                audio = np.mean(audio, axis=1)
            audio = audio.astype(np.float32)
            # float32로 변환 및 1차원 배열로 변환
            #audio = audio.flatten().astype(np.float32)

            result = model.transcribe(audio, language="en", fp16=False)

            
            print(result["text"])


if __name__ == "__main__":
    try:
        audio_to_text()
    except KeyboardInterrupt:
        print("Recording stopped.")
