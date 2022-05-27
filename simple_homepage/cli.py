from pkg_resources import resource_string

def main():
    print('hello')
    template_dir = resource_string(__name__, 'template')
    settings = resource_string(__name__, 'settings.yaml')
    print('done')