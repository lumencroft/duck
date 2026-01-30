import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

video_path = "video_2026-01-30_15-48-17.mp4" 

try:
    print("오디오 추출 중...")
    y, sr = librosa.load(video_path) 

    plt.figure(figsize=(12, 6))
    
    librosa.display.waveshow(y, sr=sr, alpha=0.6, color='b')
    
    plt.title('Rain Impact Noise Analysis (Duck Bill Simulation)', fontsize=15)
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Amplitude (Impact Vibration)', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    rms = np.sqrt(np.mean(y**2))
    print(f"이 구간의 평균 충격 에너지(RMS): {rms:.5f}")

    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"에러 났어: {e}")