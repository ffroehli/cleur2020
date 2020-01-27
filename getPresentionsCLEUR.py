__author__ = "Simon Melotte"

import os
import requests
import sys
import json
import re

def createDirectory(directory):
    try: 
        if not os.path.exists(directory):
            os.mkdir(directory)
    except OSError:  
        print ("Creation of the directory {} failed".format(directory) )
    else:  
        print ("Successfully created the directory {} ".format(directory) )

def getPresentations(url, filename, directory):
    with open(filename) as json_file:  
        data = json.load(json_file)
        rex = re.compile(r"\W+")
        
        for item in data: 
            print("Evaluating followig file: {} - description = {}".format(item["name"], item["description"]) )           
            filename = item["name"].rstrip() + ".pdf"
            long_filename = rex.sub(" ", item["description"] ) + ".pdf"
            fullpath = url + filename
            print ("= URL fullpath is: {}".format(fullpath) )
            
            try:
                my_file = os.path.join(directory, long_filename)
                
                byte = 0
                if os.path.isfile(my_file):
                    byte = os.path.getsize( my_file )
                    print ("== File was found: {} byte= {}".format(filename, str(byte) ) )

                if not os.path.isfile(my_file) or byte < 30000:
                    print ("==== Start downloading: {}".format(filename))
                    r = requests.get(fullpath)
                    if r.status_code == 200:
                        print ("==== File was downloaded:{}".format(filename))
                        with open( my_file , "wb") as f:  
                            f.write(r.content)
                    else:
                        print ("==== File was not found: {}".format(filename))
                else:
                    print ("=== File already exists and size is bigger than one page - Filename = {}".format(long_filename))
            except:
                print ("=============== Exception for {}".format(long_filename) )

def main():    
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    PDFS =  os.path.join(THIS_FOLDER, "pdfs")
    URL = "https://www.ciscolive.com/c/dam/r/ciscolive/emea/docs/2020/pdf/"

    filename = THIS_FOLDER + os.sep + "cleur-sessions.2020.json"
    createDirectory(PDFS)
    getPresentations(URL, filename, PDFS)

if __name__ == "__main__":
    main()