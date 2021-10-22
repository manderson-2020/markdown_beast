from marko import Markdown
from hypermark_protocol.render_beast import RenderBeast

mark = Markdown(renderer=RenderBeast)

print("doing stuff")


with open('tests/fixtures/sample_md.md') as md:
  parsed_md = mark.parse(md.read())
  mark.render(parsed_md)
  # print(mark.render(parsed_md))

print("stuff done")
