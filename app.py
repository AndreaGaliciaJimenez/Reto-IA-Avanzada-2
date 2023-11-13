import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import replicate
import random

# Función para inicializar el modelo
def init_model():
    model_id = "proximasanfinetuning/luna-diffusion-v2.5"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe.to("cuda")
    return pipe

# Streamlit UI
def main():
    st.title("Generador de Imágenes Promocionales")

    # Entrada de datos del usuario
    products = st.text_input("Producto", "Coca-cola bottle")
    style = st.text_input("Estilo", "announcement")
    background = st.text_input("Fondo", "Mexican kitchen")
    additional = st.text_input("Elementos adicionales", "Fresh, summer")
    num_images = st.number_input("Número de imágenes", min_value=1, max_value=10, value=1)

    # Botón para generar imágenes
    if st.button("Generar Imágenes"):
        with st.spinner("Generando..."):
            # Aquí va la lógica para generar las imágenes
            pipe = init_model()
            prompt = f"A {products} promotional with {style} style. {background} as background. Additional elements: {additional}"
            for i in range(num_images):
                h = random.randint(64, 128)
                w = random.randint(64, 128)
                image = pipe(prompt, height=8*h, width=8*w).images[0]
                st.image(image)

if __name__ == "__main__":
    main()
