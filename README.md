<div align="center">

# 📷 FreePhoto

**免费、本地、开源的图片处理工具**

压缩 · 调尺寸 · 格式转换 · 去 EXIF —— 图片留在你的设备里，不上传服务器。

[![License: GPL-3.0](https://img.shields.io/github/license/AIPMAndy/FreePhoto?style=flat-square&color=blue)](LICENSE)
[![Stars](https://img.shields.io/github/stars/AIPMAndy/FreePhoto?style=flat-square&color=f5b301)](https://github.com/AIPMAndy/FreePhoto/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/AIPMAndy/FreePhoto?style=flat-square)](https://github.com/AIPMAndy/FreePhoto/commits/main)
[![Build & Pages](https://img.shields.io/github/actions/workflow/status/AIPMAndy/FreePhoto/pages.yml?branch=main&style=flat-square&label=Build%20%26%20Pages)](https://github.com/AIPMAndy/FreePhoto/actions/workflows/pages.yml)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)
![PWA](https://img.shields.io/badge/PWA-支持-5A0FC8?style=flat-square&logo=pwa&logoColor=white)
[![Based on MAZANOKE](https://img.shields.io/badge/based%20on-MAZANOKE-6B7280?style=flat-square)](https://github.com/civilblur/mazanoke)

[**🌐 在线使用**](https://aipmandy.github.io/FreePhoto/) · [🐛 问题反馈](https://github.com/AIPMAndy/FreePhoto/issues)

</div>

---

FreePhoto 是 [AIPMAndy](https://github.com/AIPMAndy) 维护的独立开源项目（GPL-3.0），基于 civilblur 的 [MAZANOKE](https://github.com/civilblur/mazanoke) 二次开发，保留上游浏览器端处理引擎和第三方署名。构建时锁定 MAZANOKE commit `ceab516ade2a68f3c0abef8bd8fa03ada3ac3e7b`。

## 👀 效果预览

<div align="center">

<a href="https://aipmandy.github.io/FreePhoto/"><img src="docs/screenshot.webp" alt="FreePhoto 在线工具首页截图" width="860"></a>

<sub>点击图片打开在线版 · <a href="https://aipmandy.github.io/FreePhoto/">aipmandy.github.io/FreePhoto</a></sub>

</div>

## ✨ 功能

- 🗜️ **图片压缩**：调整质量或目标大小，适合分享照片、优化网站图片
- 📏 **调整尺寸**：按最长边缩小，支持常用宽高限制
- 🔄 **格式转换**：输出 JPG、PNG、WebP 等，支持 HEIC 等浏览器可解码的输入格式
- 🔒 **隐私处理**：本地处理，无文件上传接口；重新编码通常会移除 EXIF
- 📦 **批量导出**，中文落地页、响应式布局和基础 PWA 支持

## 🚀 快速开始

**在线使用**：打开 [aipmandy.github.io/FreePhoto](https://aipmandy.github.io/FreePhoto/)。

**本地构建**（需要 Python 3.12+、git，首次构建需联网拉取上游）：

```bash
git clone https://github.com/AIPMAndy/FreePhoto.git
cd FreePhoto
python3 build.py --out dist
python3 -m http.server 8765 -d dist
```

浏览器打开 http://localhost:8765 。也可以用 `--from-source /path/to/mazanoke` 对本地已下载的上游代码打补丁。

## 🧪 质量保障

```bash
python3 -m unittest discover -s tests -v -p 'test_*.py'
```

GitHub Actions 会校验源码、运行 Chromium 回归测试、构建完整静态站点，并部署到 GitHub Pages。

## 🧱 技术栈

| 部分 | 说明 |
|---|---|
| 处理引擎 | MAZANOKE（浏览器端图片处理，GPL-3.0） |
| 构建 | Python 3.12+ 脚本 `build.py`：拉取锁定版本上游 + 打补丁 + 生成站点 |
| 前端 | HTML / CSS / JavaScript，中文界面与 PWA |
| 测试与部署 | Python unittest + Chromium 回归测试，GitHub Actions + GitHub Pages |

## ⚠️ 已知限制

iPhone Safari 真机和相机 HEIC 兼容性尚未完全验证。基准测试不代表全面领先。部分动态提示可能仍为英文。涉及敏感信息的图片请自行核对：重新编码通常会去除 EXIF，但请检查最终输出。

## 📄 许可与致谢

本项目与原版 MAZANOKE 引擎均为 [GPL-3.0](LICENSE)。生成的网站分发包含完整的上游 `LICENSE`、`FORK-NOTICE.md` 和打包第三方代码的 `docs/ATTRIBUTIONS.md`。再分发时请保留署名，并核对各依赖的许可。

> English: FreePhoto is a free, local-first, open-source image toolkit (compress, resize, convert, strip EXIF), derived from [MAZANOKE](https://github.com/civilblur/mazanoke) by civilblur, licensed under GPL-3.0.

---

## 👤 作者

<div align="center">

**AI 酋长 Andy** · 星觉科技

前腾讯/百度 AI 产品负责人 → 大模型公司 VP → AI 创业者

[![GitHub](https://img.shields.io/badge/GitHub-AIPMAndy-181717?style=flat-square&logo=github)](https://github.com/AIPMAndy)
[![X](https://img.shields.io/badge/X-@AIPMAndy-000000?style=flat-square&logo=x)](https://x.com/AIPMAndy)
![WeChat](https://img.shields.io/badge/微信-AIPMAndy-07C160?style=flat-square&logo=wechat&logoColor=white)
[![Website](https://img.shields.io/badge/官网-metaver.vip-111827?style=flat-square)](https://metaver.vip/)

觉得有用，欢迎点个 ⭐ Star，也欢迎提 Issue / PR 一起改进。

</div>
