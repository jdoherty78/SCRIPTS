import shutil, os

NEW = input("Enter a new folder: ")
OLD = input("Enter a folder that exists: ")

if OLD not in os.listdir("."):
    print("This folder does not exist. Try again")
else:
    all_files = [i for i in os.listdir(OLD)
	         if "." in i and i.split(".")[1] in ["ipynb", "txt"]]  #file extensions to focus on

    if not os.path.exists(NEW):
        os.mkdir(NEW)    

    for f in all_files:
        old = OLD +"/" + f
        new = NEW + "/" + f
        shutil.move(old, new)
    print("Files have been moved to {}".format(NEW))
