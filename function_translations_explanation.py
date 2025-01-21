from manim import *
from functools import partial

BACKGROUND_COLOR = "#12121a"    # button-background-color
PURPLE_COLOR = "#292630"        # article-lighter-background-color
GREEN_COLOR = "#204e49"    # article-border-color
OTHER_BLUE_COLOR = "#375773"          # button-top-border-color
BLUE_COLOR = "#56DCC6"    # content-link-color
LIGHTER_BLUE_COLOR = "#ADEEE3"  # content-visited-link-color
BEIGE_COLOR = "#fff4d9"          # content-text-color
ORANGE_COLOR = "#ffc375"         # button-hover-bottom-border-color
YELLOW_COLOR = "#fdff91"     # button-hover-highlight-color
MORE_BLUE_COLOR = "#4877a0"

ORIG_FUNC_COLOR = MORE_BLUE_COLOR
OTHER_FUNC_COLOR = BLUE_COLOR

def save_frame(self):
    image = self.camera.get_image()
    image.save("C:\\Users\\Bobi\\Documents\\last_frame.png")

# Graphs f(x) = g(x) + a
class vertical_translation(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        left_end = ValueTracker(-5)
        right_end = ValueTracker(5)
        mending_point = ValueTracker(-1)
        def linear_plot_updater(mobj, plane, x_range, y_range, a, b, color_to_set_to):
            if mending_point is not None:
                x_range = [
                    x_range[0].get_value(),  # Left limit
                    x_range[1].get_value()  # Update dynamically
                ]
            #print(x_range[1], mending_point.get_value())
            xr = [
                (y_range[0]-b.get_value())/a.get_value(),
                (y_range[1]-b.get_value())/a.get_value()
            ]
            xr.sort()
            xr = [
                max(xr[0],x_range[0]),
                min(xr[1],x_range[1])
            ]
            mobj.become(
                plane.plot(
                    lambda x: a.get_value()*x+b.get_value(),
                    x_range=xr,
                    use_smoothing=False,
                ).set_color(color_to_set_to)
            )
        ## CACHING MESSES THIS UP, BE CAREFUL

        num_plane = always_redraw(
            lambda:
            NumberPlane(
                axis_config={
                    "include_numbers": True,
                    "font_size": 15,
                    "line_to_number_buff": 0.05,
                    "label_direction": DOWN
                },
                x_range=[-5, 5, 1],
                y_range=[-5, 5, 1],
                x_length=5,
                y_length=5,
                background_line_style={
                    "stroke_width": 1,
                    "stroke_opacity": 0.5
                }
            )
        )

        orig_func_left_a = ValueTracker(-4)
        orig_func_left_b = ValueTracker(-8)
        orig_func_right_a = ValueTracker(1)
        orig_func_right_b = ValueTracker(-3)
        other_func_left_a = ValueTracker(-4)
        other_func_left_b = ValueTracker(-8)
        other_func_right_a = ValueTracker(1)
        other_func_right_b = ValueTracker(-3)

        orig_func_left = VMobject()
        orig_func_right = VMobject()
        other_func_left = VMobject()
        other_func_right = VMobject()

        orig_func_left_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[left_end, mending_point],
            y_range=[-5, 5],
            a=orig_func_left_a,
            b=orig_func_left_b,
            color_to_set_to=ORIG_FUNC_COLOR
        )
        orig_func_left.add_updater(orig_func_left_updater)
        
        orig_func_right_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[mending_point, right_end],
            y_range=[-5, 5],
            a=orig_func_right_a,
            b=orig_func_right_b,
            color_to_set_to=ORIG_FUNC_COLOR
        )
        orig_func_right.add_updater(orig_func_right_updater)
        
        other_func_left_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[left_end, mending_point],
            y_range=[-5, 5],
            a=other_func_left_a,
            b=other_func_left_b,
            color_to_set_to=OTHER_FUNC_COLOR
        )
        other_func_left.add_updater(other_func_left_updater)
        
        other_func_right_updater = partial(
            linear_plot_updater,
            plane=num_plane,
            x_range=[mending_point, right_end],
            y_range=[-5, 5],
            a=other_func_right_a,
            b=other_func_right_b,
            color_to_set_to=OTHER_FUNC_COLOR
        )
        other_func_right.add_updater(other_func_right_updater)

        some_stupid_label = MathTex(
                    "f(x)",
                    "=",
                    "g(",
                    "x",
                    ")",
                    ("+" if other_func_left_b.get_value() - orig_func_left_b.get_value() >= 0 else "-"),
                    "{:.2f}".format(abs(3)),
                    font_size=40
                ).set_color(BEIGE_COLOR)\
                .set_color_by_tex("g(", color=ORIG_FUNC_COLOR)\
                .set_color_by_tex(")", color=ORIG_FUNC_COLOR)\
                .set_color_by_tex("x", color=OTHER_FUNC_COLOR)\
            .next_to(num_plane.get_bottom(), DOWN)\
            .align_to(num_plane.get_left(), LEFT)\

        self.add(num_plane, some_stupid_label)
        self.add(orig_func_left, orig_func_right)
        #self.add(other_func_left, other_func_right)
        self.play(orig_func_left_a.animate.set_value(orig_func_left_a.get_value()),
                  orig_func_right_a.animate.set_value(orig_func_right_a.get_value()),
                  run_time=0.001)
        self.remove(orig_func_left, orig_func_right)
        self.play(Create(orig_func_left))
        self.play(Create(orig_func_right))

        silly_dot_x_coord = ValueTracker(-3.25)

        silly_dot = always_redraw(
            lambda:
            Dot(
                num_plane.c2p(
                    silly_dot_x_coord.get_value(),
                    (silly_dot_x_coord.get_value() * orig_func_left_a.get_value() + orig_func_left_b.get_value()) if silly_dot_x_coord.get_value() < mending_point.get_value() else (silly_dot_x_coord.get_value() * orig_func_right_a.get_value() + orig_func_right_b.get_value()) 
                )
            ).set_color(ORIG_FUNC_COLOR)
        )
        self.wait()
        self.play(Create(silly_dot))
        self.wait()
        self.play(silly_dot_x_coord.animate.set_value(-2))
        self.wait()
        
        new_dot_offset = ValueTracker(0)
        new_dot = always_redraw(
            lambda:
                Dot(
                    num_plane.c2p(
                        silly_dot_x_coord.get_value(),
                        ((silly_dot_x_coord.get_value() * orig_func_left_a.get_value() + orig_func_left_b.get_value() + new_dot_offset.get_value()) if silly_dot_x_coord.get_value() < mending_point.get_value() else (silly_dot_x_coord.get_value() * orig_func_right_a.get_value() + orig_func_right_b.get_value()))
                    )
                ).set_color(OTHER_FUNC_COLOR)
        )
        self.play(Write(new_dot)) 
        self.wait()
        self.play(new_dot_offset.animate.set_value(3))
        self.wait()


