import streamlit as st
import numpy as np
import random

st.set_page_config(page_title="Pac-Man Completo", layout="centered")
st.title("🟡 Pac-Man en Streamlit (versión avanzada)")

ROWS, COLS = 10, 15

def inicializar_tablero():
    board = np.full((ROWS, COLS), ".", dtype=str)

    # Muros alrededor
    board[0, :] = "#"
    board[-1, :] = "#"
    board[:, 0] = "#"
    board[:, -1] = "#"

    # Muros internos
    for i in range(2, 8):
        board[i, 5] = "#"
        board[i, 9] = "#"

    # Posiciones iniciales
    pacman_pos = (1, 1)
    ghost_pos = (ROWS - 2, COLS - 2)

    board[pacman_pos] = "P"
    board[ghost_pos] = "G"

    return board, pacman_pos, ghost_pos, 0

# Inicialización
if "board" not in st.session_state:
    board, pacman_pos, ghost_pos, score = inicializar_tablero()
    st.session_state.board = board
    st.session_state.pacman_pos = pacman_pos
    st.session_state.ghost_pos = ghost_pos
    st.session_state.score = score
    st.session_state.game_over = False

# Mover Pac-Man
def mover_pacman(dx, dy):
    if st.session_state.game_over:
        return

    x, y = st.session_state.pacman_pos
    new_x, new_y = x + dx, y + dy

    if st.session_state.board[new_x][new_y] == "#":
        return

    # Comer punto
    if st.session_state.board[new_x][new_y] == ".":
        st.session_state.score += 10

    # Ver si choca con el fantasma
    if (new_x, new_y) == st.session_state.ghost_pos:
        st.session_state.game_over = True
        return

    st.session_state.board[x][y] = " "
    st.session_state.board[new_x][new_y] = "P"
    st.session_state.pacman_pos = (new_x, new_y)

    mover_fantasma()

# Movimiento simple del fantasma hacia Pac-Man
def mover_fantasma():
    if st.session_state.game_over:
        return

    gx, gy = st.session_state.ghost_pos
    px, py = st.session_state.pacman_pos

    options = []
    if px > gx:
        options.append((1, 0))
    if px < gx:
        options.append((-1, 0))
    if py > gy:
        options.append((0, 1))
    if py < gy:
        options.append((0, -1))

    random.shuffle(options)

    for dx, dy in options:
        new_x, new_y = gx + dx, gy + dy
        if st.session_state.board[new_x][new_y] not in ["#", "G"]:
            # Colisión con Pac-Man
            if (new_x, new_y) == st.session_state.pacman_pos:
                st.session_state.game_over = True
                return

            st.session_state.board[gx][gy] = " "
            st.session_state.board[new_x][new_y] = "G"
            st.session_state.ghost_pos = (new_x, new_y)
            break

# Dibujar tablero
def render_board():
    rendered = ""
    for row in st.session_state.board:
        rendered += "".join(row) + "\n"
    return rendered

# Mostrar tablero y puntaje
st.text(render_board())
st.markdown(f"**Puntaje:** {st.session_state.score}")

if st.session_state.game_over:
    st.error("👻 ¡Perdiste! Pac-Man fue atrapado por el fantasma.")
    if st.button("Reiniciar juego"):
        board, pacman_pos, ghost_pos, score = inicializar_tablero()
        st.session_state.board = board
        st.session_state.pacman_pos = pacman_pos
        st.session_state.ghost_pos = ghost_pos
        st.session_state.score = score
        st.session_state.game_over = False
    st.stop()

# Controles
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("⬆️"):
        mover_pacman(-1, 0)
with col1:
    if st.button("⬅️"):
        mover_pacman(0, -1)
with col3:
    if st.button("➡️"):
        mover_pacman(0, 1)
with col2:
    if st.button("⬇️"):
        mover_pacman(1, 0)
