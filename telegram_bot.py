from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import configparser

# アクセストークンは定義ファイルから読み込む
CONFIG = configparser.ConfigParser()
CONFIG_PATH = '../ini/python_telegram_config.ini'

class TelegramBot:
    def __init__(self, system):
        self.system = system
        CONFIG.read(CONFIG_PATH, encoding='utf-8')
    
    def start(self, bot, update):
        # inputにユーザIDを設定
        input = {'utt': None, 'sessionId': str(update.message.from_user.id)}

        # システムからの最初の発話をinitial_messageから取得し、送信
        update.message.reply_text(self.system.initial_message(input)["utt"])

    def message(self, bot, update):
        # inputにユーザからの発話とユーザIDを設定
        input = {'utt': update.message.text, 'sessionId': str(update.message.from_user.id)}

        # replyメソッドによりinputから発話
        system_output = self.system.reply(input)
        update.message.reply_text(system_output["utt"])

    def run(self):
        updater = Updater(CONFIG['SETTINGS']['Token'])
        db = updater.dispatcher
        db.add_handler(CommandHandler("start", self.start))
        db.add_handler(MessageHandler(Filters.text, self.message))
        updater.start_polling()
        updater.idle()
