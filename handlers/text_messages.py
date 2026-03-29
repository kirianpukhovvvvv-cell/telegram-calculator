from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN
from handlers.commands import start_command, help_command, convert_command
from handlers.text_messages import handle_message

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Регистрируем обработчики команд
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("convert", convert_command))

    # Регистрируем обработчик текстовых сообщений (все остальные сообщения)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
