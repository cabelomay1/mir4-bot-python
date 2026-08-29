import cv2
import numpy as np
from PIL import ImageGrab
import logging

logger = logging.getLogger('MIR4_BOT')

class BotDetection:
    """
    Classe responsável pela detecção de elementos na tela.
    """
    
    def __init__(self, debug_mode=False):
        """
        Inicializa o detector.
        
        Args:
            debug_mode (bool): Se True, salva screenshots para debug
        """
        self.debug_mode = debug_mode
        self.screenshot_counter = 0
    
    def capturar_tela(self):
        """
        Captura a tela atual.
        
        Returns:
            np.ndarray: Imagem da tela em formato BGR
        """
        try:
            # Capturar tela
            screenshot = ImageGrab.grab()
            
            # Converter para formato OpenCV (BGR)
            imagem = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            
            if self.debug_mode:
                self._salvar_screenshot(imagem)
            
            return imagem
        except Exception as e:
            logger.error(f"Erro ao capturar tela: {e}")
            return None
    
    def detectar_botao_missao_principal(self, imagem):
        """
        Detecta o botão de "Missão Principal" na tela.
        
        Args:
            imagem (np.ndarray): Imagem capturada da tela
        
        Returns:
            tuple: (encontrado: bool, posicao: (x, y)) ou (False, None)
        """
        try:
            if imagem is None:
                return False, None
            
            # Converter para escala de cinza
            cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            
            # Aplicar blur para reduzir ruído
            blur = cv2.GaussianBlur(cinza, (5, 5), 0)
            
            # Threshold para encontrar áreas claras (botões geralmente são)
            _, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
            
            # Encontrar contornos
            contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            # Procurar por um retângulo que pareça um botão
            for contorno in contornos:
                x, y, w, h = cv2.boundingRect(contorno)
                
                # Filtrar por tamanho (botão deve ter tamanho mínimo)
                if 50 < w < 300 and 30 < h < 100:
                    # Retorna o centro do botão
                    centro_x = x + w // 2
                    centro_y = y + h // 2
                    
                    logger.debug(f"Botão detectado em ({centro_x}, {centro_y})")
                    return True, (centro_x, centro_y)
            
            return False, None
        
        except Exception as e:
            logger.error(f"Erro ao detectar botão: {e}")
            return False, None
    
    def detectar_progresso_missao(self, imagem):
        """
        Detecta se uma missão está em progresso.
        
        Args:
            imagem (np.ndarray): Imagem capturada da tela
        
        Returns:
            bool: True se uma missão está em progresso
        """
        try:
            if imagem is None:
                return False
            
            # Procurar por cores específicas que indicam progresso
            # (Este é um exemplo básico - você pode melhorar)
            
            cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(cinza, 150, 255, cv2.THRESH_BINARY)
            
            # Se houver muita atividade na tela, assumir que há uma missão em progresso
            pixels_ativos = cv2.countNonZero(thresh)
            
            return pixels_ativos > 10000
        
        except Exception as e:
            logger.error(f"Erro ao detectar progresso: {e}")
            return False
    
    def _salvar_screenshot(self, imagem):
        """
        Salva screenshot para debug.
        
        Args:
            imagem (np.ndarray): Imagem a ser salva
        """
        import os
        
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')
        
        filename = f'screenshots/screenshot_{self.screenshot_counter:04d}.png'
        cv2.imwrite(filename, imagem)
        self.screenshot_counter += 1
        logger.debug(f"Screenshot salvo: {filename}")