import random
import uuid

# while True:
#     id = str(uuid.uuid4())
#     texte = id[:random.randint(1, len(id) - 1)]
#     espaces = " " * random.randint(1, 50)
#     print("{}{}".format(espaces, texte))



def hack():
    while True:
        id = str(uuid.uuid4())
        texte = id[:random.randint(1, len(id) - 1)]
        espaces = " " * random.randint(1, 50)
        print("{}{}".format(espaces, texte))

hack()