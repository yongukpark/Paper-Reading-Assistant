# Paper-Reading-Assistant
Let's make custom paper reading assistant!!
논문 리딩 어시스턴트를 만드는 것을 목표로 합니다!!

## 1. Repository Structure
```text
PRA/
├── README.md
├── config.py
├── ingest.py
├── main.py
├── requirement.txt
├── data/
│   ├── raw/
│   │   └── *.pdf
│   ├── new/
│   └── paper_context_embeddings/
│       ├── chroma.sqlite3
│       └── 77cf69fe-6232-4ec0-845e-bebbd44b31dd/
├── src/
│   ├── chat/
│   │   └── chat.py
│   ├── ingestion/
│   │   ├── loader.py
│   │   ├── chunker.py
│   │   └── embedder.py
│   └── retrieval/
│       └── retriever.py
└── .env
```


## 2. File Roles
- `ingest.py`: PDF 로드 -> 청킹 -> 임베딩 생성까지의 인덱싱 파이프라인 실행
- `main.py`: 검색/질의응답 실행을 위한 메인 엔트리 포인트
- `config.py`: 임베딩 모델, 저장 경로, 배치 크기 같은 공통 설정 관리
- `src/ingestion/loader.py`: `data/raw` 아래 PDF 파일 로드
- `src/ingestion/chunker.py`: 문서를 chunk 단위로 분할
- `src/ingestion/embedder.py`: chunk들을 임베딩하고 Chroma 벡터스토어에 저장
- `src/retrieval/retriever.py`: 저장된 벡터스토어에서 관련 문맥 검색
- `src/chat/chat.py`: 검색 결과를 바탕으로 대화/응답 처리
- `data/new/`: chunking 전 논문 저장 위치
- `data/raw/`: chunking 후 논문 저장 위치 (중복 chunking 방지)
- `data/paper_context_embeddings/`: Chroma 벡터 DB 저장 위치
