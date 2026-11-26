from manim import *
import numpy as np

# Configuración global del estilo
COLOR_PUNTO = TEAL
COLOR_VECTOR = ORANGE
COLOR_LINEA = BLUE_D
COLOR_TEXTO = WHITE
COLOR_DESTACADO = YELLOW

def agregar_firma(scene):
    firma = Tex("UC-Matemática y Computación - David Duarte", color=GRAY).scale(0.45)
    firma.to_edge(DOWN + RIGHT, buff=0.25)
    scene.add(firma)

class Escena1DefinicionEspacioAfin(Scene):
    def construct(self):
        agregar_firma(self)
        # Título
        titulo = Tex("1. Estructura de Espacio Afín", color=COLOR_DESTACADO).scale(1.2)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)

        # Definición
        definicion = Tex(
            r"Un \textbf{Espacio Afín} es una terna $(\mathcal{A}, V, +)$ donde:\\"
            r"$\mathcal{A}$ es un conjunto de \textbf{puntos},\\"
            r"$V$ es un \textbf{espacio vectorial} sobre $\mathbb{R}$, y\\"
            r"$+$ es una acción $+: \mathcal{A} \times V \to \mathcal{A}$ que asocia a cada $(P, \vec{v})$ un punto $Q = P + \vec{v}$."
        ).scale(0.8)
        definicion.next_to(titulo, DOWN, buff=0.5)
        self.play(FadeIn(definicion))
        self.wait(3)
        self.play(FadeOut(definicion))

        # Ilustración de Puntos y Vectores
        punto_P = Dot(point=[-2, -1, 0], color=COLOR_PUNTO)
        label_P = MathTex("P", color=COLOR_PUNTO).next_to(punto_P, DOWN)
        
        vector_v = Arrow(start=[-2, -1, 0], end=[2, 1, 0], buff=0, color=COLOR_VECTOR)
        label_v = MathTex(r"\vec{v}", color=COLOR_VECTOR).next_to(vector_v.get_center(), UP + LEFT*0.2)
        
        punto_Q = Dot(point=[2, 1, 0], color=COLOR_PUNTO)
        label_Q = MathTex("Q", color=COLOR_PUNTO).next_to(punto_Q, DOWN)

        self.play(FadeIn(punto_P), Write(label_P))
        self.wait(1)
        self.play(GrowArrow(vector_v), Write(label_v))
        self.play(FadeIn(punto_Q), Write(label_Q))
        self.wait(1)

        # Relación Suma y Resta
        formula_suma = MathTex("P + \\vec{v} = Q", color=COLOR_DESTACADO).to_edge(UP + RIGHT*2)
        self.play(Write(formula_suma))
        self.wait(1.5)

        formula_resta = MathTex("Q - P = \\vec{v}", color=COLOR_DESTACADO).next_to(formula_suma, DOWN, buff=0.3)
        self.play(Write(formula_resta))
        self.wait(2)

        # Propiedades (Axiomas)
        self.play(FadeOut(formula_suma), FadeOut(formula_resta))
        
        axiomas_titulo = Tex(r"\textbf{Axiomas Fundamentales:}", color=COLOR_DESTACADO).scale(0.8).to_edge(LEFT + UP*2)
        axioma_1 = MathTex(r"1. \quad P + \vec{0} = P \quad \forall P \in \mathcal{A}", color=COLOR_TEXTO).scale(0.8).next_to(axiomas_titulo, DOWN, aligned_edge=LEFT)
        axioma_2 = MathTex(r"2. \quad (P + \vec{u}) + \vec{v} = P + (\vec{u} + \vec{v})", color=COLOR_TEXTO).scale(0.8).next_to(axioma_1, DOWN, aligned_edge=LEFT)
        axioma_3 = MathTex(r"3. \quad \forall P, Q \in \mathcal{A}, \; \exists ! \, \vec{v} \in V : P + \vec{v} = Q", color=COLOR_TEXTO).scale(0.8).next_to(axioma_2, DOWN, aligned_edge=LEFT)

        self.play(Write(axiomas_titulo))
        self.play(Write(axioma_1))
        self.wait(1.5)
        
        # Animación del Axioma 2
        punto_P_aux = Dot(point=[-3, -2, 0], color=COLOR_PUNTO)
        label_P_aux = MathTex("P").scale(0.8).next_to(punto_P_aux, DOWN)
        vec_u = Arrow(start=[-3, -2, 0], end=[-1, -0.5, 0], buff=0, color=BLUE)
        label_u = MathTex(r"\vec{u}").scale(0.8).next_to(vec_u.get_center(), UP+LEFT*0.1)
        punto_Pu = Dot(point=[-1, -0.5, 0], color=COLOR_PUNTO)
        label_Pu = MathTex("P+\\vec{u}").scale(0.8).next_to(punto_Pu, UP)
        vec_v2 = Arrow(start=[-1, -0.5, 0], end=[2, -1.5, 0], buff=0, color=ORANGE)
        label_v2 = MathTex(r"\vec{v}").scale(0.8).next_to(vec_v2.get_center(), UP)
        punto_Puv = Dot(point=[2, -1.5, 0], color=COLOR_PUNTO)
        label_Puv = MathTex("P+\\vec{u}+\\vec{v}").scale(0.8).next_to(punto_Puv, DOWN)
        
        vec_u_v = Arrow(start=[-3, -2, 0], end=[2, -1.5, 0], buff=0, color=RED)
        label_uv = MathTex(r"\vec{u}+\vec{v}").scale(0.8).next_to(vec_u_v.get_center(), DOWN+RIGHT*0.1)

        self.play(
            FadeOut(punto_P), FadeOut(label_P), FadeOut(vector_v), FadeOut(label_v), FadeOut(punto_Q), FadeOut(label_Q),
            FadeIn(punto_P_aux), Write(label_P_aux)
        )
        self.play(Write(axioma_2))
        self.play(GrowArrow(vec_u), Write(label_u))
        self.play(FadeIn(punto_Pu), Write(label_Pu))
        self.play(GrowArrow(vec_v2), Write(label_v2))
        self.play(FadeIn(punto_Puv), Write(label_Puv))
        self.wait(1)
        self.play(GrowArrow(vec_u_v), Write(label_uv))
        self.wait(2)

        # Limpiar escena
        self.play(
            FadeOut(titulo), FadeOut(axiomas_titulo), FadeOut(axioma_1), FadeOut(axioma_2),
            FadeOut(punto_P_aux), FadeOut(label_P_aux), FadeOut(vec_u), FadeOut(label_u),
            FadeOut(punto_Pu), FadeOut(label_Pu), FadeOut(vec_v2), FadeOut(label_v2),
            FadeOut(punto_Puv), FadeOut(label_Puv), FadeOut(vec_u_v), FadeOut(label_uv)
        )
        
        # Axioma 3
        self.play(Write(axioma_3))
        self.wait(3)
        self.play(FadeOut(axioma_3))


