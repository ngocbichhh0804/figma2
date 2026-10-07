# figma2 (Modish) — Figma → HTML/CSS

Cắt tay từ Figma sang HTML semantic và **CSS thuần**. Không framework, không
bước build, **không JavaScript**.

**Live:** _điền URL_ · **Source:** _điền URL_ · **Thiết kế:** _điền link Figma_

## Độ khớp với bản thiết kế

| Trang | Khung Figma | Sai lệch màu TB (/765) | Pixel lệch ≤ 30 | Ghi chú |
| --- | --- | --- | --- | --- |
| Modish (`index.html`) | 1920 × 6053 | 2.1 | 98.9 % (≤ 60: 99.6 %) | 61/88 vùng khớp 0px, phần còn lại lệch 1–2px ở mép chữ |

Ảnh đối chiếu nằm trong `docs/comparison/<trang>/`. Tự kiểm trực tiếp: mở
`dev/<trang>-overlay.html` (bốn chế độ Code only / Overlay 50% / Figma only /
Slider — không JavaScript, nút là radio input đọc bằng `:has()`).

"Code only" hiện ảnh chụp bản code 1x (`<slug>-build.png`) thay cho trang chạy
trực tiếp, để so độ đậm nét chữ cùng độ phân giải với ảnh Figma trên màn Retina.
Ảnh là bản chụp: sửa CSS xong chạy lại `compare.py … --out docs/comparison/<slug> <slug>`.

## Không flexbox, không grid

Bố cục dựng bằng kỹ thuật trước thời flexbox: `float` + `calc()`, `flow-root`,
`inline-block` + `font-size: 0`, `line-height` + `vertical-align`,
`position: absolute`.

## Font

Cả ba font trong Figma đều là font mở (SIL OFL) nên dùng đúng font gốc, tự lưu woff2 (latin) trong `assets/fonts/`.

| Font Figma | Dùng | File | Weight |
| --- | --- | --- | --- |
| Jost | chữ thân, nav, nút, tiêu đề mục | `jost-latin-wght-normal/italic.woff2` (variable) | 300 / 400 / 500 / 700 |
| Bodoni Moda | tiêu đề lớn (hero, Women/Men, Reviews, Subscribe) | `bodoni-moda-latin-opsz-normal.woff2` (variable, trục opsz) | 400 |
| Lora Italic | logo "modish." | `lora-latin-400-italic.woff2` | 400 |

## Chỗ khác bản thiết kế

- Trang Modish: vài số không có ảnh panel Figma nên đo trên ảnh export và ghi nhãn `[ĐO]`. Ví dụ: tiêu đề "Customer's reviews" / "Subscribe us" là Bodoni Moda 102px, ls 6 %; trích dẫn là Jost 300, 26px, ls 0.02em; giá và tên khách là Jost 700; link đang chọn (ABOUT) là Jost 500; placeholder là Jost đứng 285 nghiêng giả 14° (Figma không dùng Jost Italic thật, xem `css/fonts.css`), ls 0.01em.
- Figma dựng Bodoni Moda **không kerning**, nên các tiêu đề Bodoni đặt `font-kerning: none`. Jost vẫn giữ kerning (tắt đi thì lệch nhiều hơn).
- Nút trắng: theo đúng panel Figma, padding 10/50 và bề rộng Hug ghi thẳng (243 / 208 / 181). Nút Women/Men lệch 1px ở mép phải vì trong ảnh export Figma chúng nằm ở toạ độ lẻ nửa pixel.
- Gạch chân: Figma vẽ nét mảnh khử răng cưa trên 2 hàng pixel (25 % rồi 50 % màu chữ), còn `text-decoration` của Chrome luôn ra 1 hàng đặc. Vì vậy gạch chân được vẽ bằng `::after` cao 2px, nền gradient 25 % / 50 %, khớp từng hàng pixel.
- Placeholder ô email: Figma nghiêng giả chữ đứng (chữ "a" mang dáng chữ đứng), nên CSS dùng họ "Jost Upright" (chỉ có mặt đứng) với `font-style: oblique 14deg`. Lệch còn 1px ở mép.

## Còn cần từ phía khách

- **`Women.png`, `Men.png`, `Video.png` đang dính sẵn chữ / nút / nút play trong ảnh.** Trang dựng chữ thật bằng HTML đè đúng vị trí nên ở khổ 1920 trông khớp, nhưng ở khổ nhỏ ảnh bị cắt (`object-fit: cover`) nên chữ trong ảnh lệch khỏi chữ HTML. Cần export lại 3 ảnh này **ẩn layer chữ, nút và nút play**.
- Icon `ion_*.png` chỉ có bản 1x (14 × 14). Xin bản SVG hoặc @2x cho màn hình retina.
- Mũi tên carousel đang vẽ bằng SVG inline theo ảnh đo (91 × 65, nét 1.5px). Nếu có file export thì gửi để thay.
- Ảnh đối chiếu `Modish.jpg` là JPEG, nên vùng ảnh có sai lệch nén nhỏ. Bản PNG 1x sẽ đo chính xác hơn.
