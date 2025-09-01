import json
import os
import shutil
from datetime import date
from datetime import datetime


#directories with relative paths
dir_source_files = r'sourcefiles'
dir_destination = r'destination'
dir_logfiles = r'logfiles'



def move_sourcefiles():    
    json_object_open = open("saved keywords clean.json")
    saved_keywords_clean_json = json.load(json_object_open)
    list_of_dicts_dstFolderNames_and_keywords = []
    list_of_sourcefiles_seen_and_notToBeDisplayedAnymore = []
    for key, value in saved_keywords_clean_json.items():
        dict_dstFolder_and_keywords = {key:value}
        list_of_dicts_dstFolderNames_and_keywords.append(dict_dstFolder_and_keywords)
    print("List of dictionaries with Foldernames and Keywords generated, here is the list:")
    print(str(list_of_dicts_dstFolderNames_and_keywords))
    print("")
    print("Now iterating through the list of dictionaries from textboxes")
    listboxcounter=-1
    
    #sourcefiles from textbox 1
    while listboxcounter <= 9: #we have 10 textboxes for keywords, the looptherefore goes 10 times (0-9)
        listboxcounter+=1
        try:
            for dstFolderName, keywords_with_hashtags in list_of_dicts_dstFolderNames_and_keywords[listboxcounter].items():
                path_for_new_dir = os.path.join(dir_destination, dstFolderName)
                try:
                    #os.makedirs(path_for_new_dir, exist_ok = False)
                    print(f"path {path_for_new_dir} created")
                except OSError as error:
                    pass
                list_SrcFilesSeenFirstTime_and_therefore_to_be_moved = []
                for sourcefile in os.scandir(dir_source_files):
                    if sourcefile in list_of_sourcefiles_seen_and_notToBeDisplayedAnymore:
                        print(f"file {sourcefile.name} was already seen and will not be displayed")
                        continue
                    else:
                        keywords_without_hashtags = keywords_with_hashtags.rstrip().split('#') #automatically creates list and removes the hashtag from every keyword
                        keywords_without_hashtags.remove('') #removes empty entries from list
                        keywords_without_hashtags
                        for keyword in keywords_without_hashtags:
                            keyword=keyword.rstrip()
                            if keyword == "":
                                continue
                            if keyword in sourcefile.name:
                                print(f"keyword '{keyword}' found in sourcefile '{sourcefile.name}'")
                                list_SrcFilesSeenFirstTime_and_therefore_to_be_moved.append(sourcefile)
                                list_SrcFilesSeenFirstTime_and_therefore_to_be_moved=list(set(list_SrcFilesSeenFirstTime_and_therefore_to_be_moved))
                print(f"")
                print(f"")
                print(f"the following files will be moved:")
                print(list_SrcFilesSeenFirstTime_and_therefore_to_be_moved)
                for sourcefile_to_be_moved in list_SrcFilesSeenFirstTime_and_therefore_to_be_moved:
                    print(f"Now moving {sourcefile_to_be_moved} to {path_for_new_dir}.")
                    #shutil.move(sourcefile_to_be_moved, path_for_new_dir)
        except IndexError:
                pass


def extract_files_from_subfolder_in_source_files():
        for possible_dir in os.scandir(dir_source_files):
            if possible_dir.is_dir():
                subfolder_path_in_source_files = os.listdir(dir_source_files + "/" + possible_dir.name)
                for subfolder_file in subfolder_path_in_source_files:
                    #shutil.move(os.path.join(possible_dir.path, subfolder_file), dir_source_files)
                    print(f"FILE: {subfolder_file} extracted from {possible_dir} and moved to {dir_source_files}.")
        print("All files scanned for subfolders")



def delete_empty_folder_in_source_files():
        for a_possibly_empty_folder in os.scandir(dir_source_files):
            if a_possibly_empty_folder.is_dir():
                subfolder_path = os.listdir(dir_source_files + "/" + a_possibly_empty_folder.name)
                if len(subfolder_path) == 0:
                    print(f"EMPTY FOLDER FOUND \n The folder {a_possibly_empty_folder} is empty and will be deleted.\n")
                    #shutil.rmtree(a_possibly_empty_folder)