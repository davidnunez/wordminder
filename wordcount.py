#!/usr/bin/env python
import envoy
import requests
import time
import os
import _keys


def print_directory(rootdir):
	for subdir, dirs, files in os.walk(rootdir):
	    for file in files:
	        print subdir+'/'+file

def analyze_directory(rootdir):
        total_words = 0
	for subdir, dirs, files in os.walk(rootdir):
	    for file in files:
                total_words += analyze_file(subdir+'/'+file)
                print subdir+'/'+file
        return total_words

# code from http://www.daniweb.com/software-development/python/code/216495/wordcount-of-a-text-file-python

def analyze_file(filename):
        # count lines, sentences, and words of a text file
        # set all the counters to zero
        lines, blanklines, sentences, words = 0, 0, 0, 0
        print '-' * 50
        try:
          # use a text file you have, or google for this one ...
          filename = 'lipsum.txt'
          textf = open(filename, 'r')
        except IOError:
          print 'Cannot open file %s for reading' % filename
          import sys
          sys.exit(0)
        # reads one line at a time
        for line in textf:
          print line,   # test
          lines += 1

          if line.startswith('\n'):
            blanklines += 1
          else:
            # assume that each sentence ends with . or ! or ?
            # so simply count these characters
            sentences += line.count('.') + line.count('!') + line.count('?')

            # create a list of words
            # use None to split at any whitespace regardless of length
            # so for instance double space counts as one space
            tempwords = line.split(None)
            print tempwords  # test

            # word total count
            words += len(tempwords)

        textf.close()
        print '-' * 50
        print "Lines      : ", lines
        print "Blank lines: ", blanklines
        print "Sentences  : ", sentences
        print "Words      : ", words
        return words

# code from https://gist.github.com/MichaelBlume/3962894

#r = envoy.run("find /Users/mike/Dropbox/writing | grep -v DS_Store | xargs wc -c")
#count = r.std_out.split()[-2]
#kb_written = int(count) // 1024

words = analyze_directory(_keys.THESIS_DIRECTORY)

r = requests.post(_keys.BEEMINDER_URL,
        {'auth_token': _keys.BEEMINDER_TOKEN
        ,'timestamp': time.time()
        ,'value': words
        })

print r.text
