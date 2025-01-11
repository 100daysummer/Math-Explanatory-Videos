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

class part_4(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        f_text = MathTex("f:A\\rightarrowB", color=BEIGE_COLOR, tex_to_color_map={"A": GREEN_COLOR, "B": OTHER_BLUE_COLOR}).scale(1.25).to_corner(UL)

        self.play(
            Write(f_text[:1])
        )
        self.wait()

        set_A = Ellipse(
            width=2,
            height=4,
            color=GREEN_COLOR,
            fill_opacity=0.5,
            stroke_width=10
        )
        set_B = set_A.copy().set_color(OTHER_BLUE_COLOR).shift(4 * RIGHT)
 
        label_A = MathTex("A", color=BEIGE_COLOR)
        label_A.add_updater(
            lambda mobject: mobject.next_to(set_A, DOWN)
        )
        label_B = MathTex("B", color=BEIGE_COLOR)
        label_B.add_updater(
            lambda mobject: mobject.next_to(set_B, DOWN)
        )

        
        dots_A = VGroup(
            Dot(color=BEIGE_COLOR).shift(1.2 * UP),
            Dot(color=BEIGE_COLOR).shift(0 * UP),
            Dot(color=BEIGE_COLOR).shift(-1.2 * UP),
        )
        dot_labels_A = VGroup(
            Text("a1", color=BEIGE_COLOR, font_size=35).next_to(dots_A[0], UP),
            Text("a2", color=BEIGE_COLOR, font_size=35).next_to(dots_A[1], UP),
            Text("a3", color=BEIGE_COLOR, font_size=35).next_to(dots_A[2], UP)
        )
        dot_name_labels_A = VGroup(
            Text("Антон", color=BEIGE_COLOR, font_size=30).next_to(dots_A[0], UP),
            Text("Борислав", color=BEIGE_COLOR, font_size=30).next_to(dots_A[1], UP),
            Text("Гергана", color=BEIGE_COLOR, font_size=30).next_to(dots_A[2], UP)
        )
        dots_A.add_updater(
            lambda asdf: asdf.move_to(set_A.get_center() + DOWN*0.2)
        )
        dot_labels_A.add_updater(
            lambda asdfa: asdfa.move_to(set_A.get_center() + UP*0.2)
        )

        
        dots_B = VGroup(
            Dot(color=BEIGE_COLOR).shift(0.6 * UP),
            Dot(color=BEIGE_COLOR).shift(0.6 * DOWN)
        )
        dot_labels_B = VGroup(
            Text("b1", color=BEIGE_COLOR, font_size=35).next_to(dots_A[0], UP),
            Text("b2", color=BEIGE_COLOR, font_size=35).next_to(dots_A[1], UP)
        )
        dot_date_labels_B = VGroup(
            Text("23.04", color=BEIGE_COLOR, font_size=35).next_to(dots_A[0], UP),
            Text("20.08", color=BEIGE_COLOR, font_size=35).next_to(dots_A[1], UP)
        )
        dots_B.add_updater(
            lambda asdfaa: asdfaa.move_to(set_B.get_center() + DOWN*0.2)
        )
        dot_labels_B.add_updater(
            lambda asdfaaa: asdfaaa.move_to(set_B.get_center() + UP*0.2)
        )

        self.play(
            Create(set_A)
        )
        self.wait()
        self.play(
            Write(label_A),
            Write(f_text[1])
        )
        self.wait()

        set_a_description = Paragraph(
            "A съдържа всички",
            "възможни аргументи",
            line_spacing=0.5, 
            t2c={"A": GREEN_COLOR},
            t2s={"A": ITALIC},
            font_size=26,
            alignment="center",
            color=BEIGE_COLOR
        ).next_to(f_text, DOWN, buff=0.625).to_edge(LEFT)
        set_b_description = Paragraph(
            "B съдържа всички",
            "възможни стойности",
            line_spacing=0.5,
            t2c={"B": OTHER_BLUE_COLOR},
            t2s={"B": ITALIC},
            font_size=26,
            alignment="center",
            color=BEIGE_COLOR
        ).next_to(set_a_description, RIGHT, buff=0.5).align_to(set_a_description.get_top(), UP)
        self.play(
            Write(set_a_description),
            Write(dot_labels_A),
            Create(dots_A)
        )

        self.wait()
        self.play(set_A.animate.next_to(set_a_description, DOWN, buff=0.5))
        self.wait()

        self.play(
            Create(set_B)
        )
        self.play(
            Write(label_B),
            Write(f_text[2:])
        )

        self.play(
            Write(set_b_description),
            Write(dot_labels_B),
            Create(dots_B)
        )
        self.wait()

        self.play(
            set_B.animate.next_to(set_b_description, DOWN, buff=0.5)
        )
        self.wait()

        arrow_1 = Arrow(start=dots_A[0].get_center(), end=dots_B[0].get_center(), color=LIGHTER_BLUE_COLOR)
        arrow_2 = Arrow(start=dots_A[1].get_center(), end=dots_B[1].get_center(), color=LIGHTER_BLUE_COLOR)
        arrow_3 = Arrow(start=dots_A[2].get_center(), end=dots_B[1].get_center(), color=LIGHTER_BLUE_COLOR)
        arrows = VGroup(arrow_1, arrow_2, arrow_3)       
        self.play(
            AnimationGroup(
                Create(arrow_1),
                Create(arrow_2),
                Create(arrow_3),
                lag_ratio=1
            )
        )
        self.wait()

        
        other_description = Paragraph(
            "Еднозначността е, че",
            "елемент от A се съпоставя",
            "с точно един елемент от B",
            line_spacing=0.5,
            t2c={"Еднозначността": BLUE_COLOR, "A": GREEN_COLOR, "B": OTHER_BLUE_COLOR},
            t2s={"A": ITALIC, "B": ITALIC},
            font_size=30,
            alignment="right",
            color=BEIGE_COLOR
        ).to_edge(RIGHT)

        self.play(Write(other_description))
        self.wait()

        dot_name_labels_A.move_to(dot_labels_A.get_center())
        dot_labels_A.clear_updaters()
        self.play(
            *[Transform(dot_labels_A[i], dot_name_labels_A[i]) for i in range(3)]
        )

        self.wait()

        dot_date_labels_B.move_to(dot_labels_B.get_center())
        dot_labels_B.clear_updaters()
        self.play(
            *[Transform(dot_labels_B[i], dot_date_labels_B[i]) for i in range(2)]
        )

        self.wait()

        label_A.clear_updaters()
        label_B.clear_updaters()
        dots_A.clear_updaters()
        dots_B.clear_updaters()
        self.play(
            Uncreate(set_A),
            Uncreate(set_B),
            Unwrite(set_a_description),
            Unwrite(set_b_description),
            Unwrite(other_description),
            Uncreate(dots_A),
            Uncreate(dots_B),
            Uncreate(arrows),
            Unwrite(f_text),
            Unwrite(dot_labels_A),
            Unwrite(dot_labels_B),
            Unwrite(label_A),
            Unwrite(label_B)
        )

        self.wait()