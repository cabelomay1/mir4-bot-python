# Pacote do MIR4 Bot

__version__ = "1.0.0"
__author__ = "cabelomay1"

from bot.automation import BotAutomation
from bot.detection import BotDetection
from bot.logger import setup_logger

__all__ = ['BotAutomation', 'BotDetection', 'setup_logger']