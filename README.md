## Sample program convert all .vtt subtitle files in a given directory to .srt, through CLI.

Clone the project and run UI.py with **`python 3.11`**, No more requirements is needed. 
By executing UI.py on your device, 
it'll get the full path of a directory that contains your vtt subtitle files in your device,
and make srt files of them with their own names in the very directory.

This program used python and `RegEx` to perform conversion [see this module](Conversion.py).

### Why I created this?
As the _**KMPlayer 64x**_ doesn't work with vtt subtitle files 
I wrote this program to convert vtt files to srt very quickly,
so I can use subtitles by **_KMPlayer_**.
Also, I wanted to write a sample project as a python beginner.


- This program has been tested by simple files in [test files](./Test_files).
