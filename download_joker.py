#!/usr/bin/env python3
"""
雨宫莲图片批量下载脚本 - 增强版
使用方法：python download_joker.py
"""

import os
import requests
import time
import json
import re
from urllib.parse import quote, urlencode
from pathlib import Path
from html import unescape
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# 配置
SAVE_DIR = Path("C:/Users/998/Desktop/joker-portfolio/images/joker_collection")
SAVE_DIR.mkdir(exist_ok=True)

# 扩展搜索关键词列表（中英文混合，更多变体）
SEARCH_QUERIES = [
    # 中文搜索
    "雨宫莲 persona5",
    "雨宫莲 怪盗",
    "雨宫莲 P5X",
    "雨宫莲 高清",
    "雨宫莲 壁纸",
    "雨宫莲 游戏",
    "雨宫莲 同人",
    "雨宫莲 插画",
    "雨宫莲 cosplay",
    "雨宫莲 手办",
    "雨宫莲 截图",
    "雨宫莲 官方",
    "雨宫莲 fanart",
    "雨宫莲 artwork",

    # 英文搜索
    "Joker persona 5 wallpaper",
    "Joker persona 5 fanart",
    "Joker persona 5 artwork",
    "Joker persona 5 screenshot",
    "Joker persona 5 official",
    "Joker Persona 5X",
    "Joker P5X",
    "Persona 5 protagonist",
    "Persona 5 main character",
    "Persona 5 Joker HD",
    "Persona 5 Joker 4K",
    "Persona 5 Amamiya Ren",
    "Persona 5 Kurusu Akira",
    "Ren Amamiya persona 5",
    "Akira Kurusu persona 5",

    # 变体搜索
    "persona 5 joker mask",
    "persona 5 joker thief",
    "persona 5 joker phantom",
    "persona 5 joker rebel",
    "persona 5 joker wild card",
    "persona 5 joker arsene",
    "persona 5 joker gun",
    "persona 5 joker sword",
    "persona 5 joker school",
    "persona 5 joker shujin",
    "persona 5 joker metaverse",
    "persona 5 joker cognitive",

    # 场景相关
    "persona 5 joker awakening",
    "persona 5 joker battle",
    "persona 5 joker all out attack",
    "persona 5 joker showtime",
    "persona 5 joker velvet room",
    "persona 5 joker mementos",
    "persona 5 joker palace",

    # 同人创作
    "persona 5 joker fan art",
    "persona 5 joker illustration",
    "persona 5 joker drawing",
    "persona 5 joker painting",
    "persona 5 joker digital art",
    "persona 5 joker anime",
    "persona 5 joker manga",

    # 壁纸和高清
    "persona 5 joker wallpaper 1080p",
    "persona 5 joker wallpaper 4k",
    "persona 5 joker desktop",
    "persona 5 joker phone wallpaper",
    "persona 5 joker mobile",

    # 周边和商品
    "persona 5 joker figure",
    "persona 5 joker nendoroid",
    "persona 5 joker statue",
    "persona 5 joker merch",
    "persona 5 joker poster",

    # 游戏截图
    "persona 5 joker cutscene",
    "persona 5 joker gameplay",
    "persona 5 joker cinematic",
    "persona 5 joker trailer",

    # P5R和P5S相关
    "persona 5 royal joker",
    "persona 5 strikers joker",
    "persona 5 scramble joker",
    "P5R joker",
    "P5S joker",

    # 其他变体
    "persona 5 protagonist art",
    "persona 5 main char",
    "persona 5 hero",
    "persona 5 leader",
    "phantom thieves joker",
    "pt joker persona 5",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

# 全局计数器和锁
download_counter = {"count": 0, "file_index": 1}
counter_lock = threading.Lock()

# 已下载URL集合（去重）
downloaded_urls = set()
urls_lock = threading.Lock()

def download_image(url, save_path, headers=None):
    """下载单张图片"""
    try:
        resp = requests.get(url, headers=headers or HEADERS, timeout=20, stream=True)
        resp.raise_for_status()

        content_type = resp.headers.get('content-type', '')
        if 'image' not in content_type and not url.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.gif')):
            return False

        with open(save_path, 'wb') as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)

        if save_path.stat().st_size < 10000:
            save_path.unlink()
            return False

        return True
    except Exception:
        if save_path.exists():
            save_path.unlink()
        return False

