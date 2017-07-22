from message_handler import logger
import telegram


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def parseInlineQuery(bot, update):
    logger.info(update)
    logger.info(update.inline_query)
    q = update.inline_query.query
    user = update.inline_query.from_user
    logger.info(user)

    if user.username:
        username = user.username
    elif user.last_name:
        username = "%s %s" % (user.first_name, user.last_name)
    else:
        username = user.first_name

    logger.info('username found as %s' % username)

    results = []
    if q.strip() != '':
        results.append(telegram.InlineQueryResultArticle(
            type='article',
            id=1,
            title='Quit:',
            description=q,
            thumb_url='http://i.imgur.com/YOiUSjS.png',
            thumb_width=32,
            thumb_height=32,
            input_message_content=telegram.InputTextMessageContent(
                message_text="`*** %s has quit (quit: %s)`" % (username, q), parse_mode='markdown')
        ))
        logger.info('result list created')

    bot.answerInlineQuery(update.inline_query.id, results, cache_time=0)
