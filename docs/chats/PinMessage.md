# PinMessage

[dev.max.ru/docs-api/methods/PUT/chats/-chatId-/pin](https://dev.max.ru/docs-api/methods/PUT/chats/-chatId-/pin)

Закрепляет сообщение в групповом чате

## Запрос {#request}

### Поля запроса{#request-parameters}

| Поле         | Тип         | Обязательный | Описание                                                 |
|--------------|-------------|--------------|----------------------------------------------------------|
| `chat_id`    | **integer** | Да           | ID чата                                                  |
| `message_id` | **string**  | Да           | ID сообщения, которое нужно закрепить                    |
| `notify`     | **boolean** | Нет          | Если `true`, участники получат уведомление с системным сообщением о закреплении (по умолчанию `true`)|

### Пример запроса {#request-example}  

*Синхронный запрос:* 

```python
bot.chats.PinMessage(PinMessageReq(
    chat_id=123456789,
    message_id="mid.000000000782a4e0019d00d3ef744e91",
    notify=true
))
```

*Асинхронный запрос:* 

```python
await bot.chats.PinMessageAsync(PinMessageReq(
    chat_id=123456789,
    message_id="mid.000000000782a4e0019d00d3ef744e91",
    notify=true
))
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
