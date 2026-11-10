# Reiniciador Instantâneo de Roteador

Este projeto contém uma automação em Python utilizando **Selenium WebDriver** para acessar a interface web do roteador ZTE / Claro (IP `192.168.0.1`) e solicitar a reinicialização remota de forma automática.

## 🚀 Funcionalidades

- Autenticação automática na interface Web do roteador.
- Tratamento automático de alertas de certificado SSL.
- Navegação direta até o menu de diagnósticos e confirmação de reboot.
- Execução oculta (*headless*) sem abrir a janela do navegador.
- Gerenciamento seguro de credenciais via variáveis de ambiente (`.env`).
- Suporte para compilação em executável único (`.exe`) via PyInstaller.

## 🛠️ Pré-requisitos

- **Python 3.x** instalado.
- **Google Chrome** instalado.
- Dependências listadas no `requirements.txt`.

## 📦 Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/httpsmaxwell/reiniciador-instantaneo-de-roteador.git](https://github.com/httpsmaxwell/reiniciador-instantaneo-de-roteador.git)
   cd reiniciador-instantaneo-de-roteador