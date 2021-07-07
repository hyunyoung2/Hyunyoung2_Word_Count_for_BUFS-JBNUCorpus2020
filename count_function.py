"""
This is sample code to count the frequency of word in BUFS-JBNUCorpus2020

 * you can download the corpus from https://github.com/bufsnlp2030/BUFS-JBNUCorpus2020

BUFS-JBNUCorpus2020 consists of the following: 

# sent_id = 1
# file = 00000
# text = 현재 사회적 대타협을 통해서 노동시장 구조를 개선하기 위해 노사정이 머리를 맞대고 노력하고 있는데 3월 말까지 좋은 합의안을 만들어 주실 것이라고 기대하고 있다 .
1	현재	현재	ADV	MAG	_	4	AP	_	_
2	사회적	사회적	DET	MM	_	3	NP	_	_
3	대타협을	대타협+을	NOUN	NNG+JKO	_	4	NP_OBJ	_	_
4	통해서	통하+어서	VERB	VV+EC	_	7	VP	_	_
5	노동시장	노동시장	NOUN	NNG	_	6	NP	_	_
6	구조를	구조+를	NOUN	NNG+JKO	_	7	NP_OBJ	_	_
7	개선하기	개선하+기	VERB	VV+ETN	_	8	VP_OBJ	_	_
8	위해	위하+어	VERB	VV+EC	_	11	VP	_	_
9	노사정이	노사정+이	NOUN	NNG+JKS	_	11	NP_SBJ	_	_
10	머리를	머리+를	NOUN	NNG+JKO	_	11	NP_OBJ	_	_
11	맞대고	맞대+고	VERB	VV+EC	_	12	VP	_	_
12	노력하고	노력하+고	VERB	VV+EC	_	13	VP	_	_
13	있는데	있+는데	AUX	VX+EC	_	18	VP	_	_
14	3월	3+월	NUM	SN+NNB	_	15	NP	_	_
15	말까지	말+까지	NOUN	NNB+JX	_	18	NP_AJT	_	_
16	좋은	좋+은	ADJ	VA+ETM	_	17	VP_MOD	_	_
17	합의안을	합의안+을	NOUN	NNG+JKO	_	18	NP_OBJ	_	_
18	만들어	만들+어	VERB	VV+EC	_	19	VP	_	_
19	주실	주+시+ㄹ	AUX	VX+EP+ETM	_	20	VP_MOD	_	_
20	것이라고	것+이+라고	VERB	NNB+VCP+EC	_	21	VNP_CMP	_	_
21	기대하고	기대하+고	VERB	VV+EC	_	22	VP	_	_
22	있다	있+다	AUX	VX+EF	_	23	VP	_	_
23	.	.	PUNC	SF	_	0	NP	_	_

The BUFS-JBNUCorpus2020 corpus consists of five format 

First, string starting with "# sent_id ="

Second, string starting with "# file ="

Third, string starting with "# text ="

Fourth, explainingg words line by line from third format "# text = "

Fifth, '' empty straing to separate sentences
"""

#-*- coding: utf-8 -*-

from glob import glob
import os
from collections import OrderedDict

ROOT_DIR = "corpus_data/"

# For Debugging option, increasing level enumerate log in detail
DEBUG_LEVEL = ["DEBUG_LEVEL_0", "DEBUG_LEVEL_1", "DEBUG_LEVEL_2"]

## if DEBUG_LEVEL is 0, No print for debugging
DEBUG = DEBUG_LEVEL[0]

## train and test corpus 
LINE_OPTS = ["# sent_id =", "# file =", "# text =", ""] # "" means empty string

