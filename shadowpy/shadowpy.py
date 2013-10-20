#!/usr/bin/python

import sys
import re
import crypt

def usage():
    ''' usage function '''
    if len(sys.argv) < 3:
        sys.exit('usage: %s shadow_file word_list' % sys.argv[0])

def return_file(source_file):
    ''' This function returns a file as a str '''
    with open(source_file, 'r') as source:
        words = source.read()
    return words.split()

def hash_extract(shadow_file):
    ''' This function returns the hashes from the shadow file '''
    hashes = []
    for x in shadow_file:
        if len(x.split(':')[1]) <= 1:
            continue
        else:
            hashes.append(x.split(':')[1])
    return hashes

def salt_extract(hashes):
    ''' This function extracts the salts from a shadow file to use with crypt '''
    saltlst = []
    for salt in hashes:
        extract = re.search('.*\$', salt)
        saltlst.append(extract.group()[:-1])
    return saltlst

if __name__ == '__main__':
    usage()
    script, shadow_file, wordlist = sys.argv
    wrd = return_file(wordlist)
    shd = return_file(shadow_file)
    hsh = hash_extract(shd)
    slt = salt_extract(hsh)
    for salt in slt:
        for word in wrd:
            money = crypt.crypt(word, salt)
            if money in hsh:
                print word, money


