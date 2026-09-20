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
async def download_torrent(torrent_path, download_path):
  torrent = Torrent(str(torrent_path))
  print("\nReading torrent...")
  await torrent.init()
  print(f"Torrent: {torrent.name}")
  for file in torrent.files:
    print(f"Downloading: {file.path}")
    await torrent.download(file)
  print("\nDownload completed!")

def main():
  print("Welcome to getDownlaoded")
  print("========================")
  filepath,dirpath=get_input()
  if filepath is None:
    return
  asyncio.run(
    download_torrent(torrent_path, download_path)
  )
if __name__=="__main__":
  main()
