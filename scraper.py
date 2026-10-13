#!/usr/bin/env python3
"""
財經網站爬蟲主程式
自動爬取財經新聞與相關資訊
"""

import os
import time
import json
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup
import pandas as pd

from config import HEADERS, REQUEST_DELAY, DATA_DIR, OUTPUT_FORMAT, TARGET_SITES


def ensure_data_dir():
    """確保資料目錄存在"""
    Path(DATA_DIR).mkdir(exist_ok=True)


def fetch_page(url: str) -> BeautifulSoup | None:
    """發送請求並回傳 BeautifulSoup 物件"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return BeautifulSoup(response.text, "lxml")
    except requests.RequestException as e:
        print(f"[錯誤] 無法取得 {url}: {e}")
        return None


def scrape_yahoo_finance_news() -> list[dict]:
    """爬取 Yahoo Finance 新聞標題與連結（示範用）"""
    site = TARGET_SITES.get("yahoo_finance")
    if not site:
        return []

    print(f"正在爬取：{site['name']} ...")
    soup = fetch_page(site["news_url"])
    if not soup:
        return []

    results = []
    # 注意：實際網站結構可能會變動，此處為示範選擇器
    # 請根據實際頁面調整
    articles = soup.select("h3 a") or soup.select("a[data-test-locator='headline']")

    for article in articles[:20]:  # 限制前 20 則
        title = article.get_text(strip=True)
        href = article.get("href", "")
        if not title:
            continue

        # 處理相對連結
        if href.startswith("/"):
            href = site["base_url"] + href

        results.append({
            "title": title,
            "url": href,
            "source": site["name"],
            "scraped_at": datetime.now().isoformat(timespec="seconds"),
        })

    print(f"  取得 {len(results)} 則新聞")
    time.sleep(REQUEST_DELAY)
    return results


def save_data(data: list[dict], filename: str = None):
    """儲存資料為 CSV 或 JSON"""
    if not data:
        print("沒有資料可儲存")
        return

    ensure_data_dir()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if filename is None:
        filename = f"finance_news_{timestamp}"

    filepath = Path(DATA_DIR) / filename

    if OUTPUT_FORMAT == "json":
        filepath = filepath.with_suffix(".json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    else:
        filepath = filepath.with_suffix(".csv")
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False, encoding="utf-8-sig")

    print(f"資料已儲存至：{filepath}")


def main():
    print("=" * 50)
    print("財經爬蟲啟動")
    print("=" * 50)

    all_data = []

    # 爬取 Yahoo Finance
    all_data.extend(scrape_yahoo_finance_news())

    # 之後可在此新增其他網站的爬取函式
    # all_data.extend(scrape_other_site())

    save_data(all_data)

    print("=" * 50)
    print("爬取完成！")
    print("=" * 50)


if __name__ == "__main__":
    main()
