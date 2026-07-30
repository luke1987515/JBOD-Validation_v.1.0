from django.apps import AppConfig


class FirmwareConfig(AppConfig):
    """
    韌體應用程式設定類別：用於定義與初始化 firmware 應用程式的配置。
    Firmware Application Configuration: Defines and initializes configurations for the firmware app.
    """

    # 應用程式的全名（PyPI 或 Python 套件路徑） / Full Python path to the application
    name = 'firmware'