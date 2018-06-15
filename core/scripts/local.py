import subprocess

if __name__ == "__main__":
    result = subprocess.check_output('python core/scripts/base.py', shell=True)
    print(result.decode())
    result = subprocess.check_output('echo $SHELL', shell=True)
    print(result.decode())

    if 'zsh' in result.decode():
        subprocess.check_output('echo "export DJANGO_SETTINGS_MODULE=core.settings.local" >> ~/.zshrc', shell=True)
        subprocess.check_output('export DJANGO_SETTINGS_MODULE=core.settings.local', shell=True)
    elif 'bash' in result.decode():
        subprocess.check_output('echo "export DJANGO_SETTINGS_MODULE=core.settings.local" >> ~/.bashrc', shell=True)
        subprocess.check_output('export DJANGO_SETTINGS_MODULE=core.settings.local', shell=True)

