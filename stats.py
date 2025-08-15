def get_book_text(file_name):
      with open(file_name) as f:
        file = f.read()
        return file

def get_num_words(text):
    words = text.split()
    return (str(len(words)))

def get_num_char(text):
    count = {
        "a": 0
    }
    for l in text:
        if l.lower() in count:
            count[l.lower()] += 1
        else:   
            count[l.lower()] = 1
    return (count)

def sort_on(items):
    return items["num"]

def sorted_list(list):
    sorted = []
    for i in list:
        sorted.append({"char": i, "num": list[i]})
    sorted.sort(reverse=True, key=sort_on)
    return (sorted)



       