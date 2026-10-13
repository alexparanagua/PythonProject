import json
import replicate
from urllib.request import urlretrieve
from pathlib import Path
from config_token import V_REPLICATE
from config_token import V_MODELO_TO_AUDIO


def normalizar_output(output):
    if isinstance(output, list):
        for item in output:
            if isinstance(item, str) and item.startswith("http"):
                return item
        return "".join(str(x) for x in output)

    if isinstance(output, dict):
        for chave in ("audio", "output", "url"):
            if chave in output:
                return output[chave]
        return json.dumps(output, ensure_ascii=False)

    return output


def gerar_audio_e_salvar(texto: str, caminho_saida: str = "output.wav") -> Path:
    output = replicate.run(
        V_MODELO_TO_AUDIO,
        input={"prompt": texto, "max_new_tokens": 128, "temperature": 0.7}
    )

    resultado = normalizar_output(output)

    # Se for URL, baixa e salva
    if isinstance(resultado, str) and resultado.startswith("https"):
        out_path = Path(caminho_saida)
        urlretrieve(resultado, out_path)
        return out_path

    # Se não for URL, salva como texto (fallback), para não perder o resultado
    out_path = Path("resultado_rep.txt")
    out_path.write_text(str(resultado), encoding="utf-8")
    return out_path


if __name__ == "__main__":
    texto = "Olá! Esta é uma demonstração final de texto para voz no módulo 36."
    arquivo = gerar_audio_e_salvar(texto, "output.wav")
    print(f"Arquivo gerado/salvo em: {arquivo.resolve()}")