# DeleteAdmin

[dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members/admins/-userId-](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members/admins/-userId-)

Отменяет права администратора у пользователя в групповом чате, лишая его административных привилегий

## Запрос {#request}  

### Поля запроса {#request-parameters}

| Поле      | Тип         | Обязательный | Описание                        |
|-----------|-------------|--------------|---------------------------------|
| `chat_id` | **integer** | Да           | ID чата                         |
| `user_id` | **integer** | Да           | ID пользователя                 |

### Пример запроса {#request-example}  

*Синхронный запрос:* 

```python
bot.chats.DeleteAdmin(DeleteAdminReq(
    chat_id=123456789,
    user_id=55555
))
```

*Асинхронный запрос:* 

```python
await bot.chats.DeleteAdminAsync(DeleteAdminReq(
    chat_id=123456789,
    user_id=55555
))
```

## Ответ {#response}

### Поля ответа  {#response-parameters}

| Поле      | Тип         | Описание                                                       |
|-----------|-------------|----------------------------------------------------------------|
| `success` | **boolean** | `true`, если запрос был успешным,`false` — в противном случае  |
| `message` | **string**  | Объяснительное сообщение, если результат не был успешным       |

### Пример тела ответа {#response-example-body}

```json
{
    "success": true
}
```
