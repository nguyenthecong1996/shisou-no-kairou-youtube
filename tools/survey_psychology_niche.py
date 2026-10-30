import json, subprocess, urllib.request, re, time, os, sys
from datetime import datetime
from collections import defaultdict
import statistics

TODAY = datetime(2026, 10, 27)

SEARCH_QUERIES = [
    "【心理学】",
    "心理学の",
    "行動心理学",
    "深層心理",
    "大人の心理学",
    "心理学 人間関係",
    "心理学 雑学",
    "心理学 聞き流し"
]

SCRATCH_DIR = "/home/congnt/.gemini/antigravity/scratch"
CACHE_FILE = os.path.join(SCRATCH_DIR, "channel_cache.json")

# Load existing channel cache
channel_cache = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            channel_cache = json.load(f)
    except Exception:
        pass

def save_cache():
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(channel_cache, f, ensure_ascii=False, indent=2)

def is_strictly_japanese(text):
    # Must contain Hiragana or Katakana (which only exist in Japanese)
    return bool(re.search(r'[\u3040-\u309F\u30A0-\u30FF]', text))

def get_channel_joined_date(channel_url, channel_id):
    if channel_id and channel_id in channel_cache:
        return channel_cache[channel_id]
        
    about_url = None
    if channel_url and channel_url.startswith("http"):
        about_url = f"{channel_url.rstrip('/')}/about"
    elif channel_id:
        about_url = f"https://www.youtube.com/channel/{channel_id}/about"
        
    if not about_url:
        return None
        
    req = urllib.request.Request(
        about_url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8", errors="replace")
            m = re.search(r'Joined\s+([A-Za-z]+)\s+(\d+),\s+(\d{4})', html)
            if m:
                month_str, day_str, year_str = m.groups()
                dt = datetime.strptime(f"{month_str} {day_str} {year_str}", "%b %d %Y")
                date_str = dt.strftime("%Y-%m-%d")
                if channel_id:
                    channel_cache[channel_id] = date_str
                    save_cache()
                return date_str
    except Exception as e:
        print(f"  [warn] Error fetching {about_url}: {e}", file=sys.stderr)
    return None

def main():
    print("=== BẮT ĐẦU KHẢO SÁT CHUẨN XÁC: NGÁCH TÂM LÝ HỌC (NHẬT BẢN) ===")
    print(f"Thời điểm khảo sát: {TODAY.strftime('%Y-%m-%d')}")
    print(f"Các từ khóa: {SEARCH_QUERIES}\n")
    
    videos = {}
    
    for query in SEARCH_QUERIES:
        print(f"--> Đang quét từ khóa: '{query}'...")
        cmd = [
            "yt-dlp",
            f"ytsearch50:{query}",
            "--flat-playlist",
            "--dump-json"
        ]
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, check=True)
            count_found = 0
            for line in res.stdout.strip().split("\n"):
                if not line.strip():
                    continue
                try:
                    item = json.loads(line)
                    vid = item.get("id")
                    title = item.get("title", "")
                    views = item.get("view_count") or 0
                    duration = item.get("duration") or 0
                    channel = item.get("channel") or item.get("uploader") or ""
                    channel_url = item.get("channel_url") or item.get("uploader_url") or ""
                    channel_id = item.get("channel_id") or ""
                    
                    # 1. Bắt buộc có ký tự Hiragana hoặc Katakana (loại bỏ tiếng Trung)
                    if not is_strictly_japanese(title) and not is_strictly_japanese(channel):
                        continue
                    # 2. Không phải Shorts (duration >= 180s)
                    if duration < 180:
                        continue
                    # 3. View >= 100.000
                    if views < 100000:
                        continue
                        
                    key = vid or title
                    if key not in videos:
                        videos[key] = {
                            "id": vid,
                            "title": title,
                            "views": views,
                            "duration": duration,
                            "channel": channel,
                            "channel_url": channel_url,
                            "channel_id": channel_id,
                            "url": f"https://www.youtube.com/watch?v={vid}" if vid else ""
                        }
                        count_found += 1
                except Exception:
                    pass
            print(f"    Tìm thấy {count_found} video Nhật thỏa mãn (view >= 100k, dài >= 3 phút).")
        except Exception as e:
            print(f"    Lỗi quét '{query}': {e}")
        time.sleep(1)

    print(f"\n==> TỔNG SỐ VIDEO TIẾNG NHẬT ĐẠT >= 100.000 VIEW: {len(videos)}")
    
    # Gom nhóm theo channel
    channels_map = defaultdict(list)
    for v in videos.values():
        cid = v["channel_id"] or v["channel_url"] or v["channel"]
        channels_map[cid].append(v)
        
    print(f"==> Thuộc về {len(channels_map)} kênh khác nhau.\n")
    print("--> Đang kiểm tra ngày thành lập của từng kênh...")
    
    channel_stats = []
    
    for idx, (cid, v_list) in enumerate(channels_map.items(), 1):
        sample = v_list[0]
        cname = sample["channel"]
        curl = sample["channel_url"]
        chid = sample["channel_id"]
        
        print(f"[{idx}/{len(channels_map)}] Kênh: {cname} (có {len(v_list)} video >= 100k view)...")
        date_str = get_channel_joined_date(curl, chid)
        
        if date_str:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            age_days = (TODAY - dt).days
            age_months = age_days / 30.4375
            is_new = age_days <= 365
        else:
            age_days = None
            age_months = None
            is_new = False
            
        max_view = max(v["views"] for v in v_list)
        total_qualifying = len(v_list)
        top_video = sorted(v_list, key=lambda x: x["views"], reverse=True)[0]
        
        channel_stats.append({
            "name": cname,
            "channel_id": chid,
            "url": curl if curl and curl.startswith("http") else (f"https://www.youtube.com/channel/{chid}" if chid else ""),
            "joined_date": date_str or "Unknown",
            "age_days": age_days,
            "age_months": round(age_months, 1) if age_months is not None else None,
            "is_new": is_new,
            "qualifying_videos_count": total_qualifying,
            "max_view": max_view,
            "top_video_title": top_video["title"],
            "top_video_views": top_video["views"],
            "top_video_url": top_video["url"]
        })
        time.sleep(0.5)

    known_channels = [c for c in channel_stats if c["age_days"] is not None]
    new_channels = [c for c in known_channels if c["is_new"]]
    old_channels = [c for c in known_channels if not c["is_new"]]
    
    all_views = [v["views"] for v in videos.values()]
    median_views = statistics.median(all_views) if all_views else 0
    mean_views = statistics.mean(all_views) if all_views else 0
    
    new_ratio = (len(new_channels) / len(known_channels) * 100) if known_channels else 0
    
    new_channels_sorted = sorted(new_channels, key=lambda x: x["max_view"], reverse=True)
    
    results = {
        "survey_date": TODAY.strftime("%Y-%m-%d"),
        "total_qualifying_videos": len(videos),
        "total_unique_channels": len(channels_map),
        "known_age_channels": len(known_channels),
        "new_channels_count": len(new_channels),
        "old_channels_count": len(old_channels),
        "new_channels_ratio_percent": round(new_ratio, 2),
        "median_views": int(median_views),
        "mean_views": int(mean_views),
        "new_channels_list": new_channels_sorted,
        "all_channels": channel_stats
    }
    
    out_file = os.path.join(SCRATCH_DIR, "survey_psychology_results.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
        
    print("\n" + "="*60)
    print("=== BÁO CÁO KHẢO SÁT NGÁCH TÂM LÝ HỌC (NHẬT BẢN) ===")
    print("="*60)
    print(f"Tổng số video tiếng Nhật đạt >= 100.000 view: {len(videos)}")
    print(f"Tổng số kênh xác định được ngày tạo: {len(known_channels)}")
    print(f"Số kênh MỚI (lập <= 12 tháng): {len(new_channels)}")
    print(f"Số kênh CŨ (> 12 tháng): {len(old_channels)}")
    print(f"--> TỶ LỆ KÊNH MỚI ĐANG THẮNG: {new_ratio:.2f}%")
    print(f"--> View TRUNG VỊ (Median Views): {int(median_views):,} views")
    print(f"--> View TRUNG BÌNH (Mean Views): {int(mean_views):,} views\n")
    print("TOP CÁC KÊNH MỚI (< 12 THÁNG) ĐANG THẮNG LỚN:")
    for i, c in enumerate(new_channels_sorted[:10], 1):
        print(f"  {i}. {c['name']} (Tuổi: {c['age_months']} tháng - Lập ngày: {c['joined_date']})")
        print(f"     View cao nhất: {c['max_view']:,} views")
        print(f"     Video: {c['top_video_title'][:60]}...")
        print(f"     Link kênh: {c['url']}")
    print("="*60)

if __name__ == "__main__":
    main()
