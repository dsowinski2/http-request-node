from PIL import Image, ImageOps
from io import BytesIO
import numpy as np
import requests
import time


class SendHttpRequest:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"token": ("STRING", ),
                              "url": ("STRING", ),
                             },
               
                }

    RETURN_TYPES = ()
    FUNCTION = "send_request"

    OUTPUT_NODE = True

    CATEGORY = "api"

    def send_request(self, url, token):
        requests.get(url)
        return {}

    def IS_CHANGED(s, images):
        return time.time()

NODE_CLASS_MAPPINGS = {
    "Send Http Request": SendHttpRequest,
}