class Escena2SubespaciosYCombinaciones(Scene):
    def construct(self):
        agregar_firma(self)
        # Título
        titulo = Tex("2. Subespacios y Combinaciones Afines", color=COLOR_DESTACADO).scale(1.2)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)

        # Explicación Subespacios
        explicacion1 = Tex(
            r"Un \textbf{subespacio afín} $S$ de $\mathcal{A}$ se define como:\\"
            r"$S = P + W = \{ P + \vec{w} \mid \vec{w} \in W \}$ donde $W \subseteq V$ es un subespacio vectorial."
        ).scale(0.8)
        explicacion1.next_to(titulo, DOWN, buff=0.5)
        self.play(FadeIn(explicacion1))
        self.wait(3)
        self.play(FadeOut(explicacion1))

        # Visualización de Subespacio Afín
        plano = NumberPlane(
            x_range=[-6, 6, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_color": GRAY, "stroke_opacity": 0.4}
        )
        self.play(Create(plano))
        
        # Subespacio vectorial W (recta que pasa por el origen)
        recta_W = Line(start=[-5, -2.5, 0], end=[5, 2.5, 0], color=GREEN, stroke_width=4)
        label_W = MathTex("W", color=GREEN).next_to(recta_W.get_end(), UP+LEFT)
        origen = Dot(point=[0, 0, 0], color=WHITE)
        label_origen = MathTex("O", color=WHITE).next_to(origen, DOWN+RIGHT*0.1)

        self.play(FadeIn(origen), Write(label_origen))
        self.play(Create(recta_W), Write(label_W))
        self.wait(1.5)

        # Punto de traslación P
        punto_P = Dot(point=[-1, 2, 0], color=COLOR_PUNTO)
        label_P = MathTex("P", color=COLOR_PUNTO).next_to(punto_P, UP+LEFT*0.1)
        vector_OP = Arrow(start=[0, 0, 0], end=[-1, 2, 0], buff=0, color=COLOR_VECTOR)
        label_OP = MathTex(r"\vec{OP}", color=COLOR_VECTOR).next_to(vector_OP.get_center(), LEFT)

        self.play(FadeIn(punto_P), Write(label_P))
        self.play(GrowArrow(vector_OP), Write(label_OP))
        self.wait(1)

        # Subespacio Afín S = P + W (traslación de la recta)
        recta_S = Line(start=[-6, -0.5, 0], end=[4, 4.5, 0], color=COLOR_DESTACADO, stroke_width=4)
        label_S = MathTex("S = P + W", color=COLOR_DESTACADO).next_to(recta_S.get_end(), DOWN+RIGHT*0.2)

        self.play(
            Transform(recta_W.copy(), recta_S, run_time=2),
            Write(label_S)
        )
        self.wait(2)

        # Limpiar elementos gráficos
        self.play(
            FadeOut(plano), FadeOut(recta_W), FadeOut(label_W), FadeOut(origen), FadeOut(label_origen),
            FadeOut(punto_P), FadeOut(label_P), FadeOut(vector_OP), FadeOut(label_OP),
            FadeOut(recta_S), FadeOut(label_S)
        )

        # Combinaciones Lineales vs Combinaciones Afines
        explicacion2 = Tex(
            r"En general, sumar puntos como $A + B$ \textbf{no tiene sentido}.\\ "
            r"Sin embargo, una \textbf{combinación afín} es válida:\\"
            r"$P = \sum_{i=1}^n \lambda_i P_i \quad \text{donde} \quad \sum_{i=1}^n \lambda_i = 1$"
        ).scale(0.8).next_to(titulo, DOWN, buff=0.5)
        
        self.play(FadeIn(explicacion2))
        self.wait(4.5)
        self.play(FadeOut(explicacion2))

        # Demostración interactiva: Combinación afín de 2 puntos (Recta)
        punto_A = Dot(point=[-2, -1, 0], color=COLOR_PUNTO)
        label_A = MathTex("A", color=COLOR_PUNTO).next_to(punto_A, DOWN)
        punto_B = Dot(point=[2, 1, 0], color=COLOR_PUNTO)
        label_B = MathTex("B", color=COLOR_PUNTO).next_to(punto_B, DOWN)

        linea_AB = Line(start=[-4, -2, 0], end=[4, 2, 0], color=GRAY, stroke_opacity=0.5)
        
        # Tracker de lambda
        lambda_tracker = ValueTracker(0.5)
        
        # Punto dinámico P
        def get_coords_P():
            l = lambda_tracker.get_value()
            return l * punto_A.get_center() + (1 - l) * punto_B.get_center()

        punto_P_din = always_redraw(lambda: Dot(point=get_coords_P(), color=COLOR_DESTACADO).scale(1.2))
        label_P_din = always_redraw(lambda: MathTex(
            rf"P = {lambda_tracker.get_value():.2f}A + {1 - lambda_tracker.get_value():.2f}B",
            color=COLOR_DESTACADO
        ).scale(0.8).next_to(punto_P_din, UP, buff=0.25))

        self.play(FadeIn(punto_A), Write(label_A), FadeIn(punto_B), Write(label_B), Create(linea_AB))
        self.play(FadeIn(punto_P_din), Write(label_P_din))
        self.wait(1)

        # Animar lambda de 0.5 a 1.2 (hacia A y más allá)
        self.play(lambda_tracker.animate.set_value(1.2), run_time=2.5, rate_func=linear)
        self.wait(0.5)
        # Animar lambda de 1.2 a -0.2 (hacia B y más allá)
        self.play(lambda_tracker.animate.set_value(-0.2), run_time=3.5, rate_func=linear)
        self.wait(0.5)
        # Regresar a 0.5 (punto medio)
        self.play(lambda_tracker.animate.set_value(0.5), run_time=2, rate_func=linear)
        self.wait(2)

        # Limpiar
        self.play(
            FadeOut(titulo), FadeOut(punto_A), FadeOut(label_A), FadeOut(punto_B), FadeOut(label_B),
            FadeOut(linea_AB), FadeOut(punto_P_din), FadeOut(label_P_din)
        )


class Escena3SistemasReferenciaYBaricentricas(Scene):
    def construct(self):
        agregar_firma(self)
        # Título
        titulo = Tex("3. Sistemas de Referencia y Coordenadas Baricéntricas", color=COLOR_DESTACADO).scale(1.1)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)

        # Definición Sistema de Referencia Afín
        ref_def = Tex(
            r"Un \textbf{sistema de referencia afín} es un par $(O, \{ \vec{e}_1, \vec{e}_2, \dots, \vec{e}_n \})$ donde:\\"
            r"$O$ es un punto llamado \textbf{origen},\\"
            r"y $\{ \vec{e}_i \}$ es una \textbf{base} del espacio vectorial asociado $V$."
        ).scale(0.8).next_to(titulo, DOWN, buff=0.5)
        self.play(FadeIn(ref_def))
        self.wait(3.5)
        self.play(FadeOut(ref_def))

        # Coordenadas Baricéntricas
        bar_def = Tex(
            r"Dado un símplex (ej. un triángulo con vértices $P_0, P_1, P_2$),\\ "
            r"cualquier punto $P$ se expresa de forma única como:\\"
            r"$P = \lambda_0 P_0 + \lambda_1 P_1 + \lambda_2 P_2$\\"
            r"donde $\lambda_0 + \lambda_1 + \lambda_2 = 1$.\\"
            r"$(\lambda_0, \lambda_1, \lambda_2)$ son las \textbf{coordenadas baricéntricas} de $P$."
        ).scale(0.8).next_to(titulo, DOWN, buff=0.5)
        self.play(FadeIn(bar_def))
        self.wait(4.5)
        self.play(FadeOut(bar_def))

        # Visualización de Triángulo y Coordenadas Baricéntricas
        v0 = np.array([-2, -1.5, 0])
        v1 = np.array([2, -1.5, 0])
        v2 = np.array([0, 2, 0])

        triangulo = Polygon(v0, v1, v2, color=BLUE_B, fill_opacity=0.1)
        dot_v0 = Dot(v0, color=BLUE)
        dot_v1 = Dot(v1, color=BLUE)
        dot_v2 = Dot(v2, color=BLUE)
        
        label_v0 = MathTex("P_0").next_to(dot_v0, DOWN+LEFT*0.1)
        label_v1 = MathTex("P_1").next_to(dot_v1, DOWN+RIGHT*0.1)
        label_v2 = MathTex("P_2").next_to(dot_v2, UP)

        self.play(
            Create(triangulo),
            FadeIn(dot_v0), Write(label_v0),
            FadeIn(dot_v1), Write(label_v1),
            FadeIn(dot_v2), Write(label_v2)
        )
        self.wait(1)

        # Tracker para mover el punto P usando coordenadas polares/barycentricas
        # Definiremos P interactivamente
        # Para hacer la animación robusta, definimos P y sus coeficientes dinámicamente
        # Usaremos un ValueTracker para representar la posición de P
        # en coordenadas cartesianas y calcularemos las baricéntricas a partir de ahí.
        
        punto_P = Dot(np.array([0, 0, 0]), color=COLOR_DESTACADO).scale(1.2)

        # Función para calcular coordenadas baricéntricas de un punto p en el triángulo v0, v1, v2
        def get_barycentric_coords(p):
            # Formar el sistema de ecuaciones:
            # l0*v0_x + l1*v1_x + l2*v2_x = p_x
            # l0*v0_y + l1*v1_y + l2*v2_y = p_y
            # l0 + l1 + l2 = 1
            A = np.array([
                [v0[0], v1[0], v2[0]],
                [v0[1], v1[1], v2[1]],
                [1, 1, 1]
            ])
            B = np.array([p[0], p[1], 1])
            try:
                coords = np.linalg.solve(A, B)
            except np.linalg.LinAlgError:
                coords = np.array([1/3, 1/3, 1/3])
            return coords
        
        # Líneas discontinuas que dividen el triángulo
        lineas_P = always_redraw(lambda: VGroup(
            DashedLine(punto_P.get_center(), v0, color=GRAY, stroke_opacity=0.6),
            DashedLine(punto_P.get_center(), v1, color=GRAY, stroke_opacity=0.6),
            DashedLine(punto_P.get_center(), v2, color=GRAY, stroke_opacity=0.6)
        ))

        # Texto dinámico de coordenadas baricéntricas
        def get_coords_text():
            p = punto_P.get_center()
            l0, l1, l2 = get_barycentric_coords(p)
            return MathTex(
                rf"\lambda_0 = {l0:.2f} \quad \lambda_1 = {l1:.2f} \quad \lambda_2 = {l2:.2f}",
                color=COLOR_DESTACADO
            ).scale(0.85).to_edge(DOWN*1.5)

        label_coords = always_redraw(get_coords_text)

        self.play(FadeIn(punto_P), Create(lineas_P))
        self.play(Write(label_coords))
        self.wait(1)

        # Mover P a distintas posiciones dentro y fuera del triángulo
        # Centro de gravedad (1/3, 1/3, 1/3) -> aprox (0, -0.33, 0)
        self.play(punto_P.animate.move_to(np.array([0, -0.33, 0])), run_time=1.5)
        self.wait(1)

        # Cerca de P2 (0, 1.5, 0) -> l2 muy grande, l0 y l1 pequeños
        self.play(punto_P.animate.move_to(np.array([0, 1.2, 0])), run_time=2)
        self.wait(1)

        # Cerca de P0 (-1.5, -1.0, 0)
        self.play(punto_P.animate.move_to(np.array([-1.5, -1.0, 0])), run_time=2)
        self.wait(1)

        # Fuera del triángulo (1.5, 1.5, 0) -> muestra coordenadas negativas
        self.play(punto_P.animate.move_to(np.array([1.5, 1.5, 0])), run_time=2)
        self.wait(1.5)

        # Regresar al centro
        self.play(punto_P.animate.move_to(np.array([0, -0.33, 0])), run_time=1.5)
        self.wait(2)

        # Limpiar escena
        self.play(
            FadeOut(titulo), FadeOut(triangulo), FadeOut(dot_v0), FadeOut(label_v0),
            FadeOut(dot_v1), FadeOut(label_v1), FadeOut(dot_v2), FadeOut(label_v2),
            FadeOut(punto_P), FadeOut(lineas_P), FadeOut(label_coords)
        )


