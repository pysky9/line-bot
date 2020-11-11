from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('TxX5SF2X3xPpd1QpOEZKt/vdchCCnLONW7x30YQl4T3wNbeUBwVXOxgB31xLD0V//t6CmrDFhqzhjQqtWRR3oPG6qOP6Jr7o320WAjJiyB8TraH1jqnXRrhVfprdyoiENJt21iW+/QngMSnt53NLggdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7e43b045e1c128c06143cc4091c07df8')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = "很抱歉，我不知道你再說甚麼"
    if msg == "hi":
        s = "hi"
    elif msg == "你好嗎":
        s = "我很好，你呢"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()