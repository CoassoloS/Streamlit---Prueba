# Streamlit---Prueba
# 🟡 Pac-Man en Streamlit

¡Bienvenido al clásico juego de Pac-Man reimaginado en Streamlit!  
Este proyecto implementa una versión simplificada pero funcional de Pac-Man directamente en una aplicación web interactiva, usando solo Python y Streamlit.

---

## 🎮 Características

- Mapa con muros, puntos comestibles, Pac-Man y un fantasma.
- Sistema de puntaje (10 puntos por cada punto comido).
- Fantasma que persigue a Pac-Man.
- Colisiones: si el fantasma atrapa a Pac-Man, el juego termina.
- Botón para reiniciar la partida.
- Control por botones de dirección (⬆️⬇️⬅️➡️).
- Totalmente basado en texto, sin dependencias externas ni gráficos complejos.

---

## ⚙️ Tecnologías utilizadas

- [Streamlit](https://streamlit.io/) – Framework para construir apps web interactivas en Python.
- `numpy` – Para gestionar la matriz del tablero y las posiciones.

---

## 📦 Instalación

1. **Clona el repositorio:**
```bash
git clone https://github.com/tu_usuario/pacman-streamlit.git
cd pacman-streamlit
```


2. **Crea un entorno virtual (opcional pero recomendado): 

```bash
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

🚀 Ejecución de la app

Para lanzar el juego en tu navegador:
```bash
streamlit run pacman_app.py
```
Esto abrirá una ventana de tu navegador con la interfaz del juego.
¡Usa los botones de flechas para mover a Pac-Man y trata de evitar al fantasma!
