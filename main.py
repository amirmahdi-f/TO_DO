import json
from datetime import datetime
from random import choice

use_token = [i for i in range (1, 1000)]
free_token = []
def date_now ():
    return datetime.now()


def make_Token(token_list):
    free_token.sort()
    if free_token != []:
        result = free_token[0]
        free_token.pop(0)
    else:
        result = use_token[0]
        token_list.pop(0)
    return result


class TO_DO:
    def __init__(self, To_Do_list):
        self.To_Do_list = To_Do_list
    def add_work (self, work, status, information):
        Token = make_Token(use_token)
        self.To_Do_list[Token] = {"name": work, "status" : status, "information" : information}

    def remove_work (self, Token):
        Token = int(Token)
        self.To_Do_list.pop(Token)
        free_token.append(Token)

    def show_all (self):
        print(self.To_Do_list)

    def change(self, Token, old_part , new_part):
        Token = int(Token)
        self.To_Do_list[Token][old_part] = new_part