# DownSort

Organizador de pasta Downloads com interface gráfica.

## Objetivo

DownSort organiza automaticamente a pasta de Downloads separando os arquivos em subpastas por extensão.

## Como usar

1. Baixe o `DownSort.exe` nas [Releases](https://github.com/Anthonyysm/DownSort/releases) ou gere-o localmente (na pasta `dist/`).
2. Execute `DownSort.exe`.
3. Selecione a pasta que deseja organizar (padrão: `C:\Users\<SeuNome>\Downloads`).
4. Clique em "Organizar agora".

Os arquivos serão movidos para pastas como `pdf/`, `jpg/`, `mp3/`, `zip/`, etc. Arquivos sem extensão vão para `sem_extensao/`.

## Compilar o executável manualmente

Requisitos: Python 3.13+ com PyInstaller.

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name DownSort down_sort_gui.py
```

O executável será gerado em `dist/DownSort.exe`.

## Detalhes

- Interface gráfica (Tkinter)
- Não sobrescreve arquivos: adiciona `(1)`, `(2)`, ... se o destino já existir
- Ignora subpastas (apenas arquivos)
- Extensões convertidas para minúsculas
- Baseado em `down_sort_gui.py`
