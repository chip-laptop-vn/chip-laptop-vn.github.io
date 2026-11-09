# Cấu hình site ts (Ghi chép chip laptop). URL gốc chỉ nằm trong file này.
BASE_URL = "https://chip-laptop-vn.github.io/"
SITE_NAME = "Ghi chép chip laptop"
PEN = "Quân"
MARK = "C"
AVATAR = "Q"
TAGLINE = "Nhật ký kỹ thuật của Quân"
LATEST_N = 12

INDEX_TITLE = "Ghi chép chip laptop - Bộ xử lý, nguồn, AI chạy cục bộ"
INDEX_DESC = ("Ghi chép kỹ thuật về chip, nguồn điện, tản nhiệt và mô hình AI chạy cục bộ trên laptop đời 2025 và 2026, "
              "có bảng thông số và cách đọc từng chỉ số.")
INDEX_OG_TITLE = INDEX_TITLE
INDEX_OG_DESC = INDEX_DESC
INDEX_H1 = "Chip, nguồn và AI trên laptop, đọc từ tài liệu kỹ thuật"
STRAP = "Mình ghi lại cách đọc thông số chip, nguồn, tản nhiệt và các mô hình AI chạy ngay trên laptop."

ABOUT_P = "Mình ghi lại cách đọc thông số chip, nguồn và AI cục bộ trên laptop đời 2025 và 2026."
ABOUT_HOME = (
    '<h2 class="sec-t">Về blog</h2>'
    '<p>Mình là Quân. Blog này là nhật ký kỹ thuật của mình về laptop: chip và xung nhịp, nguồn điện, '
    'tản nhiệt, kết nối không dây và các mô hình AI nhỏ chạy cục bộ.</p>'
    '<p>Mỗi bài mình đọc từ tài liệu công khai của hãng, ghi lại các chỉ số quan trọng vào bảng và giải thích '
    'từng dòng. Mình chỉ nhắc đến máy đời 2025 và 2026 và không ghi giá.</p>'
    '<p>Chỗ nào chưa có tài liệu rõ ràng, mình ghi thẳng là chưa rõ thay vì đoán.</p>'
)

CATS = [("ket-noi", "Kết nối"), ("nguon-nhiet", "Nguồn và nhiệt"), ("ai-cuc-bo", "AI cục bộ")]
CAT_RULES = [
    ("ket-noi", "Kết nối", ["miracast", "auracast", "wake-on-lan", "ket-noi"]),
    ("nguon-nhiet", "Nguồn và nhiệt", ["vrm", "throttlestop", "fan", "tut-xung"]),
    ("ai-cuc-bo", "AI cục bộ", ["ai", "saluki", "granite", "mo-hinh"]),
]
CAT_DEFAULT = ("nguon-nhiet", "Nguồn và nhiệt")

FONTS_URL = ("https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&"
             "family=Space+Mono:wght@400;700&display=swap")

HEADER = (
    '<body>\n<a class="skip" href="#main">Bỏ qua đến nội dung</a>\n'
    '<header class="top"><div class="wrap bar">'
    '<a class="brand" href="@HOME@"><span class="mark" aria-hidden="true">@MARK@</span>'
    '<span class="bn">@NAME@</span><span class="tag">@TAGLINE@</span></a>'
    '<nav class="nav" aria-label="Chính">@NAV@</nav>'
    '</div></header>\n'
)
FOOTER = (
    '<footer class="foot"><div class="wrap fo">'
    '<p class="fn">@NAME@</p>'
    '<p>Nhật ký kỹ thuật cá nhân của @PEN@ về laptop đời 2025 và 2026.</p>'
    '<p class="sm">Năm @YEAR@. Nội dung viết lại từ tài liệu công khai của hãng.</p>'
    '</div></footer>\n</body>\n</html>\n'
)
ABOUT = (
    '<section class="w w-about"><span class="av" aria-hidden="true">@AV@</span>'
    '<div><h2 class="w-t">@PEN@</h2><p>@ABOUT@</p><a class="more" href="@R@#ve-blog">Về blog</a></div></section>'
)
POST = (
    '@HEADER@'
    '<div class="wrap lay"><main id="main" class="col post">\n'
    '<p class="crumb"><a href="@R@">Trang chủ</a><span aria-hidden="true"> / </span><span>@CATLABEL@</span></p>\n'
    '@ARTICLE@\n@RELATED@\n</main>\n'
    '<aside class="side">@ABOUT@@CATS@</aside></div>\n'
    '@FOOTER@'
)
INDEX = (
    '@HEADER@'
    '<main id="main">\n'
    '<div class="intro"><div class="wrap"><p class="lab">Nhật ký kỹ thuật · @TOTAL@ bài</p>'
    '<h1>@H1@</h1><p class="st">@STRAP@</p></div></div>\n'
    '<div class="wrap"><section class="hero-wrap" aria-label="Bài mới nhất">@HERO@</section></div>\n'
    '<div class="wrap lay"><div class="col">\n'
    '<section id="bai-moi"><h2 class="sec-t">Bài mới nhất</h2>\n<div class="stack">\n@LATEST@\n</div></section>\n'
    '<section id="chu-de"><h2 class="sec-t">Theo chủ đề</h2>\n<div class="tps">@TOPICS@</div></section>\n'
    '<section id="ve-blog" class="about-home">@ABOUT_HOME@</section>\n'
    '</div>\n<aside class="side">@SIDEBAR@</aside></div>\n</main>\n'
    '@FOOTER@'
)
NOTFOUND = (
    '@HEADER@'
    '<main id="main" class="wrap nf"><h1>Không tìm thấy trang này</h1>'
    '<p>Đường dẫn có thể đã đổi hoặc bài chưa được đăng. Quay về trang chủ để xem danh sách bài.</p>'
    '<p><a class="btn" href="@R@">Về trang chủ</a></p></main>\n'
    '@FOOTER@'
)
CARDS = {
    "hero": (
        '<article class="hero"><a class="hero-media" href="@HREF@" tabindex="-1" aria-hidden="true">@MEDIA@</a>'
        '<div class="hero-tx"><p class="lab">@CAT@ · mới nhất</p>'
        '<h2><a href="@HREF@">@TITLE@</a></h2><p class="dk">@DESC@</p>'
        '<p class="meta"><time datetime="@ISO@">@DATE@</time><span aria-hidden="true"> / </span>@READ@</p></div></article>'
    ),
    "latest": (
        '<article class="item"><span class="ord" aria-hidden="true">@ORD@</span>'
        '<a class="item-media" href="@HREF@" tabindex="-1" aria-hidden="true">@MEDIA@</a>'
        '<div class="item-tx"><p class="lab">@CAT@</p>'
        '<h3><a href="@HREF@">@TITLE@</a></h3><p class="dk">@DESC@</p>'
        '<p class="meta"><time datetime="@ISO@">@DATE@</time><span aria-hidden="true"> / </span>@READ@</p></div></article>'
    ),
}
