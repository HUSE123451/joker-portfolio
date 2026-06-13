#!/bin/bash
# ============================================================
# P5X Music Downloader (NetEase Music)
# 用法: ./download_music.sh
# 从网易云音乐下载 P5X 相关音乐
# ============================================================

AUDIO_DIR="$(dirname "$0")/audio"

echo "P5X Music Downloader (NetEase Music)"
echo "====================================="
echo "输出: $AUDIO_DIR"
echo ""

mkdir -p "$AUDIO_DIR"

# 搜索并下载函数
download_netease() {
    local query="$1"
    local output="$2"
    local display_name="$3"

    echo "搜索: $display_name ..."

    # 搜索歌曲 ID
    local song_id=$(curl -s "https://music.163.com/api/search/get/s=${query}&type=1&limit=1" \
        -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
        -H "Referer: https://music.163.com" | grep -o '"id":[0-9]*' | head -1 | cut -d: -f2)

    if [ -z "$song_id" ]; then
        echo "   未找到: $display_name"
        return 1
    fi

    echo "   找到歌曲 ID: $song_id"
    echo "   下载中..."

    curl -L -o "$AUDIO_DIR/$output" \
        "https://music.163.com/song/media/outer/url?id=$song_id" \
        -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
        -H "Referer: https://music.163.com" \
        --progress-bar

    if [ -f "$AUDIO_DIR/$output" ]; then
        local size=$(stat -f%z "$AUDIO_DIR/$output" 2>/dev/null || stat -c%s "$AUDIO_DIR/$output" 2>/dev/null)
        if [ "$size" -gt 100000 ]; then
            echo "   下载成功! ($(($size / 1024 / 1024))MB)"
        else
            echo "   文件过小，可能下载失败"
            rm -f "$AUDIO_DIR/$output"
            return 1
        fi
    else
        echo "   下载失败"
        return 1
    fi
}

# 下载 Full Moon, Full Life
download_netease "Full Moon Full Life Persona Reload" "full_moon_full_life.mp3" "Full Moon, Full Life"

echo ""

# 下载 星と僕らと (tofubeats Remix)
download_netease "星と僕らと tofubeats Remix" "tofubeats_remix.mp3" "星と僕らと (tofubeats Remix)"

echo ""
echo "检查下载结果..."
ls -lh "$AUDIO_DIR"/*.mp3 2>/dev/null

echo ""
echo "完成!"
