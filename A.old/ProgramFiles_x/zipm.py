import os
import pyzipper
import sys
import zipfile

def zip_folderPyzipper(folder_path, output_path):
    parent_folder = os.path.dirname(folder_path)
    print(parent_folder)
    contents = os.walk(folder_path)
    try:
        zip_file = pyzipper.AESZipFile('new_test.zip','w',compression=pyzipper.ZIP_DEFLATED,encryption=pyzipper.WZ_AES)
        zip_file.pwd=b'PASSWORD'
        for root, folders, files in contents:
            for folder_name in folders:
                absolute_path = os.path.join(root, folder_name)
                relative_path = absolute_path.replace(parent_folder + '\\','')
                print ("Adding '%s' to archive." % absolute_path)
                zip_file.write(absolute_path, relative_path)
            for file_name in files:
                absolute_path = os.path.join(root, file_name)
                relative_path = absolute_path.replace(parent_folder + '\\','')
                print ("Adding '%s' to archive." % absolute_path)
                zip_file.write(absolute_path, relative_path)
        print ("'%s' created successfully." % output_path)
    except IOError as message:
        print (message)
        sys.exit(1)
    except OSError as message:
        print(message)
        sys.exit(1)
    except zipfile.BadZipfile as message:
        print (message)
        sys.exit(1)
    finally:
        zip_file.close()


# zip_folderPyzipper(os.path.join(os.getcwd(), os.path.join("System", os.path.join("Data", os.path.join("artex.chat", "assets")))), "temp")

def unzip_folder(input_zip, output_path, password):
    try:
        with pyzipper.AESZipFile(input_zip) as zip_file:
            zip_file.pwd = password.encode()  # Convert password to bytes
            zip_file.extractall(output_path)
            print(f"Successfully extracted '{input_zip}' to '{output_path}'.")
    except pyzipper.BadZipFile as m:
        print(f"{m} Incorrect password provided for decryption.")
        sys.exit(1)
    except zipfile.BadZipFile as message:
        print(f"Error extracting {input_zip}: {message}")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred during extraction: {str(e)}")
        sys.exit(1)

# unzip_folder("new_test.zip", os.path.join(os.getcwd(), os.path.join("System", "Media")), "PASSWORD")