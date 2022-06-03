#-*- encoding: UTF-8-*-
import re

msg = 'input: Robot please distribute {category}s to everyone in the {room}.'

result=re.sub(r"([?.!,])", r" \1 ", msg)
result=re.sub(r'[" "]+'," ",result)
result=re.sub(r"[^a-zA-z?.!, ]+", " ",result)

result = result.rstrip(" .")
print(result)

