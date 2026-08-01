from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "TOKENNI_BU_YERGA_QO'YING"

keyboard = [
    ["📚 Darslar", "📝 Testlar"],
    ["🛡 Kiberxavfsizlik", "🧑‍💻 Etik xakerlik"],
    ["🌐 Tarmoq xavfsizligi", "🔐 Parol xavfsizligi"],
    ["🐍 Python", "🐧 Linux"],
    ["💻 Kali Linux", "📡 Wi-Fi xavfsizligi"],
    ["🎣 Phishing", "🦠 Viruslar"],
    ["📞 Admin", "ℹ️ Bot haqida"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡 Kiberxavfsizlik botiga xush kelibsiz!\n\nKerakli bo'limni tanlang:",
        reply_markup=reply_markup
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚 Darslar":
        javob = "📚 Darslar:\n\n1. Kiberxavfsizlik asoslari\n2. Linux\n3. Python\n4. Tarmoq xavfsizligi"

    elif text == "📝 Testlar":
        javob = "📝 Testlar tez orada qo'shiladi."

    elif text == "🛡 Kiberxavfsizlik":
        javob = "🛡 Kiberxavfsizlik - axborotni himoya qilish fanidir."

    elif text == "🧑‍💻 Etik xakerlik":
        javob = "🧑‍💻 Etik xakerlik - tizimlarni egasining ruxsati bilan tekshirish."

    elif text == "🌐 Tarmoq xavfsizligi":
        javob = "🌐 Tarmoqni himoya qilish usullari haqida ma'lumot."

    elif text == "🔐 Parol xavfsizligi":
        javob = "🔐 Kuchli va noyob parollardan foydalaning."

    elif text == "🐍 Python":
        javob = "🐍 Python darslari."

    elif text == "🐧 Linux":
        javob = "🐧 Linux buyruqlari."

    elif text == "💻 Kali Linux":
        javob = "💻 Kali Linux haqida ma'lumot."

    elif text == "📡 Wi-Fi xavfsizligi":
        javob = "📡 Wi-Fi tarmog'ini himoyalash bo'yicha tavsiyalar."

    elif text == "🎣 Phishing":
        javob = "🎣 Phishing - soxta sahifalar orqali ma'lumot o'g'irlash usuli."

    elif text == "🦠 Viruslar":
        javob = "🦠 Kompyuter viruslari va ulardan himoyalanish."

    elif text == "📞 Admin":
        javob = "📞 Admin: @username"

    elif text == "ℹ️ Bot haqida":
        javob = "🤖 Ushbu bot kiberxavfsizlikni o'rganish uchun yaratilgan."

    else:
        javob = "Kerakli menyuni tanlang."

    await update.message.reply_text(javob)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

print("✅ Bot ishga tushdi...")
app.run_polling()
