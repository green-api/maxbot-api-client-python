# EditChat

[dev.max.ru/docs-api/methods/PATCH/chats/-chatId-](https://dev.max.ru/docs-api/methods/PATCH/chats/-chatId-)

Позволяет редактировать информацию о групповом чате, включая название, иконку и закреплённое сообщение 

## Запрос {#request}

### Поля запроса {#request-parameters}

| Поле      | Тип          | Обязательный | Описание                                                                                                     |
|-----------|--------------|--------------|--------------------------------------------------------------------------------------------------------------|
| `chat_id` | **integer**  | Да           | ID изменяемого чата                                                                                          |
| `icon`    | [**object**](../objects/Chat.md#поля-объекта-imageimage) | Нет | Запрос на прикрепление изображения (все поля являются взаимоисключающими) |
| `title`   | **string**   | Нет          | Новое название чата (от 1 до 200 символов)                                                                   |
| `pin`     | **string**   | Нет          | ID сообщения для закрепления в чате                                                                          |
| `notify`  | **boolean**  | Нет          | Если `true`, участники получат системное уведомление об изменении (по умолчанию: `true`)                     |

### Пример запроса {#request-example}

*Синхронный запрос:*

```python
response = bot.chats.EditChat(EditChatReq(
    chat_id=123456789,
    title="Новое название группы",
    notify=False
))
```

*Асинхронный запрос:* 

```python
response = await bot.chats.EditChatAsync(EditChatReq(
    chat_id=123456789,
    title="Новое название группы",
    notify=False
))
```

## Ответ {#response}

[**Объект `Chat`**](../objects/Chat.md)

### Поля ответа {#response-parameters}

| Поле                 | Тип                            | Описание                                                                      |
|----------------------|--------------------------------|-------------------------------------------------------------------------------|
| `chat_id`            | **integer**                    | ID чата                                                                       |
| `type`               | **string**                     | Для групп принимает значение `chat`                                           |
| `status`             | **string**                     | Статус чата. Возможные значения:                                              |
|                      |                                | `active` — Бот является активным участником чата.                             |
|                      |                                | `removed` — Бот был удалён из чата.                                           |
|                      |                                | `left` — Бот покинул чат.                                                     |
|                      |                                | `closed` — Чат был закрыт.                                                    |
| `title`              | **string**                     | Обновленное название чата (если было изменено)                                |
| `icon`               | [**object**](../objects/Chat.md#поля-объекта-imageimage) | Иконка чата                                         |
| `last_event_time`    | **integer**                    | Время последнего события в чате                                               |
| <nobr>`participants_count`</nobr> | **integer**       | Количество участников чата. Для диалогов всегда 2                             |
| `owner_id`           | **integer**                    | ID владельца чата                                                             |
| `participants`       | **object**                     | Участники чата с временем последней активности                                |
| `is_public`          | **boolean**                    | Доступен ли чат публично                                                      |
| `link`               | **string**                     | Ссылка на чат                                                                 |
| `description`        | **string**                     | Описание чата                                                                 |
| `dialog_with_user`   | [**object**](../objects/Chat.md#поля-объекта-dialogwithuser-dialogwithuser)  | Данные о пользователе в диалоге |
| `chat_message_id`    | **string**                     | ID сообщения, содержащего кнопку, через которую был инициирован чат           |
| `pinned_message`     | [**object**](../objects/Message.md#message)   | Закреплённое сообщение в чате                                  |


### Пример тела ответа {#response-example-body}

**Успех:**

```json
{
    "chat_id": -72245307758082,
    "type": "chat",
    "status": "active",
    "title": "New title",
    "last_event_time": 1774253771796,
    "participants_count": 3,
    "is_public": false,
    "owner_id": 123456789,
    "messages_count": 4
}
```
