from typing import Any, Tuple
from manim import *

__version__ = "0.1.0"

ALIGN_LEFT = -1
ALIGN_RIGHT = 1

DEFAULT_FONT_SIZE = 24
DEFAULT_LATEX_FONT_SIZE = 36

def create_addcirclebox(color: color) -> VGroup:
    addbox = VGroup()
    box = Circle(radius=0.2, fill_color=color, fill_opacity=0.5, stroke_color=color)
    add_sign = Text("+", font_size=24).move_to(box.get_center())
    addbox.add(box, add_sign) # add both objects to the VGroup
    return addbox


def create_textbox(color: color, string: str, font_size=DEFAULT_FONT_SIZE, width=2) -> VGroup:
    textbox = VGroup() # create a VGroup
    box = Rectangle(  # create a box
        width=width, height=.5, fill_color=color, 
        fill_opacity=0.5, stroke_color=color
    )
    text = Text(string, font_size=font_size).move_to(box.get_center()) # create text
    textbox.add(box, text) # add both objects to the VGroup
    return textbox


def create_latexbox(color: color, latex: str, font_size=DEFAULT_LATEX_FONT_SIZE, width=2) -> VGroup:
    textbox = VGroup() # create a VGroup
    box = Rectangle(  # create a box
        width=width, height=.5, fill_color=color, 
        fill_opacity=0.5, stroke_color=color
    )
    text = Tex(latex, font_size=font_size).move_to(box.get_center()) # create latex
    textbox.add(box, text) # add both objects to the VGroup
    return textbox


def create_dot_with_text(
        string: str,
        pos: Point=None,
        align=ALIGN_RIGHT,
        font_size=DEFAULT_FONT_SIZE) -> Tuple[VMobject, VMobject]:

    dot = Dot() if pos is None else Dot(pos)
    next_to_pos = RIGHT if align == ALIGN_RIGHT else LEFT
    text = Text(string, font_size=font_size).next_to(dot, next_to_pos) # create text
    return dot, text


def create_dot_with_latex(
        latex: str,
        pos: Point=None,
        align=ALIGN_RIGHT,
        font_size=DEFAULT_LATEX_FONT_SIZE) -> Tuple[VMobject, VMobject]:
    dot = Dot() if pos is None else Dot(pos)
    next_to_pos = RIGHT if align == ALIGN_RIGHT else LEFT
    text = Tex(latex, font_size=font_size).next_to(dot, next_to_pos) # create latex
    return dot, text


def create_90_elbowed_arrow_start_horizontal(start: Point, end: Point, **kwargs: Any) -> VGroup:
    print("create_90_elbowed_arrow_start_horizontal")
    elbowed_arrow = VGroup()
    elbow_radius = 0.3
    elbow_start_delta = -elbow_radius if start[0] < end[0] else elbow_radius
    elbow_start = [end[0]+elbow_start_delta, start[1], start[2]]
    elbow_end_delta = elbow_radius if start[1] < end[1] else -elbow_radius
    elbow_end = [end[0], start[1]+elbow_end_delta, start[2]]
    angle = 1.5707963267948966
    if (start[0] > end[0] and start[1] < end[1]) or \
        (start[0] < end[0] and start[1] > end[1]):
        angle = -angle
    line = Line(start=start, end=elbow_start, **kwargs)
    arc = ArcBetweenPoints(start=elbow_start, end=elbow_end, angle=angle, **kwargs)
    arrow = Arrow(
        start=elbow_end, end=end, buff=0, max_tip_length_to_length_ratio=0.05, **kwargs
        )
    elbowed_arrow.add(line, arc, arrow)
    return elbowed_arrow

def create_90_elbowed_arrow_start_vertical(start: Point, end: Point, **kwargs: Any) -> VGroup:
    elbowed_arrow = VGroup()
    elbow_radius = 0.3
    elbow_start_delta = -elbow_radius if start[1] < end[1] else elbow_radius
    elbow_start = [start[0], end[1]+elbow_start_delta, start[2]]
    elbow_end_delta = elbow_radius if start[0] < end[0] else -elbow_radius
    elbow_end = [start[0]+elbow_end_delta, end[1], start[2]]
    angle = 1.5707963267948966
    if (start[0] < end[0] and start[1] < end[1]) or \
        (start[0] > end[0] and start[1] > end[1]):
        angle = -angle
    line = Line(start=start, end=elbow_start, **kwargs)
    arc = ArcBetweenPoints(start=elbow_start, end=elbow_end, angle=angle, **kwargs)
    arrow = Arrow(
        start=elbow_end, end=end, buff=0, max_tip_length_to_length_ratio=0.05, **kwargs
        )
    elbowed_arrow.add(line, arc, arrow)
    return elbowed_arrow

def create_90_elbowed_arrow(start: Point, end: Point, start_vertical=False, **kwargs: Any) -> VGroup:
    if start_vertical:
        return create_90_elbowed_arrow_start_vertical(start, end, **kwargs)
    else:
        return create_90_elbowed_arrow_start_horizontal(start, end, **kwargs)