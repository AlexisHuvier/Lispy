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
        chars = chars.replace("(", " ( ").replace(")", " ) ").replace("\n", "")
        regex = re.compile(r"(\")((?:[^\\\"]|\\.)*)(\")")
        chars = regex.sub(" \\1 \\2 \\3 ", chars)
        tokens = chars.split()
        escaped = {
            "\\r": "\r", "\\n": "\n", "\\t": "\t", "\\b": "\b", '\\"': "\"", "\\\\": "\\"
        }
        tlist = []
        while len(tokens):
            token = tokens.pop(0)
            if token == '"':
                text = '"'
                try:
                    while tokens[0] != '"':
                        if text == '"':
                            temp = tokens[0]
                        else:
                            temp = " " + tokens[0]
                        for i in escaped.keys():
                            temp = temp.replace(i, escaped[i])
                        text += temp
                        tokens.pop(0)
                    text += '"'
                    tokens.pop(0)
                except IndexError:
                    print("Expected \"")
                    sys.exit(0)
                tlist.append(text)
            elif tokens != "":
                tlist.append(token)
        return tlist

