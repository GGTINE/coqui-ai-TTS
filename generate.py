import warnings
warnings.filterwarnings('ignore')

import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

tts = TTS(model_path="/home/bikim/tts/run/training/iu/", config_path="/home/bikim/tts/run/training/iu/config.json").to(device)
tts.tts_to_file(text="안녕하세요. 저는 CVPR 연구실에서 학습용으로 제작된 AI 아이유 입니다.",
                speaker_wav="/home/bikim/tts/datasets/iu/iu_refer.wav",
                language='ko',
                file_path="/home/bikim/tts/datasets/iu/output.wav",
                )
