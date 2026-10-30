import sys, os, json, subprocess, time
from pathlib import Path

# Add watch scripts to sys.path
sys.path.insert(0, "/home/congnt/.agents/skills/watch/scripts")
from whisper import transcribe_video

VIDEO_DIR = Path("/home/congnt/Documents/Codex/2026-10-27/h-y/outputs/hanh-trinh-30-ngay")
SCRATCH = Path("/home/congnt/.gemini/antigravity/scratch")
TRANSCRIPT_DIR = SCRATCH / "transcripts"
FRAMES_DIR = SCRATCH / "frames"
AUDIO_DIR = SCRATCH / "audio"

TRANSCRIPT_DIR.mkdir(parents=True, exist_ok=True)
FRAMES_DIR.mkdir(parents=True, exist_ok=True)
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

# List of files in logical order
file_order = [
    "Mở đầu - Ý tưởng - Hành trình 30 ngày làm youtube kiếm tiền [1723472608768948].mp4",
    "01 - Tìm chủ đề - Hành trình 30 ngày kiếm tiền với youtube [2112433349657962].mp4",
    "02 - Hành trình 30 ngày kiếm tiền với youtube - xác định thị trường với tuyến nội dung [1377703687671619].mp4",
    "03 - Thiết lập kênh - Hành trình 30 ngày kiếm tiền với youtube [1620637799670844].mp4",
    "Ngày 04 - Hành trình 30 ngày kiếm tiền với Youtube [2061965827745612].mp4",
    "Ngày 05 - Hành trình 30 ngày kiếm tiền với Youtube [903185092578685].mp4",
    "Ngày 06 - Hành trình 30 ngày kiếm tiền với Youtube [1708286400274624].mp4",
    "Ngày 07 - Hành trình 30 ngày kiếm tiền với Youtube [1601953424903510].mp4",
    "Ngày 08 - Hành trình 30 ngày kiếm tiền với Youtube [1473733357914042].mp4",
    "Ngày 09 - Hành trình 30 ngày kiếm tiền với Youtube - Công thức v7 [2114962119102648].mp4",
    "Ngày 10 - Kéo kênh mới - Hành trình 30 ngày kiếm tiền với youtube [1403200464610194].mp4",
    "Ngày 11 - Doanh nghiệp 1 người với Youtube - Hành trình 30 ngày kiếm tiền với ytb [855287190975603].mp4",
    "Ngày 12 - Xử lý 0 view, cách ly kênh ytb [1138954905324585].mp4",
]

def format_ts(seconds):
    m = int(seconds // 60)
    s = int(seconds % 60)
    return f"{m:02d}:{s:02d}"

for idx, filename in enumerate(file_order, 1):
    video_path = VIDEO_DIR / filename
    slug = f"{idx:02d}_{video_path.stem[:30]}".replace(" ", "_").replace("/", "_")
    json_path = TRANSCRIPT_DIR / f"{slug}.json"
    txt_path = TRANSCRIPT_DIR / f"{slug}.txt"
    video_frames_dir = FRAMES_DIR / slug
    video_frames_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n[{idx}/{len(file_order)}] Processing {filename}...")
    
    # 1. Transcribe if not done
    if not json_path.exists():
        audio_tmp = AUDIO_DIR / f"{slug}.mp3"
        try:
            segments, backend = transcribe_video(str(video_path), audio_tmp, backend="groq")
            data = {"file": filename, "segments": segments, "backend": backend}
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(f"# {filename}\n\n")
                for s in segments:
                    f.write(f"[{format_ts(s['start'])}] {s['text'].strip()}\n")
            print(f"Transcribed {len(segments)} segments.")
        except Exception as e:
            print(f"Transcription error: {e}")
        # Small sleep to respect rate limits
        time.sleep(2)
    else:
        print(f"Transcript exists: {json_path}")
        
    # 2. Extract frames (1 frame every 10 seconds)
    existing_frames = list(video_frames_dir.glob("*.jpg"))
    if not existing_frames:
        print(f"Extracting frames to {video_frames_dir}...")
        cmd = [
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
            "-i", str(video_path),
            "-vf", "fps=1/10,scale=720:-1",
            str(video_frames_dir / "frame_%03d.jpg")
        ]
        subprocess.run(cmd)
        print(f"Extracted {len(list(video_frames_dir.glob('*.jpg')))} frames.")
    else:
        print(f"Frames already extracted ({len(existing_frames)} frames).")

print("\nAll videos processed successfully!")
