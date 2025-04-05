import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Тестовое задание

def f(y1, y2):
    return -y2 + y1 * (y1 ** 2 + y2 ** 2 - 1), y1 + y2 * (y1 ** 2 + y2 ** 2 - 1)


def runge_kutta(h, y1, y2):
    k1_1, k1_2 = f(y1, y2)
    k2_1, k2_2 = f(y1 + h * k1_1 / 2, y2 + h * k1_2 / 2)
    k3_1, k3_2 = f(y1 + h * k2_1 / 2, y2 + h * k2_2 / 2)
    k4_1, k4_2 = f(y1 + h * k3_1, y2 + h * k3_2)

    y1_new = y1 + h * (k1_1 + 2 * k2_1 + 2 * k3_1 + k4_1) / 6
    y2_new = y2 + h * (k1_2 + 2 * k2_2 + 2 * k3_2 + k4_2) / 6

    return y1_new, y2_new


def get_y1(x):
    return np.cos(x) / ((1 + np.exp(2 * x)) ** (1 / 2))


def get_y2(x):
    return np.sin(x) / ((1 + np.exp(2 * x)) ** (1 / 2))


t0, t1 = 0, 5
h = 0.01
t_values = np.arange(t0, t1 + h, h)
initial_y1 = get_y1(0)
initial_y2 = get_y2(0)
values_y1 = []
values_y2 = []
rung_values_y1 = []
rung_values_y2 = []
max_err = 0
for t in t_values:
    y1 = get_y1(t)
    y2 = get_y2(t)
    y1_rung, y2_rung = runge_kutta(h, initial_y1, initial_y2)
    values_y1.append(y1)
    values_y2.append(y2)
    rung_values_y1.append(y1_rung)
    rung_values_y2.append(y2_rung)

    initial_y1, initial_y2 = y1_rung, y2_rung

    print(f"Точка: {t}\n"
          f"Значение y1 Рунге-Кутта: {y1_rung}\n"
          f"Фактическое значение y1: {y1}\n"
          f"Значение y2 Рунге-Кутта: {y2_rung}\n"
          f"Фактическое значение y2: {y2}\n")


plt.plot(t_values, values_y1, label='Exact y1')
plt.plot(t_values, values_y2, label='Exact y2')
plt.plot(t_values, rung_values_y1, label='Runge-Kutta y1')
plt.plot(t_values, rung_values_y2, label='Runge-Kutta y2')
plt.xlabel('t')
plt.ylabel('y')
plt.title(f'Comparison of Exact and Runge-Kutta Solutions(h = {h})')
plt.legend()
plt.show()

# Подсчет ошибок
def error_plot():
    h_cur = h
    k = 5
    h_values = []
    y1_errors = []
    y2_errors = []

    for i in range(k):
        t0, t1 = 0, 5
        t_values = np.arange(t0, t1 + h_cur, h_cur)
        initial_y1 = get_y1(0)
        initial_y2 = get_y2(0)
        max_error_y1 = -np.inf
        max_error_y2 = -np.inf

        for t in t_values:
            y1_exact = get_y1(t)
            y2_exact = get_y2(t)
            y1_rk, y2_rk = runge_kutta(h_cur, initial_y1, initial_y2)
            error_y1 = np.abs(y1_rk - y1_exact)
            error_y2 = np.abs(y2_rk - y2_exact)

            if error_y1 > max_error_y1:
                max_error_y1 = error_y1
            if error_y2 > max_error_y2:
                max_error_y2 = error_y2

            initial_y1, initial_y2 = y1_rk, y2_rk

        y1_errors.append(max_error_y1 / h)
        y2_errors.append(max_error_y2 / h)
        h_values.append(h_cur)
        h_cur /= 2

    plt.plot(h_values, y1_errors, label='Error in y1')
    plt.plot(h_values, y2_errors, label='Error in y2')
    plt.gca().invert_xaxis()
    plt.xlabel('Step Size (h)')
    plt.ylabel('Max Error (e / h)')
    plt.title('Error Analysis with Step Size')
    plt.legend()
    plt.show()


error_plot()


def f(y1, y2, y3, alpha):
    return 1 + (y1 ** 2 * y2) - (y3 + 1) * y1, y1 * y3 - (y1 ** 2 * y2), -y1 * y3 + alpha


def runge_kutta(h, y1, y2, y3, alpha):
    k1_1, k1_2, k1_3 = f(y1, y2, y3, alpha)
    k2_1, k2_2, k2_3 = f(y1 + h * k1_1 / 2, y2 + h * k1_2 / 2, y3 + h * k1_3 / 2, alpha)
    k3_1, k3_2, k3_3 = f(y1 + h * k2_1 / 2, y2 + h * k2_2 / 2, y3 + h * k2_3 / 2, alpha)
    k4_1, k4_2, k4_3 = f(y1 + h * k3_1, y2 + h * k3_2, y3 + h * k3_3, alpha)

    y1_new = y1 + h * (k1_1 + 2 * k2_1 + 2 * k3_1 + k4_1) / 6
    y2_new = y2 + h * (k1_2 + 2 * k2_2 + 2 * k3_2 + k4_2) / 6
    y3_new = y3 + h * (k1_3 + 2 * k2_3 + 2 * k3_3 + k4_3) / 6

    return y1_new, y2_new, y3_new


