import requests
import tkinter as tk
from tkinter import ttk

moedas = [
    "<USD-BRL>Dólar Americano/Real Brasileiro",
    "<USD-BRLT>Dólar Americano/Real Brasileiro Turismo",
    "<CAD-BRL>Dólar Canadense/Real Brasileiro",
    "<EUR-BRL>Euro/Real Brasileiro",
    "<GBP-BRL>Libra Esterlina/Real Brasileiro",
    "<ARS-BRL>Peso Argentino/Real Brasileiro",
    "<BTC-BRL>Bitcoin/Real Brasileiro",
    "<LTC-BRL>Litecoin/Real Brasileiro",
    "<JPY-BRL>Iene Japonês/Real Brasileiro",
    "<CHF-BRL>Franco Suíço/Real Brasileiro",
    "<AUD-BRL>Dólar Australiano/Real Brasileiro",
    "<CNY-BRL>Yuan Chinês/Real Brasileiro",
    "<ILS-BRL>Novo Shekel Israelense/Real Brasileiro",
    "<ETH-BRL>Ethereum/Real Brasileiro",
    "<XRP-BRL>XRP/Real Brasileiro",
    "<DOGE-BRL>Dogecoin/Real Brasileiro",
]

def chamar_endpoint(moeda1, valor_secundario_moeda1, valor):
    url = "https://economia.awesomeapi.com.br/json/last/"
    response = requests.get(url + moeda1)
    data = response.json()

    bid = float(data[moeda1 + valor_secundario_moeda1]["bid"])
    resultado = bid * int(valor)
    label_resultado.config(text=f"Resultado: {resultado:.2f}")

def converter():
    moeda1 = var_opcao.get()
    valor = campo_numero.get()
    valor_temp_moeda1 = moeda1[moeda1.find("<") + 1:moeda1.find(">")]
    valor_moeda1, valor_secundario_moeda1 = valor_temp_moeda1.split("-")
    print(valor_moeda1, valor_secundario_moeda1)
    chamar_endpoint(valor_moeda1, valor_secundario_moeda1, valor)


root =tk.Tk()
root.title("Convertor de moeda")

var_opcao = tk.StringVar(root)
var_opcao.set(moedas[0])

menu_opcao = ttk.OptionMenu(root, var_opcao, *moedas)
menu_opcao.pack(pady=10)

campo_numero = ttk.Entry(root, validate="key")
campo_numero.pack(pady=10)

botao = ttk.Button(root, text="Converter", command=converter)
botao.pack(pady=5)

label_resultado = ttk.Label( root, text="Resultado: ")
label_resultado.pack(pady=10)

root.mainloop()