import streamlit as st
import numpy as np
from matplotlib.animation import FuncAnimation

import matplotlib.pyplot as plt

# Fungsi untuk animasi bunga mawar
def rose_animation():
    fig, ax = plt.subplots()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.axis('off')

    t = np.linspace(0, 2 * np.pi, 1000)
    x = np.sin(t) * np.cos(5 * t)
    y = np.sin(t) * np.sin(5 * t)
    line, = ax.plot([], [], lw=2, color='red')

    def update(frame):
        line.set_data(x[:frame], y[:frame])
        return line,

    ani = FuncAnimation(fig, update, frames=len(t), interval=20, blit=True)
    return ani

# Fungsi untuk animasi stick bergerak
def stick_animation():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    stick, = ax.plot([], [], lw=4, color='blue')

    def update(frame):
        x = [frame, frame + 1]
        y = [5, 5]
        stick.set_data(x, y)
        return stick,

    ani = FuncAnimation(fig, update, frames=np.arange(0, 9, 0.1), interval=50, blit=True)
    return ani

# Streamlit UI
st.title("Animasi Bunga Mawar dan Stick Bergerak")
option = st.selectbox("Pilih Animasi", ["Bunga Mawar", "Stick Bergerak"])

if option == "Bunga Mawar":
    st.write("Animasi Bunga Mawar Mekar")
    ani = rose_animation()
    ani.save("rose_animation.gif", writer="imagemagick")
    st.image("rose_animation.gif")
elif option == "Stick Bergerak":
    ani = stick_animation()
    ani.save("stick_animation.gif", writer="imagemagick")
    st.image("stick_animation.gif")
    st.pyplot(ani._fig)
    
    