def search_bing_images(query, count=200):
    """从Bing图片搜索获取图片URL"""
    images = []
    offset = 0

    while len(images) < count and offset < 800:
        params = {
            "q": query,
            "form": "HDRSC2",
            "first": offset,
            "count": 35,
            "qft": "+filterui:photo-photo",
        }

        url = f"https://www.bing.com/images/search?{urlencode(params)}"

        try:
            resp = requests.get(url, headers=HEADERS, timeout=20)
            resp.raise_for_status()
            html = resp.text

            pattern = r'murl&quot;:&quot;(https?://[^&]+\.(?:jpg|jpeg|png|webp|gif))'
            matches = re.findall(pattern, html, re.IGNORECASE)

            if not matches:
                pattern = r'"murl":"(https?://[^"]+\.(?:jpg|jpeg|png|webp|gif))"'
                matches = re.findall(pattern, html, re.IGNORECASE)

            if not matches:
                break

            for img_url in matches:
                img_url = unescape(img_url)
                if img_url not in images:
                    images.append(img_url)
                    if len(images) >= count:
                        break

            offset += 35
            time.sleep(0.3)

        except Exception as e:
            print(f"  搜索失败: {str(e)[:30]}")
            break

    return images[:count]

def download_single_image(args):
    """下载单张图片（用于并发）"""
    img_url, total_count = args

    # 检查是否已下载过
    with urls_lock:
        if img_url in downloaded_urls:
            return None
        downloaded_urls.add(img_url)

    with counter_lock:
        if download_counter["count"] >= total_count:
            return None
        file_index = download_counter["file_index"]
        download_counter["file_index"] += 1

    ext = "jpg"
    url_lower = img_url.lower()
    if ".png" in url_lower:
        ext = "png"
    elif ".webp" in url_lower:
        ext = "webp"
    elif ".gif" in url_lower:
        ext = "gif"

    filename = f"joker_{file_index:04d}.{ext}"
    save_path = SAVE_DIR / filename

    if save_path.exists():
        return None

    if download_image(img_url, save_path, HEADERS):
        with counter_lock:
            download_counter["count"] += 1
            current = download_counter["count"]
        return (current, filename)
    return None

def download_from_bing(total_count=1000):
    """从Bing图片搜索并发下载"""
    print("=" * 60)
    print("开始从Bing图片搜索下载雨宫莲图片（增强版）")
    print("=" * 60)

    all_image_urls = []
    seen_urls = set()

    for i, query in enumerate(SEARCH_QUERIES):
        if len(all_image_urls) >= total_count * 3:
            break

        print(f"\n[{i+1}/{len(SEARCH_QUERIES)}] 搜索关键词: {query}")
        image_urls = search_bing_images(query, 150)
        print(f"  找到 {len(image_urls)} 张图片")

        for url in image_urls:
            if url not in seen_urls:
                seen_urls.add(url)
                all_image_urls.append(url)

    print(f"\n总计找到 {len(all_image_urls)} 个不重复图片URL")
    print(f"开始并发下载（15线程）...")

    download_args = [(url, total_count) for url in all_image_urls[:total_count * 2]]

    completed = 0
    with ThreadPoolExecutor(max_workers=15) as executor:
        futures = {executor.submit(download_single_image, args): args for args in download_args}

        for future in as_completed(futures):
            result = future.result()
            if result:
                completed += 1
                current, filename = result
                print(f"  [{current}/{total_count}] 已下载: {filename}")

                if current >= total_count:
                    # 取消剩余任务
                    for f in futures:
                        f.cancel()
                    break

    return download_counter["count"]

def main():
    print("=" * 60)
    print("雨宫莲图片批量下载工具 (增强版)")
    print("=" * 60)
    print(f"保存目录: {SAVE_DIR}")
    print(f"目标数量: 1000张")
    print(f"搜索关键词: {len(SEARCH_QUERIES)}个")
    print()

    total = download_from_bing(1000)

    print()
    print("=" * 60)
    print(f"下载完成！共 {total} 张图片")
    print(f"保存位置: {SAVE_DIR}")
    print("=" * 60)

if __name__ == "__main__":
    main()
