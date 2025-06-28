from app.client.bot.bot import bot
from telebot import types
from app.client.handlers.utils.message_utils import send_or_edit_message
from app.client.handlers.knowledge_base.back_handler import back_to_knowledge_base


@bot.callback_query_handler(func=lambda call: call.data == 'base_signals')
def base_signals_handler(call):
    """
    Обработчик для раздела базы знаний о сигналах и их настройке.
    """
    chat_id = call.message.chat.id
    
    text = [
        f'🚨 *РАЗДЕЛ: СИГНАЛЫ И ИХ НАСТРОЙКА*\n\n'
        f'Здесь вы можете получить информацию о сигналах и их настройке.\n',
    ]

    inline_keyboard = types.InlineKeyboardMarkup()
    
    # Создаем кнопки для выбора типа сигнала
    buttons = [
        types.InlineKeyboardButton(text='RSI 📊', callback_data='base_rsi'),
        types.InlineKeyboardButton(text='SMA 📈', callback_data='base_sma'),
        types.InlineKeyboardButton(text='EMA 📉', callback_data='base_ema'),
        types.InlineKeyboardButton(text='Alligator 🐊', callback_data='base_alligator'),
        types.InlineKeyboardButton(text='Bollinger 📊', callback_data='base_bollinger'),
        types.InlineKeyboardButton(text='MACD 📈', callback_data='base_macd'),
        types.InlineKeyboardButton(text='LSTM 🧠', callback_data='base_lstm'),
        types.InlineKeyboardButton(text='GPT 🤖', callback_data='base_gpt'),
    ]
    
    # Добавляем по 2 кнопки в строку
    for i in range(0, len(buttons), 2):
        if i + 1 < len(buttons):
            inline_keyboard.add(buttons[i], buttons[i+1])
        else:
            inline_keyboard.add(buttons[i])
    
    # Добавляем кнопку возврата
    back_button = types.InlineKeyboardButton(text='◀️ Назад к базе знаний', callback_data='back_to_knowledge_base')
    inline_keyboard.add(back_button)
    
    send_or_edit_message(chat_id, ''.join(text), reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'base_sma')
def base_sma_handler(call):
    """
    Обработчик для информации о SMA.
    """
    chat_id = call.message.chat.id
   
    text = [       
        f'📈 *SMA (Simple Moving Average)*\n'
        f'\nSMA (Simple Moving Average) — это технический индикатор, который отображает значение простой скользящей средней в тренде.\n'
        f'\nВ данном боте сигнал SMA представляет собой пересечение двух простых скользящих средних.\n'
        f'\n📈 Быстрая скользящая средняя (Fast SMA) — это более короткая скользящая средняя, которая быстрее реагирует на изменения цен. Она рассчитывается на меньшем количестве периодов, что делает её более чувствительной к недавним движениям цен.\n'
        f'\n📊 Медленная скользящая средняя (Slow SMA) — это более длинная скользящая средняя, которая сглаживает изменения цен, используя большее количество периодов. Она менее чувствительна к краткосрочным колебаниям, что позволяет лучше выявлять долгосрочные тенденции.\n'
        f'\n🔄 Пересечение быстрой и медленной скользящей средних может служить сигналом для открытия или закрытия позиций: когда быстрая SMA пересекает медленную сверху вниз, это может указывать на сигнал продажи, а когда пересекает снизу вверх — на сигнал покупки.\n'
        f'\n🔧 Базовые настройки сигнала SMA:\n'
        f'\n    fastLength: 10\n'
        f'\n    slowLength: 30\n'
    ]

    # Создаем кнопку для возврата в меню сигналов
    inline_keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text='◀️ Назад к сигналам', callback_data='base_signals')
    inline_keyboard.add(back_button)
    
    send_or_edit_message(chat_id, ''.join(text), reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'base_ema')
