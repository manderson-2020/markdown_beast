import requests

from marko.renderer import Renderer
from marko.html_renderer import HTMLRenderer


class RenderBeast(Renderer):

  def render_children(self, element):
    print("render children here")
    children = element.children
    for child in children:
      print(child)
      self.render(child)

  def render_blank_line(self, element):
    print("this line was left blank on purpose")

  def render_heading(self, element):
    print("heading here")

  def render_paragraph(self, element):
    print("rendering_paragraph")
    # only type of paragraph right now is an api call
    # its children look like this:
    # [<marko.inline.StrongEmphasis object at 0x10ad84a30>, <marko.inline.RawText object at 0x10ad84f70>]
    verb = element.children[0].children[0]
    url = element.children[1].children.strip()
    print(verb.children == "POST")
    response = requests.get(url)
    print(url)
    print(response)

  def render_strong_emphasis(self, element):
    print("rendering strong emphasis")
    print(element.children)

  def render_raw_text(self, element):
    print("rendering raw text")
    print(element.children)