class TESTING(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        np = NumberPlane(
            axis_config={
                "include_numbers": True,
                "font_size": 15,
                "line_to_number_buff": 0.05,
                "label_direction": DOWN
            },
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=5,
            y_length=5,
            background_line_style={
                "stroke_color": BLUE_COLOR,
                "stroke_opacity": 0.2
            }
        )

        p1 = np.plot(
            lambda x: -4*x - 8 if x < -1 else x - 3
        )
        
        self.play(Create(np))
        self.wait()

class we_love_text(Scene):
    def construct(self):
        self.camera.background_color = BACKGROUND_COLOR

        PRIMARY_COLOR = OTHER_FUNC_COLOR
        OTHER_COLOR = ORIG_FUNC_COLOR

        dot = Dot(color = PRIMARY_COLOR, radius=0.15)
        text_1 = MathTex(
            "(",
            "-2",
            ",",
            "3",
            ")"
        ).set_color(BEIGE_COLOR)\
            .set_color_by_tex("f(", PRIMARY_COLOR)\
            .set_color_by_tex(" ", PRIMARY_COLOR)
        dot.next_to(text_1, LEFT)
        # self.add(dot, text_1)
        self.play(Create(dot), Write(text_1))
        self.wait()

        text_2 = MathTex(
            "(",
            "x",
            ",",
            "f(",
            "x",
            ") ",
            ")"
        ).set_color(BEIGE_COLOR)\
            .set_color_by_tex("f(", PRIMARY_COLOR)\
            .set_color_by_tex(" ", PRIMARY_COLOR)\
            .align_to(text_1, LEFT)
            #.next_to(text_1, DOWN)\
        #self.play(FadeIn(text_2, shift=DOWN))
        self.play(TransformMatchingTex(text_1, text_2))
        self.wait()


        text_3 = MathTex(
            "(",
            "x",
            ",",
            "g(",
            "x",
            ") ",
            "+3",
            ")"
        ).set_color(BEIGE_COLOR)\
            .set_color_by_tex("g(", OTHER_COLOR)\
            .set_color_by_tex(" ", OTHER_COLOR)\
            .align_to(text_1, LEFT)
            #.next_to(text_2, DOWN)\
        #self.play(FadeIn(text_3, shift=DOWN))
        self.play(TransformMatchingTex(text_2, text_3))
        self.wait()
        
        # text_4 = MathTex(
        #     "(",
        #     "-2",
        #     ",",
        #     "g(",
        #     "-2",
        #     ") ",
        #     "+3",
        #     ")"
        # ).set_color(BEIGE_COLOR)\
        #     .set_color_by_tex("g(", OTHER_COLOR).next_to(text_3, DOWN)\
        #     .set_color_by_tex(" ", OTHER_COLOR)\
        #     .align_to(text_1, LEFT)
        # self.play(FadeIn(text_4, shift=DOWN))
        # self.wait()

        # text_5 = MathTex(
        #     "(",
        #     "-2",
        #     ",",
        #     "0",
        #     "+3",
        #     ")"
        # ).set_color(BEIGE_COLOR)\
        #     .set_color_by_tex("g(", OTHER_COLOR)\
        #     .next_to(text_4, DOWN)\
        #     .align_to(text_1, LEFT)
        # self.play(FadeIn(text_5, shift=DOWN))
        # self.wait()
        
        # text_6 = MathTex(
        #     "(",
        #     "-2",
        #     ",",
        #     "3"
        #     ")"
        # ).set_color(BEIGE_COLOR)\
        #     .next_to(text_5, DOWN)\
        #     .align_to(text_1, LEFT)
        # self.play(FadeIn(text_6, shift=DOWN))
        # self.wait()

        text_objects = [text_1, text_2]#, text_3, text_4, text_5, text_6]
        # for i in range(len(text_objects) - 1, 0, -1):
        #     self.play(
        #         FadeOut(text_objects[i - 1]),
        #         text_objects[i].animate.shift(UP * (text_objects[i - 1].get_center()[1] - text_objects[i].get_center()[1])),
        #         run_time=0.5
        #     )
        #     text_objects.remove(text_objects[i - 1])
        
        self.wait()