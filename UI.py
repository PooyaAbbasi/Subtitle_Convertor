""" This is the CLI module for interaction with user ."""
from Conversion import convert_vtt_files_to_srt
from file_paths import get_vtt_file_paths

print("This program will convert a .vtt file to .srt \n" +
      ".srt file will be saved in directory of your .vtt file")


while True:
    given_dir = input("\nEnter the complete path of directory contains .vtt files " +
                      "\n or type 'exit' to close the program :\n")
    if given_dir == 'exit':
        break

    convert_vtt_files_to_srt(*get_vtt_file_paths(given_dir))

    print("\n\n Your srt files crated successfully!")
    break


print("\n I hope you enjoy from this program ! \n Thank you")
