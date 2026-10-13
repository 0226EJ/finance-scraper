# Finance Scraper 財經爬蟲專案

一個簡單的 Python 網路爬蟲專案，用來自動爬取財經網站的資料。

## 功能
- 爬取財經新聞、股價等資訊
- 支援多個常見財經網站（可擴充）
- 資料輸出為 CSV / JSON

## 安裝

```bash
pip install -r requirements.txt
```

## 使用方式

```bash
python scraper.py
```

## 專案結構

```
finance-scraper/
├── scraper.py          # 主爬蟲程式
├── requirements.txt    # 依賴套件
├── config.py           # 設定檔
├── data/               # 存放爬取的資料
└── README.md
```

## 注意事項
- 請遵守目標網站的 robots.txt 與服務條款
- 建議加入適當的延遲，避免對伺服器造成負擔
- 僅供學習與個人使用

## 授權
MIT License
