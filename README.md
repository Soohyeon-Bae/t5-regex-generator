# t5-regex-generator
This mini-project is to automatically generate a regular expression based on the tags and sample values you enter. 


t5-regex-generator/
│── 📂 data/                    # 데이터셋 저장 폴더
│   ├── regex_data.csv          # 정규식 학습 데이터 (입력-출력 쌍)
│── 📂 models/                  # 학습된 모델 저장 폴더
│   ├── t5_regex_model/         # 저장된 모델 체크포인트
│── 📂 src/                     # 주요 소스 코드 폴더
│   ├── train.py                # 모델 학습 코드
│   ├── generate.py             # 정규식 생성 코드 (테스트용)
│   ├── dataset.py              # 데이터셋 로드 및 처리 코드
│── 📂 notebooks/               # 실험 및 테스트 Jupyter Notebook
│   ├── t5_regex_training.ipynb # 학습 과정 시각화 (Colab 용)
│── .gitignore                  # Git에서 제외할 파일 설정
│── requirements.txt            # 필요한 라이브러리 목록
│── README.md                   # 프로젝트 설명 문서
