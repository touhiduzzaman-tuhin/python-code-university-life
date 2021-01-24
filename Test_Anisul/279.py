import re

pattern = r"you"

print(re.findall(pattern, "you are a boy, but notyou, do you know youtube is good"))