def base_ema_handler(call):
    """
    Обработчик для информации о EMA.
    """
    chat_id = call.message.chat.id
    
    text = [
        f'📉 *EMA (Exponential Moving Average)*\n'
        f'\nEMA (Exponential Moving Average) — это технический индикатор, который вычисляет скользящую среднюю, придавая большее значение последним ценам. Это делает её более чувствительной к изменениям цен по сравнению с SMA.\n'
        f'\n🔍 В данном боте сигнал EMA также представляет собой пересечение двух экспоненциальных скользящих средних.\n'
        f'\n📈 Быстрая экспоненциальная скользящая средняя (Fast EMA) — это более короткая EMA, которая быстрее реагирует на изменения цен, так как она использует меньшее количество периодов и придаёт больший вес последним значениям.\n'
        f'\n📊 Медленная экспоненциальная скользящая средняя (Slow EMA) — это более длинная EMA, которая сглаживает изменения, используя большее количество периодов. Это позволяет лучше выявлять долгосрочные тренды, но она реагирует медленнее на краткосрочные колебания.\n'
        f'\n🔄 Пересечение быстрой и медленной EMA может служить сигналом для открытия или закрытия позиций: когда быстрая EMA пересекает медленную сверху вниз, это может указывать на сигнал продажи, а когда пересекает снизу вверх — на сигнал покупки.\n'
        f'\n🔧 Базовые настройки сигнала EMA:\n'
        f'\n    fastLength: 10\n'
        f'\n    slowLength: 30\n'
    ]

    # Создаем кнопку для возврата в меню сигналов
    inline_keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text='◀️ Назад к сигналам', callback_data='base_signals')
    inline_keyboard.add(back_button)
    
    send_or_edit_message(chat_id, ''.join(text), reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'base_rsi')
def base_rsi_handler(call):
    """
    Обработчик для информации о RSI.
    """
    chat_id = call.message.chat.id
    
    text = [
        f'📊 *RSI (Relative Strength Index)*\n'
        f'\nRSI (Relative Strength Index) — это осциллятор, который измеряет скорость и изменения ценовых движений. Он используется для определения уровней перекупленности и перепроданности на рынке.\n'
        f'\n🔍 RSI колеблется в диапазоне от 0 до 100, и обычно значения выше 70 указывают на перекупленность, а ниже 30 — на перепроданность. Это может помочь трейдерам определить, когда стоит открывать или закрывать позиции.\n'
        f'\n📈 Чем выше RSI, тем сильнее восходящий тренд, тогда как низкие значения RSI указывают на силу нисходящего тренда.\n'
        f'\n🔄 Пересечение RSI с уровнями 30 и 70 может служить сигналом для действий: когда RSI пересекает уровень 30 снизу вверх, это может указывать на возможный рост цены (сигнал покупки); а пересечение уровня 70 сверху вниз может указывать на возможное снижение (сигнал продажи).\n'
        f'\n🔧 Базовые настройки сигнала RSI:\n'
        f'\n    period: 14 — это количество периодов, за которое рассчитывается индекс, и позволяет определять силу текущего тренда.\n'
        f'\n    highLevel: 70 — уровень перекупленности, выше которого можно ожидать коррекцию.\n'
        f'\n    lowLevel: 30 — уровень перепроданности, ниже которого возможен рост.\n'
    ]

    # Создаем кнопку для возврата в меню сигналов
    inline_keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text='◀️ Назад к сигналам', callback_data='base_signals')
    inline_keyboard.add(back_button)
    
    send_or_edit_message(chat_id, ''.join(text), reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'base_alligator')
