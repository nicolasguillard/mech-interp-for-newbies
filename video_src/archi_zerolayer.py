from manim import *
from utils import *

DEFAULT_ARROW_BUFF = 0.0

def new_arrow(start, end, buff=DEFAULT_ARROW_BUFF):
    line = Line(
        start=start, end=end, stroke_width=2, buff=buff
        )
    line.add_tip(ArrowTriangleFilledTip(color=line.color, stroke_width=1).scale(.5))
    return line


class Archi0Layer(Scene):
    def tokens_embed(self):
        group = VGroup()

        tokens = create_textbox(GRAY, "tokens")
        embed = create_textbox(LIGHT_BROWN, "embed")
        embed.next_to(tokens, 2*UP)
        arrow_tokens_embed = new_arrow(tokens.get_top(), embed.get_bottom())
        group.add(tokens, arrow_tokens_embed, embed)

        return group
    

    def unembed_logits(self):
        group = VGroup()

        unembed = create_textbox(LIGHT_BROWN, "unembed")
        logits = create_textbox(GRAY, "logits")
        logits.next_to(unembed, 2*UP)
        arrow_unembed_tokens = new_arrow(unembed.get_top(), logits.get_bottom())
        group.add(unembed, arrow_unembed_tokens, logits)

        return group


    def architecture(self):
        archi = VGroup()

        tokens_embed = self.tokens_embed()
        unembed_logits = self.unembed_logits()
        unembed_logits.next_to(tokens_embed, 2*UP)
        arrow = new_arrow(tokens_embed.get_top(), unembed_logits.get_bottom())

        archi.add(tokens_embed, arrow, unembed_logits)

        archi.center()
        return archi


    def construct(self):
        archi = self.architecture()
        self.play(FadeIn(archi))

        tokens = VGroup()
        for i in range(0, 10):
            token = Rectangle(height=0.1, width=0.1, color=YELLOW, stroke_width=1)
            token.set_fill(YELLOW, opacity=0.5)
            tokens.add(token)
        tokens.arrange(RIGHT, buff=0.1)

        sequence = MarkupText(
            f'According to Asimov\'s laws,\na robot may not <span fgcolor="{PURPLE}">...</span>', font_size=DEFAULT_FONT_SIZE, slant=ITALIC
            )
        sequence.next_to(archi[0][0], DOWN, buff=0.25)
        self.play(Create(sequence))
        sequence2 = sequence.copy()
        self.add(sequence2)
        self.wait(1)

        tokens.next_to(archi[0][0], UP, buff=0.1)
        self.play(Transform(sequence, tokens, run_time=1, lag_ratio=.1))
        self.add(tokens)
        self.play(FadeOut(sequence))
        self.wait(1)

        self.play(tokens.animate.next_to(archi[0][-1], UP, buff=0.1).set_color(BLUE).set_fill(BLUE, opacity=0.5))
        self.wait(1)

        self.play(tokens.animate.next_to(archi[-1][0], DOWN, buff=0.1))
        self.wait(1)

        self.play(tokens.animate.next_to(archi[-1][0], UP, buff=0.1).set_color(RED).set_fill(RED, opacity=0.5))
        last_pos = tokens[-1].copy()
        self.add(last_pos)
        self.play(FadeOut(tokens, run_time=1))
        
        self.wait(.5)
        next_token = Text("injure", font_size=DEFAULT_FONT_SIZE, slant=ITALIC, color=PURPLE)
        next_token.next_to(archi[-1][-1], UP, buff=0.25)
        self.play(Transform(last_pos, next_token, run_time=1.1, lag_ratio=.1))
        self.wait(1)

        self.play(VGroup(archi, sequence2, last_pos, next_token).animate.shift(3*LEFT))

        

