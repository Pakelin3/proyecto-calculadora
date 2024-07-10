import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

def menu():
    print("\n--- Calculadora de Probabilidades ---")
    print("1. Distribución Binomial")
    print("2. Distribución de Poisson")
    print("3. Distribución Hipergeométrica")
    print("4. Distribución Normal")
    print("5. Salir")

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("¡Error! Ingrese un número válido.")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("¡Error! Ingrese un número entero válido.")

# Funciones que pasan los valores de cada metodo para graficarlos(x,y)
# y les da un titulo
def plot_binomial(n, p):
    x = np.arange(0, n+1)
    pmf_values = stats.binom.pmf(x, n, p)
    plt.bar(x, pmf_values, label=f'Binomial(n={n}, p={p})', alpha=0.7)
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.title('Distribución Binomial')
    plt.legend()
    plt.show()

def plot_normal(mu, sigma):
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)
    pdf_values = stats.norm.pdf(x, mu, sigma)
    plt.plot(x, pdf_values, label=f'Normal(mu={mu}, sigma={sigma})')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.title('Distribución Normal')
    plt.legend()
    plt.show()

def plot_hypergeometric(M, n, N):
    x = np.arange(max(0, N-M+n), min(n, N)+1)
    pmf_values = stats.hypergeom.pmf(x, M, n, N)
    plt.bar(x, pmf_values, label=f'Hipergeométrica(M={M}, n={n}, N={N})', alpha=0.7)
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.title('Distribución Hipergeométrica')
    plt.legend()
    plt.show()

def plot_poisson(mu):
    x = np.arange(0, 10*mu+1)  # Ajustes del rango para mostrar suficientes puntos en el grafico
    pmf_values = stats.poisson.pmf(x, mu)
    plt.bar(x, pmf_values, label=f'Poisson(mu={mu})', alpha=0.7)
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.title('Distribución de Poisson')
    plt.legend()
    plt.show()

def calculate_binomial():
    print("\n--- Distribución Binomial ---")
    n = get_int_input("Ingrese el número de ensayos (n): ")
    p = get_float_input("Ingrese la probabilidad de éxito (p): ")
    xi = get_int_input("Ingrese el valor específico (xi): ")
    
    if n <= 0 or p < 0 or p > 1 or xi < 0 or xi > n:
        print("¡Error! Valores incorrectos para la distribución binomial.")
        return
    
    P_x_gt_xi = 1 - stats.binom.cdf(xi, n, p)
    P_x_lt_xi = stats.binom.cdf(xi - 1, n, p)
    P_x_ge_xi = 1 - stats.binom.cdf(xi - 1, n, p)
    P_x_le_xi = stats.binom.cdf(xi, n, p)
    P_xi_lt_x_lt_xi = stats.binom.pmf(xi - 1, n, p)
    P_xi_le_x_le_xi = stats.binom.pmf(xi, n, p)
    
    print("\nProbabilidades para distribución binomial:")
    
    print(f"P(x > xi): {P_x_gt_xi}")
    print(f"P(x < xi): {P_x_lt_xi}")
    print(f"P(x >= xi): {P_x_ge_xi}")
    print(f"P(x <= xi): {P_x_le_xi}")
    print(f"P(xi < x < xi): {P_xi_lt_x_lt_xi}")
    print(f"P(xi <= x <= xi): {P_xi_le_x_le_xi}")
    
    plot_binomial(n, p)

def calculate_normal():
    print("\n--- Distribución Normal ---")
    mu = get_float_input("Ingrese el valor de la media (mu): ")
    sigma = get_float_input("Ingrese el valor de la desviación estándar (sigma): ")
    xi = get_float_input("Ingrese el valor específico (xi): ")
    
    if sigma <= 0:
        print("¡Error! La desviación estándar debe ser positiva.")
        return
    
    P_x_gt_xi = 1 - stats.norm.cdf(xi, mu, sigma)
    P_x_lt_xi = stats.norm.cdf(xi, mu, sigma)
    P_x_ge_xi = 1 - stats.norm.cdf(xi - 1e-9, mu, sigma)
    P_x_le_xi = stats.norm.cdf(xi + 1e-9, mu, sigma)
    P_xi_lt_x_lt_xi = stats.norm.pdf(xi, mu, sigma)
    P_xi_le_x_le_xi = stats.norm.pdf(xi, mu, sigma)
    
    print("\nProbabilidades para distribución normal:")
    print(f"P(x > xi): {P_x_gt_xi}")
    print(f"P(x < xi): {P_x_lt_xi}")
    print(f"P(x >= xi): {P_x_ge_xi}")
    print(f"P(x <= xi): {P_x_le_xi}")
    print(f"P(xi < x < xi): {P_xi_lt_x_lt_xi}")
    print(f"P(xi <= x <= xi): {P_xi_le_x_le_xi}")
    
    plot_normal(mu, sigma)

