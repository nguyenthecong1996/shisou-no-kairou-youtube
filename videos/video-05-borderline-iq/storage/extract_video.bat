@echo off
chcp 65001 > nul
echo =================================================================
echo  [1/3] Đang ghép các phần zip trên Windows...
echo =================================================================
copy /b final_video_borderline_iq_japanese.zip.part_* final_video_borderline_iq_japanese.zip

echo  [2/3] Đang giải nén video master...
tar -xf final_video_borderline_iq_japanese.zip

echo  [3/3] Đang dọn dẹp file zip tạm...
del final_video_borderline_iq_japanese.zip

echo =================================================================
echo Hoàn tất giải nén Video Master #5!
echo  - final_video_borderline_iq_japanese.mp4
echo =================================================================
pause
