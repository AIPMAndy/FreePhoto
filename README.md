# FreePhoto

**FreePhoto — 免费、本地、开源的图片处理工具。**  
Website (after GitHub Pages is enabled): https://aipmandy.github.io/FreePhoto/

FreePhoto is an independent, public, GPL-3.0 project by [AIPMAndy](https://github.com/AIPMAndy), derived from [MAZANOKE](https://github.com/civilblur/mazanoke) by civilblur. It keeps the upstream browser-based processing engine and third-party attributions. The build pins MAZANOKE commit `ceab516ade2a68f3c0abef8bd8fa03ada3ac3e7b`.

## Features
- Image compression, format conversion and dimension adjustment.
- JPEG, PNG, WebP and additional browser-supported input formats.
- Batch export; privacy-first local processing. No file upload API.
- Chinese landing page, responsive layout and basic PWA support.

## Build
Requires Python 3.12+, git, and network access during the initial build.

```sh
python3 build.py --out dist
python3 -m http.server 8765 -d dist
```

Open http://localhost:8765 . You may also use `--from-source /path/to/mazanoke` to patch a locally downloaded upstream tree.

## Quality
Run tests with `python3 -m unittest discover -s tests -v -p 'test_*.py'`. GitHub Actions validates the source, runs Chromium regression tests, builds a complete static site, and deploys it using GitHub Pages when enabled.

## License and acknowledgments
This fork and the original MAZANOKE engine are GPL-3.0. Generated website distributions include the full upstream `LICENSE`, `FORK-NOTICE.md`, and `docs/ATTRIBUTIONS.md` for bundled third-party code. Please preserve attribution and check individual dependency licensing before redistribution.

## Known limitations
True iPhone Safari and real camera HEIC compatibility have not yet been fully verified. Benchmarks are not evidence of global superiority. Some dynamic messages may remain in English. User photos must be validated before sensitive disclosure; re-encoding normally strips EXIF, but inspect the final output.
