from src.acrostic.generator import AcrosticGenerator
import sys

if __name__ == "__main__":
    name = sys.argv[1]
    acrostic = AcrosticGenerator.generate(name)
    for a in acrostic:
        print(a)
