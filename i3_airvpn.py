from time import time
from airvpn import airvpn

class Py3status:
    cache_timeout = 10
    def __init__(self):
        pass
    def kill(self, i3s_output_list, i3s_config):
        pass
    def on_click(self, i3s_output_list, i3s_config, event):
        pass
    def format_arivpn(self, i3s_output_list, i3s_config):
        response = {
                'cached_until': time() + self.cache_timeout,
                'full_text': airvpn("a1fbb4df01cbc3888219ad354358318c0d1a677d")
                }
        return response

if __name__ == "__main__":
    from time import sleep
    x = Py3status()
    config = {
            'color_bad': '#FF0000',
            'color_degraded': '#FFFF00',
            'color_good': '#00FF00'
            }
    while True:
        print(x.format_airvpn([], config))
        sleep(1)