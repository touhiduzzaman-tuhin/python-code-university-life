import re

pattern = r"(an)+"

if re.match(pattern, "colouyr"):

    print("Match")


# a* means one or More found


import re

pattern = r"a+b"

if re.match(pattern, "abcolouyr"):

    print("Match")


# a* means  or More found

import re

pattern = r"a*b"

if re.match(pattern, "colouyr"):

    print("Match")


# a* means  or More found