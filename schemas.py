class VocabularySchema:
    def __init__(
            self,
            name: str,
            pronunciation: str = None,
            content_zh: str = None,
            content_en: str = None,
            variant: str = None,
        ) -> None:
        self.name = name
        self.pronunciation = pronunciation
        self.content_zh = content_zh
        self.content_en = content_en
        self.variant = variant

    def __repr__(self):
        return f"<VocabularySchema: {self.name}>"