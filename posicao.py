import pyautogui

# alteração no script para capturar a diversas posições de uma vez só

posicoes = []

print("Posicione o cursor e pressione Enter para capturar.")
print("Digite 'sair' e pressione Enter para encerrar.\n")

while True:
    comando = input("Pressione Enter para capturar ou digite 'sair': ")
    if comando.lower() == 'sair':
        break
    x, y = pyautogui.position()
    posicoes.append((x, y))
    print(f"Capturado: X={x}, Y={y}")

print("\nCoordenadas capturadas:")
for i, (x, y) in enumerate(posicoes, start=1):
    print(f"{i}: X={x}, Y={y}")