class Escena4TransformacionesAfines(Scene):
    def construct(self):
        agregar_firma(self)
        # Título
        titulo = Tex("4. Transformaciones Afines", color=COLOR_DESTACADO).scale(1.2)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)

        # Explicación teórica
        explicacion = Tex(
            r"Una \textbf{transformación afín} $f: \mathcal{A} \to \mathcal{A}$ es una aplicación tal que:\\"
            r"1. Preserva la \textbf{colinealidad} (rectas se transforman en rectas).\\"
            r"2. Preserva la \textbf{razón simple} de tres puntos colineales:\\"
            r"$\frac{\vec{AC}}{\vec{CB}} = \frac{\vec{f(A)f(C)}}{\vec{f(C)f(B)}}$"
        ).scale(0.8).next_to(titulo, DOWN, buff=0.5)
        self.play(FadeIn(explicacion))
        self.wait(4.5)
        self.play(FadeOut(explicacion))

        # Crear plano cartesiano de referencia
        plano = NumberPlane(
            x_range=[-6, 6, 1], y_range=[-4, 4, 1],
            background_line_style={"stroke_color": GRAY, "stroke_opacity": 0.4}
        )
        self.play(Create(plano))

        # Puntos iniciales colineales A, C, B. C divide AB en razón 2:1
        # A = (-3, -1), B = (3, 1). Vector AB es (6, 2).
        # C está a 2/3 de distancia de A. C = A + 2/3 * (6, 2) = (-3+4, -1+4/3) = (1, 1/3)
        # Razón simple AC / CB = 2.
        pos_A = np.array([-3, -1, 0])
        pos_B = np.array([3, 1, 0])
        pos_C = np.array([1, 1/3, 0])

        recta = Line(start=pos_A - np.array([1.5, 0.5, 0]), end=pos_B + np.array([1.5, 0.5, 0]), color=COLOR_LINEA)
        
        dot_A = Dot(pos_A, color=COLOR_PUNTO)
        dot_B = Dot(pos_B, color=COLOR_PUNTO)
        dot_C = Dot(pos_C, color=RED) # Destacamos C

        label_A = MathTex("A").next_to(dot_A, DOWN+RIGHT*0.1)
        label_B = MathTex("B").next_to(dot_B, DOWN+RIGHT*0.1)
        label_C = MathTex("C").next_to(dot_C, UP+LEFT*0.1)

        self.play(Create(recta))
        self.play(
            FadeIn(dot_A), Write(label_A),
            FadeIn(dot_B), Write(label_B),
            FadeIn(dot_C), Write(label_C)
        )
        
        # Mostrar razón simple inicial
        # \vec{AC} = (4, 4/3), \vec{CB} = (2, 2/3). Razón es exactamente 2.0.
        texto_razon = MathTex(
            r"\text{Razón Simple: } \frac{\vec{AC}}{\vec{CB}} = \frac{4}{2} = 2",
            color=COLOR_DESTACADO
        ).to_edge(UP+RIGHT*1.5)
        self.play(Write(texto_razon))
        self.wait(2)

        # Definir una transformación afín (Cizallamiento/Shear + Rotación + Traslación)
        # Matriz lineal: M = [[1.2, 0.6], [0.3, 0.8]]
        # Vector traslación: T = [0.5, -0.5]
        # f(x, y) = M * [x, y] + T
        M = np.array([[1.1, 0.5], [0.2, 0.9]])
        T = np.array([0.5, -0.5, 0])

        def transform_point(p):
            coords_2d = p[:2]
            transformed_2d = M.dot(coords_2d) + T[:2]
            return np.array([transformed_2d[0], transformed_2d[1], 0])

        # Aplicar la transformación de forma animada a los objetos de la escena
        pos_A_tf = transform_point(pos_A)
        pos_B_tf = transform_point(pos_B)
        pos_C_tf = transform_point(pos_C)

        recta_tf = Line(
            start=pos_A_tf - 1.5 * (pos_B_tf - pos_A_tf) / 6,
            end=pos_B_tf + 1.5 * (pos_B_tf - pos_A_tf) / 6,
            color=COLOR_LINEA
        )

        dot_A_tf = Dot(pos_A_tf, color=COLOR_PUNTO)
        dot_B_tf = Dot(pos_B_tf, color=COLOR_PUNTO)
        dot_C_tf = Dot(pos_C_tf, color=RED)

        label_A_tf = MathTex("f(A)").next_to(dot_A_tf, DOWN+RIGHT*0.1)
        label_B_tf = MathTex("f(B)").next_to(dot_B_tf, DOWN+RIGHT*0.1)
        label_C_tf = MathTex("f(C)").next_to(dot_C_tf, UP+LEFT*0.1)

        # Animar la cuadrícula del plano deformándose para ilustrar la transformación afín
        self.play(
            plano.animate.apply_matrix(M).shift(T),
            Transform(recta, recta_tf),
            Transform(dot_A, dot_A_tf),
            Transform(dot_B, dot_B_tf),
            Transform(dot_C, dot_C_tf),
            Transform(label_A, label_A_tf),
            Transform(label_B, label_B_tf),
            Transform(label_C, label_C_tf),
            run_time=3
        )
        self.wait(1.5)

        # Mostrar razón simple transformada
        # \vec{f(A)f(C)} y \vec{f(C)f(B)}
        vec_AC_tf = pos_C_tf - pos_A_tf
        vec_CB_tf = pos_B_tf - pos_C_tf
        norm_AC_tf = np.linalg.norm(vec_AC_tf)
        norm_CB_tf = np.linalg.norm(vec_CB_tf)
        
        texto_razon_tf = MathTex(
            rf"\text{{Razón Transformada: }} \frac{{\|\vec{{f(A)f(C)}}\|}}{{\|\vec{{f(C)f(B)}}\|}} = \frac{{{norm_AC_tf:.2f}}}{{{norm_CB_tf:.2f}}} = 2",
            color=COLOR_DESTACADO
        ).to_edge(UP+RIGHT*1.5)

        self.play(
            Transform(texto_razon, texto_razon_tf)
        )
        self.wait(3)

        # Limpieza de la escena
        self.play(
            FadeOut(titulo), FadeOut(plano), FadeOut(recta),
            FadeOut(dot_A), FadeOut(dot_B), FadeOut(dot_C),
            FadeOut(label_A), FadeOut(label_B), FadeOut(label_C),
            FadeOut(texto_razon)
        )

        # Mensaje de Cierre
        cierre = Tex(
            r"\textbf{Resumen:}\\"
            r"1. Los puntos afines se relacionan mediante vectores.\\"
            r"2. Los subespacios afines generalizan rectas/planos desplazados.\\"
            r"3. Las coordenadas baricéntricas expresan puntos respecto a vértices.\\"
            r"4. Las transformaciones afines conservan rectas y proporciones."
        ).scale(0.8)
        self.play(FadeIn(cierre))
        self.wait(4.5)
        self.play(FadeOut(cierre))
