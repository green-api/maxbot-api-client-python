# AnswerCallback

[dev.max.ru/docs-api/methods/POST/answers](https://dev.max.ru/docs-api/methods/POST/answers)

Метод предназначен для подтверждения нажатия инлайн-кнопки пользователем (убирает индикатор загрузки на клиенте).

## Запрос {#request}

### Поля запроса {#request-parameters}

| Поле                         | Тип        | Обязательный | Описание                                                                          |
|------------------------------|------------|--------------|-----------------------------------------------------------------------------------|
| `callback_id`                | **string** | Да           | ID коллбэка, полученного из входящего события                                     |
| `message` | [**object**](../objects/NewMessageBody.md) | Нет  | Обновление сообщения или клавиатуры в ответ на нажатие                       |
| <nobr>`notification`</nobr>  | **string** | Нет          | Заполните это, если хотите просто отправить одноразовое уведомление пользователю  |

### Пример запроса {#request-example}  

*Синхронный запрос:* 

```python
response = bot.messages.AnswerCallback(AnswerCallbackReq(
    callback_id="f9LHodD0cOLW7qZQo5Yp4sWNbFSb7DnBL1K2N5O5vMYCShXQUyMx0IUn",
    message=NewMessageBody(
        text="Action confirmed!"
    )
))
```

*Асинхронный запрос:* 

```python
response = await bot.messages.AnswerCallbackAsync(AnswerCallbackReq(
    callback_id="f9LHodD0cOLW7qZQo5Yp4sWNbFSb7DnBL1K2N5O5vMYCShXQUyMx0IUn",
    message=NewMessageBody(
        text="Action confirmed!"
    )
))
```

## Ответ {#response}

### Поля ответа {#response-parameters}

| Поле      | Тип         | Описание                                                       |
|-----------|-------------|----------------------------------------------------------------|
| `success` | **boolean** | `true`, если запрос был успешным,`false` — в противном случае  |
| `code`    | **string**  | Код ошибки операции                                            |
| `message` | **string**  | Объяснительное сообщение, если результат не был успешным       |

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
    "message": "callback_id: Callback identifier is invalid"
}
```
