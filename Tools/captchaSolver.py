import os
from anticaptchaofficial.imagecaptcha import *
from Tools.data_config import API_CAPTCHA


def solver_captcha(link):
    link_image = requests.get(link)
    dowloaded_image = open('captcha.img', 'wb')
    dowloaded_image.write(link_image.content)
    dowloaded_image.close()
    solver = imagecaptcha()
    solver.set_verbose(1)
    solver.set_key(API_CAPTCHA)
    captcha_text = solver.solve_and_return_solution("captcha.img")
    os.remove("captcha.img")
    if captcha_text != 0:
        return captcha_text
    else:
        assert "task finished with error " + solver.error_code
