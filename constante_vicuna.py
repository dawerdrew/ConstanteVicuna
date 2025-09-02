from mpmath import mp, mpf, ln, log1p, power

# Parámetros para evitar errores
mp.dps = 60  # 60 dígitos de precisión
phi = (1 + mp.sqrt(5)) / 2  # Número áureo exacto
ln_phi = ln(phi)  # Lado derecho de la ecuación

def precompute_fib_and_weights(max_n):
    """Precomputa Fibonacci y pesos φ^{-n} hasta max_n + 2 para tail_bound."""
    F = [mpf(0)] * (max_n + 3)
    w = [mpf(0)] * (max_n + 3)
    F[1] = mpf(1)
    F[2] = mpf(1)
    w[1] = 1 / phi
    for n in range(3, max_n + 3):
        F[n] = F[n-1] + F[n-2]
    for n in range(2, max_n + 3):
        w[n] = w[n-1] / phi
    return F, w

def f(x, max_n, F, w):
    """Suma finita hasta max_n términos, con precomputados y log1p para estabilidad."""
    s = mpf(0)
    invx = 1 / x
    for n in range(1, max_n + 1):
        s += w[n] * log1p(power(invx, F[n]))
    return s

def f_derivative(x, max_n, F, w):
    """Calcula la derivada de f(x) hasta max_n términos."""
    s = mpf(0)
    invx = 1 / x
    x2 = x * x
    for n in range(1, max_n + 1):
        t_n = power(invx, F[n])
        s += w[n] * F[n] * power(invx, F[n] - 1) / (x2 * (1 + t_n))
    return s

def tail_bound(x, max_n, F, w):
    """Cota superior conservadora para la cola (primer término omitido)."""
    n = max_n + 1
    return w[n] * log1p(power(1/x, F[n]))

def geometric_tail_bound(x, max_n, F, w):
    """Cota geométrica basada en la razón empírica."""
    n = max_n + 1
    first_omit = w[n] * log1p(power(1/x, F[n]))
    next_omit = w[n+1] * log1p(power(1/x, F[n+1])) if n+1 < len(w) else first_omit / phi
    ratio = next_omit / first_omit if first_omit != 0 else 1.0
    return first_omit / (1 - ratio) if abs(ratio) < 1 and first_omit != 0 else first_omit

def certified_tail_bound(x, max_n, F, w):
    """Cota certificada para la cola usando log(1+t) <= t."""
    n = max_n + 1
    invx = 1 / x
    first = w[n] * power(invx, F[n])
    r = (1 / phi) * power(invx, F[n-1])
    return first / (1 - r) if r < 1 else mp.inf

def solve_omega(max_n):
    """Resolver x con bisección adaptativa."""
    F, w = precompute_fib_and_weights(max_n)
    low = mpf(1.98)
    high = mpf(1.99)
    while high - low > mp.eps * 10:
        mid = (low + high) / 2
        if f(mid, max_n, F, w) > ln_phi:
            low = mid
        else:
            high = mid
    return (low + high) / 2

# Prueba de estabilidad con diferentes max_n
for max_n in [10, 20, 40, 60, 80, 100]:
    omega = solve_omega(max_n)
    F, w = precompute_fib_and_weights(max_n)
    residual = f(omega, max_n, F, w) - ln_phi
    tail_simple = tail_bound(omega, max_n, F, w)
    tail_geom = geometric_tail_bound(omega, max_n, F, w)
    tail_cert = certified_tail_bound(omega, max_n, F, w)
    f_prime = f_derivative(omega, max_n, F, w)
    delta_x = tail_cert / abs(f_prime) if f_prime != 0 else mp.inf
    print(f"Con {max_n} términos:")
    print(f"Ωᵛ ≈ {omega}")
    print(f"Residual (debe ser cerca de 0): {residual}")
    print(f"Cota simple para cola: {tail_simple}")
    print(f"Cota geométrica para cola: {tail_geom}")
    print(f"Cota certificada para cola: {tail_cert}")
    print(f"Derivada f'(Ωᵛ): {f_prime}")
    print(f"Error de truncamiento Δx ≈ {delta_x}")
    print("---")
