# Kế hoạch Sản xuất Toàn diện: Video 2 Full Tiếng Nhật (15 Cuts, 15 Phút 20 Giây)

Dựa trên kịch bản tiếng Nhật hoàn chỉnh [kich-ban-video-2-tieng-nhat.md](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/kich-ban-video-2-tieng-nhat.md) và bộ 16 hình ảnh AI Dark Academia độc bản đã tạo sẵn, hệ thống lập kế hoạch chi tiết để nạp vào công cụ tự động hóa sản xuất video (Z-Mech Production Pipeline) với thời lượng **15 phút 20 giây** (920 giây), chuẩn phong cách thư giãn triết lý Nhật Bản (**Kikilagashi Style - 聞き流し**).

---

## 1. Mục tiêu & Tiêu chuẩn Sản xuất (Production Standards)

### 🎙️ Ngôn ngữ & Thuyết minh (Voiceover):
* **Giọng đọc:** Giọng nam Tokyo chuẩn `ja-JP-KeitaNeural` (hoặc `Voicepeak Male`), tốc độ thong thả **0.92x** (~320 ký tự/phút).
* **Định dạng:** 15 file audio tương ứng 15 Cuts (`storage/tasks_v2_ja/cut_ja_{i}/voice.mp3`) và file phụ đề `.srt` đồng bộ 100% ngữ âm.
* **Chuẩn hóa âm thanh:** Volume normalize đạt chuẩn phát thanh **-14 LUFS** (Peak: -1.0 dB).

### 🖋️ Typography & Phụ đề tiếng Nhật:
* **Font chữ:** `NotoSansCJK-Bold.ttc` (hoặc `ShipporiMincho-Bold.ttf` cho phong cách Dark Academia cổ kính).
* **Màu sắc:** Kem ấm `#FFF8E7`, viền đen nét mảnh `#000000` (độ dày 2.5px), tạo cảm giác êm mắt khi xem đêm trước khi ngủ.
* **Vị trí căn chỉnh:** Căn giữa màn hình (Center-Bottom), `MarginV: 75px` (chống bị che khuất bởi thanh Progress Bar của YouTube).

### ⏳ Quy chuẩn Nhịp điệu & Chuyển cảnh (Kikilagashi Style):
* **Thời lượng mỗi shot:** Kéo dài từ **11s đến 14s** (loại bỏ hoàn toàn cảm giác giật vội).
* **Chuyển cảnh:** Hòa tan mềm mại (Crossfade / Dissolve thời lượng **1.0s**) bằng bộ lọc FFmpeg:
  ```text
  xfade=transition=fade:duration=1.0:offset={T}
  ```
* **Chuyển động Ken Burns:** Chuyển động cực chậm (Slow Zoom In / Pan) trên canvas độ phân giải cao **8000x4500**, triệt tiêu 100% lỗi rung giật điểm ảnh (micro-jitter) trước khi downscale về 1920x1080.

### 🛡️ 0% Lặp hình (Zero Repetition) & Văn hóa Nhật Bản:
* **77 Clips độc bản:** Toàn bộ video được cấu thành từ 77 clips ngắn (11s–13s/clip). Tuyệt đối **không lặp lại bất kỳ hình ảnh hay clip nào** xuyên suốt 15 phút 20 giây.
* **100% Thuần Nhật Bản:** Tư liệu B-Roll Pexels / Video-AC được kiểm duyệt khắt khe: Phố mưa Tokyo, văn phòng Marunouchi, giảng đường đại học cổ kính, vườn Zen mưa, trà đạo, thư viện sách cổ. **Tuyệt đối không có chữ tiếng Nga/Cyrillic, không hình xăm, không biển hiệu đèn đỏ.**

### 🎵 Nhạc nền Bản quyền An toàn:
* **Track BGM:** `Kiss the Sky (Aakash Gandhi)` kết hợp tiếng mưa rơi tự nhiên `storage/bgm/kiss_the_sky_rain.mp3`.
* **Thông số hòa âm:** Âm lượng `0.18` (-16 dB), fade-out 3.5s ở cuối video. Bảo đảm an toàn bật kiếm tiền (YPP) 100%.

