from environs import Env

env = Env()
env.read_env()

API_CAPTCHA = env.str("API_CAPTCHA")
