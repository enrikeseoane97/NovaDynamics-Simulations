from vpython import *
# CAMBIO 1: Importamos CuPy y lo llamamos 'np'. ¡Esto usa la GPU!
import cupy as np 
import time # Para medir el tiempo de aceleración

# --- 1. CONFIGURACIÓN INICIAL DE LA ESCENA ---
scene.caption = "Simulación de Péndulo Simple (Nova Dynamics) - Acelerado por CUDA"
scene.autoscale = True
scene.range = 2.0

# --- 2. PARÁMETROS FÍSICOS Y TEMPORALES ---
g = 9.8                         # Aceleración de la gravedad (m/s^2)
L = 1.0                         # Longitud de la cuerda (m)

# CAMBIO 2: Convertimos la variable inicial a un array de CuPy (GPU)
# Esto es esencial si fueran cientos de péndulos, pero lo aplicamos.
theta_initial_cpu = 60 * np.pi / 180 
theta_initial = np.asarray(theta_initial_cpu) 

omega = np.asarray(0.0)         # Velocidad angular inicial (rad/s)
t = 0.0                         # Tiempo inicial

dt = 0.005                      # Paso de tiempo para la simulación (s). 
velocidad_visual = 100          # Cuántas veces por segundo refrescamos la vista (rate(X))

# --- 3. CREACIÓN DE OBJETOS 3D (VPython solo acepta posiciones de CPU) ---
# Convertimos el ángulo de la GPU de vuelta a CPU para VPython
theta_cpu = np.asnumpy(theta_initial)

# Punto de anclaje
Anclaje = sphere(pos=vector(0, 0, 0), radius=0.05, color=color.white)
# Masa (bob)
masa = sphere(pos=vector(L * np.sin(theta_cpu), -L * np.cos(theta_cpu), 0), 
               radius=0.08, color=color.red, make_trail=True, trail_type="ribbon")
# Cuerda
cuerda = cylinder(pos=Anclaje.pos, axis=masa.pos - Anclaje.pos, radius=0.01)

# --- 4. BUCLE DE SIMULACIÓN (EL CORAZÓN DEL CÁLCULO) ---
start_time = time.time() # Iniciamos la medición de tiempo

while t < 20.0: # Simular durante 20 segundos
    rate(velocidad_visual)
    
    # 1. CÁLCULO DE LA ACELERACIÓN ANGULAR (ALFA) - ¡ESTO LO HACE LA GPU!
    alfa = - (g / L) * np.sin(theta_initial) 
    
    # 2. MÉTODO DE EULER para ACTUALIZAR VELOCIDAD Y POSICIÓN (DISCRETIZACIÓN) - ¡GPU!
    omega = omega + alfa * dt      
    theta_initial = theta_initial + omega * dt 
    
    # 3. ACTUALIZAR POSICIÓN 3D DE LOS OBJETOS (Debe ser en la CPU para VPython)
    # Convertimos el ángulo de CuPy (GPU) a NumPy (CPU)
    theta_cpu = np.asnumpy(theta_initial)
    
    x = L * np.sin(theta_cpu)
    y = -L * np.cos(theta_cpu)
    masa.pos = vector(float(x), float(y), 0)
    cuerda.axis = masa.pos - Anclaje.pos
    
    # 4. AVANZAR EL TIEMPO
    t = t + dt

end_time = time.time()
print("Simulación completada. Tiempo de CPU/GPU:", end_time - start_time, "segundos")