def read_raw_corpus(path):
    """Reading data line by line from BUFS-JBNUCorpus2020

    This function aim to files under 'corpus_data' directory

    Each file format is the following:

    # sent_id = 1
    # file = 00000
    # text = 현재 사회적 대타협을 통해서 노동시장 구조를 개선하기 위해 노사정이 머리를 맞대고 노력하고 있는데 3월 말까지 좋은 합의안을 만들어 주실 것이라고 기대하고 있다 .
    1	현재	현재	ADV	MAG	_	4	AP	_	_
    2	사회적	사회적	DET	MM	_	3	NP	_	_
    3	대타협을	대타협+을	NOUN	NNG+JKO	_	4	NP_OBJ	_	_
    ....

    Arg:
      path(str): The path of the file to be read 
    
    return:
      data(list): A list of lines in raw file like 
                  ["line1_str", "line2_str", ..., "line_n_str"]
    """
    ## For debugging 
    assert isinstance(path, str), "Type Check, path is {} in 'read_raw_corpus'".format(type(path))


    with open(path, "r") as wr:
        data = [val.strip() for val in wr.readlines()] # to strip the front and back from the text

    
    if DEBUG in DEBUG_LEVEL[1:]: # ["DEBUG_LEVEL_0", "DEBUG_LEVEL_1", "DEBUG_LEVEL_2"]
        print("The number of lines: {}".format(len(data)))
        print("for top 5 of examples, \n{}".format(data[0:5]))

    return data

def write_word_dict_file(word_dict, path, sort_opt=True):
    """write word count dictionary

    The dictionary format is 

    "word\tFre."
    "word_i\t3"

    It is sorted by Frequency 

    Args:
        word_dict(dict): The dictionary pairing word symbol with its frequency  
        path(str): The location of word dictionary, by defualt 'word_dict' in the current directory
        sort_opt(bool): sorting option, if True, sorting
                                        if False, not sorting

    Return:
        None
    """
    
    ## For debugging
    assert isinstance(word_dict, dict), "Type Check, word_dict is {} in 'write_word_dict_file'".format(type(path)) 
    assert isinstance(path, str), "Type Check, path is {} in 'write_word_dict_file'".format(type(path))
    assert isinstance(sort_opt, bool), "Type Check, sort_opt is {} in 'count_word'".format(type(sort_opt))

    ## dict head
    word_dict_head = ["WORD", "Fre."]

    ## dict file 
    dict_loc = path+"word_dict"

    with open(dict_loc, "w") as wf:

        wf.write("\t".join(word_dict_head)+"\n")

        if sort_opt == True:
            ## sorting dictionary with decreasing order 
            ## If you want to change to increasing order
            ## Set 'reverse=True' to 'reverse=False'
            final_word_cnt = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
            for word_idx, word_val in enumerate(final_word_cnt):
                wf.write(word_val[0]+"\t"+str(word_val[1])+"\n")
        else:
            for word_idx, word_val in word_dict.items(): 
                wf.write(word_idx+"\t"+str(word_val)+"\n")
             
    print("\n===== Writing word dictionary is done in {} ======".format(dict_loc))  
 

def count_word(file_data, word_dict):
    """Counting the number of words in BUFS-JBNUCorpus2020

    When counting the frequencies of words in this function,
   
    functuation mark like ',.' is dealt with as word symbol    

    Args:
       file_data(list): sentences read corpus line by line
       word_cnt(dict): Dictionary to count the nubmer of words, pairing word symbole with the frequencies
                       like {"word_1": 1, "word_2": 2, ...} 

    Returns:
       None
    """
   
    ## For Debugging
    assert isinstance(file_data, list), "Type Check, file_path is {} in 'count_word'".format(type(file_data))
    assert isinstance(word_dict, dict), "Type Check, sort_opt is {} in 'count_word'".format(type(word_dict))

    word_cnt = word_dict 
 
    ## considerging
    ## LINE_OPTS = ["# sent_id =", "# file =", "# text =", ""] # "" means empty string
    for line_idx, line_val in enumerate(file_data):
       
        if LINE_OPTS[2] in line_val: 
            temp_sent = line_val.split()[3:]

            for word_idx, word_val in enumerate(temp_sent):
                if  word_cnt.get(word_val):
                    word_cnt[word_val] += 1
                else:
                    word_cnt[word_val] = 1

    if DEBUG in DEBUG_LEVEL[2:]: # ["DEBUG_LEVEL_0", "DEBUG_LEVEL_1", "DEBUG_LEVEL_2"]
        print("\n===== Check Word Count =====")
        print("The total of word_cnt: {}".format(len(word_cnt)))
        print("The top 5 examples: {}".format(list(word_cnt.items())[0:5]))

        
