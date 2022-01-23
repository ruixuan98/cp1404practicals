import wikipedia

phrase = input("Enter a page title or phrase: ")
while phrase != '':
    try:
        page = wikipedia.page(phrase, auto_suggest=False)
        print(page.title)
        print(page.summary)
        phrase = input("Enter a page title or phrase: ")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e)
        phrase = input("Enter a page title or phrase: ")
    except wikipedia.exceptions.PageError as a:
        print(a)
        phrase = input("Enter a page title or phrase: ")