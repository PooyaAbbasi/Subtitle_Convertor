""" This is the CLI module for interaction with user ."""
from Conversion import convert_vtt_to_srt

print("This program will convert a .vtt file to .srt \n" +
      ".srt file will be saved in directory of your .vtt file")


def validate_file_extension(vtt_file_path: str):
    return vtt_file_path.endswith(".vtt")


while True:
    vtt_file_path = input("\nEnter the complete path to the .vtt file " +
                          "\n or type 'exit' to close the program :\n").strip('"').strip()
    if vtt_file_path == 'exit':
        break

    elif not validate_file_extension(vtt_file_path):
        print(" Your file path is not a have .vtt extension ")
        continue

    elif type(result := convert_vtt_to_srt(vtt_file_path)) == FileNotFoundError:
        print(result)
        continue
    else:
        print(" Your srt file crated successfully!")
        break


print("\n I hope you enjoy from this program ! \n Thank you")
