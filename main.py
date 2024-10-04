
from enum import Enum

import sys
from sqlalchemy.exc import NoResultFound

from models import Vocabulary
from utils import lookup
from schemas import VocabularySchema
from db import get_session
from exceptions import VocabularyNofound



class TextColor(Enum):
    RED = "\x1b[0;31;40m"
    GREEN = "\x1b[0;32;40m"
    BLUE = "\x1b[0;34;40m"
    BOLD_RED= "\x1b[1;31;40m"
    ENDCOLOR = "\x1b[0m"


def main(keyword):
    session_gen = get_session()
    db_session = next(session_gen)
    try:
        vocabulary = db_session.query(Vocabulary).filter_by(name=keyword).one()
    except NoResultFound:
        print(f"vocabulary: {keyword} not found in database, try search on Dr.eye")
        vocabulary_obj = lookup(keyword)
        if vocabulary_obj is None:
            raise VocabularyNofound
        
        vocabulary = Vocabulary(**vocabulary_obj.__dict__)
        db_session.add(vocabulary)
        db_session.commit()

    vocabulary_obj = VocabularySchema(
        name=vocabulary.name,
        pronunciation=vocabulary.pronunciation,
        variant=vocabulary.variant,
        content_en=vocabulary.content_en,
        content_zh=vocabulary.content_zh,
    )

    print(
        f"{TextColor.BOLD_RED.value}{vocabulary_obj.name}{TextColor.ENDCOLOR.value}\n"
        f"{TextColor.BLUE.value}{vocabulary_obj.pronunciation}{TextColor.ENDCOLOR.value}\n"
        f"{vocabulary_obj.variant}\n\n"
        f"{vocabulary.content_zh}"
    )



if __name__ == "__main__":
    keyword = None
    try:
        keyword = sys.argv[1]
    except IndexError:
        pass

    if not keyword:
        print("Please provide serach keyword")
        exit(1)

    try:
        main(keyword)
    except VocabularyNofound as e:
        print(e.message, f"provided keyword: {keyword}")