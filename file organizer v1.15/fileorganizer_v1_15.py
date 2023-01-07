# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 18:50:44 2022

v1.0
folders created

v1.1
destination dir added
created functions

v1.2
added
- identify_needed_folders function as create_dir_by_keywordFile

v1.3
create_dir_by_keywordFile:
    - creation of test folder enabled

v1.4
create_dir_by_keywordFile:
    - creation of test folder with .txt file name
    - exception for creation added in case dir already exists
    
v1.5
scandir value strings added

v1.6
os.scandir() is an exhausted iterator -> fixed
print commands added


v1.7
    with open(file) as f
    read hashtag-separated keywords in text in read_keywords()
    put keywords into a list
    remove hashtags from keywords
    return keyword

v1.8
    fixed read_keywords() function. removed empty list entries
    created global list list_keywords
    renamed read_keywords into fill_list_keywords()
    scan_dir_keyword_files() removed
    
v1.9
    creating adding nested list method to create_dir_by_keyword_filename()
    
v1.10
    big function
    cild lists added
    
v1.11
    comparing src files to keywords

v1.12
    import shutil


v1.13
    moving source files to dst
    
v1.14
    extracting files from folders and deleting empty folders

v1.15
    creating logfile function
    creating identify_before_moving function

"""

import os
import sys
import shutil
from datetime import date
from datetime import datetime


#directories with relative paths
dir_source_files = r'source files'
dir_destination = r'destination'
dir_keyword_files = r'keywords'
dir_logfiles = r'logfiles'


def create_folders_and_move_files():
    #now a new directory is created and has the same name as the .txt file
    scanned_dir_keyword_files = os.scandir(dir_keyword_files)
    for file in scanned_dir_keyword_files: #creates new dirs named after .txt files in destination folder
        print((f".txt file found in dir_keyword_files:\n{file} name of new folder: " + os.path.splitext(file.name)[0]))
        new_dir_name = str(os.path.splitext(file.name)[0])
        path_for_new_dir = os.path.join(dir_destination, new_dir_name)

        try:
            os.makedirs(path_for_new_dir, exist_ok = False)
            print(f"directory creation succesful. Created directory: {new_dir_name}\n")
        except OSError as error:
            print(f"directory creation failed. '{new_dir_name}' already exists\n")    
    
    #creating a clean keywordlist, finding keywords in sourcefiles, moving sourcefiles when matched
    for txt_file_with_keywords in os.scandir(dir_keyword_files):
        print(f"    TASK 1: iterating through parent txt-keywordfile:\n {txt_file_with_keywords} ")
        keywordlist_a = []
        with open(txt_file_with_keywords) as txt_full_with_hashtags:
            for keyword_with_hashtags in txt_full_with_hashtags.readlines():
                keywords_without_hashtags = keyword_with_hashtags.rstrip().split('#') #automatically creates list and removes the hashtag from every keyword
                keywords_without_hashtags.remove('') #removes empty entries from list
            print(f"    TASK 2: fill child keywordlist_a with keywords from parent:") 
            for keyword_without_hashtag in keywords_without_hashtags:
                keywordlist_a.append(keyword_without_hashtag)
                print('keyword added to keywordlist_a: ' + keyword_without_hashtag)
            print("keywordlist_a ready:")
            print(keywordlist_a)
                
                #### this is where the fun begins:
            for scanned_dir_destination in os.scandir(dir_destination):
                print("This is the destination path " + str(os.path.realpath(scanned_dir_destination)))                    
                for keyword_a in keywordlist_a:
                        for scanned_scource_file in os.scandir(dir_source_files):
                            print(f"    TASK 3: comparing keyword '{keyword_a}' to '{scanned_scource_file}'")
                            if keyword_a.lower() in str(scanned_scource_file).lower():
                                print(f"Bingo! '{keyword_a}' found in '{scanned_scource_file}'")
                                try:
                                    shutil.move(scanned_scource_file, scanned_dir_destination)
                                    print(f"    TASK 4: moving {scanned_scource_file} to {scanned_dir_destination}")
                                except:
                                 pass
            print("\n")            
 
                
def extract_files_from_subfolder_in_source_files():
    for possible_dir in os.scandir(dir_source_files):
        if possible_dir.is_dir():
            subfolder_path_in_source_files = os.listdir(dir_source_files + "/" + possible_dir.name)
            print(f"Subfolder found in source folder: {possible_dir}.")
            for subfolder_file in subfolder_path_in_source_files:
                shutil.move(os.path.join(possible_dir.path, subfolder_file), dir_source_files)
                print(f"FILE: {subfolder_file} extracted from {possible_dir} and moved to {dir_source_files}.")
    print("All files scanned for subfolders")


def delete_empty_folder_in_source_files():
    for a_possibly_empty_folder in os.scandir(dir_source_files):
        print(a_possibly_empty_folder)
        if a_possibly_empty_folder.is_dir():
            print(f"{a_possibly_empty_folder} is dir")
            subfolder_path = os.listdir(dir_source_files + "/" + a_possibly_empty_folder.name)
            if len(subfolder_path) == 0:
                print(f"EMPTY FOLDER FOUND \n The folder {a_possibly_empty_folder} is empty and will be deleted.\n")
                shutil.rmtree(a_possibly_empty_folder)
                

#extract_files_from_subfolder_in_source_files()
#create_folders_and_move_files()
#delete_empty_folder_in_source_files()

def create_logfile():
    current_date = datetime.now()
    dt_string = current_date.strftime("%Y%m%d%H%M%S")
    print(f"creating logfile: {dt_string}.txt")
    try:
        logfile = open(f"{dir_logfiles}\logfile {dt_string}.txt", "x+")
    except OSError as error:
        print(f"logfile creation failed. logfile already exists\n")
        pass
    
    
def give_dict_destinationFolders_and_listOf_srcFiles():
    dict_destinationFolder_and_listOf_srcFiles = {}
    for txt_file_with_keywords in os.scandir(dir_keyword_files): #creates new dirs named after .txt files in destination folder
        list_value_listOf_srcFiles=[]
        new_dir_name = str(os.path.splitext(txt_file_with_keywords.name)[0])
        keywordlist_a = []
        with open(txt_file_with_keywords) as txt_full_with_hashtags:
            for keyword_with_hashtags in txt_full_with_hashtags.readlines():
                keywords_without_hashtags = keyword_with_hashtags.rstrip().split('#') #automatically creates list and removes the hashtag from every keyword
                keywords_without_hashtags.remove('') #removes empty entries from list
            for keyword_without_hashtag in keywords_without_hashtags:
                keywordlist_a.append(keyword_without_hashtag)
               
        #### this is where the fun begins:
        for keyword_a in keywordlist_a:
            for scanned_scource_file in os.scandir(dir_source_files):
                if keyword_a.lower() in str(scanned_scource_file).lower():
                    #appending source file titles to a list. the list will become values in the dict "dict_destinationName_and_listOf_srcFiles"
                    list_value_listOf_srcFiles.append(str((os.path.splitext(scanned_scource_file.name)[0]))+str((os.path.splitext(scanned_scource_file.name)[1])))
                    list(dict.fromkeys(list_value_listOf_srcFiles))#removing double entries
        dict_destinationFolder_and_listOf_srcFiles[new_dir_name]=list_value_listOf_srcFiles
    return(dict_destinationFolder_and_listOf_srcFiles)





def giveNames_of_destinationFolders_and_srcFiles():
    for destination_folder, list_srcFiles in give_dict_destinationFolders_and_listOf_srcFiles().items():
        print(f"Following files will be moved to destination folder '{destination_folder}':")
        for src_file in list_srcFiles:
            print(f"    - {src_file}")
        print("\n")
            

giveNames_of_destinationFolders_and_srcFiles()    
    
    
    
    
    
    
    
    
    