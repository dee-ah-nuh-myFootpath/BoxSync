import glob
import os.path

#Download group enrolled for the day that would be yesterday (so yesterday or 3 days ago if a weekend) \
#and set as enrolled yesterday
#Download group enrolled for today and thats today
def recent_file(path,extension,location):
    files = glob.glob(path + extension)
    max_file=sorted(files,key=os.path.getctime)[-location]
    return max_file
