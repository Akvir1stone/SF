def check_poli(text):
    text.lower()
    text.replace(' ', '')
    if text == text[::-1]:
        return True
    else:
        return False


print(check_poli(input('type text ')))
