# musicscript
recompressing folders of audio conveniently

takes a folder with .flac or .wav files and creates a ninja file to convert all of it to .opus as fast as possible

example: 
```
./compress.py -i /home/user/Music -o /home/opusmusic
ninja -f compress.ninja
```