import re

pattern = r"(an)*"

if re.match(pattern, "colouyr"):

    print("Match")


# a* means zero  or More found