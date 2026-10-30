#!/usr/bin/env bash
# ==============================================================================
# Trình giải nén Video Master #5: 境界知能 IQ 70-84 (1080p Full HD)
# ==============================================================================
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "================================================================="
echo " [1/3] Đang ghép 14 phần lưu trữ (.zip.part_*)..."
echo "================================================================="
cat final_video_borderline_iq_japanese.zip.part_* > final_video_borderline_iq_japanese.zip

echo " [2/3] Đang kiểm tra mã toàn vẹn SHA-256..."
sha256sum -c final_video_borderline_iq_japanese.zip.sha256

echo " [3/3] Đang giải nén video & thumbnail master..."
unzip -o final_video_borderline_iq_japanese.zip

echo "--> Đang dọn dẹp file zip tạm..."
rm -f final_video_borderline_iq_japanese.zip

echo "================================================================="
echo "✅ HOÀN TẤT GIẢI NÉN THÀNH CÔNG!"
echo "   - Video Master: final_video_borderline_iq_japanese.mp4 (620.97 MB)"
echo "   - Thumbnail Master: thumbnail_video_5_borderline_iq.jpg"
echo "================================================================="
