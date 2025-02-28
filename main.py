import discord
import random
import threading
from discord.ext import commands
from flask import Flask

# Archivo donde están las cuentas
file_path = "filtered_accounts_corrected.txt"

# Configurar el bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

# Función para cargar las cuentas
def cargar_cuentas():
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

# Función para guardar la lista actualizada
def guardar_cuentas(cuentas):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n".join(cuentas))

# Función para obtener una cuenta aleatoria
def obtener_cuenta():
    cuentas = cargar_cuentas()

    if not cuentas:
        return "❌ No quedan más cuentas en la lista."

    cuenta = random.choice(cuentas)
    cuentas.remove(cuenta)  # Eliminar la cuenta elegida
    guardar_cuentas(cuentas)  # Guardar la lista sin esa cuenta

    return f"# 🎲 Cuenta generada: ||{cuenta}||"

# Comando para generar una cuenta
@bot.command()
async def generar(ctx):
    cuenta = obtener_cuenta()
    await ctx.send(cuenta)

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

# ----------------------
#   KEEP ALIVE SYSTEM
# ----------------------

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=3000)

def keep_alive():
    server = threading.Thread(target=run)
    server.start()

# Mantener el bot vivo
keep_alive()

# Iniciar el bot (reemplaza con tu token)
bot.run("MTIzMDE3NTk5MzY1MDQ3OTE5Ng.GYDuDE.sOl55bsS4ZRRDnIEHF_ORab45nHK7FrTXYNlMo")
