# getdownload 🔽

A simple, asynchronous BitTorrent downloader written in Python. Point it at a `.torrent` file, choose a destination folder, and getdownload connects to the swarm and downloads your files — complete with a live progress bar.

## Features

- 🧵 Fully asynchronous downloads using `asyncio` and [`aiotorrent`](https://pypi.org/project/python-aiotorrent/)
- 📂 Downloads directly to any destination directory you choose
- 📊 Real-time progress bar showing download percentage per file
- 🔍 Validates pieces against the torrent's SHA-1 hashes before writing
- 📦 Supports both single-file and multi-file torrents

## Requirements

- Python 3.8+
- [python-aiotorrent](https://pypi.org/project/python-aiotorrent)

## Installation

```bash
git clone https://github.com/dev-Aswinkumar/getdownload.git
cd getdownload
python -m venv venv
source venv/bin/activate
pip install python-aiotorrent
```

## Usage

```bash
python src/main.py
```

You will be prompted for:

1. **The filepath** — path to your `.torrent` file (e.g. `~/Downloads/ubuntu.iso.torrent`)
2. **The destination** — an existing directory where the downloaded files should be saved

```
Welcome to getDownlaoded
========================
Enter the filepath: /home/user/Downloads/ubuntu.iso.torrent
Enter the destination /home/user/Downloaded

Reading torrent...
Torrent: ubuntu-26.04.1-live-server-amd64.iso

Downloading: ubuntu-26.04.1-live-server-amd64.iso
ubuntu-26.04.1-live-server-amd64.iso: [██████████----------] 25.00%
```

The downloaded files are written directly into the destination directory.

> **Note:** Ensure the destination directory exists before running. Downloads require at least one reachable peer in the swarm.

## Project Structure

```
getdownload/
├── src/
│   └── main.py          # Entry point, input handling, progress bar
├── requirements.txt
├── README.md
└── LICENSE
```
## Ai used

used opencode for the progress bar

## License

[MIT-style public domain (Unlicense)](LICENSE) — free and unencumbered software released into the public domain.
