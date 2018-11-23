# movie_subtitle_yml_converter
A simple python script to convert movie subtitles (only tested with .srt files) into yml files, so they can be for chatbots
The operation is very simple. Download the subtitles you'd like to convert, from here for example: https://www.opensubtitles.org/en/search/subs
then run the script, with the file as an argument:

$ ./convert.py [path to your movie subtitles]

I only ever used .srt files. The output file will be in .yml, and can be used to train chatbots. It works fairly well, if you
picked a good movie :)
