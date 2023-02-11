import re

def hashtag_to_link(sentence):
    """This function replace hashtag text into HTML link and returns 
        the new text."""
    pattern = "(#[\w\d_]+)"
    replacement = r'<a href="">\1</a>'
    result = re.sub(pattern, replacement, sentence)

    return result


print(hashtag_to_link("Like soccer? Stay tuned to watch #PSG vs #Bayern on Feb. 14, #2023."))