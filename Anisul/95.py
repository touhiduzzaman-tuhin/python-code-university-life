import re

pattern = r"[0-9][A-Z][a-z]"

if re.match(pattern, "0Aadjfdjkidd"):

    print("Match")
