# 🏛️ 思索の回廊@大人の教養心理学 (Shisou no Kairou - YouTube Automation Suite)

Chào mừng bạn đến với kho lưu trữ mã nguồn và tài nguyên sản xuất nội dung hoàn chỉnh của kênh YouTube **思索の回廊@大人の教養心理学** (Hành lang Tư duy - Tâm lý học Giáo dưỡng cho Người trưởng thành).

Dự án này tích hợp toàn bộ quy trình từ nghiên cứu đề tài triệu view, kiến trúc kịch bản Z-Mech 15 Cuts, prompt tạo ảnh AI Dark Academia x Tokyo Noir, tài liệu SEO đa nền tảng và hệ thống 4 AI Subagents tự động hóa hoàn toàn.

---

## 🧭 CẤU TRÚC KHO LƯU TRỮ (REPOSITORY DIRECTORY)

```text
shisou-no-kairou-youtube/
├── README.md                           # Giới thiệu kênh, triết lý sản xuất & hướng dẫn sử dụng
├── agent.md                            # Master System Prompt & Operational Context cho AI đọc hiểu
├── VIDEOS_DASHBOARD.md                 # Bảng ma trận quản trị toàn bộ Video 1 -> 6
├── .gitignore                          # Cấu hình loại trừ file rác, file tạm, cache
│
├── .agents/                            # Hệ thống 4 AI Subagents chuyên trách
│   └── agents/
│       ├── youtube_script_architect/   # Agent viết kịch bản Z-Mech 15 Cuts & nghiên cứu đối thủ
│       ├── youtube_image_generator/    # Agent tạo ảnh Chiaroscuro 16:9 Dark Academia
│       ├── youtube_uploader_bot/       # Agent tự động đăng bài qua Chrome CDP 9222
│       └── youtube_30day_expert/       # Agent cố vấn thuật toán YouTube & SOP 30 ngày
│
├── docs/                               # Cẩm nang thực chiến & phân tích chuyên sâu
│   ├── cam-nang-thuc-chien-30-ngay-an-ong-chi-tiet.md  # SOP 30 ngày bóc tách phương pháp An Ong
│   └── phan-tich-chuoi-30-ngay-kiem-tien-youtube.md    # Phân tích nguyên lý thuật toán kéo - đẩy
│
├── videos/                             # Trọn bộ kịch bản và tài nguyên chi tiết từng video
│   ├── video-01-thinking-levels/       # Video #1: Level tư duy & Sự tĩnh lặng [ID: gKO6vCPVoyM]
│   ├── video-02-iq-contrast/           # Video #2: Khoảng cách nhận thức IQ 70 vs IQ 160
│   ├── video-03-solitude-intelligence/ # Video #3: Người thông minh không hứng thú với người khác [ID: RJ7RAh76WI8]
│   ├── video-04-articulation-brain/    # Video #4: Não bộ diễn đạt ngôn từ & Kỹ thuật Feynman
│   ├── video-05-borderline-iq/         # Video #5: Trí tuệ ranh giới IQ 70-84 & Trọn bộ 16 ảnh AI
│   └── video-06-intellectual-thinking/ # Video #6: Người thông minh nghĩ gì? Não nội độc thoại
│
└── tools/                              # Scripts công cụ hỗ trợ
    ├── survey_psychology_niche.py      # Script khảo sát ma trận từ khóa ngách tâm lý
    └── batch_process.py                # Xử lý tự động hóa phụ đề và tư liệu
```

---

## ⚙️ QUY CHUẨN SẢN XUẤT Z-MECH (PRODUCTION STANDARDS)

* **Thời lượng:** 15 đến 21 phút (tối ưu hóa giữ chân người xem và doanh thu quảng cáo).
* **Cấu trúc:** 15 Cuts = đúng 75 Clips độc bản (11–13s/shot), tỷ lệ lặp lại hình ảnh: **0.0%**.
* **Phong cách thị giác:** **Dark Academia x Tokyo Noir** (Ánh sáng Chiaroscuro, bàn gỗ sồi, đèn dầu amber, mưa đêm Tokyo, sổ tay bút máy, tĩnh tại và sâu lắng).
* **Giọng đọc:** Giọng nam Tokyo chuẩn `ja-JP-KeitaNeural` (tốc độ thong thả **0.92x**, ~310-320 ký tự/phút).
* **Âm thanh:** Chuẩn phát thanh quốc tế **-14 LUFS**, nhạc nền `Kiss the Sky` hòa quyện cùng tiếng mưa rơi nhẹ tự nhiên (-16 dB).
* **Khung giờ đăng vàng:** **21:30 VN** (tức 23:30 giờ Tokyo) — đón trọn luồng khán giả trí thức nghe đêm trước khi ngủ.

---

## 🤖 HƯỚNG DẪN DÀNH CHO AI (AGENT INSTRUCTIONS)

Nếu bạn là một AI Agent (Claude, ChatGPT, Windsurf, Cursor, Antigravity) đang tiếp nhận dự án này:
👉 **Vui lòng đọc file [agent.md](./agent.md) đầu tiên** để nắm vững toàn bộ quy tắc nghiệp vụ, bảng mã màu, tiêu chuẩn giọng đọc và quy trình sản xuất các video tiếp theo.

---

## 🚀 THÔNG TIN PHÁT TRIỂN & BẢN QUYỀN

* **Kênh YouTube:** [思索の回廊@大人の教養心理学](https://www.youtube.com/channel/UCYBqrHJ4P28dFjwKTMq9ISg)
* **Email quản trị kênh:** `congnt2154@gmail.com`
* **Git Developer:** `thecong1996@gmail.com`
