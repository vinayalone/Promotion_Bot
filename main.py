import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# 🔐 SECURITY: Load Token from Environment Variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Check if token exists
if not BOT_TOKEN:
    print("❌ ERROR: No BOT_TOKEN found! Add it to Railway Variables.")
    exit(1)

# --- CONFIGURATION ---
ADMIN_USERNAME = "EvilxStar"

# Professional Promo Message
PROMO_TEXT = (
    "<b>🚀 Premium Promotion Services</b>\n\n"
    "<b>✨ Skyrocket Your Visibility!</b>\n"
    "👉 <b>Massive Audience:</b> Access to millions of engaged users.\n\n"
    "📈 <b>Guaranteed Traffic:</b> Our advanced bots accept over <b>100,000+ users daily!</b>\n\n"
    "<b>📆 Available Plans:</b>\n"
    "• 1,000 Users — <code>2,000 INR</code>\n"
    "• 2,500 Users — <code>4,000 INR</code>\n"
    "• 5,000 Users — <code>8,000 INR</code>\n"
    "• 10,000 Users — <code>15,000 INR</code>\n\n"
    "<b>💳 Payment Methods:</b>\n"
    "• 🪙 UPI (Preferred)\n"
    "• 🎁 Gift Cards\n"
    "• 💸 PayPal\n\n"
    "<b>⚠️ How it works:</b>\n"
    "1. Your post remains private until approved.\n"
    "2. Admin reviews & publishes after payment.\n\n"
    "<b>Ready to grow? Contact us below! 👇</b>"
)

# --- LOGGING ---
logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# --- THE /START COMMAND HANDLER ---
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    try:
        # Create the "Contact Admin" button
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📨 Contact Admin to Buy", url=f"https://t.me/{ADMIN_USERNAME}")]
        ])
        
        # Send the message
        await message.answer(text=PROMO_TEXT, reply_markup=keyboard)
        print(f"✅ User {message.from_user.id} viewed the promo menu.")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# --- MAIN LOOP ---
async def main():
    print("🚀 Promo Bot Started...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try: asyncio.run(main())
    except KeyboardInterrupt: print("Bot Stopped")
