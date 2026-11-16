<p align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0d9488&height=170&section=header&text=URL%20Cleaner&fontSize=40&fontColor=ffffff&animation=fadeIn" width="100%" alt="URL Cleaner banner">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=21&pause=900&color=2DD4BF&center=true&vCenter=true&width=700&lines=Normalize%20links%20and%20remove%20tracking%20noise" alt="Animated project title">
</p>
<p align="center">
<a href="https://github.com/CyberLoop-dev/url-cleaner/blob/main/LICENSE"><img src="https://img.shields.io/github/license/CyberLoop-dev/url-cleaner?style=flat-square" alt="License"></a>
<img src="https://img.shields.io/badge/language-Python-0d9488?style=flat-square" alt="Python">
<a href="https://github.com/CyberLoop-dev/url-cleaner/stargazers"><img src="https://img.shields.io/github/stars/CyberLoop-dev/url-cleaner?style=flat-square" alt="Stars"></a>
<img src="https://img.shields.io/github/last-commit/CyberLoop-dev/url-cleaner?style=flat-square" alt="Last commit">
</p>
<p align="center"><img src="assets/icon.svg" width="520" alt="URL Cleaner illustration"></p>

## 🧭 Overview
Normalize URL lists, remove common tracking parameters, and deduplicate links while preserving useful query data.

## ✨ Features
- 🧹 Remove common tracking parameters such as utm_* and fbclid.
- 🌐 Normalize scheme and hostname casing and default ports.
- 🧾 Preserve meaningful query parameters and fragments.
- 📄 Deduplicate cleaned URLs while keeping first-seen order.

## 🖥️ Demo
~~~bash
python main.py examples/urls.txt --output clean-urls.txt
~~~
Try it with the included sample input or your own local files.

## 🚀 Quick Start
~~~bash
git clone https://github.com/CyberLoop-dev/url-cleaner.git
cd url-cleaner
python main.py examples/urls.txt --output clean-urls.txt
~~~

## 🧰 Tech Stack
- Python 3.10+
- urllib.parse, argparse, pathlib (standard library)

## 🗂️ Folder Structure
~~~text
url-cleaner/\n├── assets/icon.svg\n├── examples/urls.txt\n├── tests/test_main.py\n├── LICENSE\n├── README.md\n├── main.py\n└── requirements.txt
~~~

## 🗺️ Roadmap
- [ ] Add configurable tracking-parameter lists.
- [ ] Add JSON and CSV input formats.

## 🤝 Contributing
Issues and focused pull requests are welcome. Add tests for behavior changes and keep the project easy to run locally.

## 📄 License
Released under the MIT License. See LICENSE.

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d9488,100:111827&height=110&section=footer" width="100%" alt="Animated wave footer"></p>
