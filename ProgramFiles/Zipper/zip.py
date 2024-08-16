import os
import pyzipper
import sys
import zipfile
# from rich import print

def zip_folder(folder_path, zip_name, password):
    parent_folder = os.path.dirname(folder_path)
    contents = os.walk(folder_path)
    zip_file = pyzipper.AESZipFile(zip_name,'w',compression=pyzipper.ZIP_DEFLATED,encryption=pyzipper.WZ_AES)
    zip_file.pwd=password
    for root, folders, files in contents:
        for folder_name in folders:
            absolute_path = os.path.join(root, folder_name)
            relative_path = absolute_path.replace(parent_folder + '\\','')
            print ("[green italic]Adding '%s' to archive.[/green italic]" % absolute_path)
            zip_file.write(absolute_path, relative_path)
        for file_name in files:
            absolute_path = os.path.join(root, file_name)
            relative_path = absolute_path.replace(parent_folder + '\\','')
            print ("[green italic]Adding '%s' to archive.[/green italic]" % absolute_path)
            zip_file.write(absolute_path, relative_path)
    print ("[green italic]Created successfully.[/green italic]")
    zip_file.close()

def unzip_folder(input_zip, output_path, password):
    try:
        with pyzipper.AESZipFile(input_zip) as zip_file:
            zip_file.pwd = password
            zip_file.extractall(output_path)
        return [True]
    except pyzipper.BadZipFile as m:
        return [False, m]