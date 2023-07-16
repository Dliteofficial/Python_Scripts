import os
#Build a file moving script which moves files with the name module to a dir module

def move(src, dst, common_denominator):
    if not os.path.exists(src):
        print("ERR: Source Directory Doesnt Exist!!!")
        return

    if not os.path.exists(dst):
        print("Destination Doesnt Exist. Creating One Now!")
        os.mkdir(dst)
    
    for file in os.listdir(src):
        if common_denominator.lower() in file.lower():
            file_src = os.path.join(src, file)
            file_dst = os.path.join(dst, file)
            os.rename(file_src, file_dst)
            print(f"files with {file} in their name has been moved from {(os.path.join(src, file)).lower()} to {(os.path.join(dst, file)).lower()}")

try:
    src = input('Enter the source directory: \n')
    dst = input('Enter the destination directory: \n')
    common_denominator = input('What would be the common denominator: \n')

    move(src.lower(), dst.lower(), common_denominator.lower())

except KeyboardInterrupt:
    print("ERR: KEYBOARD INTERRUPTION!!!")