---

## 2. Phân tích Chi tiết 15 Cuts & Ma trận Phân bổ Tư liệu (77 Clips)

| Cut # | Tiêu đề Phân đoạn (Tiếng Nhật & Ý nghĩa) | Thời lượng Audio | Số Clip Cần (11–13s/clip) | Tư liệu Kết hợp (Ảnh AI Độc Bản + B-Roll Nhật Bản Pexels/Video-AC) |
| :---: | :--- | :---: | :---: | :--- |
| **01** | 和室書斎のコンパス円形図面<br>*(Vòng tròn compa trên giấy washi)* | 45.0s | **4 clips** | • **Clip 1 (AI):** [v2_cut1_cake_compass_1793094055730.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut1_cake_compass_1793094055730.jpg) (Slow zoom)<br>• **Clip 2 (Pexels):** Khói trà xanh bốc lên cạnh hiên nhà gỗ dưới mưa (`japanese tea ceremony tatami room`)<br>• **Clip 3 (Pexels):** Giọt mưa lăn trên ô cửa sổ gỗ kiểu Nhật (`rain dripping wooden roof`)<br>• **Clip 4 (AI):** Cận cảnh compa đồng và nét mực đen trên giấy washi |
| **02** | 放射状3分割 vs 縦2本分割の比較<br>*(So sánh 2 cách cắt bánh)* | 45.0s | **4 clips** | • **Clip 1 (AI):** [v2_cut2_divided_cake_1793094077443.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut2_divided_cake_1793094077443.jpg) (Pan ngang)<br>• **Clip 2 (Pexels):** Bàn tay cầm bút máy viết lên giấy kẻ ô Genkou (`fountain pen writing japanese paper`)<br>• **Clip 3 (Video-AC):** Dao cắt bánh đặt tĩnh lặng bên đĩa gốm mộc (`ケーキ 切り分け`)<br>• **Clip 4 (AI):** Cận cảnh 2 đường cắt thẳng đứng song song kỳ lạ |
| **03** | 東大講義室と正規分布ベル曲線<br>*(Giảng đường Todai & Đồ thị chuông)* | 55.0s | **5 clips** | • **Clip 1 (AI):** [v2_cut3_bell_curve_1793094125285.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut3_bell_curve_1793094125285.jpg) (Slow pan)<br>• **Clip 2 (Pexels):** Giáo sư viết phấn trắng lách cách lên bảng đen (`chalkboard writing math formula`)<br>• **Clip 3 (Pexels):** Giảng đường đại học cổ kính ngập bụi nắng qua cửa vòm (`vintage university lecture hall`)<br>• **Clip 4 (AI):** Zoom chi tiết dải số 70 đến 84 trên đường cong chuẩn<br>• **Clip 5 (Pexels):** Sinh viên Nhật ngồi chăm chú lắng nghe trong giảng đường (`japanese college students`) |
| **04** | 境界知能IQ70の日常と書類の困惑<br>*(IQ 70: Bối rối trước thủ tục hành chính)* | 70.0s | **6 clips** | • **Clip 1 (AI):** [v2_cut4_iq70_confusion_1793094233671.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut4_iq70_confusion_1793094233671.jpg) (Focus ánh mắt)<br>• **Clip 2 (Video-AC):** Đóng con dấu mộc đỏ Inkan lên tờ khai thuế (`印鑑 捺印 書類`)<br>• **Clip 3 (Pexels):** Ngã tư Tokyo mưa đêm phản chiếu ánh đèn neon qua kính xe (`tokyo street rain night neon`)<br>• **Clip 4 (Pexels):** Ngón tay mệt mỏi lật các trang hợp đồng dày đặc chữ Kanji (`flipping paperwork contract fatigue`)<br>• **Clip 5 (AI):** Góc nghiêng người đàn ông xoa thái dương bất lực<br>• **Clip 6 (Pexels):** Đồng tiền xu Nhật Bản nằm trên mặt bàn gỗ tối màu (`japanese yen coins wooden table`) |
| **05** | 少年院の面談室と境界知能の悲劇<br>*(Phòng tư vấn & Bi kịch ranh giới)* | 75.0s | **6 clips** | • **Clip 1 (AI):** [v2_cut5_juvenile_tragedy_1793094336310.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut5_juvenile_tragedy_1793094336310.jpg) (Slow pan)<br>• **Clip 2 (Video-AC):** Lớp học trường cấp 3 Nhật Bản chiều tà vắng lặng (`学校 教室 放課後 夕方`)<br>• **Clip 3 (Pexels):** Đồng hồ treo tường cổ điển giật từng giây (`antique wall clock ticking pendulum`)<br>• **Clip 4 (Pexels):** Bàn tay học sinh siết chặt vạt áo đồng phục thể hiện tự ti (`nervous hands student desk`)<br>• **Clip 5 (AI):** Gương mặt người thầy tư vấn đăm chiêu thấu cảm<br>• **Clip 6 (Pexels):** Cửa sổ hành lang trường học lay nhẹ trong gió chiều (`school corridor window breeze`) |
| **06** | 丸の内の整然としたオフィスとIQ100<br>*(IQ 100: Chuẩn mực của xã hội)* | 55.0s | **5 clips** | • **Clip 1 (AI):** [v2_cut6_iq100_office_1793150220626.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut6_iq100_office_1793150220626.jpg) (Pan từ bàn ra cửa sổ)<br>• **Clip 2 (Pexels):** Dòng nhân viên văn phòng vest đen rảo bước qua ga Marunouchi (`tokyo business salaryman walking`)<br>• **Clip 3 (Video-AC):** Đồng nghiệp văn phòng gõ phím nhịp nhàng đều đặn (`オフィス 業務 パソコン`)<br>• **Clip 4 (Pexels):** Dòng người che ô trật tự sang đường ngã tư Tokyo (`tokyo pedestrian crossing umbrella orderly`)<br>• **Clip 5 (AI):** Bàn tay cầm bút dạ đánh dấu hoàn thành checklist sổ tay |
| **07** | IQ100の死角・マニュアル喪失のパニック<br>*(Điểm mù IQ 100: Tê liệt khi mất quy trình)* | 60.0s | **5 clips** | • **Clip 1 (AI):** [v2_cut7_iq100_panic_1793150247285.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut7_iq100_panic_1793150247285.jpg) (Zoom cận người)<br>• **Clip 2 (Video-AC):** Nhân viên ôm đầu trước màn hình tăng ca đêm muộn (`頭を抱える ビジネスマン 残業`)<br>• **Clip 3 (Pexels):** Con lắc đồng hồ kim loại đu đưa tích tắc gay gắt (`vintage grandfather clock pendulum swing`)<br>• **Clip 4 (AI):** Cận cảnh ánh mắt bàng hoàng nhìn vào con số 0<br>• **Clip 5 (Pexels):** Đèn văn phòng tắt dần chỉ còn lại ánh sáng xanh màn hình (`dark empty office night computer glow`) |
| **08** | IQ130の思考マインドマップと抽象ネットワーク<br>*(IQ 130: Bản đồ tư duy trực quan 3D)* | 60.0s | **5 clips** | • **Clip 1 (AI):** [v2_cut8_iq130_mindmap_1793150276641.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut8_iq130_mindmap_1793150276641.jpg) (Camera lượn theo hạt sáng)<br>• **Clip 2 (Pexels):** Lật nhanh các trang sách triết học dày cộp dưới ánh đèn vàng (`flipping heavy book pages library night`)<br>• **Clip 3 (Pexels):** Mạng lưới sợi quang và hạt sáng kết nối dạng nơ-ron (`abstract golden plexus network lines`)<br>• **Clip 4 (AI):** Cận cảnh các ký tự Kanji (理, 心, 知, 実存主義) tự xoay chuyển<br>• **Clip 5 (Video-AC):** Thư viện gỗ sồi với hàng ngàn cuốn sách tĩnh mịch (`本 ページめくり 書斎`) |
| **09** | 会議室の退屈と摩擦・孤立するギフテッド<br>*(Sự buồn chán và ma sát trong phòng họp)* | 65.0s | **5 clips** | • **Clip 1 (AI):** [v2_cut9_iq130_boredom_1793150305271.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut9_iq130_boredom_1793150305271.jpg) (Focus vào chàng trai)<br>• **Clip 2 (Video-AC):** Ban giám đốc Tokyo tranh cãi căng thẳng quanh máy chiếu (`会議室 議論 日本人 重役`)<br>• **Clip 3 (Pexels):** Ngón tay chàng trai xoay chiếc bút bi trong vô thức buồn chán (`bored hand tapping pen table`)<br>• **Clip 4 (AI):** Ánh nhìn cô độc hướng ra cửa sổ trời mưa ngoài phòng họp<br>• **Clip 5 (Pexels):** Chiếc đồng hồ tròn trên tường phòng họp trôi chậm chạp (`office wall clock slow movement`) |
| **10** | IQ160の宇宙・触れる抽象概念の風景<br>*(IQ 160: Khái niệm trừu tượng thành cảnh quan)* | 65.0s | **5 clips** | • **Clip 1 (AI):** [v2_cut10_iq160_cosmos_1793150332332.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut10_iq160_cosmos_1793150332332.jpg) (Vũ trụ xoay chuyển)<br>• **Clip 2 (Video-AC):** Vòm kính thiên văn mở ra dải ngân hà vùng núi tuyết Nhật (`星空 タイムラプス 天の川`)<br>• **Clip 3 (Pexels):** Dải sao băng bay qua bầu trời đêm vắt ngang núi (`night sky milky way stars timelapse`)<br>• **Clip 4 (Pexels):** Bàn tay phác thảo các mô hình hình học không gian đa chiều (`hands sketching geometry diagrams`)<br>• **Clip 5 (AI):** Cận cảnh khối đa diện phát sáng lơ lửng như vật thể thực |
| **11** | 深夜の鏡像・絶対的な孤独と非同期発達<br>*(Bi kịch IQ 160: Cô độc tuyệt đối 2h sáng)* | 70.0s | **6 clips** | • **Clip 1 (AI):** [v2_cut11_iq160_isolation_1793150362507.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut11_iq160_isolation_1793150362507.jpg) (Camera lùi xa dần)<br>• **Clip 2 (Video-AC):** Giọt mưa ròng ròng trên mặt kính mờ hơi nước nhìn ra Tokyo (`窓 雨粒 夜景 東京`)<br>• **Clip 3 (Pexels):** Bóng lưng người ngồi lặng lẽ trong phòng tối đêm khuya (`silhouette person sitting alone dark room`)<br>• **Clip 4 (AI):** Cận cảnh gương mặt phản chiếu trong gương với ánh mắt kiệt sức<br>• **Clip 5 (Pexels):** Khói thuốc hoặc hơi thở tan chậm trong không gian tĩnh mịch (`smoke swirling slow motion dark room`)<br>• **Clip 6 (Video-AC):** Chiếc đèn bàn vàng hắt bóng đơn độc trên sàn gỗ (`一人 孤独 影 部屋`) |
| **12** | ターマンの70年研究記録アーカイブ<br>*(Nghiên cứu 70 năm của Terman)* | 60.0s | **5 clips** | • **Clip 1 (AI):** [v2_cut12_terman_archive_1793150393854.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut12_terman_archive_1793150393854.jpg) (Lật tài liệu cổ)<br>• **Clip 2 (Pexels):** Ngón tay kéo ngăn kéo thẻ mục lục thư viện cổ bằng gỗ sồi (`vintage archive library drawer card catalog`)<br>• **Clip 3 (Video-AC):** Lật từng trang sách ố vàng phủ bụi của thế kỷ 20 (`古文書 図書館 書架`)<br>• **Clip 4 (Pexels):** Tấm ảnh chụp chân dung trắng đen lịch sử với con dấu đỏ (`vintage photographs sepia portraits`)<br>• **Clip 5 (AI):** Cận cảnh số liệu thống kê 1.500 đứa trẻ thiên tài |
| **13** | フリン効果・100年の知能変遷<br>*(Hiệu ứng Flynn: 100 năm tiến hóa nhận thức)* | 70.0s | **6 clips** | • **Clip 1 (AI):** [v2_cut13_flynn_effect_1793150426994.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut13_flynn_effect_1793150426994.jpg) (Chuyển thời đại)<br>• **Clip 2 (NHK / Pexels):** Thợ mộc truyền thống Nhật (Miyadaiku) đục mộng gỗ dựng nhà (`traditional japanese carpentry timber`)<br>• **Clip 3 (NHK Archive):** Nông thôn Nhật Bản thời Đại Chính cần cù trên ruộng lúa (`大正 昭和 日本 農村 木造建築`)<br>• **Clip 4 (Pexels):** Chuyển cảnh sang đoàn tàu Shinkansen lao vút qua Tokyo mưa (`shinkansen train bullet train tokyo speed`)<br>• **Clip 5 (Pexels):** Đường chân trời Tokyo hiện đại với tháp Tokyo Skytree (`tokyo city skyline overcast`)<br>• **Clip 6 (AI):** Nhân vật hiện đại đứng ngắm nhìn sự tiếp nối thế hệ |
| **14** | 翻訳者（トランスレーター）の架け橋<br>*(Đỉnh cao trí tuệ: Kẻ Phiên Dịch)* | 65.0s | **5 clips** | • **Clip 1 (AI):** [v2_cut14_the_translator_1793150461564.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut14_the_translator_1793150461564.jpg) (Zoom trang vẽ)<br>• **Clip 2 (Video-AC):** Cọ lông chấm mực đen Sumi vẽ nét uyển chuyển trên giấy (`書道 筆 墨 手元`)<br>• **Clip 3 (Pexels):** Hai đồng nghiệp gật đầu mỉm cười thấu hiểu trên bàn trà (`two colleagues nodding smiling meeting`)<br>• **Clip 4 (AI):** Bản vẽ sơ đồ 3 bước hành động tỏa sáng ấm áp giữa bàn<br>• **Clip 5 (Video-AC):** Ánh đèn lồng Washi tỏa ánh sáng vàng dịu trong phòng trà (`和室 対話 笑顔`) |
| **15** | 夜明けの東京と富士山・思索の回廊<br>*(Kết luận: Khác biệt góc nhìn & Bình minh)* | 60.0s | **5 clips** | • **Clip 1 (AI):** [v2_cut15_tokyo_dawn_1793150500103.jpg](file:///home/congnt/.gemini/antigravity/brain/ab250fd5-bd65-43cf-be15-51525e9c4f5a/v2_cut15_tokyo_dawn_1793150500103.jpg) (Toàn cảnh bình minh)<br>• **Clip 2 (Video-AC):** Núi Phú Sĩ ửng hồng trong ánh bình minh rạng rỡ qua biển mây (`富士山 朝焼け 絶景`)<br>• **Clip 3 (Pexels):** Tách trà xanh gốm sứ Nhật Bản nghi ngút khói bên cửa sổ (`steaming green tea ceramic cup table`)<br>• **Clip 4 (AI):** Bàn tay khẽ khép cuốn sổ da ghi chép suy tưởng<br>• **Clip 5 (Pexels):** Bầu trời Tokyo sáng bừng trong veo đón ngày mới (`tokyo morning sunrise sky peaceful`) |

> **Tổng kết Phân bổ:** **15 Cuts = 77 Clips độc lập** (15 Tranh AI Dark Academia + 62 Video B-Roll Pexels/Video-AC/NHK). Tỷ lệ lặp lại: **0.0%**.

---

## 3. Quy trình Triển khai Kỹ thuật (Implementation Plan)

### Bước 1: Thu thập & Chuẩn hóa Kho Footage Nhật Bản (`storage/pexels_curated_v2_ja/`)
1. Tải về 62 video clips theo đúng các từ khóa trong bảng trên từ Pexels API / Video-AC.
2. Chuẩn hóa tất cả clips thành chuẩn đồng nhất bằng lệnh FFmpeg:
   ```bash
   ffmpeg -i input.mp4 -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30" -an -c:v libx264 -preset fast -crf 18 storage/pexels_curated_v2_ja/clip_{id}.mp4 -y
   ```

### Bước 2: Tạo các clips Ken Burns cho 15 Tranh AI Độc Bản
1. Tạo chuyển động pan/zoom siêu chậm từ canvas 8000x4500 về 1920x1080 cho 15 tranh AI tương ứng với thời lượng của từng Cut (mỗi tranh xuất hiện 2 lần: lần 1 làm Keyframe 12s, lần 2 làm Zoom chi tiết 11s).
2. Lệnh FFmpeg mẫu chống rung:
   ```bash
   ffmpeg -loop 1 -i v2_cut_{i}.jpg -vf "scale=8000:4500,zoompan=z='min(zoom+0.0006,1.15)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=360:s=1920x1080:fps=30" -t 12 -c:v libx264 -pix_fmt yuv420p storage/tasks_v2_ja/cut_ja_{i}/ai_clip.mp4 -y
   ```

### Bước 3: Dựng 15 Cuts độc lập với hòa tan Crossfade 1.0s & Phụ đề Tiếng Nhật
1. Ghép 4 đến 6 clips thành phần trong mỗi Cut bằng bộ lọc xfade:
   ```bash
   ffmpeg -i clip1.mp4 -i clip2.mp4 -i clip3.mp4 -i clip4.mp4 \
     -filter_complex "[0:v][1:v]xfade=transition=fade:duration=1.0:offset=11[v01]; \
                      [v01][2:v]xfade=transition=fade:duration=1.0:offset=22[v02]; \
                      [v02][3:v]xfade=transition=fade:duration=1.0:offset=33[v03]" \
     -map "[v03]" -c:v libx264 -pix_fmt yuv420p storage/tasks_v2_ja/cut_ja_{i}/video_stitched.mp4 -y
   ```
2. Đốt phụ đề tiếng Nhật `.srt` bằng font `NotoSansCJK-Bold.ttc`, màu `#FFF8E7`, `MarginV: 75px` và ghép file âm thanh giọng đọc `ja-JP-KeitaNeural`.

### Bước 4: Ghép nối 15 Cuts & Master Nhạc Nền Xuyên suốt 15 Phút 20 Giây
1. Nối 15 cuts thành Master Video dài 920 giây bằng `concat`.
2. Mix track âm thanh `kiss_the_sky_rain.mp3` ở mức volume `0.18`, áp dụng fade-out 3.5s ở giây thứ 916.5:
   ```bash
   ffmpeg -i master_concat.mp4 -i storage/bgm/kiss_the_sky_rain.mp3 \
     -filter_complex "[1:a]volume=0.18,afade=t=out:st=916.5:d=3.5[bgm]; \
                      [0:a][bgm]amix=inputs=2:duration=first:dropout_transition=2[aout]" \
     -map 0:v -map "[aout]" -c:v copy -c:a aac -b:a 192k storage/final_video_iq70_vs_iq160_japanese.mp4 -y
   ```

---

## 4. Kế hoạch Xác minh (Verification Plan)

### 🔬 Kiểm tra Kỹ thuật Tự động:
* **Thời lượng:** Dùng `ffprobe` kiểm tra đạt chính xác **920s ± 2s** (~15 phút 20 giây).
* **Độ phân giải & Frame Rate:** 1920x1080, chuẩn 30.0 fps, bitrate 5.000–6.000 kbps.
* **Âm thanh:** AAC Stereo 192 kbps, sampling rate 48.000 Hz, âm lượng voiceover nổi bật rõ nét trên tiếng mưa rào và nhạc piano.
* **Không lặp hình:** Quét mã băm perceptual hash (pHash) trên 77 clips để xác nhận 0% trùng lặp.

### 👁️ Kiểm tra Thẩm mỹ & Trải nghiệm Khán giả:
* Trích xuất frame tại các giây thứ 10, 45, 120, 300, 600, 900 để kiểm tra độ sắc nét của font chữ Kanji, đảm bảo phụ đề nằm gọn gàng phía trên thanh điều khiển của YouTube.
* Xác nhận 100% bối cảnh mang đậm không khí trí thức Tokyo, không xuất hiện các chi tiết lạc lõng của văn hóa Tây phương.
