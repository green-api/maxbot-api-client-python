# UnpinMessage

[dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/pin](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/pin)

Удаляет закреплённое сообщение в групповом чате

## Запрос {#request}

### Поля запроса  {#request-parameters}

| Поле      | Тип         | Обязательный | Описание                      |
|-----------|-------------|--------------|-------------------------------|
| `chat_id` | **integer** | Да           | ID чата                       |

### Пример запроса {#request-example}  

*Синхронный запрос:* 

```python
request = UnpinMessageReq(
    chat_id=123456789
)
bot.chats.unpin_message(request)
```

*Асинхронный запрос:* 

```python
request = UnpinMessageReq(
    chat_id=123456789
)
await bot.chats.unpin_message_async(request)
```

## Ответ {#response}

### Поля ответа  {#response-parameters}

| Поле      | Тип         | Описание                                                       |
|-----------|-------------|----------------------------------------------------------------|
| `success` | **boolean** | `true`, если запрос был успешным,`false` — в противном случае  |
| `message` | **string**  | Объяснительное сообщение, если результат не был успешным       |

### Пример тела ответа {#response-example-body}

```json
{
    "success": true
}
```