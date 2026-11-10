# Automação para Reinicialização de Roteador ZTE / Claro

Este projeto contém uma automação em Python utilizando **Selenium WebDriver** para acessar a interface web do roteador (IP `192.168.0.1`) e solicitar a reinicialização remota.

## 🚀 Funcionalidades

- Autenticação automática via interface Web.
- Tratamento de alertas de certificado SSL.
- Navegação até o menu de diagnósticos e confirmação de reboot.
- Suporte a execução oculta (*headless*).
- Leitura de credenciais de forma segura usando variáveis de ambiente (`.env`).

## 🛠️ Pré-requisitos

- Python 3.x
- Google Chrome instalado

## 📦 Instalação e Configuração

1. Clone o repositório:
   ```bash
   git clone [https://github.com/httpsmaxwell/Reinicializador-roteador-instantaneo.git](https://github.com/seu-usuario/Reinicializador-roteador-instantaneo.git)
   cd nome-do-repositorio