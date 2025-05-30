PC 에서 출력되는 sound를 가상 sound output(blackhole)로 전송하여,
whisper 에서 제공하는 Speech to Text 로 output 생성

1.python vserion
3.11

2.requried library install
pip install openai-whisper sounddevice numpy

3. requried program
   blackhole 2ch : https://existential.audio/blackhole/

4. PC setting
   mac : command + space > audio MIDI setup > add > create multi output devices > primary device : blackhole 2ch
 
   . 오디오 MIDI 설정에서 가상 장치 구성
   응용 프로그램 > 유틸리티 > 오디오 MIDI 설정 실행
   좌측 하단 + 버튼 클릭 → 다중 출력 장치 생성
   오른쪽에서 내장 출력과 BlackHole 2ch 모두 체크
   기본 출력을 방금 만든 다중 출력 장치로 설정
   (필요시) BlackHole 2ch를 기본 입력으로 설정

5. execute Balckhole_STT.py
   
     
