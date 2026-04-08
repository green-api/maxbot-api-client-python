# LeaveChat

[dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members/me](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members/me)

Удаляет бота из участников группового чата

## Запрос {#request}

### Поля запроса  {#request-parameters}

| Поле      | Тип         | Обязательный | Описание                        |
|-----------|-------------|--------------|---------------------------------|
| `chat_id` | **integer** | Да           | ID чата, который нужно покинуть |

### Пример запроса {#request-example}

*Синхронный запрос:*

```python
bot.chats.leave_chat(chat_id=123456789)
```

*Асинхронный запрос:* 

```python
await bot.chats.leave_chat_async(chat_id=123456789)
```

## Ответ {#response}

### Поля ответа {#response-parameters}

| Поле       | Тип         | Описание                                                          |
|------------|-------------|-------------------------------------------------------------------|
| `success`  | **boolean** | `true`, если запрос был успешным, `false` — в противном случае    |
| `message`  | **string**  | Объяснительное сообщение, если результат не был успешным          |

### Пример тела ответа {#response-example-body}

```json
{
    "success": true
}
```