def make_word_dict(raw_corpus_dir_path, dict_dir_path, sorting):
    """Make word dictrionary with BUFS-JBNUCorpus2020

    using the structure of directory 

    Args:
        raw_corpus_dir_path(str): The location of raw corpus directory
        dict_dir_path(str):  The location of directory for word dictionary 

    Return: 
       None 
    """

    ## For Debugging
    assert isinstance(raw_corpus_dir_path, str), "Type Check, raw_corpus_dir_path is {} in 'make_word_dict'".format(type(raw_corpus_dir_path))
    assert isinstance(dict_dir_path, str), "Type Check, dict_dir_path is {} in 'make_word_dict'".format(type(dict_dir_path))
    assert isinstance(sorting, bool), "Type Check, sorting is {} in 'make_word_dict'".format(type(sorting))

    ## Word dictionary
    word_cnt_dict = OrderedDict()

    list_of_files = glob(raw_corpus_dir_path+"*", recursive=True)
     
    files_sorted = sorted(list_of_files)
  
    if DEBUG in DEBUG_LEVEL[0:]:
        print("\n===== Check corpus directory =====")
        print("The type of 'list_of_files': {}".format(type(list_of_files)))
        print("The number of files: {}".format(len(list_of_files)))
        print("For top 5 of examples:\n{}".format(list_of_files[0:5]))
        print("\n===== a list of files is sorted =====")
        print("The type of 'files_sorted': {}".format(type(files_sorted)))
        print("The number of files sorted: {}".format(len(files_sorted)))
        print("For top 5 of examples sorted:\n{}".format(files_sorted[0:5]))

    for idx, val in enumerate(files_sorted):

        if DEBUG in DEBUG_LEVEL[1:]: # ["DEBUG_LEVEL_0", "DEBUG_LEVEL_1", "DEBUG_LEVEL_2"]
            print("\n===== Preprocessing the file {} =====".format(val))

        raw_data = read_raw_corpus(val)

        if DEBUG in DEBUG_LEVEL[1:]: # ["DEBUG_LEVEL_0", "DEBUG_LEVEL_1", "DEBUG_LEVEL_2"]
            print("\n===== Reading the file {} is done ! =====".format(val))
            print("\n===== Counting word starts in 'make_word_dict' function with 'count_word' function =====") 

        count_word(file_data=raw_data, word_dict=word_cnt_dict)

        if DEBUG in DEBUG_LEVEL[1:]: # ["DEBUG_LEVEL_0", "DEBUG_LEVEL_1", "DEBUG_LEVEL_2"]
            print("\n===== Counting word ends in 'make_word_dict' function with 'count_word' function =====") 

    write_word_dict_file(word_dict=word_cnt_dict, path=dict_dir_path, sort_opt=sorting)

    
if __name__ == "__main__":
    """
    ROOT_DIR = "corpus_data/"

    # For Debugging option, increasing level enumerate log in detail
    DEBUG_LEVEL = ["DEBUG_LEVEL_0", "DEBUG_LEVEL_1", "DEBUG_LEVEL_2"]

    ## if DEBUG_LEVEL is 0, No print for debugging
    DEBUG = DEBUG_LEVEL[0]

    ## train and test corpus 
    LINE_OPTS = ["# sent_id =", "# file =", "# text =", ""] # "" means empty string
    """

    raw_corpus_dir = ROOT_DIR

    dict_dir = "./" # by default  current directory

    sort_option = True # If True, order decreased by frequency of word
                       # If False, order inserting word into dictionary
 
    make_word_dict(raw_corpus_dir_path=raw_corpus_dir, dict_dir_path=dict_dir, sorting=sort_option)

