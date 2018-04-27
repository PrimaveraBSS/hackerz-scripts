# hackerz-scripts

I do not work for Primavera anymore, contact me via [private email](mailto:prodrigues1990@gmail.com) or via any of the GitHub
options. 

## time-report (alpha)
Faz o report de horas automaticamente no portal do IM

### requerimentos
* [python 3.5.1 ou superior](https://www.python.org/downloads/)
* [caminho para python.exe na variavel PATH](http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7)
* [Selenium python package](http://selenium-python.readthedocs.org/installation.html)
* [Selenium Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* [Chrome Browser](https://www.google.com/chrome/browser/desktop/)

### como usar
* pela linha de comandos, navega até à pasta onde está o ficheiro `time-report.py`
* executa o comando `time-report-activity-list.py`, introduzir o username e password para o IM conforme pedido pela linha de comandos, deve ser criado um ficheiro `time-report-activity-list.json` com uma lista de projectos e actividades disponíveis na tua conta
* deves alterar os dados exemplo que estão no ficheiro `time-report.json` com os dados que queres colocar no IM
* executa o comando `time-report.py`, introduz o username e password para o IM conforme pedido pela linha de comandos
* enjoy :)

### contribui
Vais precisar:
* [git](https://git-scm.com/)
* IDLE (incluído com as distribuições de python)
* + os requerimentos para executar
* envia um patch para o mail [pedro.rodrigues@primaverabss.com](mailto:pedro.rodrigues@primaverabss.com), ou um pull request em [GitHub](https://github.com/PrimaveraBSS/hackerz-scripts)
