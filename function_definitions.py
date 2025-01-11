from manim import *

BACKGROUND_COLOR = "#12121a"    # button-background-color
PURPLE_COLOR = "#292630"        # article-lighter-background-color
GREEN_COLOR = "#204e49"    # article-border-color
OTHER_BLUE_COLOR = "#375773"          # button-top-border-color
BLUE_COLOR = "#56DCC6"    # content-link-color
LIGHTER_BLUE_COLOR = "#ADEEE3"  # content-visited-link-color
BEIGE_COLOR = "#fff4d9"          # content-text-color
ORANGE_COLOR = "#ffc375"         # button-hover-bottom-border-color
YELLOW_COLOR = "#fdff91"     # button-hover-highlight-color


class video_intro(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        title = Text("Функции", color=BEIGE_COLOR, font_size=120)
        title_top_left = Text("Функции", color=BEIGE_COLOR, font_size=45).to_corner(UL)
        subtitle = Text("I - Дефиниция", color=BEIGE_COLOR, font_size=80)

        self.play(Write(title))

        self.wait(1)

        self.play(Transform(title, title_top_left), run_time=0.75)

        self.wait(0.25)

        self.play(Write(subtitle))

        self.wait(1.5)

        self.play(Unwrite(title), Unwrite(subtitle), run_time=0.5)

        self.wait(1)

class part_1(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        function_text_begin = MathTex("f(", color=BEIGE_COLOR).scale(2.5)
        function_text_end = MathTex(")", color=BEIGE_COLOR).scale(2.5).next_to(function_text_begin, RIGHT)

        function_text_1 = VGroup(function_text_begin, function_text_end).center()

        self.play(Write(function_text_1))
        self.wait(0.5)

        middle_object = MathTex("x", color=BEIGE_COLOR).scale(2.5)
        middle_text = MathTex("x", color=BEIGE_COLOR).scale(2.5)
        middle_square = Square(color=ORANGE_COLOR, stroke_width=10, side_length=1)
        middle_circle = Circle(color=YELLOW_COLOR, stroke_width=10, radius=0.5)
        middle_triangle = Triangle(color=BLUE_COLOR, stroke_width=10).center().scale(0.8)

        self.remove_object_and_add(None, middle_object, function_text_begin, function_text_end, 'write', 'write', 'blabla')
        self.wait(1)
        
        parameter_text = Text("Параметър", color=ORANGE_COLOR, font_size=30, slant=ITALIC).next_to(middle_text, DOWN, buff = 1.75)
        parameter_arrow = Arrow(start=parameter_text.get_top(), end=(middle_text.get_bottom() + DOWN * 0.25), color=BEIGE_COLOR)
        
        self.play(
            Write(parameter_text),
            Create(parameter_arrow)
        )
        self.wait(1)

        self.remove_object_and_add(middle_object, middle_square, function_text_begin, function_text_end, 'write', 'create', 'transform')
        self.wait(1)
        self.remove_object_and_add(middle_object, middle_circle, function_text_begin, function_text_end, 'create', 'create', 'transform')
        self.wait(1)
        self.remove_object_and_add(middle_object, middle_triangle, function_text_begin, function_text_end, 'create', 'create', 'transform')
        self.wait(1)
        self.remove_object_and_add(middle_object, middle_text, function_text_begin, function_text_end, 'create', 'write', 'transform')
        self.wait(1)

        self.play(
            Unwrite(parameter_text),
            Uncreate(parameter_arrow)
        )

        self.wait(1)

        self.play(
            Unwrite(function_text_begin),
            Unwrite(middle_object),
            Unwrite(function_text_end),
            duration=0.5
        )
        self.wait(1)
        

    def remove_object_and_add(self, object_to_remove, object_to_add, left_paranthesis, right_paranthesis, write_or_create_1, write_or_create_2, version):
        if version == 'transform':
            if object_to_remove is not None:
                self.play(
                    left_paranthesis.animate.next_to(object_to_add, LEFT),
                    right_paranthesis.animate.next_to(object_to_add, RIGHT),
                    Transform(object_to_remove, object_to_add)
                )
            else:
                if write_or_create_2 == 'write':
                    self.play(
                        left_paranthesis.animate.next_to(object_to_add, LEFT),
                        right_paranthesis.animate.next_to(object_to_add, RIGHT),
                        Write(object_to_add)
                    )
                elif write_or_create_2 == 'create':
                    self.play(
                        left_paranthesis.animate.next_to(object_to_add, LEFT),
                        right_paranthesis.animate.next_to(object_to_add, RIGHT),
                        Create(object_to_add)
                    )
        else:
            if object_to_remove is not None:
                if write_or_create_1 == 'write':
                    self.play(Unwrite(object_to_remove))
                elif write_or_create_1 == 'create':
                    self.play(Uncreate(object_to_remove))
            
            self.wait(1)

            self.play(
                left_paranthesis.animate.next_to(object_to_add, LEFT),
                right_paranthesis.animate.next_to(object_to_add, RIGHT)
            )

            self.wait(1)

            if write_or_create_2 == 'write':
                self.play(Write(object_to_add))
            elif write_or_create_2 == 'create':
                self.play(Create(object_to_add))

class part_2(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        function_text = MathTex("f(x)", " = ", "y", color=BEIGE_COLOR).scale(2.5)
        text_part_1_orig_pos = function_text[0].get_center()
        function_text[0].center()
        self.play(Write(function_text[0]))
        self.wait(1)

        self.play(
            function_text[0].animate.move_to(text_part_1_orig_pos),
        )
        self.play(
            Write(function_text[1]),
            Write(function_text[2])
        )
        self.wait(1)
        self.play(Circumscribe(function_text[2], color=BLUE_COLOR))
        self.wait(1)

        value_text = Text("Стойност", color=ORANGE_COLOR, font_size=30, slant=ITALIC).next_to(function_text[2], DOWN, buff = 1.5)
        value_arrow = Arrow(start=value_text.get_top(), end=(function_text[2].get_bottom()), color=BEIGE_COLOR)
        self.play(
            Create(value_arrow),
            Write(value_text)
        )
        self.wait(1)
        self.play(
            Uncreate(value_arrow),
            Unwrite(value_text)
        )
        self.wait(1)

class part_2_2(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        function_text = MathTex("f(", "x", ")", " = ", "y", color=BEIGE_COLOR).scale(2.5)
        self.add(function_text)
        self.wait(1)
        self.play(Indicate(function_text[1], color=BLUE_COLOR))
        self.wait(1)
        function_text_2 = MathTex("f(", "3", ")", " = ", "y", color=BEIGE_COLOR).scale(2.5)
        self.play(Transform(function_text, function_text_2))
        self.wait(1)
        self.play(Unwrite(function_text))
        self.wait(1)

class part_3(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        text_font_size = 50

        function_text = Text("f(име) = дата", color=BEIGE_COLOR, font_size=text_font_size)
        self.play(
            Write(function_text)
        )
        self.wait(1)
        self.play(
            function_text.animate.to_corner(UL)
        )
        self.wait(1)
        
        function_text_anton = Text("f(Антон) = 23.04", color=BEIGE_COLOR, font_size=text_font_size)
        function_text_borislav = Text("f(Борислав) = 20.08", color=BEIGE_COLOR, font_size=text_font_size)
        function_text_gergana = Text("f(Гергана) = 20.08", color=BEIGE_COLOR, font_size=text_font_size)

        function_text_group = VGroup(function_text_anton, function_text_borislav, function_text_gergana)
        function_text_group.arrange(DOWN, aligned_edge=LEFT)

        self.play(
            Write(function_text_anton)
        )
        self.wait(1)
        self.play(
            Write(function_text_borislav)
        )
        self.wait(1)
        self.play(
            Write(function_text_gergana)
        )
        self.wait(1)

        self.play(
            Indicate(function_text_borislav[12::], color=BLUE_COLOR),
            Indicate(function_text_gergana[11::], color=BLUE_COLOR)
        )
        self.wait(1)

        self.play(
            Unwrite(function_text),
            Unwrite(function_text_anton),
            Unwrite(function_text_borislav),
            Unwrite(function_text_gergana),
            run_time = 1
        )

        self.wait(1)