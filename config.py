# 爬蟲設定檔

# 目標網站（可自行新增）
TARGET_SITES = {
    "yahoo_finance": {
        "name": "Yahoo Finance",
        "base_url": "https://finance.yahoo.com",
        "news_url": "https://finance.yahoo.com/news/",
    },
    # 可在此新增其他財經網站
}

# 請求設定
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
}

# 請求間隔（秒），避免被封鎖
REQUEST_DELAY = 2

# 資料存放目錄
DATA_DIR = "data"

# 輸出格式：csv 或 json
OUTPUT_FORMAT = "csv"
