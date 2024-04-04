import os
from colorama import init, Fore
init()

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            try:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
            except Exception as e:
                print(f"Error accessing {filename}: {e}")
    return total_size

def main():
    #get the directory where the script is located
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    #traverse through each folder in the current directory
    for folder in os.listdir(current_directory):
        folder_path = os.path.join(current_directory, folder)
        
        #check if the item is a directory
        if os.path.isdir(folder_path):
            try:
                total_size = get_directory_size(folder_path)
                if total_size > 1073741824:
                    print(f"{Fore.RED}{folder}: {total_size/1073741824} gigabytes{Fore.RESET}")
                elif total_size > 1048576:
                    print(f"{Fore.GREEN}{folder}: {total_size/1048576} megabytes{Fore.RESET}")
                else:
                    print(f"{Fore.GREEN}{folder}: {total_size/1024} kilobytes{Fore.RESET}")
            except Exception as e:
                print(f"Error processing {folder}")

if __name__ == "__main__":
    main()

#made with love by zezenta