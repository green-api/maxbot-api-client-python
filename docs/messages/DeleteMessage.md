# DeleteMessage

[dev.max.ru/docs-api/methods/DELETE/messages](https://dev.max.ru/docs-api/methods/DELETE/messages)

Метод предназначен для удаления ранее отправленного сообщения по его ID.

## Запрос {#request}

### Поля запроса  {#request-parameters}

| Поле         | Тип        | Обязательный | Описание                 |
|--------------|------------|--------------|--------------------------|
| `message_id` | **string** |  Да          | ID удаляемого сообщения  |

### Пример запроса {#request-example}  

*Синхронный запрос:* 

```python
response = bot.messages.delete_message(
    message_id="mid.000000000782a4e0019d00d3ef744e91"
)
```

*Асинхронный запрос:* 

```python
response = await bot.messages.delete_message_async(
    message_id="mid.000000000782a4e0019d00d3ef744e91"
)
```

## Ответ {#response}

### Поля ответа {#response-parameters}

| Поле      | Тип         | Описание                                                      |
|-----------|-------------|---------------------------------------------------------------|
| `success` | **boolean** | `true`, если запрос был успешным,`false` — в противном случае |
| `code`    | **string**  | Код ошибки операции                                           |
| `message` | **string**  | Объяснительное сообщение, если результат не был успешным      |

### Пример тела ответа {#response-example-body}

**Успех:** 

```json
{
    "success": true
}
```

**Ошибка:**

```json
{
    "code": "proto.payload",
    "message": "Invalid message_id: 000000000782a4e0019d00d3ef744e91"
}
```