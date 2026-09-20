from pathlib import Path
import asyncio
from aiotorrent import Torrent

def get_input():
  filepath=Path(input("Enter the filepath: ").strip())
  destpath=Path(input("Enter the destination ").strip())
  if not filepath.is_file():
    print("The file or directory doesn't exist")
    return None,None
  if not destpath.is_dir():
    print("The file or directory doesn't exist")
    return None,None
  return filepath,destpath

def render_progress(file, width=40):
  percent = file.get_download_progress() if file.size else 100
  filled = int(width * percent / 100)
  bar = "█" * filled + "-" * (width - filled)
  return f"{file.name}: [{bar}] {percent:.2f}%"

async def download_torrent(torrent_path, download_path):
  torrent = Torrent(str(torrent_path))
  print("\nReading torrent...")
  await torrent.init()
  print(f"Torrent: {torrent.name}")
  torrent.torrent_info['name'] = str(download_path)
  for file in torrent.files:
    print(f"\nDownloading: {file.name}")
    task = asyncio.create_task(torrent.download(file))
    while not task.done():
      print(f"\r{render_progress(file)}", end="", flush=True)
      await asyncio.sleep(1)
    await task
    print(f"\r{render_progress(file)}", flush=True)
  print("\nDownload completed!")

def main():
  print("Welcome to getDownlaoded")
  print("========================")
  filepath,dirpath=get_input()
  if filepath is None:
    return
  asyncio.run(
    download_torrent(filepath, dirpath)
  )
if __name__=="__main__":
  main()