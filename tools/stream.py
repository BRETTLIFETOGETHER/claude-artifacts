import json

SRC = '/Users/evelinechu22/Desktop/Code/conversations.json'
DEC = json.JSONDecoder()

def iter_conversations(path=SRC, chunk=8 << 20):
    """Yield top-level conversation objects from a huge JSON array without loading it all."""
    f = open(path, 'r', encoding='utf-8')
    buf = ''
    pos = 0
    # prime: find opening '['
    while '[' not in buf:
        buf += f.read(chunk)
    pos = buf.index('[') + 1
    while True:
        # skip whitespace and commas
        while True:
            while pos < len(buf) and buf[pos] in ' \t\r\n,':
                pos += 1
            if pos < len(buf):
                break
            more = f.read(chunk)
            if not more:
                return
            buf = buf[pos:]; pos = 0; buf += more
        if buf[pos] == ']':
            return
        while True:
            try:
                obj, end = DEC.raw_decode(buf, pos)
                break
            except ValueError:
                more = f.read(chunk)
                if not more:
                    return
                buf += more
        yield obj
        buf = buf[end:]
        pos = 0
