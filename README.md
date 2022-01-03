# Dashboard
![](https://github.com/ydty/dashboard/workflows/pytest/badge.svg)

## Usage

### Dockerを用いた起動例
```bash
# ビルド
$ docker-compose build

# 起動(localhost:8501)
$ docker-compose up -d
```

### Localでの起動例

**前提 Python3.8/poetryをPCにインストール済みであること**

#### 各種ライブラリのインストール
```cmd
poetry install
```

#### dashboard(streamlit)の起動
```cmd
rem 起動(localhost:8501)
streamlit run src/dashboard/main.py
```