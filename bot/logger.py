import logging
import os
from datetime import datetime

def setup_logger(debug_mode=True):
    """
    Configura o sistema de logs do bot.
    
    Args:
        debug_mode (bool): Se True, mostra logs DEBUG também
    
    Returns:
        logging.Logger: Logger configurado
    """
    
    # Criar diretório de logs se não existir
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Nome do arquivo de log com data/hora
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = f'logs/mir4_bot_{timestamp}.log'
    
    # Configurar logger
    logger = logging.getLogger('MIR4_BOT')
    level = logging.DEBUG if debug_mode else logging.INFO
    logger.setLevel(level)
    
    # Handler para arquivo
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    
    # Handler para console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    
    # Formato das mensagens
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger