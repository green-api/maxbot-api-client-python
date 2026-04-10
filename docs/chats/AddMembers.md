# AddMembers  

[dev.max.ru/docs-api/methods/POST/chats/-chatId-/members](https://dev.max.ru/docs-api/methods/POST/chats/-chatId-/members)

Добавляет участников в групповой чат. Для этого могут потребоваться дополнительные права

## Запрос {#request}

### Поля запроса  {#request-parameters}

| Поле       | Тип         | Обязательный | Описание                                 |
|------------|-------------|--------------|------------------------------------------|
| `chat_id`  | **integer** | Да           | ID чата                                  |
| `user_ids` | **array**   | Да           | Массив ID добавляемых пользователей      |

### Пример запроса {#request-example}

*Синхронный запрос:*

```python
request = AddMembersReq(
    chat_id=123456789,
    user_ids=[77777, 88888]
)
response = bot.chats.add_members(request)
```

*Асинхронный запрос:* 

```python
request = AddMembersReq(
    chat_id=123456789,
    user_ids=[77777, 88888]
)
response = await bot.chats.add_members_async(request)
```

## Ответ {#response}

### Поля ответа {#response-parameters}

| Поле                  | Тип         | Описание                                                                                                      |
|-----------------------|-------------|---------------------------------------------------------------------------------------------------------------|
| `success`             | **boolean** | `true`, если запрос был успешным,`false` — в противном случае                                                 |
| `message`             | **string**  | Объяснительное сообщение, если результат не был успешным                                                      |
| `failed_user_ids`     | **array**   | Массив ID пользователей, которых не удалось добавить                                                          |
| `failed_user_details` | [**object**](#поля-объекта-faileduserdetails-faileduserdetails)  | Детальная информация об ошибках для каждого пользователя |

### Поля объекта `FailedUserDetails` {#failedUserDetails}

| Поле          | Тип         | Описание                                                 |
|---------------|-------------|----------------------------------------------------------|
| <nobr>`error_code`</nobr>  | **string**  | Код ошибки <br>Возможные значения:          |
||| `add.participant.privacy` — ошибки конфиденциальности при добавлении пользователей   |
||| `add.participant.not.found` — пользователи не найдены                                |
| `user_ids`    | **array**   | ID пользователей с данной ошибкой                        |

### Пример тела ответа {#response-example-body}

**Успех:**

```json
{
    "success": true,
}
```

**Ошибка:**

```json
{
    "success": false,
    "failed_user_ids": [
        123456789
    ],
    "failed_user_details": [
        {
            "error_code": "add.participant.not.found",
            "user_ids": [
                123456789
            ]
        }
    ]
}
```