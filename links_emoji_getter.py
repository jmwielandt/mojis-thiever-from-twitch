import os
import re
import sys


FOLDER_DEST = "mojis"
LEVEL = 3  # el tamaño
PATTERN = f"https://static-cdn\.jtvnw\.net/emoticons/v1/\d+/{LEVEL}\.0"


if not os.path.exists(FOLDER_DEST):  # creo la carpeta de destino si no existe
    os.mkdir(FOLDER_DEST)

for file_name in sys.argv[1:]:  # por cada archivo que le paso como entrada...
    with open(file_name, "r", encoding="utf-8") as f:
        content = f.read()

    a = re.findall(PATTERN, content)

    with open(file_name.replace(".", ".links.", 1), "w", encoding="utf-8") as f:
        print(*a, sep="\n", file=f)
