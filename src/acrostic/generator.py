from typing import List
from wonderwords import RandomWord

class AcrosticGenerator:
    __generator = RandomWord()
    
    @classmethod
    def get_random_word(cls, starting_letter):
        return cls.__generator.word(
            starts_with=starting_letter,
            include_parts_of_speech=["adjectives"]
        )

    @classmethod
    def generate(cls, key: str) -> List[str]:
        acrostic = []
        for char in list(key):
            acrostic.append(AcrosticGenerator.get_random_word(char))
        return acrostic
