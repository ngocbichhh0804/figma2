# figma2 — Figma → HTML/CSS

Chuyển thiết kế Figma sang HTML semantic + CSS thuần. Không framework, không
bước build, **không một dòng JavaScript nào được gửi xuống trình duyệt**.

Chú thích trong code viết tiếng Việt cho dễ đọc lúc phát triển — chuyển sang
tiếng Anh trước khi bàn giao.

## Quy ước bắt buộc — đọc trước khi sửa bất cứ gì

- **Không flexbox, không grid, không `gap`.** Bố cục dựng bằng `float` +
  `calc()`, `clear`, `flow-root`, `inline-block` + `font-size: 0` ở cha,
  `line-height` + `vertical-align`, `position: absolute`.
- **Không JavaScript** trên trang giao cho khách. Trạng thái mở/đóng dùng
  `:target`, `<details>`, radio/checkbox + `:has()`. `dev/*-overlay.html` là
  công cụ nội bộ (cũng không JS).
- **CSS chia theo cascade layer**, khai báo một lần trong `<head>`:
  `reset, tokens, base, layout, components, utilities`. Không `!important`
  (trừ khối `prefers-reduced-motion`).
- **`css/tokens.css` chỉ chứa giá trị dùng chung** (màu, font, thang độ đậm,
  leading, chuyển động, bo góc). Số đo riêng của component ghi thẳng trong
  file component. Số dùng ở nhiều rule trong cùng component thì làm biến cục
  bộ trên selector gốc (vd. `.card { --card-title-gap: 87px; }`), không đưa lên
  `:root`. Mọi con số đều ghi nhãn nguồn gốc ngay bên cạnh:
  - `[FIGMA]` — đọc thẳng từ panel inspector
  - `[ĐO]` — đo bằng script quét pixel trên ảnh export 1:1
  - `[MẪU]` — lấy từ file asset được cung cấp
  - `[ƯỚC]` — ước lượng, chờ xác nhận lại
- Đặt tên BEM, specificity phẳng, không selector lồng quá một cấp, không dùng
  ID để style.
- **Pixel-perfect**: mỗi trang render đúng khổ khung Figma; đối chiếu bằng
  overlay + script so pixel. Đã chốt số đo thì không đổi.
- Font thương mại → thay bằng font OFL, tự lưu `.woff2` trong `assets/fonts/`
  (không gọi Google Fonts).

## Cấu trúc

```
*.html                   mỗi trang Figma một file
css/
├── reset.css / fonts.css / tokens.css / base.css / layout.css
├── components/          mỗi khối một file BEM: btn, site-header, hero, category,
│                        section-head, products, reviews, video, articles,
│                        subscribe, site-footer
└── utilities.css        .visually-hidden, .skip-link
assets/fonts|icon|img/
dev/pages.json           danh sách trang (nguồn sinh overlay)
dev/*-overlay.html       đè ảnh Figma lên bản code (Code / 50% / Figma / Slider)
docs/comparison/<slug>/  <slug>-figma.png, -build, -side-by-side, -overlay, -difference
```

## Trạng thái các trang

- **Modish** (`index.html`, 1920 × 6053): đã dựng. Sai lệch TB 2.1/765, 98.9 % pixel ≤ 30,
  61/88 vùng khớp 0px (còn lại 1–2px ở mép chữ). Overlay: `dev/home-overlay.html`.
  Thông số: `docs/comparison/home/spec.md`, vùng đo: `docs/comparison/home/regions.txt`.
  Ảnh `Women.png`, `Men.png`, `Video.png` đang dính chữ/nút, chờ bản export sạch.
  Responsive: ≥ 1484px giữ đúng số Figma; < 1684px mũi tên sản phẩm xuống dưới thẻ;
  < 1200px tablet; < 768px điện thoại (1 cột). Women/Men và Video co giãn bằng biến `--u`
  (container query `cqi`) để chữ/nút HTML luôn đè khít chữ in sẵn trong ảnh.

## Font

| Font Figma | File (OFL, tự lưu) |
| --- | --- |
| Jost | `assets/fonts/jost-latin-wght-{normal,italic}.woff2` (variable) |
| Bodoni Moda | `assets/fonts/bodoni-moda-latin-opsz-normal.woff2` (variable, opsz) |
| Lora Italic | `assets/fonts/lora-latin-400-italic.woff2` |

## Chạy thử

```bash
npm install     # chỉ để có browser-sync
npm run dev     # http://localhost:3000
```

Không có npm: `python3 dev/serve.py` (như http.server nhưng gửi `Cache-Control: no-store`, Chrome không giữ CSS cũ).
