# Constante de Vicuna (Ωᵛ)

Implementación en Python para calcular la **Constante de Vicuna (Ωᵛ)**, definida mediante una construcción fractal que combina la **secuencia de Fibonacci** y el **número áureo (φ)** en una suma/producto infinito con estructura logarítmico-exponencial.

> **Nota:** Se usa *Vicuna* (sin “ñ”) para facilitar su uso internacional. El nombre proviene del apellido del autor (*Vicuña*).

---

## Definición matemática

Sea \(F_n\) el n-ésimo número de Fibonacci y \(\varphi=\tfrac{1+\sqrt{5}}{2}\) el número áureo. La **Constante de Vicuna** \(\Omega^{v}\) es el **único** \(x>1\) que satisface:

\[
\sum_{n=1}^{\infty} \varphi^{-n}\,\ln\!\big(1+x^{-F_n}\big)=\ln \varphi.
\]

Forma equivalente (producto):

\[
\prod_{n=1}^{\infty}\big(1+x^{-F_n}\big)^{\varphi^{-n}}=\varphi.
\]

---

## Valor numérico

Con 60 dígitos de precisión y truncando desde \(n\ge 20\):

\[
\Omega^{v} \approx 1.98832658765224017964669107869242528410912236293597311717525
\]

El error de truncamiento \(\Delta x\) es despreciable (ver sección de cotas de error).

---

## Contenido del repositorio

- `vicuna_constant.py`  
  - Cálculo de \( \Omega^{v} \) por bisección.  
  - Cotas de cola: simple, geométrica y certificada.  
  - Derivada y estimación de error \(\Delta x\).  
  - Prueba de estabilidad con diferentes valores de corte \(n\).

---

## Requisitos

- Python 3.10+  
- [mpmath](https://mpmath.org/)

Instalación:
```bash
pip install mpmath
```

---

## Uso

Ejecuta el script:

```bash
python vicuna_constant.py
```

Ejemplo de salida:
```
Con 20 términos:
Ωᵛ ≈ 1.98832658765224017964669107869242528410912236293597311717525
Residual (debe ser cerca de 0): ~1e-61
Cota simple/geométrica/certificada para cola: ~2.31e-3272
Derivada f'(Ωᵛ): magnitud ~ 0.249
Error de truncamiento Δx ≈ ~9.3e-3272
```

---

## Cotas de error

La serie converge rápidamente porque \(\log(1+t)\le t\) y \(F_n\) crece como \(\varphi^n/\sqrt{5}\).

El código calcula tres cotas para la cola:
- **Simple:** primer término omitido.  
- **Geométrica:** usa la razón entre términos.  
- **Certificada:** reemplaza \(\log(1+t)\) por \(t\), dando una cota superior garantizada.

El error en \(x\) se estima como:
\[
\Delta x \;\approx\; \frac{\text{tail}}{|f'(x)|}.
\]

---

## Autoría y cita

**Autor:** Pablo Vicuna (Vicuña)  
**Año:** 2025  
**Denominación:** Constante de Vicuna (Ωᵛ)  

**Cita sugerida:**
> Vicuna, P. (2025). *Constante de Vicuna (Ωᵛ): definición y cálculo numérico.*  
> Implementación en Python con mpmath; suma infinita basada en Fibonacci y el número áureo.  
> URL del repositorio.

---

## Licencia

MIT License © 2025 Pablo Vicuna
