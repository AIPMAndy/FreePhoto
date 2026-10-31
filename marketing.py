"""FreePhoto marketing and product landing sections around the upstream working tool.

Only changes presentation and metadata. Original MAZANOKE image engine remains intact.
"""
from pathlib import Path
import json
import shutil

HERO = """<section class="fp-hero" aria-labelledby="fp-heading">
  <div class="fp-eyebrow"><span class="fp-led"></span> FREE &amp; OPEN SOURCE · LOCAL FIRST</div>
  <h2 id="fp-heading">每一张照片，<br><em>轻一点，自由一点。</em></h2>
  <p class="fp-lead">免费压缩图片、转换格式、调整尺寸，顺手清理可能包含定位信息的照片元数据。无需注册，图片在你的浏览器里处理。</p>
  <div class="fp-hero-actions">
    <a class="fp-action-primary" href="#tool">开始处理图片 <span aria-hidden="true">↗</span></a>
    <a class="fp-action-secondary" href="https://github.com/AIPMAndy/FreePhoto" target="_blank" rel="noopener noreferrer">查看开源代码 <span aria-hidden="true">↗</span></a>
  </div>
  <div class="fp-trust"><span>◎ 不用上传云端</span><span>✳ 无水印</span><span>↻ 批量处理</span><span>◈ 支持离线使用</span></div>
</section>
"""
DETAILS = """<section class="fp-lower" aria-label="FreePhoto 产品说明">
  <div class="fp-section-intro"><span class="fp-kicker">FOUR TOOLS. ONE PLACE.</span>
    <h2>常用的图片工作，<br>一次处理好。</h2><p>高频功能，做得简单。保留原始文件，结果需要时再下载。</p>
  </div>
  <div class="fp-features">
    <article><span class="fp-feature-num">01 / COMPRESS</span><h3>图片压缩</h3><p>调整质量或目标大小，适合分享照片、优化网站图片。</p></article>
    <article><span class="fp-feature-num">02 / RESIZE</span><h3>调整尺寸</h3><p>按最长边缩小图片，支持常用图片宽高限制。</p></article>
    <article><span class="fp-feature-num">03 / CONVERT</span><h3>格式转换</h3><p>支持 JPG、PNG、WebP 等输出，以及 HEIC 等图片输入。</p></article>
    <article><span class="fp-feature-num">04 / PRIVACY</span><h3>隐私处理</h3><p>处理时不发送图片给本站服务器，重新编码通常移除 EXIF 数据。</p></article>
  </div>
  <div class="fp-privacy" id="privacy"><div><span class="fp-kicker">PRIVACY BY DESIGN</span><h2>你的照片，<br>留在你的设备里。</h2></div>
    <p>FreePhoto 在浏览器本地处理图片。这里没有上传账户，也不需要订阅会员。部分格式受浏览器和设备支持限制；对涉及敏感信息的图片，请在分享前核验输出元数据。站点初次加载需要网络访问静态资源。</p>
  </div>
  <section class="fp-faq" aria-labelledby="faq-heading"><span class="fp-kicker">GOOD TO KNOW</span><h2 id="faq-heading">使用前，你可能想知道</h2>
    <details><summary>图片会发送到服务器吗？</summary><p>产品图像处理逻辑运行在浏览器本地，不设文件上传接口。页面及依赖代码首次加载仍会通过网络传输；请在可信的部署来源使用。</p></details>
    <details><summary>支持哪些图片格式？</summary><p>常见 JPG、PNG、WebP 图片可以直接处理。支持部分 HEIC、AVIF、GIF、SVG、TIFF 等图片输入，实际以浏览器和设备能力为准；部分动画只处理静态帧。</p></details>
    <details><summary>为什么图片压缩后反而更大？</summary><p>取决于原图格式、清晰度、尺寸和输出编码方式。可尝试调整画质或选择 WebP；重要图片请保留原件并检查输出效果。</p></details>
    <details><summary>开源协议和项目来源是什么？</summary><p>FreePhoto 基于 MAZANOKE 的 GPL-3.0 代码改造。感谢原作者 civilblur 及依赖项目贡献者。<a href="https://github.com/civilblur/mazanoke" target="_blank" rel="noopener noreferrer">查看上游项目</a>。</p></details>
  </section>
  <section class="fp-contact" id="contact" aria-labelledby="fp-contact-heading">
    <div class="fp-contact-copy">
      <span class="fp-kicker">MADE WITH CARE · AI 酋长 Andy</span>
      <h2 id="fp-contact-heading">好用的工具，<br>也欢迎一起交流。</h2>
      <p>FreePhoto 免费开源。如果你正在做 AI 产品、个人 IP 或企业 AI 应用，欢迎从官网了解我，也可以通过微信交流。</p>
    </div>
    <div class="fp-contact-actions">
      <a class="fp-contact-website" href="https://metaver.vip/" target="_blank" rel="noopener noreferrer" aria-label="访问 AI 酋长 Andy 的个人官网">
        <span><small>PERSONAL WEBSITE</small><strong>metaver.vip</strong></span><span aria-hidden="true">↗</span>
      </a>
      <div class="fp-contact-wechat">
        <div class="fp-contact-wechat-text"><small>WECHAT · 微信</small><strong id="fp-wechat-id">AIPMAndy</strong><span>微信搜索这个 ID 添加</span></div>
        <button type="button" class="fp-copy-wechat" id="fp-copy-wechat" data-wechat-id="AIPMAndy" aria-describedby="fp-wechat-id">复制微信号</button>
      </div>
      <p class="fp-contact-status" id="fp-copy-status" role="status" aria-live="polite"></p>
    </div>
  </section>
  <div class="fp-endnote"><strong>FreePhoto.</strong><span>免费使用 · 公开代码 · 官网 metaver.vip · 微信 AIPMAndy</span>
    <div><a href="https://github.com/AIPMAndy/FreePhoto" target="_blank" rel="noopener noreferrer">GitHub 源码 ↗</a><a href="https://metaver.vip/" target="_blank" rel="noopener noreferrer">个人官网 ↗</a></div>
  </div>
</section>"""