def plot_trajectories(alpha_values):
    t0, t1 = 0, 5
    h = 0.01
    t_values = np.arange(t0, t1 + h, h)

    for alpha in alpha_values:
        y1_values = []
        y2_values = []
        y3_values = []

        y1, y2, y3 = 1, 1 + alpha, 1 + alpha

        for t in t_values:
            y1_values.append(y1)
            y2_values.append(y2)
            y3_values.append(y3)

            y1, y2, y3 = runge_kutta(h, y1, y2, y3, alpha)

        plt.plot(y1_values, y2_values, label=f'alpha={alpha}')

    plt.xlabel('y1')
    plt.ylabel('y2')
    plt.title('Phase Space Trajectories (y1 vs y2)')
    plt.legend()
    plt.show()

    for alpha in alpha_values:
        y1_values = []
        y2_values = []
        y3_values = []

        y1, y2, y3 = 1, 1 + alpha, 1 + alpha

        for t in t_values:
            y1_values.append(y1)
            y2_values.append(y2)
            y3_values.append(y3)

            y1, y2, y3 = runge_kutta(h, y1, y2, y3, alpha)

        plt.plot(y2_values, y3_values, label=f'alpha={alpha}')

    plt.xlabel('y2')
    plt.ylabel('y3')
    plt.title('Phase Space Trajectories (y2 vs y3)')
    plt.legend()
    plt.show()

    for alpha in alpha_values:
        y1_values = []
        y2_values = []
        y3_values = []

        y1, y2, y3 = 1, 1 + alpha, 1 + alpha

        for t in t_values:
            y1_values.append(y1)
            y2_values.append(y2)
            y3_values.append(y3)

            y1, y2, y3 = runge_kutta(h, y1, y2, y3, alpha)

        plt.plot(y1_values, y3_values, label=f'alpha={alpha}')

    plt.xlabel('y1')
    plt.ylabel('y3')
    plt.title('Phase Space Trajectories (y1 vs y3)')
    plt.legend()
    plt.show()


alpha_values = [0.5, 1.0, 1.2, 1.3, 1.4, 2.0]
plot_trajectories(alpha_values)

# Определение символьных переменных
y1, y2, y3, alpha = sp.symbols('y1 y2 y3 alpha')

# Задание уравнений
eq1 = 1 + (y1 ** 2 * y2) - (y3 + 1) * y1
eq2 = y1 * y3 - (y1 ** 2 * y2)
eq3 = -y1 * y3 + alpha

# Решение системы уравнений
solutions = sp.solve((eq1, eq2, eq3), (y1, y2, y3))

# Проверка количества решений
if len(solutions) == 1:
    y1_val, y2_val, y3_val = solutions[0]
    print(f"Стационарное решение единственно и соответствует условиям: y1 = {y1_val}, y2 = {y2_val}, y3 = {y3_val}")
elif len(solutions) > 1:
    print("Стационарное решение не единственно")
else:
    print("Стационарные решения не найдены")



# Составление вектора функций
f = sp.Matrix([eq1, eq2, eq3])

# Вычисление матрицы Якоби
Jacobian_matrix = f.jacobian([y1, y2, y3])

# Вывод матрицы Якоби
print("(∂f/∂y):")
print(Jacobian_matrix)
print()

print("y1 = 1\n"
      "y2 = alpha\n"
      "y3 = alpha\n"
      "(∂f/∂y):\n")

print("[alpha - 1    1    -1]\n"
      "[-alpha    -1    1]\n"
      "[-alpha    0    -1]")

# Определение символьных переменных
alpha, lambda_var = sp.symbols('alpha lambda')

# Задание матрицы Якоби с подставленными значениями
Jacobian_matrix = sp.Matrix([[alpha - 1, 1, -1],
                             [-alpha, -1, 1],
                             [-alpha, 0, -1]])

# Вычисление характеристического многочлена
char_poly = Jacobian_matrix.charpoly(lambda_var)

# Приведение из вида exp(lambda) -> lambda
char_poly = char_poly.as_expr().subs(sp.exp(lambda_var), lambda_var)

# Вывод характеристического многочлена
print("Характеристический многочлен матрицы:")
print(char_poly.simplify())
print()

# Характеристический многочлен
# char_poly = lambda_var ** 3 + (3 - alpha) * lambda_var ** 2 + (3 - 2 * alpha) * lambda_var + 1

# Проверка условия устойчивости для каждого значения alpha
for alpha_val in alpha_values:
    if alpha_val < (9 - sp.sqrt(17)) / 4:
        print(f"Условие устойчивости выполняется для alpha = {alpha_val}")
    else:
        print(f"alpha = {alpha_val}: Предельный цикл или взрыв")
