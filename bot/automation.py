import pyautogui
import time
import logging
from threading import Thread
from pynput import keyboard

logger = logging.getLogger('MIR4_BOT')

class BotAutomation:
    """
    Classe responsável pela automação de cliques e ações no bot.
    """
    
    def __init__(self, config):
        """
        Inicializa a automação.
        
        Args:
            config (dict): Configuração do bot carregada de config.json
        """
        self.config = config
        self.ativo = False
        self.pausado = False
        
        # Configurar listener para ESC
        self._configurar_listener_teclado()
        
        # Desabilitar failsafe do pyautogui (você consegue pará-lo com ESC)
        pyautogui.FAILSAFE = False
    
    def _configurar_listener_teclado(self):
        """
        Configura listener para o botão ESC parar o bot.
        """
        def on_press(key):
            try:
                if key == keyboard.Key.esc:
                    logger.info("ESC pressionado - Parando bot...")
                    self.parar()
            except AttributeError:
                pass
        
        # Iniciar listener em thread separada
        listener = keyboard.Listener(on_press=on_press)
        listener.daemon = True
        listener.start()
    
    def clicar(self, x, y, delay=None):
        """
        Realiza um clique na posição especificada.
        
        Args:
            x (int): Coordenada X
            y (int): Coordenada Y
            delay (float): Delay antes do clique em segundos
        """
        try:
            if delay:
                time.sleep(delay)
            
            velocidade = self.config.get('velocidade_clique', 0.5)
            
            logger.debug(f"Clicando em ({x}, {y})")
            pyautogui.click(x, y, duration=velocidade)
            
            # Aguardar um pouco após o clique
            time.sleep(0.2)
        
        except Exception as e:
            logger.error(f"Erro ao clicar em ({x}, {y}): {e}")
    
    def mover_mouse(self, x, y):
        """
        Move o mouse para uma posição.
        
        Args:
            x (int): Coordenada X
            y (int): Coordenada Y
        """
        try:
            logger.debug(f"Movendo mouse para ({x}, {y})")
            pyautogui.moveTo(x, y, duration=0.3)
        
        except Exception as e:
            logger.error(f"Erro ao mover mouse: {e}")
    
    def pressionar_tecla(self, tecla):
        """
        Pressiona uma tecla.
        
        Args:
            tecla (str): Nome da tecla a pressionar
        """
        try:
            logger.debug(f"Pressionando tecla: {tecla}")
            pyautogui.press(tecla)
            time.sleep(0.1)
        
        except Exception as e:
            logger.error(f"Erro ao pressionar tecla: {e}")
    
    def digitar_texto(self, texto):
        """
        Digita um texto.
        
        Args:
            texto (str): Texto a digitar
        """
        try:
            logger.debug(f"Digitando: {texto}")
            pyautogui.typewrite(texto, interval=0.05)
        
        except Exception as e:
            logger.error(f"Erro ao digitar: {e}")
    
    def aguardar(self, segundos):
        """
        Aguarda por um tempo determinado.
        
        Args:
            segundos (float): Tempo em segundos
        """
        logger.debug(f"Aguardando {segundos} segundos...")
        time.sleep(segundos)
    
    def iniciar(self):
        """
        Inicia o bot.
        """
        self.ativo = True
        logger.info("Bot iniciado")
    
    def parar(self):
        """
        Para o bot.
        """
        self.ativo = False
        logger.info("Bot parado")
    
    def pausar(self):
        """
        Pausa o bot (pode ser retomado).
        """
        self.pausado = True
        logger.info("Bot pausado")
    
    def retomar(self):
        """
        Retoma o bot do estado pausado.
        """
        self.pausado = False
        logger.info("Bot retomado")
    
    def esta_ativo(self):
        """
        Verifica se o bot está ativo.
        
        Returns:
            bool: True se ativo e não pausado
        """
        return self.ativo and not self.pausado