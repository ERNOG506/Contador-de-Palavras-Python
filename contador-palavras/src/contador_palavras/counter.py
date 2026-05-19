import re
from pathlib import Path


PADRAO_PALAVRA = re.compile(r"\b[\wÀ-ÿ]+(?:[-'][\wÀ-ÿ]+)?\b", re.UNICODE)


def contar_palavras(texto: str) -> int:
    """Conta palavras em um texto, ignorando pontuacao solta."""
    return len(PADRAO_PALAVRA.findall(texto))


def contar_palavras_em_arquivo(caminho_arquivo: str | Path) -> int:
    caminho = Path(caminho_arquivo)

    if not caminho.exists():
        raise FileNotFoundError("Arquivo nao encontrado.")

    if not caminho.is_file():
        raise ValueError("O caminho informado nao e um arquivo.")

    conteudo = caminho.read_text(encoding="utf-8")
    return contar_palavras(conteudo)
