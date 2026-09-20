from pathlib import Path
def get_Input():
  filepath=Path(input("Enter the filepath: ").strip())
  destpath=Path(input("Enter the destination ").strip())
  if not filepath.is_file():
    print("The file doesn't exist")
    return None,None
  if not destpath.is_dir():
    print("The directory doesn't exist")
    return None,None
  return filepath,destpath
def main():
  print("Welcome to getDownlaoded")
  print("========================")
  filepath,dirpath=get_Input()
  if filepath==None:
    return
 
if __name__=="__main__":
  main()
