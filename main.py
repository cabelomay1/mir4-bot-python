#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MIR4 Bot - Automação de Missões Principais

Este é o arquivo principal do bot. Execute este arquivo para iniciar o bot.

Uso:
    python main.py

Controles:
    - ESC: Para o bot imediatamente

Aviso:
    Este bot é apenas para fins educacionais. Verifique os Termos de Serviço
    do MIR4 antes de usar. O desenvolvedor não se responsabiliza por banimentos.
"""

import json
import time
import os
from bot.logger import setup_logger
from bot.automation import BotAutomation
from bot.detection import BotDetection

def carregar_configuracao():
    """
    Carrega o arquivo de configuração config.json.
    
    Returns:
        dict: Configuração do bot
    """
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Erro: Arquivo config.json não encontrado!")
        exit(1)
    except json.JSONDecodeError:
        print("Erro: config.json não é um JSON válido!")
        exit(1)

def exibir_banner():
    """
    Exibe o banner do bot.
    """
    banner = """
    ╔════════════════════════════════════════════════════════╗
    ║           🎮 MIR4 BOT - MISSÕES AUTOMÁTICAS 🎮         ║
    ║                  v1.0.0 - by cabelomay1               ║
    ╚════════════════════════════════════════════════════════╝
    
    ⚠️  AVISO: Verifique os Termos de Serviço do MIR4!
    ⚠️  O bot pode resultar em ban da sua conta!
    
    Pressione CTRL+C ou ESC para parar o bot.
    
    """
    print(banner)

def executar_bot():
    """
    Executa o loop principal do bot.
    """
    
    # Exibir banner
    exibir_banner()
    
    # Carregar configuração
    print("[*] Carregando configuração...")
    config = carregar_configuracao()
    
    # Configurar logger
    debug_mode = config.get('modo_debug', True)
    logger = setup_logger(debug_mode)
    logger.info("=" * 60)
    logger.info("MIR4 BOT INICIADO")
    logger.info("=" * 60)
    
    # Inicializar componentes
    print("[*] Inicializando componentes...")
    bot = BotAutomation(config)
    detector = BotDetection(debug_mode=debug_mode)
    
    print("[*] Bot pronto! Iniciando em 5 segundos...")
    print("[*] Posicione a janela do MIR4 em foco.")
    
    # Aguardar 5 segundos antes de iniciar
    for i in range(5, 0, -1):
        print(f"[*] Iniciando em {i}...")
        time.sleep(1)
    
    bot.iniciar()
    logger.info("Bot iniciado - Começando a executar")
    
    # Variáveis de controle
    missoes_completadas = 0
    tempo_inicio = time.time()
    
    try:
        # Loop principal
        while bot.esta_ativo():
            try:
                # Capturar tela
                imagem = detector.capturar_tela()
                if imagem is None:
                    time.sleep(1)
                    continue
                
                # Detectar botão de missão principal
                encontrado, posicao = detector.detectar_botao_missao_principal(imagem)
                
                if encontrado and posicao:
                    logger.info(f"Botão de missão encontrado em {posicao}")
                    print(f"[✓] Missão principal detectada! Clicando...")
                    
                    # Clicar no botão
                    bot.clicar(posicao[0], posicao[1])
                    
                    # Aguardar a missão ser processada
                    tempo_espera = config.get('delay_entre_missoes', 5)
                    logger.info(f"Aguardando {tempo_espera}s até a próxima verificação")
                    
                    bot.aguardar(tempo_espera)
                    missoes_completadas += 1
                    print(f"[✓] Missões completadas: {missoes_completadas}")
                    
                    # Verificar se precisa fazer uma pausa
                    pausa_a_cada = config.get('numero_missoes_antes_pausa', 10)
                    if missoes_completadas % pausa_a_cada == 0:
                        tempo_pausa = config.get('tempo_pausa_minutos', 5)
                        print(f"[*] Fazendo pausa de {tempo_pausa} minutos...")
                        logger.info(f"Pausa programada por {tempo_pausa} minutos")
                        bot.aguardar(tempo_pausa * 60)
                else:
                    # Não encontrou o botão, aguardar e tentar novamente
                    intervalo = config.get('intervalo_verificacao', 2)
                    time.sleep(intervalo)
            
            except Exception as e:
                logger.error(f"Erro no loop principal: {e}")
                time.sleep(1)
    
    except KeyboardInterrupt:
        logger.info("Bot interrompido pelo usuário (Ctrl+C)")
        print("\n[!] Bot interrompido!")
    
    finally:
        # Finalizar
        bot.parar()
        tempo_total = time.time() - tempo_inicio
        
        logger.info("=" * 60)
        logger.info(f"Bot finalizado após {tempo_total:.2f} segundos")
        logger.info(f"Missões completadas: {missoes_completadas}")
        logger.info("=" * 60)
        
        print(f"\n[!] Bot finalizado!")
        print(f"[!] Missões completadas: {missoes_completadas}")
        print(f"[!] Tempo total: {tempo_total:.2f} segundos")

if __name__ == "__main__":
    try:
        executar_bot()
    except Exception as e:
        print(f"Erro fatal: {e}")
        exit(1)