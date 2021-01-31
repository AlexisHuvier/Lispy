import sys
import re


class Parser:
    @classmethod
    def parse(cls, program):
        return cls.read_from_tokens(cls.tokenize(program))

    @classmethod
    def read_from_tokens(cls, tokens):
        if len(tokens) == 0:
            return []
        token = tokens.pop(0)
        if token == '(':
            L = []
            while tokens[0] != ')':
                L.append(cls.read_from_tokens(tokens))
                if len(tokens) == 0:
                    print("Unexpected EOF :", tokens)
                    return []
            tokens.pop(0)
            return L
        elif token == ')':
            print("Unexpected ) : ", tokens)
            return []
        else:
            return cls.atom(token)

    @classmethod
    def atom(cls, token):
        try:
            return int(token)
        except ValueError:
            try:
                return float(token)
            except ValueError:
                return str(token)
    
    @classmethod
    def tokenize(cls, chars):
        chars = chars.replace("\n", "")
        escaped = {
            "\\r": "\r", "\\n": "\n", "\\t": "\t", "\\b": "\b", '\\"': "\"", "\\\\": "\\"
        }
        for i in escaped.keys():
            chars = chars.replace(i, escaped[i])
        tlist = []
        current = 0
        state = 0
        text = ""
        while(current != len(chars)):
            if state == 1 and (chars[current] != '"' or chars[current-1] == "\\") :
                text += chars[current]
            elif state == 1:
                tlist.append('"'+text+'"')
                text = ""
                state = 0
            elif chars[current] == "(":
                if text != "":
                    tlist.append(text)
                text = ""
                tlist.append("(")
            elif chars[current] == ")":
                if text != "":
                    tlist.append(text)
                text = ""
                tlist.append(")")
            elif chars[current] == '"':
                text = ""
                state = 1
            elif chars[current] == " ":
                if text != "":
                    tlist.append(text)
                text = ""
            else:
                text += chars[current]
            current += 1
        if text != "":
            tlist.append(text)
        return tlist


