from typing import List
from wonderwords import RandomWord

class AcrosticGenerator:
    __generator = RandomWord()

    @classmethod
    def generate(cls, key: str) -> List[str]:
        acrostic = []
        for char in list(key):
            acrostic.append(
                cls.__generator.word(
                    starts_with=char,
                    include_parts_of_speech=["adjectives"]
                )
            )
        return acrostic
