
import requests
from typing import Optional

from bs4 import BeautifulSoup

from schemas import VocabularySchema



def lookup(keyword: str) -> Optional[VocabularySchema]:
    """
    Search by keyword from Dr.eye and return a VocabularySchema object.
    Return None if result not found
    """
    url = f"https://yun.dreye.com/dict_new/dict.php?w={keyword}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    main = soup.find("div", {"class": "main"})
    q_middle = main.find("div", {"class": "q_middle"})
    if "ews_sys_msg" in q_middle.p.get("class", []):
        print(f"No result matched for \"{keyword}\"")
        print(q_middle.p.text)
        return
    display_word = q_middle.find("div", {"id": "display_word"})
    name = display_word.span.string.strip()  # the lookup word
    q_middle_bd = q_middle.find("div", {"class": "q_middle_bd"})
    pronunciation = None
    pronunciation_span = q_middle_bd.find("span", {"class": "phonetic"})  # KK pronunciation
    if pronunciation_span:
        pronunciation = pronunciation_span.text.strip()
    content_digest = q_middle_bd.find(id="digest")
    variant = ""
    if content_digest:
        variant = " ".join(map(lambda x: x.string.strip(), content_digest.p.children))  # verb variants
    description_body = q_middle_bd.find_next("div", {"class": "q_middle_bd"})
    content_zh_div = description_body.find("div", {"id": "usual", "class": "content"})
    # English to Chinese explanation 
    content_zh = ""
    for line in content_zh_div.find_all():
        if line.string:
            content_zh = content_zh + line.string.strip() + "\n"

    content_zh = content_zh.rstrip()
    # English to English explanation 
    content_en_div = description_body.find("div", {"id": "oxfordEE", "class": "content"})
    content_en = ""
    for line in content_en_div.find_all():
        if line.string:
            content_en = content_en + line.string.strip() + "\n"

    content_en = content_en.rstrip()

    vocabulary = VocabularySchema(name, pronunciation=pronunciation, content_en=content_en, content_zh=content_zh, variant=variant)

    return vocabulary
