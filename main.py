import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

@bot.command('hi')
async def hi(message):
    await message.send('''
                        **Привет! Мы рады преветствовать тебя в нашем Manhattan боте!
                       
                       Здесь ты можешь быстро заказать бургер $burger, а также безалкогольные напитки $drinks**
                        ''')

@bot.command('burger')
async def burger(message):
    await message.send('''Почему мы так хотим познакомиться? Потому что дальше бургер делает всё сам. Люди видят, что он вкусный, и возвращаются снова. Нам главное первый раз это показать.
                        Вообще бургер — очень простая штука, её сложно испортить. Достаточно хороших ингредиентов. Это конструктор, если детали качественные, то и результат будет в порядке.''')
    await message.send('Бургеры:')
    with open('images/burgers.png', 'rb') as f:
        picture = discord.File(f)
    await message.send(file=picture)
    await message.send('''**Какой из них вы хотите?**
                       Гамбургер - $b1
                       Чикен бургер - $b2
                       Чизбургер - $b3
                       Мега бургер - $b4
                       ''')
    @bot.command('b1')
    async def b1(message):
        await message.send('''
                        **Ваш заказ: Гамбургер принят! Ожидайте заказ в течении часа.**
                        ''')
    @bot.command('b2')
    async def b2(message):
        await message.send('''
                        **Ваш заказ: Чикен бургер принят! Ожидайте заказ в течении часа.**
                        ''')
    @bot.command('b3')
    async def b3(message):
        await message.send('''
                        **Ваш заказ: Чизбургер принят! Ожидайте заказ в течении часа.**
                        ''')
    @bot.command('b4')
    async def b4(message):
        await message.send('''
                        **Ваш заказ: Мега бургер принят! Ожидайте заказ в течении часа.**
                        ''')

@bot.command('drinks')
async def drinks(message):
    await message.send('''Холодные безалкогольные напитки - спасут ваш жаркий день!''')
    await message.send('Напитки:')
    with open('images/drinks.png', 'rb') as f:
        picture = discord.File(f)
    await message.send(file=picture)
    await message.send('''**Какой из них вы хотите?**
                       Аква Минерале без газа, 0.5л - $d1
                       Чай Липтон Зеленый чай, 0.5л - $d2
                       Фрустайл Апельсин 0.33л - $d3
                       Эвервесс Кола 0.33л - $d4
                       ''')
    @bot.command('d1')
    async def d1(message):
        await message.send('''
                        **Ваш заказ: Аква Минерале без газа, 0.5л принят! Ожидайте заказ в течении часа.**
                        ''')
    @bot.command('d2')
    async def d2(message):
        await message.send('''
                        **Ваш заказ: Чай Липтон Зеленый чай, 0.5л принят! Ожидайте заказ в течении часа.**
                        ''')
    @bot.command('d3')
    async def d3(message):
        await message.send('''
                        **Ваш заказ: Фрустайл Апельсин 0.33л принят! Ожидайте заказ в течении часа.**
                        ''')
    @bot.command('d4')
    async def d4(message):
        await message.send('''
                        **Ваш заказ: Эвервесс Кола 0.33л принят! Ожидайте заказ в течении часа.**
                        ''')

bot.run("your token") 
