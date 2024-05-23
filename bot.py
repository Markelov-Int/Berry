import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

def webapp_builder()-> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(text="Let's Click!", web_app=WebAppInfo(url=""))
    return builder.as_markup()

# Bot token can be obtained via https://t.me/BotFather

# All handlers should be attached to the Router (or Dispatcher)
router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply("Click! Click! CLick!", reply_markup=webapp_builder()
    )


async def main() -> None:
    bot = Bot("6993695487:AAF5JQKQatkfmVhjch6UT99_zPjlgyORwpM", parse_mode=ParseMode.HTML)
    dp=Dispatcher()
    dp.include_router(router)
    
    await bot.delete_webhook(True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())