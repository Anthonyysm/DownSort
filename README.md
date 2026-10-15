# DownSort

Organizador da pasta Downloads com interface gráfica.

## Funcionalidades

- Organiza arquivos automaticamente separando por extensão.
- Cria subpastas por tipo (ex.: `pdf/`, `jpg/`, `mp3/`, `zip/`).
- Arquivos sem extensão vão para `sem_extensao/`.
- Evita sobrescrita ao renomear com `(1)`, `(2)`, etc.
- Interface simples e prática.

## Download

Baixe a versão mais recente em [Releases](https://github.com/Anthonyysm/DownSort/releases). Basta baixar o `DownSort.exe` e executar.

## Como Usar

1. Baixe o arquivo executável (`DownSort.exe`) disponível nas Releases.
2. Execute o aplicativo.
3. Selecione a pasta que deseja organizar (padrão: `C:\Users\<SeuNome>\Downloads`).
4. Clique em "Organizar agora".

## Compilar manualmente

Requisitos: Python 3.13+ com PyInstaller.

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name DownSort --icon=icon.ico down_sort_gui.py
```

O executável será gerado em `dist/DownSort.exe`.