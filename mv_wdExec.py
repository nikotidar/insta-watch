from os import name, getlogin, sep
from shutil import move
from os.path import  abspath, isfile, dirname, realpath
from insta_watch import GetWebdriver


supportedWebdrivers = GetWebdriver().supportedDrivers()
wdExecDestPath = f'{dirname(realpath(__file__))}'
if name == 'nt':
    downloadsPath = f'{abspath(sep)}Users\\{getlogin()}\\Downloads'
    try:
        for i in range(0, len(supportedWebdrivers)):
            wdExecOriginPath = isfile(f'{downloadsPath}\\{supportedWebdrivers[i]}')
            if isfile(wdExecOriginPath):
                move(wdExecOriginPath, wdExecDestPath)
                print(f'\n// "{supportedWebdrivers[i]}" moved to the project\'s root folder.')
                break
    except:
        print('\n// Webdriver executable not found!')
else:
    downloadsPath = f'/home/{getlogin()}/Downloads'
    try:
        for i in range(0, len(supportedWebdrivers)):
            wdExecOriginPath = f'{downloadsPath}/{supportedWebdrivers[i]}'
            if isfile(wdExecOriginPath):
                move(wdExecOriginPath, wdExecDestPath)
                print(f'\n// "{supportedWebdrivers[i]}" moved to the project\'s root folder.')
                break
    except:
        print('\n// Webdriver executable not found!')
