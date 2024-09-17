from manim import *


class test(Scene):
    def construct(self):
        def advanced_show(mobject):
            num = Text("0").to_edge(DOWN)
            self.add(num)
            for i in range(len(mobject)):
                num.become(Text(str(i)).to_edge(DOWN))
                self.play(Indicate(mobject[i]))
            self.remove(num)

        # Base
        text = MathTex(
            *r"{\left(x-h\right)^{2} \over a^{2}}   -   {\left(y-k\right)^{2}\over b^{2}}=1".split(
                "   "
            )
        )
        self.play(Write(text), run_time=(2 / 3))

        # BEGIN Id: 1
        # Animation set target.
        text_target = MathTex(
            *r"-   {\left(y-k\right)^{2}\over b^{2}}=1   -   {\left(x-h\right)^{2} \over a^{2}}".split(
                "   "
            )
        )

        self.play(
            FadeIn(text_target[2]),
            TransformMatchingTex(text, text_target, path_arc=-np.pi),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            *r"-   {\left(y-k\right)^{2}\over b^{2}}=   1   -   {\left(x-h\right)^{2} \over a^{2}}".split(
                "   "
            )
        )

        self.add(text)
        # END

        # BEGIN Id: 2
        # Animation set target.
        text_target = MathTex(
            *r"{\left(y-k\right)^{2}\over b^{2}}=   {\left(x-h\right)^{2} \over a^{2}}   -   1".split(
                "   "
            )
        )

        self.play(
            FadeOut(text[0]),
            TransformMatchingTex(text, text_target, path_arc=np.pi),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            *r"{   \left(y-k\right)^{2}   \over b^{2}   }   =   {\left(x-h\right)^{2} \over a^{2}}   -   1".split(
                "   "
            )
        )

        self.add(text)
        # END

        # BEGIN Id: 3
        # Animation set target.
        text_target = MathTex(
            *r"{   \left(y-k\right)^{2}   }   =   b^{2}   {\left(x-h\right)^{2} \over a^{2}}   -   b^{2}".split(
                "   "
            )
        )

        self.play(
            TransformMatchingTex(text, text_target),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            *r"\left(y-k\right)   ^{2}   =   b^{2} {\left(x-h\right)^{2} \over a^{2}} - b^{2}".split(
                "   "
            )
        )

        self.add(text)
        # END

        # BEGIN Id: 4
        # Animation set target.
        text_target = MathTex(
            *r"\sqrt{   \left(y-k\right)   ^{2}   }   =   \sqrt{   b^{2} {\left(x-h\right)^{2} \over a^{2}} - b^{2}   }".split(
                "   "
            )
        )

        self.play(
            TransformMatchingTex(text, text_target),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            *r"\sqrt{   \left(   y-k   \right)   ^{2}   }   =   \sqrt{b^{2} {\left(x-h\right)^{2} \over a^{2}} - b^{2}}".split(
                "   "
            )
        )

        self.add(text)
        # END

        # BEGIN Id: 5
        # Animation set target.
        text_target = MathTex(
            *r"y-k   =   \sqrt{b^{2} {\left(x-h\right)^{2} \over a^{2}} - b^{2}}".split(
                "   "
            )
        )

        self.play(
            TransformMatchingTex(text, text_target),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            *r"y   -   k   =\sqrt{b^{2} {\left(x-h\right)^{2} \over a^{2}} - b^{2}}".split(
                "   "
            )
        )

        self.add(text)
        # END

        # BEGIN Id: 6
        # Animation set target.
        text_target = MathTex(
            *r"y   =\sqrt{b^{2} {\left(x-h\right)^{2} \over a^{2}} - b^{2}}   +   k".split(
                "   "
            )
        )

        self.play(
            TransformMatchingTex(text, text_target, path_arc=np.pi),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            *r"y=\sqrt{b^{2}{\left(x-h\right)^{2}\over a^{2}} -   b^{2}   }+k".split(
                "   "
            )
        )

        self.add(text)
        # END

        # BEGIN Id: 7
        # Animation set target.
        text_target = MathTex(
            *r"y=\sqrt{b^{2}{\left(x-h\right)^{2}\over a^{2}} -   {   a^{2}   b^{2}   \over   a^{2}   }   }   +k".split(
                "   "
            )
        )

        self.play(
            TransformMatchingTex(text, text_target),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            r"y=\sqrt{b^2{\left(x-h\right)^2\over a^2} - { a^2 b^2 \over a^2 } }+k"
        )

        self.add(text)
        # END

        # BEGIN Id: 8
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"y=\sqrt{ { b^2 \left(x-h\right)^2\over a^2} - { a^2 b^2 \over a^2 } }+k"
        )

        self.play(
            text[0][0:3].animate.move_to(text_target[0][0:3]),
            Transform(text[0][3], text_target[0][3]),
            text[0][4:6].animate.move_to(text_target[0][4:6]),
            text[0][6:12].animate.move_to(text_target[0][6:12]),
            Transform(text[0][12], text_target[0][12]),
            text[0][13:15].animate.move_to(text_target[0][13:15]),
            text[0][15].animate.move_to(text_target[0][15]),
            text[0][16:20].animate.move_to(text_target[0][16:20]),
            text[0][20].animate.move_to(text_target[0][20]),
            text[0][21:23].animate.move_to(text_target[0][21:23]),
            text[0][23].animate.move_to(text_target[0][23]),
            text[0][24].animate.move_to(text_target[0][24]),
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = MathTex(
            r"y=\sqrt{ { b^2 \left(x-h\right)^2   \over a^2 }   -   {   a^2 b^2   \over a^2 }   }+k"
        )
        self.add(text)
        # END

        # BEGIN Id: 9
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"y=\sqrt{ { b^2 \left(x-h\right)^2   -   a^2 b^2\over a^2 }   }+k"
        )

        self.play(
            *[text[0][i].animate.move_to(text_target[0][i]) for i in range(3)],
            Transform(text[0][3], text_target[0][3]),
            *[text[0][i].animate.move_to(text_target[0][i]) for i in range(4, 12)],
            Transform(text[0][12], text_target[0][17]),
            text[0][13:15].animate.move_to(text_target[0][18:20]),
            text[0][15].animate.move_to(text_target[0][12]),
            text[0][16:20].animate.move_to(text_target[0][13:17]),
            Transform(text[0][20], text_target[0][17]),
            text[0][21:23].animate.move_to(text_target[0][18:20]),
            text[0][-2:].animate.move_to(text_target[0][-2:]),
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = text_target
        self.add(text)
        # END

        # BEGIN Id: 10
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"y=\sqrt{ {b^2 \over a^2} \left( \left(x-h\right)^2 - a^2 \right) } +k",
        )

        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            *[text[0][i].animate.move_to(text_target[0][i]) for i in range(2)],
            FadeTransform(text[0][2], text_target[0][2]),
            Transform(text[0][3], text_target[0][3]),
            *[text[0][i].animate.move_to(text_target[0][i]) for i in range(4, 6)],
            *[text[0][i].animate.move_to(text_target[0][i + 4]) for i in range(6, 15)],
            text[0][15:17].animate.move_to(text_target[0][4:6]),
            Transform(text[0][17], text_target[0][6]),
            text[0][18:20].animate.move_to(text_target[0][7:9]),
            text[0][-2:].animate.move_to(text_target[0][-2:]),
            FadeIn(text_target[0][9]),
            FadeIn(text_target[0][19]),
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = text_target
        self.add(text)
        # END

        # BEGIN Id: 11
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"y={b \over a} \sqrt{ \left(x-h\right)^2 - a^2  } +k",
        )

        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            *[text[0][i].animate.move_to(text_target[0][i]) for i in range(2)],
            FadeTransform(text[0][2], text_target[0][5]),
            Transform(text[0][3], text_target[0][6]),
            text[0][4].animate.move_to(text_target[0][2]),
            FadeOut(text[0][5]),
            Transform(text[0][6], text_target[0][3]),
            text[0][7].animate.move_to(text_target[0][4]),
            FadeOut(text[0][8]),
            FadeOut(text[0][9]),
            text[0][10:19].animate.move_to(text_target[0][7:16]),
            FadeOut(text[0][19]),
            text[0][-2:].animate.move_to(text_target[0][-2:]),
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = MathTex(
            r"y=",
            r"{b \over a} \sqrt{ \left(x-h\right)^2 - a^2  } +k",
        )
        self.add(text)
        # END

        # BEGIN Id: 12
        # Animation set target.
        text_target = MathTex(
            r"\frac{d}{dx} \left(",
            r"{b \over a} \sqrt{ \left(x-h\right)^2 - a^2  } +k",
            r"\right)",
        )

        self.play(
            TransformMatchingTex(text, text_target),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            r"{d \over dx} \left( {b \over a} \sqrt{ \left(x-h\right)^2 - a^2  } +k \right)",
        )

        self.add(text)
        # END

        # BEGIN Id: 13
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"{b \over a} {1 \over 2\sqrt{ \left(x-h\right)^2-a^2 } } 2\left(x-h\right)",
        )

        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            *[Transform(text[0][i], text_target[0][i - 5]) for i in range(5, 8)],
            *[text[0][i].animate.move_to(text_target[0][i - 2]) for i in range(8, 19)],
            FadeOut(text[0][0:5]),
            FadeOut(text[0][19:]),
            FadeIn(text_target[0][3:5]),
            FadeIn(text_target[0][5]),
            *[
                Transform(text[0][i].copy(), text_target[0][i + 8], path_arc=np.pi)
                for i in range(10, 15)
            ],
            FadeTransform(text[0][15].copy(), text_target[0][17], path_arc=np.pi),
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = MathTex(
            *r"{b \over a} {   1   \over   2 \sqrt{ \left(x-h\right)^2-a^2 } }   2   \left(x-h\right)   ".split(
                "   "
            ),
        )
        self.add(text)
        # END

        # BEGIN Id: 14
        # Animation set target.
        text_target = MathTex(
            *r"{b \over a} {   2   \left(x-h\right)   \over   2 \sqrt{ \left(x-h\right)^2-a^2 } }   ".split(
                "   "
            ),
        )

        self.play(
            TransformMatchingTex(text, text_target, path_arc=np.pi),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            *r"{b \over a} {   2   \left(x-h\right) \over   2   \sqrt{ \left(x-h\right)^2-a^2 } }   ".split(
                "   "
            ),
        )

        self.add(text)
        # END

        # BEGIN Id: 15
        # Animation set target.
        text_target = MathTex(
            *r"{b \over a} {   \left(x-h\right) \over   \sqrt{ \left(x-h\right)^2-a^2 } }   ".split(
                "   "
            ),
        )

        self.play(
            TransformMatchingTex(text, text_target),
            FadeOut(text[1]),
            FadeOut(text[3]),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            *r"{   b   \over   a   }   {   \left(x-h\right) \over   \sqrt{ \left(x-h\right)^2-a^2 } }".split(
                "   "
            ),
        )

        self.add(text)
        # END

        # BEGIN Id: 16
        # Animation set target.
        text_target = MathTex(
            *r"{   b   \left(x-h\right) \over   a   \sqrt{ \left(x-h\right)^2-a^2 } }".split(
                "   "
            ),
        )

        self.play(
            TransformMatchingTex(text, text_target),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            r"{ b \left(x-h\right) \over a \sqrt{ \left(x-h\right)^2-a^2 } }"
        )

        self.add(text)
        # END

        # BEGIN Id: 17
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"{d \over dx}\left({ b \left(x-h\right) \over a \sqrt{ \left(x-h\right)^2-a^2 } }\right)"
        )
        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            text[0][0:19].animate.move_to(text_target[0][6:25]),
            FadeIn(text_target[0][0:6], text_target[0][25:]),
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = text_target
        self.add(text)
        # END

        # BEGIN Id: 18
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"\left(\left(b\cdot a\sqrt{\left(x-h\right)^{2}-a^{2}}\right)-b\left(x-h\right)\cdot a\cdot{1\over 2\sqrt{\left(x-h\right)^{2}-a^{2}}}\cdot2\left(x-h\right)\right) \over \left(a\sqrt{\left(x-h\right)^{2}-a^{2}}\right)^{2}"
        )

        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            *[text[0][i].animate.move_to(text_target[0][i + 12]) for i in range(6, 12)],
            *[text[0][i].animate.move_to(text_target[0][i - 9]) for i in range(13, 25)],
            *[
                text[0][i].copy().animate.move_to(text_target[0][i + 27])
                for i in range(16, 21)
            ],
            *[
                FadeTransform(text[0][i].copy(), text_target[0][i + 16])
                for i in range(14, 25)
            ],
            *[
                text[0][i].copy().animate.move_to(text_target[0][i + 38])
                for i in range(13, 25)
            ],
            FadeTransform(text[0][21].copy(), text_target[0][42]),
            text[0][13].copy().animate.move_to(text_target[0][25]),
            text[0][6].copy().animate.move_to(text_target[0][2]),
            Transform(text[0][12], text_target[0][49]),
            FadeOut(text[0][0:6]),
            FadeOut(text[0][25:27]),
            FadeIn(
                text_target[0][50],
                text_target[0][63],
                text_target[0][64],
                text_target[0][0],
                text_target[0][1],
                text_target[0][3],
                text_target[0][16],
                text_target[0][24],
                text_target[0][26],
                text_target[0][17],
                text_target[0][48],
                text_target[0][41],
                text_target[0][27:30],
            ),
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = text_target
        self.add(text)
        # END

        # BEGIN Id: 19
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"{\left(\left(b\cdot a\sqrt{\left(x-h\right)^{2}-a^{2}}\right)-\frac{2ab\left(x-h\right)^{2}}{2\sqrt{\left(x-h\right)^{2}-a^{2}}}\right) \over \left(a\sqrt{\left(x-h\right)^{2}-a^{2}}\right)^{2}}"
        )

        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            FadeTransform(text[0][18], text_target[0][20], path_arc=-np.pi),
            FadeTransform(text[0][42], text_target[0][18], path_arc=np.pi),
            FadeTransform(text[0][25], text_target[0][19], path_arc=-np.pi),
            Transform(text[0][49], text_target[0][41]),
            *[
                FadeTransform(text[0][i], text_target[0][i + 2], path_arc=-np.pi)
                for i in range(19, 24)
            ],
            *[
                FadeTransform(text[0][i], text_target[0][i - 22], path_arc=np.pi)
                for i in range(43, 48)
            ],
            *[
                FadeTransform(text[0][i], text_target[0][i - 8], path_arc=-np.pi)
                for i in range(50, 64)
            ],
            *[text[0][i].animate.move_to(text_target[0][i]) for i in range(18)],
            *[text[0][i].animate.move_to(text_target[0][i - 1]) for i in range(28, 41)],
            text[0][48].animate.move_to(text_target[0][40]),
            FadeIn(text_target[0][26]),
            FadeOut(text[0][24], text[0][26], text[0][41]),
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = text_target
        self.add(text)
        # END

        # BEGIN Id: 20
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"{\left(ab\sqrt{\left(x-h\right)^{2}-a^{2}}-\frac{ab\left(x-h\right)^{2}}{\sqrt{\left(x-h\right)^{2}-a^{2}}}\right) \over \left(a\sqrt{\left(x-h\right)^{2}-a^{2}}\right)^{2}}"
        )

        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            FadeOut(text[0][1], text[0][16], text[0][18], text[0][28], text[0][3]),
            text[0][2].animate.move_to(text_target[0][2]),
            text[0][0].animate.move_to(text_target[0][0]),
            text[0][40].animate.move_to(text_target[0][35]),
            text[0][4].animate.move_to(text_target[0][1]),
            text[0][17].animate.move_to(text_target[0][14]),
            *[text[0][i].animate.move_to(text_target[0][i - 2]) for i in range(5, 16)],
            *[text[0][i].animate.move_to(text_target[0][i - 4]) for i in range(19, 27)],
            *[text[0][i].animate.move_to(text_target[0][i - 5]) for i in range(29, 40)],
            *[text[0][i].animate.move_to(text_target[0][i - 5]) for i in range(42, 57)],
            Transform(text[0][27], text_target[0][23]),
            Transform(text[0][41], text_target[0][36]),
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = text_target
        self.add(text)
        # END

        # BEGIN Id: 21
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"\frac{ab\sqrt{\left(x-h\right)^{2}-a^{2}}-\frac{ab\left(x-h\right)^{2}}{\sqrt{\left(x-h\right)^{2}-a^{2}}}}{a^{2}\left(\left(x-h\right)^{2}-a^{2}\right)}"
        )

        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            FadeOut(text[0][0], text[0][35], text[0][39:41]),
            *[text[0][i].animate.move_to(text_target[0][i - 1]) for i in range(1, 35)],
            *[text[0][i].animate.move_to(text_target[0][i - 3]) for i in range(41, 50)],
            Transform(text[0][36], text_target[0][34]),
            text[0][38].animate.move_to(text_target[0][35]),
            text[0][51].animate.move_to(text_target[0][36]),
            FadeTransform(text[0][37], text_target[0][37]),
            FadeTransform(text[0][50], text_target[0][47]),
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = text_target
        self.add(text)
        # END

        # BEGIN Id: 22
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"\frac{a\left(b\sqrt{\left(x-h\right)^{2}-a^{2}}-\frac{b\left(x-h\right)^{2}}{\sqrt{\left(x-h\right)^{2}-a^{2}}}\right)}{a^{2}\left(\left(x-h\right)^{2}-a^{2}\right)}"
        )

        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            FadeIn(text_target[0][1], text_target[0][34]),
            text[0][0].animate.move_to(text_target[0][0]),
            FadeTransform(text[0][14], text_target[0][0], path_arc=np.pi),
            Transform(text[0][34], text_target[0][35]),
            *[text[0][i].animate.move_to(text_target[0][i + 1]) for i in range(35, 48)],
            *[text[0][i].animate.move_to(text_target[0][i + 1]) for i in range(1, 14)],
            *[text[0][i].animate.move_to(text_target[0][i]) for i in range(15, 34)],
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = text_target
        self.add(text)
        # END

        # BEGIN Id: 23
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"\frac{b\sqrt{\left(x-h\right)^{2}-a^{2}}-\frac{b\left(x-h\right)^{2}}{\sqrt{\left(x-h\right)^{2}-a^{2}}}}{a\left(\left(x-h\right)^{2}-a^{2}\right)}"
        )

        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            FadeOut(text[0][0], text[0][1], text[0][34], text[0][37]),
            *[text[0][i].animate.move_to(text_target[0][i - 2]) for i in range(2, 34)],
            Transform(text[0][35], text_target[0][32]),
            text[0][36].animate.move_to(text_target[0][33]),
            *[text[0][i].animate.move_to(text_target[0][i - 4]) for i in range(38, 49)],
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = text_target
        self.add(text)
        # END

        # BEGIN Id: 24
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"\frac{\frac{b\sqrt{\left(x-h\right)^{2}-a^{2}}\cdot\sqrt{\left(x-h\right)^{2}-a^{2}}}{\sqrt{\left(x-h\right)^{2}-a^{2}}}-\frac{b\left(x-h\right)^{2}}{\sqrt{\left(x-h\right)^{2}-a^{2}}}}{a\left(\left(x-h\right)^{2}-a^{2}\right)}"
        )

        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            *[
                text[0][i].animate.move_to(text_target[0][i + 24])
                for i in range(12, 32)
            ],
            Transform(text[0][32], text_target[0][56]),
            *[
                text[0][i].animate.move_to(text_target[0][i + 24])
                for i in range(33, 45)
            ],
            *[
                text[0][i].copy().animate.move_to(text_target[0][i - 8])
                for i in range(21, 32)
            ],
            *[
                text[0][i].copy().animate.move_to(text_target[0][i + 4])
                for i in range(21, 32)
            ],
            *[FadeTransform(text[0][i], text_target[0][i]) for i in range(0, 12)],
            FadeIn(text_target[0][12]),
            FadeIn(text_target[0][24]),
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = text_target
        self.add(text)
        # END

        # BEGIN Id: 25
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"\frac{\frac{b\left(\left(x-h\right)^{2}-a^{2}\right)-b\left(x-h\right)^{2}}{\sqrt{\left(x-h\right)^{2}-a^{2}}}}{a\left(\left(x-h\right)^{2}-a^{2}\right)}"
        )

        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            Transform(text[0][0], text_target[0][0], path_arc=-np.pi),
            Transform(text[0][24], text_target[0][20]),
            Transform(text[0][44], text_target[0][20]),
            Transform(text[0][36], text_target[0][12]),
            Transform(text[0][56], text_target[0][32]),
            FadeOut(text[0][1:3], text[0][12:15]),
            *[text[0][i].animate.move_to(text_target[0][i - 1]) for i in range(3, 12)],
            *[
                text[0][i].animate.move_to(text_target[0][i - 24])
                for i in range(37, 44)
            ],
            *[
                text[0][i].animate.move_to(text_target[0][i - 24])
                for i in range(57, 69)
            ],
            *[
                text[0][i].animate.move_to(text_target[0][i - 13])
                for i in range(15, 24)
            ],
            *[text[0][i].animate.move_to(text_target[0][i - 4]) for i in range(25, 36)],
            *[
                text[0][i].animate.move_to(text_target[0][i - 24])
                for i in range(45, 56)
            ],
            FadeIn(text_target[0][11], text_target[0][1]),
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = text_target
        self.add(text)
        # END

        # BEGIN Id: 26
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"{b{\left(x-h\right)^{2}-a^{2}-\left(x-h\right)^{2} \over \sqrt{\left(x-h\right)^{2}-a^{2}}} \over a\left(\left(x-h\right)^{2}-a^{2}\right)}"
        )

        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            FadeOut(text[0][1], text[0][11]),
            FadeTransform(text[0][0], text_target[0][0], path_arc=np.pi),
            FadeTransform(text[0][13], text_target[0][0], path_arc=np.pi),
            Transform(text[0][20], text_target[0][17]),
            Transform(text[0][12], text_target[0][10]),
            *[text[0][i].animate.move_to(text_target[0][i - 1]) for i in range(2, 11)],
            *[text[0][i].animate.move_to(text_target[0][i - 3]) for i in range(14, 20)],
            *[Transform(text[0][i], text_target[0][i - 3]) for i in range(21, 45)],
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = MathTex(
            *r"{b{\left(x-h\right)^{2}   -a^{2}   -\left(x-h\right)^{2}   \over \sqrt{\left(x-h\right)^{2}-a^{2}}} \over a\left(\left(x-h\right)^{2}-a^{2}\right)}".split(
                "   "
            )
        )
        self.add(text)
        # END

        # BEGIN Id: 27
        # Animation set target.
        text_target = MathTex(
            *r"{b{\left(x-h\right)^{2}   -\left(x-h\right)^{2}   -a^{2}   \over \sqrt{\left(x-h\right)^{2}-a^{2}}} \over a\left(\left(x-h\right)^{2}-a^{2}\right)}".split(
                "   "
            )
        )

        self.play(
            TransformMatchingTex(text, text_target),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            *r"{   b{   \left(x-h\right)^{2}-\left(x-h\right)^{2}   -a^{2} \over \sqrt{\left(x-h\right)^{2}-a^{2}}} \over a\left(\left(x-h\right)^{2}-a^{2}\right)}".split(
                "   "
            )
        )

        self.add(text)
        # END

        # BEGIN Id: 28
        # Animation set target.
        text_target = MathTex(
            *r"{   b{   0   -a^{2} \over \sqrt{\left(x-h\right)^{2}-a^{2}}} \over a\left(\left(x-h\right)^{2}-a^{2}\right)}".split(
                "   "
            )
        )

        self.play(
            TransformMatchingTex(text, text_target),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = text_target

        self.add(text)
        # END

        # BEGIN Id: 29
        # Animation set target.
        text_target = MathTex(
            *r"{   b{   -a^{2} \over \sqrt{\left(x-h\right)^{2}-a^{2}}} \over a\left(\left(x-h\right)^{2}-a^{2}\right)}".split(
                "   "
            )
        )

        self.play(
            TransformMatchingTex(text, text_target),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            *r"{   b   {   -   a   ^{2}   \over \sqrt{\left(x-h\right)^{2}-a^{2}}} \over a \left(\left(x-h\right)^{2}-a^{2}\right)}".split(
                "   "
            )
        )

        self.add(text)
        # END

        # BEGIN Id: 30
        # Animation set target.
        text_target = MathTex(
            *r"{   a   {   -   a   b   \over \sqrt{\left(x-h\right)^{2}-a^{2}}} \over a \left(\left(x-h\right)^{2}-a^{2}\right)}".split(
                "   "
            )
        )

        self.play(
            TransformMatchingTex(text, text_target),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            *r"{   a   { -ab \over \sqrt{\left(x-h\right)^{2}-a^{2}}} \over   a   \left(\left(x-h\right)^{2}-a^{2}\right)}".split(
                "   "
            )
        )

        self.add(text)
        # END

        # BEGIN Id: 31
        # Animation set target.
        text_target = MathTex(
            *r"{   { -ab \over \sqrt{\left(x-h\right)^{2}-a^{2}}} \over   \left(\left(x-h\right)^{2}-a^{2}\right)}".split(
                "   "
            )
        )

        self.play(
            TransformMatchingTex(text, text_target),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(
            r"{   { -ab \over \sqrt{\left(x-h\right)^{2}-a^{2}}} \over   \left(\left(x-h\right)^{2}-a^{2}\right)}"
        )

        self.add(text)
        # END

        # BEGIN Id: 32
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"\frac{-ab}{\left(\left(x-h\right)^{2}-a^{2}\right)\left(\left(x-h\right)^{2}-a^{2}\right)^{0.5}}"
        )

        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            *[FadeTransform(text[0][i], text_target[0][i]) for i in range(3)],
            *[FadeTransform(text[0][i], text_target[0][i + 10]) for i in range(6, 15)],
            *[Transform(text[0][i], text_target[0][i - 12]) for i in range(16, 27)],
            FadeIn(text_target[0][15], text_target[0][25], text_target[0][26:29]),
            Transform(text[0][15], text_target[0][3]),
            FadeOut(text[0][3:6]),
            run_time=(2 / 3),
        )

        self.remove(*self.mobjects)

        text = MathTex(
            *r"{-ab \over   \left(\left(x-h\right)^{2}-a^{2}\right)   \left(\left(x-h\right)^{2}-a^{2}\right)   ^{   0   .5   }}".split(
                "   "
            )
        )
        self.add(text)
        # END

        # BEGIN Id: 33
        # Animation set target.
        text_target = MathTex(
            *r"{-ab \over   \left(\left(x-h\right)^{2}-a^{2}\right)   ^{   1   .5   }}".split(
                "   "
            )
        )

        self.play(
            TransformMatchingTex(text, text_target),
            run_time=(2 / 3),
        )

        # Remove everything to remove strange artifacts, and re-add final target.
        self.remove(*self.mobjects)

        # Optional: Add what text *should* be:
        text = MathTex(r"{-ab \over\left(\left(x-h\right)^{2}-a^{2}\right)^{1.5}}")

        self.add(text)
        # END

        # BEGIN Id: 34
        # Unlucky, I gotta take matters into my own hands...
        text_target = MathTex(
            r"{-ab \over\left(\sqrt{\left(x-h\right)^{2}-a^{2}}\right)^{3}}"
        )

        # Toolbox
        # advanced_show(text[0])
        # self.remove(*self.mobjects)
        # advanced_show(text_target[0])
        # self.remove(*self.mobjects)
        # self.wait(2)
        # self.add(text)
        # self.wait()

        self.play(
            *[Transform(text[0][i], text_target[0][i]) for i in range(4)],
            FadeTransform(text[0][4], text_target[0][4]),
            FadeTransform(text[0][14], text_target[0][16]),
            Transform(text[0][15:18], text_target[0][17], path_arc=np.pi),
            FadeIn(text_target[0][5:7]),
            run_time=(2 / 3),
        )

        # END

        self.wait()