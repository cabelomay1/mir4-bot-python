# 🎮 MIR4 Bot - Automação de Missões Principais

Um bot automático para MIR4 que completa as missões principais automaticamente.

## ⚠️ AVISO IMPORTANTE

**Este projeto é apenas para fins educacionais!** Verifique os Termos de Serviço do MIR4 antes de usar. O desenvolvedor não se responsabiliza por banimentos ou problemas causados pelo uso deste bot.

## 📋 Requisitos

- Python 3.8 ou superior
- Windows 10/11
- MIR4 instalado e rodando
- Dependências Python (veja `requirements.txt`)

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/cabelomay1/mir4-bot-python.git
cd mir4-bot-python
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure o bot
Edite `config.json` com suas preferências

### 4. Execute o bot
```bash
python main.py
```

## 📁 Estrutura do Projeto

```
mir4-bot-python/
├── main.py              # Arquivo principal do bot
├── config.json          # Configurações do bot
├── requirements.txt     # Dependências Python
├── bot/
│   ├── __init__.py
│   ├── automation.py    # Funções de automação de tela
│   ├── detection.py     # Detecção de elementos na tela
│   └── logger.py        # Sistema de logs
└── README.md            # Este arquivo
```

## ⚙️ Como Funciona

1. **Detecção**: O bot procura pelo botão de "Missão Principal" na tela
2. **Clique**: Clica automaticamente no botão quando encontra
3. **Conclusão**: Aguarda a conclusão da missão
4. **Repetição**: Repete o processo

## 🎮 Controles

- **Atalho**: Pressione `ESC` a qualquer momento para parar o bot
- **Modo pausado**: O bot só funciona quando a janela do MIR4 está em foco

## 📝 Configuração (config.json)

```json
{
  "velocidade_clique": 0.5,
  "intervalo_verificacao": 2,
  "modo_debug": true,
  "tempo_maximo_missao": 300
}
```

## 🛠️ Troubleshooting

### O bot não detecta os botões
- Verifique se a resolução da tela é 1920x1080
- Tente capturar screenshots em `screenshots/` para debug

### O bot é lento
- Aumente o valor de `intervalo_verificacao` em `config.json`
- Reduza o valor de `velocidade_clique`

## 📚 Para Aprender Python

Recomendados:
- [Python.org Documentação](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)

## 🤝 Contribuindo

Sinta-se livre para fazer fork e enviar pull requests!

## 📄 Licença

MIT License - veja LICENSE para mais detalhes

---

**Desenvolvido por**: @cabelomay1
**Última atualização**: 2026-08-29