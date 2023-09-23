def text_editor(text, sym, ch):
    for i in range(len(text) - len(sym) + 1):
        if text[i:i + len(sym)] == sym:
            text = text[:i] + ch + text[i + len(sym):]
    return text
