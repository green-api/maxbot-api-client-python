# SendFile

Универсальный метод для упрощенной отправки файлов

## Запрос {#request}

### Поля запроса {#request-parameters}

| Поле                   | Тип          | Обязательный | Описание                                                                                          |
|------------------------|--------------|--------------|---------------------------------------------------------------------------------------------------|
| `file_source`          | **string**   | Да           | URL-адрес файла (начинается с http/https) или путь к локальному файлу                             |
| `chat_id`              | **integer**  | Нет*         | ID чата (обязательно, если не передан `user_id`)                                                  |
| `disable_link_preview` | **boolean**  | Нет | Если `false`, сервер не будет генерировать превью для ссылок в тексте сообщения                            |
| `user_id`              | **integer**  | Нет*         | ID пользователя (обязательно, если не передан `chat_id`)                                          |
| `text`                 | **string**   | Нет          | Новый текст сообщения (до 4000 символов)                                                          |
| `attachments`          | **array**    | Нет          | Вложения сообщения. Если пусто, все вложения будут удалены                                        |
| `link`                 | [**object**](../objects/NewMessageBody.md#поля-объекта-newmessagelinknewmessagelink) | Нет        | Ссылка на другое сообщение  |
| `notify`               | **boolean**  | Нет          | Отправлять ли пуш-уведомление пользователю (`true`/`false`)                                       |
| `format`               | **string**   | Нет          | Формат разметки текста (`HTML`, `Markdown`)                                                       |

### Пример запроса {#request-example}

*Синхронный запрос:*

```python
bot.helpers.SendFile(
    chat_id=123456789,
    text="Вот отчет за этот месяц",
    file_source="./reports/march.pdf",
    notify=True
)
```

*Асинхронный запрос:* 

```python
await bot.helpers.SendFileAsync(
    user_id=987654321,
    text="Посмотри на эту статью: https://example.com/article",
    file_source="https://example.com/image.png",
    disable_link_preview=True
)
```

## Ответ {#response}

[**объект `message`**](../objects/Message.md)

### Поля ответа {#response-parameters}

| Поле            | Тип                                                    | Описание                                                                          |
|-----------------|--------------------------------------------------------|-----------------------------------------------------------------------------------|
| `sender`        | [**object**](../objects/User.md)                       | Пользователь, отправивший сообщение                                               |
| `recipient`     | [**object**](../objects/Message.md#поля-объекта-recipient-recipient)          | Получатель сообщения. Может быть пользователем или чатом   |
| `timestamp`     | **integer**                                            | Время создания сообщения в формате Unix-time                                      |
| <nobr>`linked_message`</nobr> | [**object**](../objects/Message.md#поля-объекта-linkedmessage-linkedmessage) | Пересланное или ответное сообщение            |
| `body`          | [**object**](../objects/Message.md#поля-объекта-messagebody-messagebody)        | Содержимое сообщения                                     |
| `stat`          | [**object**](../objects/Message.md#поля-объекта-messagestat--messagestat) | Статистика сообщения. Возвращается только для постов в каналах |
| `url`           | **string**                                             | Публичная ссылка на пост в канале. Отсутствует для диалогов и групповых чатов     |
### Пример тела ответа {#response-example-body}

```json
{
    "sender": {
        "user_id": 111222,
        "first_name": "MyBot",
        "is_bot": true
    },
    "recipient": {
        "chat_id": 123456789,
        "chat_type": "group"
    },
    "timestamp": 1679051234,
    "body": {
        "mid": "msg-111222333",
        "seq": 42,
        "text": "Вот отчет за этот месяц",
        "attachments": [
            {
                "type": "file",
                "payload": {
                    "token": "file_token_xyz",
                    "filename": "march.pdf"
                }
            }
        ]
    }
}
```
