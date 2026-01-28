import gradio as gr

# Conectamos con el motor de generación más duro del momento (FLUX)
# Este motor no tiene marcas de agua y es nivel profesional
def generar_imagen(prompt):
    # Añadimos el "Vibe" de La Nave automáticamente al prompt del socio
    vibe_nvvex = ", professional photography, cinematic lighting, high resolution, 4k, neon green accents, urban style"
    try:
        # Aquí invocamos el motor externo para no usar recursos de su Mac
        client = gr.load("models/black-forest-labs/FLUX.1-schnell")
        return client.predict(prompt + vibe_nvvex, api_name="/predict")
    except Exception as e:
        return None

# Creamos la interfaz limpia que el Socio aprobó
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🛸 RADAR VISION - NVVEX STUDIOS")
    gr.Markdown("Escribe el nombre del artista o el tema y deja que La Nave fabrique la imagen.")
    
    with gr.Row():
        with gr.Column():
            entrada = gr.Textbox(label="¿Qué busca el Radar hoy?", placeholder="Ej: Bad Bunny en un búnker tecnológico...")
            boton = gr.Button("GENERAR IMAGEN 4K", variant="primary")
        with gr.Column():
            salida = gr.Image(label="Resultado NVVEX")

    boton.click(fn=generar_imagen, inputs=entrada, outputs=salida)

demo.launch()
