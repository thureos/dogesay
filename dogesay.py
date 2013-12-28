#!/usr/bin/python

from argparse import ArgumentParser
from random   import randrange, choice

DOGE_PREFIXES   = ["such", "much", "so", "many", "wow", "very"]
DOGE_EJACULATES = ["wow"]
DOGE_FACE_PATHS = {"norm" : "static/doge.txt",
                   "ascii": "static/doge_ascii.txt"}

WOW_CHANCE = 5
MAX_WHITESPACE = 15
MIN_WHITESPACE = 2

MAX_PREPENDEE_LEN = 0

def doge_syntax(clause):
    return clause if len(clause.split())>1 else choice(DOGE_PREFIXES)+" "+clause

used_indices = []
def random_select_no_repeat(max, ref_pool):
    index =  randrange(0,max)
    while index in ref_pool:
        index =  randrange(0,max)
    ref_pool.append(index)
    return index
    
def prepend(orig, addition):
    orig = addition + orig    

def random_insert_clause(clause, img_file):
    img_file[random_select_no_repeat(len(img_file), used_indices)] += (random_whitespace()+clause)
    # TODO: implement prepending as well
    # if randrange(0,2)==1:
    #     img_file[random_select_no_repeat(len(img_file), used_indices)] += (random_whitespace()+clause)
    # else:
    #     index = random_select_no_repeat(len(img_file), used_indices)
    #     prependee = clause + ""

    #     img_file[index] = prependee + img_file[index]
    #     if len(clause)>MAX_PREPENDEE_LEN:
    #         global MAX_PREPENDEE_LEN
    #         MAX_PREPENDEE_LEN = len(clause)
    #         # TODO: normalize prepending whitespace

def random_whitespace():
    return randrange(MIN_WHITESPACE, MAX_WHITESPACE)*" "
    
if __name__ == "__main__":
    parser = ArgumentParser(description="Cowsay for a new generation.")
    parser.add_argument("inputfile", metavar="<input file>")
    parser.add_argument("-a", "--ascii", action="store_true",
                        help="Use ASCII doge")

    args = parser.parse_args()

    doge_face_path = DOGE_FACE_PATHS["ascii" if args.ascii else "norm"]
    doge_face_file = open(doge_face_path, "r").read().splitlines()

    clauses_file = open(args.inputfile, "r")

    for clause in clauses_file:
        clause = random_whitespace()+doge_syntax(clause.strip())

        move_next_iter = False
        while not move_next_iter:
            if randrange(0,10) > WOW_CHANCE:
                random_insert_clause(choice(DOGE_EJACULATES), doge_face_file) 
            move_next_iter = True

        random_insert_clause(clause, doge_face_file)

    for line in doge_face_file:
        print(line)
