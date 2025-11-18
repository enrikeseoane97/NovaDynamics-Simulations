# 🛰️ Nova Dynamics - Simulaciones Científicas Avanzadas

Bienvenidos al repositorio oficial de **Nova Dynamics**, una iniciativa enfocada en el desarrollo de **simulaciones físicas y algoritmos predictivos** utilizando Python.

Nuestro objetivo es explorar la dinámica del mundo real a través de modelos matemáticos y la visualización de datos de alta fidelidad.

---

## 🔬 Proyecto 1: Simulación de Péndulo Simple

Este es nuestro primer proyecto: una implementación del modelo físico de un péndulo simple utilizando el **Método de Euler** para la integración numérica y **Matplotlib** para la visualización 3D.

### 🌟 Características Principales

* **Modelo Físico:** Implementación del movimiento del péndulo simple, asumiendo fricción y amortiguamiento mínimos.
* **Integración Numérica:** Uso del **Método de Euler** para calcular la posición y velocidad en cada paso de tiempo ($dt=0.005$ segundos).
* **Visualización:** Renderizado 3D de la simulación mediante la librería Matplotlib, lo que garantiza una ejecución robusta y multiplataforma.

### 🛠️ Requisitos e Instalación

Para ejecutar este proyecto, necesitarás tener [Python](https://www.python.org/) y las siguientes librerías:

1.  Asegúrate de tener tu entorno virtual activado (`(venv_nd)`).
2.  Instala las dependencias necesarias:

    ```bash
    pip install numpy matplotlib
    ```

### 🚀 Ejecución del Código

Una vez instaladas las dependencias, ejecuta el script `pendulo_simple.py` desde la terminal (asegúrate de estar en el directorio correcto):

```bash
python pendulo_simple.py