def calculate_hypergeometric():
    print("\n--- Distribución Hipergeométrica ---")
    M = get_int_input("Ingrese el tamaño de la población total (M): ")
    n = get_int_input("Ingrese el número de elementos en la muestra (n): ")
    N = get_int_input("Ingrese el tamaño de la muestra (N): ")

    if n > M or N > M or n > N or M <= 0 or n <= 0 or N <= 0:
        print("¡Error! Valores incorrectos para la distribución hipergeométrica.")
        return

    xi = get_int_input("Ingrese el valor específico (xi): ")
    
    P_x_gt_xi = 1 - stats.hypergeom.cdf(xi, M, n, N)
    P_x_lt_xi = stats.hypergeom.cdf(xi - 1, M, n, N)
    P_x_ge_xi = 1 - stats.hypergeom.cdf(xi - 1, M, n, N)
    P_x_le_xi = stats.hypergeom.cdf(xi, M, n, N)
    P_xi_lt_x_lt_xi = stats.hypergeom.pmf(xi - 1, M, n, N)
    P_xi_le_x_le_xi = stats.hypergeom.pmf(xi, M, n, N)
    
    print("\nProbabilidades para distribución hipergeométrica:")
    print(f"P(x > xi): {P_x_gt_xi}")
    print(f"P(x < xi): {P_x_lt_xi}")
    print(f"P(x >= xi): {P_x_ge_xi}")
    print(f"P(x <= xi): {P_x_le_xi}")
    print(f"P(xi < x < xi): {P_xi_lt_x_lt_xi}")
    print(f"P(xi <= x <= xi): {P_xi_le_x_le_xi}")
    
    plot_hypergeometric(M, n, N)

def calculate_poisson():
    print("\n--- Distribución de Poisson ---")
    mu = get_float_input("Ingrese el valor de lambda (mu): ")
    xi = get_int_input("Ingrese el valor específico (xi): ")

    if mu <= 0 or xi < 0:
        print("¡Error! Valores incorrectos para la distribución de Poisson.")
        return
    
    P_x_gt_xi = 1 - stats.poisson.cdf(xi, mu)
    P_x_lt_xi = stats.poisson.cdf(xi - 1, mu)
    P_x_ge_xi = 1 - stats.poisson.cdf(xi - 1, mu)
    P_x_le_xi = stats.poisson.cdf(xi, mu)
    P_xi_lt_x_lt_xi = stats.poisson.pmf(xi - 1, mu)
    P_xi_le_x_le_xi = stats.poisson.pmf(xi, mu)
    
    print("\nProbabilidades para distribución de Poisson:")
    print(f"P(x > xi): {P_x_gt_xi}")
    print(f"P(x < xi): {P_x_lt_xi}")
    print(f"P(x >= xi): {P_x_ge_xi}")
    print(f"P(x <= xi): {P_x_le_xi}")
    print(f"P(xi < x < xi): {P_xi_lt_x_lt_xi}")
    print(f"P(xi <= x <= xi): {P_xi_le_x_le_xi}")
    
    plot_poisson(mu)

# Funcion principal para ejecutar todo el programa
def main():
    while True:
        menu()
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == '1':
            calculate_binomial()
        elif opcion == '2':
            calculate_poisson()
        elif opcion == '3':
            calculate_hypergeometric()
        elif opcion == '4':
            calculate_normal()
        elif opcion == '5':
            print("\nCerrando la calculadora xD")
            break
        else:
            print("Opción no válida. Seleccione nuevamente.")

if __name__ == "__main__":
    main()