def enhance_website(target: Path) -> None:
    html_file = target / "index.html"
    source = html_file.read_text(encoding="utf-8")
    opening = '    <div class="content">'
    ending = '    <footer>'
    if source.count(opening) != 1 or source.count(ending) != 1:
        raise RuntimeError("Upstream DOM changed; cannot safely mount FreePhoto site")
    source = source.replace(opening, HERO + '\n    <div class="content" id="tool">', 1)
    source = source.replace(ending, DETAILS + '\n    <footer>', 1)
    target_marker = '<link rel="stylesheet" href="./freephoto-theme.css" />'
    if source.count(target_marker) != 1:
        raise RuntimeError("Missing FreePhoto theme marker")
    source = source.replace(target_marker, target_marker + '\n    <link rel="stylesheet" href="./freephoto-site.css" />', 1)
    source = source.replace('</head>', '''<link rel="canonical" href="https://aipmandy.github.io/FreePhoto/" />
    <meta name="keywords" content="免费图片压缩,在线图片压缩,图片格式转换,WebP转换,HEIC转JPG,调整图片尺寸,批量压缩图片,去除EXIF,本地图片处理,FreePhoto" />
    <meta name="author" content="AI 酋长 Andy" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="FreePhoto" />
    <meta property="og:locale" content="zh_CN" />
    <meta property="og:url" content="https://aipmandy.github.io/FreePhoto/" />
    <meta property="og:title" content="FreePhoto — 免费本地图片工具箱" />
    <meta property="og:description" content="免费图片压缩、转换格式、调整尺寸，图片在浏览器本地处理。开源、无水印、免登录。" />
    <meta property="og:image" content="https://aipmandy.github.io/FreePhoto/freephoto-og.png" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:image:alt" content="FreePhoto 免费在线图片压缩工具首页" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="FreePhoto — 免费在线图片压缩、格式转换" />
    <meta name="twitter:description" content="免费图片压缩、转换格式、调整尺寸，图片在浏览器本地处理。开源、无水印、免登录。" />
    <meta name="twitter:image" content="https://aipmandy.github.io/FreePhoto/freephoto-og.png" />
    <meta name="twitter:creator" content="@AIPMAndy" />
    <script type="application/ld+json">{"@context": "https://schema.org", "@type": ["WebApplication", "SoftwareApplication"], "name": "FreePhoto", "url": "https://aipmandy.github.io/FreePhoto/", "image": "https://aipmandy.github.io/FreePhoto/freephoto-og.png", "description": "免费、本地、开源的图片工具箱：图片压缩、调整尺寸、格式转换与 EXIF 清理，图片在浏览器本地处理。", "applicationCategory": "MultimediaApplication", "operatingSystem": "Web", "inLanguage": "zh-CN", "isAccessibleForFree": true, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "CNY"}, "license": "https://www.gnu.org/licenses/gpl-3.0.html", "isBasedOn": "https://github.com/civilblur/mazanoke", "sameAs": ["https://github.com/AIPMAndy/FreePhoto"], "author": {"@type": "Person", "name": "AI 酋长 Andy", "alternateName": "AIPMAndy", "url": "https://github.com/AIPMAndy", "sameAs": ["https://x.com/AIPMAndy", "https://metaver.vip/"]}}</script>
    <script type="application/ld+json">{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "图片会发送到服务器吗？", "acceptedAnswer": {"@type": "Answer", "text": "产品图像处理逻辑运行在浏览器本地，不设文件上传接口。页面及依赖代码首次加载仍会通过网络传输；请在可信的部署来源使用。"}}, {"@type": "Question", "name": "支持哪些图片格式？", "acceptedAnswer": {"@type": "Answer", "text": "常见 JPG、PNG、WebP 图片可以直接处理。支持部分 HEIC、AVIF、GIF、SVG、TIFF 等图片输入，实际以浏览器和设备能力为准；部分动画只处理静态帧。"}}, {"@type": "Question", "name": "为什么图片压缩后反而更大？", "acceptedAnswer": {"@type": "Answer", "text": "取决于原图格式、清晰度、尺寸和输出编码方式。可尝试调整画质或选择 WebP；重要图片请保留原件并检查输出效果。"}}, {"@type": "Question", "name": "开源协议和项目来源是什么？", "acceptedAnswer": {"@type": "Answer", "text": "FreePhoto 基于 MAZANOKE 的 GPL-3.0 代码改造。感谢原作者 civilblur 及依赖项目贡献者。查看上游项目。"}}]}</script>
  </head>''', 1)
    source = source.replace('href="./assets/images/favicon-32x32.png"', 'href="./freephoto-mark.svg"')
    source = source.replace('href="./assets/images/favicon-16x16.png"', 'href="./freephoto-mark.svg"')
    source = source.replace('href="./assets/images/apple-touch-icon.png"', 'href="./freephoto-apple-touch-icon.png"')
    marker = '<script defer src="./freephoto-i18n.js"></script>'
    if source.count(marker) != 1:
        raise RuntimeError("FreePhoto localization script marker missing")
    source = source.replace(marker, marker + '\n    <script defer src="./freephoto-contact.js"></script>', 1)
    html_file.write_text(source, encoding="utf-8")
    (target / "freephoto-mark.svg").write_text("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 192"><rect width="192" height="192" rx="44" fill="#285d46"/><rect x="35" y="42" width="122" height="108" rx="18" fill="#f1f6ef"/><circle cx="117" cy="75" r="14" fill="#a2c6a6"/><path d="M41 126 76 90 105 120 127 99 151 127v16H41Z" fill="#5a9877"/></svg>""",encoding="utf-8")
    shutil.copy2(Path(__file__).with_name("freephoto-site.css"), target / "freephoto-site.css")
    shutil.copy2(Path(__file__).with_name("freephoto-contact.js"), target / "freephoto-contact.js")
    service_worker = target / "service-worker.js"
    if service_worker.exists():
        sw=service_worker.read_text(encoding="utf-8")
        marker='"./freephoto-theme.css",'
        if marker not in sw:
            raise RuntimeError("Required PWA asset list entry missing")
        service_worker.write_text(sw.replace(marker, marker + '\n  "./freephoto-site.css",\n  "./freephoto-contact.js",', 1),encoding="utf-8")
    (target / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://aipmandy.github.io/FreePhoto/sitemap.xml\n",encoding="utf-8")
    (target / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<url><loc>https://aipmandy.github.io/FreePhoto/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>\n</urlset>\n',encoding="utf-8")
    for asset in ("freephoto-og.png", "freephoto-apple-touch-icon.png"):
        shutil.copy2(Path(__file__).with_name(asset), target / asset)
    (target / ".nojekyll").write_text("",encoding="utf-8")
    manifest_path=target/"manifest.json"
    info=json.loads(manifest_path.read_text(encoding="utf-8"))
    info["icons"].append({"src":"./freephoto-mark.svg","sizes":"any","type":"image/svg+xml"})
    manifest_path.write_text(json.dumps(info,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
