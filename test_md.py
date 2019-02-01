import markdown
import codecs

input_file = codecs.open("markdown.md", mode="r", encoding="utf-8")
text = input_file.read()
html = markdown.markdown(text)

output_file = codecs.open("html.html", "w",encoding="utf-8", errors="xmlcharrefreplace")
output_file.write(html)