import os
import pyzipper
import sys
import zipfile
# from rich import print

def zip_folder(folder_path, zip_name, password):
    parent_folder = os.path.dirname(folder_path)
    contents = os.walk(folder_path)
    try:
        # print("[green italic]Initializing zip module.[/green italic]")
        # print("\n")
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
        # print("\n")
        print ("[green italic]Created successfully.[/green italic]")
    except IOError as message:
        # print(f"[red italic]Error: {message}.[/red italic]")
        sys.exit(1)
    except OSError as message:
        # print(f"[red italic]Error: {message}.[/red italic]")
        sys.exit(1)
    except zipfile.BadZipfile as message:
        # print(f"[red italic]Error: {message}.[/red italic]")
        sys.exit(1)
    finally:
        # print("[green italic]Finished with zip module.[/green italic]")
        zip_file.close()

def unzip_folder(input_zip, output_path, password):
    try:
        print("[green italic]Initializing zip module.[/green italic]")
        with pyzipper.AESZipFile(input_zip) as zip_file:
            zip_file.pwd = password  # Convert password to bytes
            print("[green italic]Extracting the assets directory.[/green italic]")
            zip_file.extractall(output_path)
            print(f"[green italic]Successfully extracted '{input_zip}' to '{output_path}'.[/green italic]")
    except pyzipper.BadZipFile as m:
        print(f"[red italic]Error: {m} Incorrect password provided for decryption.[/red italic]")
        sys.exit(1)
    except zipfile.BadZipFile as message:
        print(f"[red italic]Error: extracting {input_zip}: {message}[/green italic]")
        sys.exit(1)
    except Exception as e:
        print(f"[red italic]Error: during extraction: {str(e)}.[/red italic]")
        sys.exit(1)