import io
import os
import time
import pathlib
import logging
from typing import List

import requests
import streamlit as st
from PIL import Image
import replicate

from config_token import V_REPLICATE

logging.basicConfig(level=logging.INFO)

st.set_page_config(page_title="Text-to-Image com Replicate", page_icon="🖼️")
st.title("🖼️ Geração de Imagens a partir de Texto (Replicate)")
st.caption("App didático com parâmetros essenciais (texto, itens a evitar, steps, guidance, tamanho, seed).")

if not V_REPLICATE:
    st.error("Defina REPLICATE_API_TOKEN no arquivo .env para continuar.")
    st.stop()

OUTPUT_DIR = pathlib.Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def save_bytes_as_png(image_bytes: bytes, prefix: str = "img") -> str:
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    fname = f"{prefix}_{int(time.time() * 1000)}.png"
    outpath = OUTPUT_DIR / fname
    img.save(outpath)
    return str(outpath)


def grid_show(png_paths: List[str]):
    cols = st.columns(min(4, max(1, len(png_paths))))
    for i, p in enumerate(png_paths):
        with cols[i % len(cols)]:
            st.image(p, use_column_width=True)
            with open(p, "rb") as f:
                st.download_button(
                    "⬇️ Baixar",
                    data=f.read(),
                    file_name=os.path.basename(p),
                    mime="image/png"
                )


def run_replicate(model_slug: str, input_dict: dict, client: replicate.Client) -> List[str]:
    try:
        model = client.models.get(model_slug)
        version = model.versions.list()[0]
        full_slug = f"{model_slug}:{version.id}"
    except Exception as e:
        logging.warning(
            f"Não foi possível obter a versão mais recente do modelo '{model_slug}'. "
            f"Tentando slug simples. Detalhes: {e}"
        )
        full_slug = model_slug

    st.info(f"Executando modelo: `{full_slug}` com inputs: `{list(input_dict.keys())}`")

    output = client.run(full_slug, input=input_dict)

    png_paths = []
    for i, item in enumerate(output):
        if isinstance(item, (bytes, bytearray)):
            path = save_bytes_as_png(item, prefix=f"gen_{i}")
        else:
            url = str(item)
            resp = requests.get(url, timeout=60)
            resp.raise_for_status()
            path = save_bytes_as_png(resp.content, prefix=f"gen_{i}")
        png_paths.append(path)

    return png_paths


with st.sidebar:
    st.header("⚙️ Parâmetros de geração")

    text_description = st.text_area(
        "Texto descritivo (o que você quer gerar)",
        "A cozy reading nook, warm light, pastel colors, ultra-detailed, 4k",
        height=120
    )

    avoid_text = st.text_input(
        "Texto do que evitar (itens indesejados)",
        "blurry, low quality, watermark, text"
    )

    num_outputs = st.slider("Quantidade de imagens", 1, 4, 2)
    width = st.selectbox("Largura", [512, 768, 1024], index=0)
    height = st.selectbox("Altura", [512, 768, 1024], index=0)
    steps = st.slider("Passos (inference steps)", 10, 60, 30)
    guidance = st.slider("Guidance/CFG (força do texto)", 1.0, 15.0, 7.5, 0.5)
    seed = st.number_input("Seed (-1 para aleatório)", value=42)

    st.markdown("---")
    st.caption("Dica: steps e resolução mais altos aumentam tempo/custo, mas tendem a melhorar detalhes.")

st.subheader("Modelo a usar (Replicate)")
model_slug = st.selectbox(
    "Selecione o modelo",
    [
        "stability-ai/stable-diffusion",
        "cjwbw/anything-v4",
        "black-forest-labs/flux-dev",
    ],
    index=0
)

if st.button("Gerar imagens", type="primary", use_container_width=True):
    if not text_description.strip():
        st.warning("Informe um texto descritivo.")
        st.stop()

    client = replicate.Client(api_token=V_REPLICATE)

    replicate_input = {
        "prompt": text_description,
        "negative_prompt": avoid_text or None,
        "width": width,
        "height": height,
        "num_inference_steps": steps,
        "guidance_scale": guidance,
        "num_outputs": num_outputs,
        "seed": None if seed < 0 else int(seed),
    }

    with st.spinner("Gerando... isso pode levar alguns segundos ⏳"):
        try:
            png_paths = run_replicate(model_slug, replicate_input, client)
            st.success("Imagens geradas com sucesso!")
            st.subheader("Resultados")
            grid_show(png_paths)
        except Exception as e:
            st.error(f"Falha ao gerar imagens: {e}")
            with st.expander("Detalhes do erro"):
                st.exception(e)