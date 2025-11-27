from config import settings
import platform
import sys

def create_allure_environment_file():

    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    properties = '\n'.join(items)
    properties += '\n'+f'os_info={platform.system()}, {platform.release()}'
    properties += '\n'+f'python_version={sys.version}'


    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)