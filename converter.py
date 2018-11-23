#!/usr/bin/env python
#
#by Eduardo"

#import TrillianRestaurationProject
import re
import sys

class converter:
    def __init__(self, file_name):
        pass
        self.file_name = file_name
        self.save_directory = '/usr/lib/python3.7/site-packages/chatterbot_corpus/data/english'
        self.header = 'categories:\n- movies\nconversations:\n'

    def set_new_file(self, new_name):
        pass
        self.file_name = new_name

    def convert_file(self):
        pass
        subtitles = open(self.file_name, 'r')
        converted_file = open(self.file_name.split('.')[0]+'.yml', 'w')
        converted_file.write(self.header)
        current_line = '- -'
        i = 0
        lines = subtitles.readlines()
        while i < len(lines):
            if re.search('-->', lines[i]):
                i += 1
                while len(lines[i]) != 1:
                    current_line += ' ' + lines[i]
                    i += 1
                current_line = current_line.replace('\n', '') + '\n'
                current_line = current_line.replace('\"', '\\\"')
                current_line = current_line.replace('\'', '\\\'')
                current_line = current_line.replace('<i>', '')
                current_line = current_line.replace('</i>', '')
                converted_file.write(current_line)
                if re.search('(- - )', current_line):
                    current_line = '  -'
                else:
                    current_line = '- -'
            else:
                i += 1


    def save_conversion(self):
        pass

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please add a file to convert.')
        print('$ converter \"my_cool_subtitles_to_convert\"')
        exit()
    c = converter(sys.argv[1])
    c.convert_file()