def base_alligator_handler(call):
    """
    Обработчик для информации об индикаторе Аллигатор.
    """
    chat_id = call.message.chat.id
    
    text = [
        f'🐊 *Индикатор Аллигатор*\n'
        f'\nИндикатор Аллигатор — это осцилляторный индикатор технического анализа, разработанный известным трейдером Биллом Уильямсом. Он используется для определения изменений в рыночном тренде, выявляя моменты перехода от трендового движения к боковому и наоборот.\n'
        f'\n🔍 График индикатора состоит из трех линий, которые представляют собой сглаженные скользящие средние (SMA) с разными периодами и смещением. Все линии основаны на средней цене, рассчитываемой как (High + Low) / 2.\n'
        f'\n📈 Синяя линия (Челюсть) — период 21, сдвиг 8 баров: показывает возможное местоположение цены при отсутствии важных новостей. Если линия находится ниже графика цены, это сигнализирует о восходящем движении. Если выше, то о нисходящем.\n'
        f'\n📊 Красная линия (Зубы) — период 11, сдвиг 5 баров: демонстрирует текущую тенденцию на часовом графике.\n'
        f'\n💋 Зеленая линия (Губы) — период 8, сдвиг 3 бара: отображает краткосрочные тенденции на дневных таймфреймах.\n'
        f'\n🔄 Пересечения линий могут служить сигналами для торговли: когда губы пересекают зубы и зубы пересекают челюсть снизу вверх — это сигнал на покупку; когда сверху вниз — сигнал на продажу.\n'
        f'\n🔧 Базовые настройки сигнала Аллигатора:\n'
        f'\n    jaw_period: 21 — период для челюсти.\n'
        f'\n    jaw_shift: 8 — смещение для челюсти.\n'
        f'\n    teeth_period: 11 — период для зубов.\n'
        f'\n    teeth_shift: 5 — смещение для зубов.\n'
        f'\n    lips_period: 8 — период для губ.\n'
        f'\n    lips_shift: 3 — смещение для губ.\n'
    ]

    # Создаем кнопку для возврата в меню сигналов
    inline_keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text='◀️ Назад к сигналам', callback_data='base_signals')
    inline_keyboard.add(back_button)
    
    send_or_edit_message(chat_id, ''.join(text), reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'base_bollinger')
def base_bollinger_handler(call):
    """
    Обработчик базы знаний для сигнала Bollinger Bands.
    """
    chat_id = call.message.chat.id
    
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.add(types.InlineKeyboardButton(text='◀️ Назад к базе знаний', callback_data='back_to_kb'))
    
    text = [
        "🚨 *Bollinger Bands (Полосы Боллинджера)*\n\n",
        "Полосы Боллинджера - это индикатор технического анализа, который создает канал, состоящий из трех линий вокруг цены актива.\n\n",
        "Как работают полосы Боллинджера:\n",
        "• Средняя линия - это простая скользящая средняя (SMA)\n",
        "• Верхняя полоса - средняя линия плюс несколько стандартных отклонений\n",
        "• Нижняя полоса - средняя линия минус несколько стандартных отклонений\n\n",
        "Сигналы Bollinger Bands:\n",
        "• Покупка: когда цена касается или пробивает нижнюю полосу и начинает возвращаться\n",
        "• Продажа: когда цена касается или пробивает верхнюю полосу и начинает возвращаться\n\n",
        "Параметры настройки в боте:\n",
        "- Period: период для скользящей средней (рекомендуется 20)\n",
        "- Deviation: количество стандартных отклонений (рекомендуется 2)\n",
        "- Type MA: тип скользящей средней (SMA, EMA, WMA, DEMA)\n\n",
        "Полосы Боллинджера хорошо работают как на спокойном, так и на волатильном рынке, поскольку они адаптируются к изменениям волатильности."
    ]
    
    send_or_edit_message(chat_id, ''.join(text), reply_markup=inline_keyboard, parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'base_macd')
def base_macd_handler(call):
    """
    Обработчик базы знаний для сигнала MACD.
    """
    chat_id = call.message.chat.id
    
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.add(types.InlineKeyboardButton(text='◀️ Назад к базе знаний', callback_data='back_to_kb'))
    
    text = [
        "🚨 *MACD (Moving Average Convergence Divergence)*\n\n",
        "MACD - это технический индикатор, который показывает связь между двумя скользящими средними цены.\n\n",
        "Как работает MACD:\n",
        "• Быстрая линия (Fast Length) - это короткая EMA, обычно 12 периодов\n",
        "• Медленная линия (Slow Length) - это длинная EMA, обычно 26 периодов\n",
        "• Сигнальная линия (Signal Length) - это EMA от разницы между быстрой и медленной линиями, обычно 9 периодов\n\n",
        "Сигналы MACD:\n",
        "• Покупка: когда быстрая линия пересекает медленную снизу вверх\n",
        "• Продажа: когда быстрая линия пересекает медленную сверху вниз\n\n",
        "Параметры настройки в боте:\n",
        "- Fast Length: период быстрой EMA (рекомендуется 12)\n",
        "- Slow Length: период медленной EMA (рекомендуется 26)\n",
        "- Signal Length: период для сигнальной линии (рекомендуется 9)\n\n",
        "Для достижения наилучших результатов рекомендуется использовать MACD в сочетании с другими индикаторами."
    ]
    
    send_or_edit_message(chat_id, ''.join(text), reply_markup=inline_keyboard, parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'base_lstm')
