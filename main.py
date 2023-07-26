import pyautogui
import time
import pandas as pd

# pyautogui.write -> escrever
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(1)

# Fazer login
# selecionar o campo de email
pyautogui.click(x=923, y=360)
pyautogui.write("test@test.com")

# selecionar o campo de senha
pyautogui.click(x=813, y=457)
pyautogui.write("12345678")

# selecionar o campo de senha
pyautogui.click(x=913, y=519)

# Importar a base de produtos 
tabela = pd.read_csv("./produtos.csv")

total_registered = 0

# Cadastrar os produtos 
for row in tabela.index:
  # Selecionar o campo código do produto
  pyautogui.click(x=781, y=241)
  pyautogui.write(str(tabela.loc[row, "codigo"]))

  # Selecionar o campo marca do produto
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[row, "marca"]))

  # Selecionar o campo tipo do produto
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[row, "tipo"]))

  # Selecionar o campo categoria do produto
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[row, "categoria"]))

  # Selecionar o campo preço do produto
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[row, "preco_unitario"]))

  # Selecionar o campo custo do produto
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[row, "custo"]))

  # Selecionar o campo observação do produto
  pyautogui.press("tab")
  obs = tabela.loc[row, "obs"]

  if not pd.isna(obs):
    pyautogui.write(str(obs))
    
  # Clicar no botão enviar
  pyautogui.press("tab")
  pyautogui.press("enter")
  
  # usando o scroll para depois a posição do botão
  pyautogui.scroll(999999)
  pyautogui.click(x=860, y=908)
  
  total_registered = total_registered + 1
  
print(f"{total_registered} produtos cadastrados")