import sys
import tempfile
import unittest
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT_DIR / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from contador_palavras.counter import contar_palavras, contar_palavras_em_arquivo


class ContadorPalavrasTestCase(unittest.TestCase):
    def test_conta_palavras_de_uma_frase(self):
        frase = "Bem, e so mais um dia para eu ser um profissional em programacao."

        quantidade = contar_palavras(frase)

        self.assertEqual(quantidade, 13)

    def test_ignora_pontuacao_solta(self):
        frase = "Python, testes e GitHub: portfolio profissional!"

        quantidade = contar_palavras(frase)

        self.assertEqual(quantidade, 6)

    def test_conta_palavras_em_arquivo(self):
        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "texto.txt"
            caminho.write_text("Aprender Python abre muitas oportunidades.", encoding="utf-8")

            quantidade = contar_palavras_em_arquivo(caminho)

        self.assertEqual(quantidade, 5)


if __name__ == "__main__":
    unittest.main()