def base_lstm_handler(call):
    """
    Обработчик для информации о LSTM.
    """
    chat_id = call.message.chat.id
    
    text = [
        f'🧠 *LSTM (Long Short-Term Memory)*\n'
        f'\nLSTM — это тип рекуррентной нейронной сети (RNN), способной запоминать зависимости в последовательных данных. Он особенно эффективен для анализа временных рядов, таких как цены акций.\n'
        f'\n🔍 Основные особенности LSTM:\n'
        f'- **Запоминание зависимостей**: LSTM может запоминать информацию на долгие промежутки времени, что позволяет учитывать прошлые значения при прогнозировании будущих цен.\n'
        f'- **Справляется с нехваткой данных**: Модель может использовать ограниченное количество данных для предсказания, что делает её полезной в условиях недостатка информации.\n'
        f'\n💡 Как работает LSTM для прогнозирования цен акций:\n'
        f'1. **Обучение**: Модель обучается на исторических данных цен закрытия акций, где она использует последние 60 значений для предсказания следующего.\n'
        f'2. **Предсказание**: После обучения модель использует последние доступные данные для генерации прогноза цены закрытия.\n'
        f'3. **Генерация сигналов**:\n'
        f'   - **Сигнал на покупку** генерируется, если предсказанная цена выше текущей.\n'
        f'   - **Сигнал на продажу** генерируется, если предсказанная цена ниже текущей и прибыль положительна.\n'
        f'   - В противном случае сигнал будет «держать» (hold).\n'
        f'\n🔧 **Настройки**: Модель LSTM не имеет настраиваемых параметров, она обучается на исторических данных и предсказывает цены на основе обученных зависимостей.\n'
    ]

    # Создаем кнопку для возврата в меню сигналов
    inline_keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text='◀️ Назад к сигналам', callback_data='base_signals')
    inline_keyboard.add(back_button)
    
    send_or_edit_message(chat_id, ''.join(text), reply_markup=inline_keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'base_gpt')
def base_gpt_handler(call):
    """
    Обработчик для информации о GPT.
    """
    chat_id = call.message.chat.id
    
    text = [
        f'🤖 *GPT (Generative Pre-trained Transformer)*\n'
        f'\nGPT — это мощная языковая модель, способная генерировать текст и анализировать информацию на основе заданного промпта. Она использует знания из огромного объёма текста для генерации ответов, что делает её полезной в различных сценариях.\n'
        f'\n🔍 Основные особенности использования GPT для анализа:\n'
        f'- **Анализ данных**: Вы можете вводить текст с вопросами или запросами на анализ, и модель предоставит осмысленные ответы.\n'
        f'- **Интерактивность**: Пользователи могут задавать вопросы, уточнять запросы и получать соответствующие ответы в реальном времени.\n'
        f'- **Контекст**: GPT учитывает информацию о текущей прибыли и тикере, чтобы генерировать более точные и актуальные ответы.\n'
        f'\n💡 Как использовать GPT:\n'
        f'1. **Ввод промпта**: Пользователь вводит текст, который может включать вопросы о рынках, анализе акций и других темах.\n'
        f'2. **Получение ответа**: Модель обрабатывает запрос и предоставляет ответ, который может помочь в принятии торговых решений.\n'
        f'\n🔧 **Настройки**: GPT не имеет фиксированных настроек, и пользователь может свободно вводить любые текстовые запросы для получения информации.\n'
        f'\n⚠️ **Замечание**: Результаты, полученные от GPT, являются рекомендациями и не должны восприниматься как финансовые советы.\n'
    ]

    # Создаем кнопку для возврата в меню сигналов
    inline_keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton(text='◀️ Назад к сигналам', callback_data='base_signals')
    inline_keyboard.add(back_button)
    
    send_or_edit_message(chat_id, ''.join(text), reply_markup=inline_keyboard)








