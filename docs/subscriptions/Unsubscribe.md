# Unsubscribe

[dev.max.ru/docs-api/methods/DELETE/subscriptions](https://dev.max.ru/docs-api/methods/DELETE/subscriptions)

Удаляет подписку и отключает доставку обновлений бота на указанный Webhook.     

После вызова этого метода вы можете снова получать обновления методом долгого опроса [`GetUpdates`](./GetUpdates.md).

## Запрос {#request}

### Поля запроса  {#request-parameters}

| Поле  | Тип        | Обязательный | Описание                                                                |
|-------|------------|--------------|-------------------------------------------------------------------------|
| `url` | **string** | Да           | URL-адрес вебхука, который необходимо удалить из списка подписок бота.  |

### Пример запроса {#request-example}

*Синхронный запрос:*

```python
response = bot.subscriptions.unubscribe(
    url="https://webhook.site/my-bot-endpoint"
)
```

*Асинхронный запрос:* 

```python
response = await bot.subscriptions.unubscribe_async(
    url="https://webhook.site/my-bot-endpoint"
)
```

## Ответ {#response}

### Поля ответа {#response-parameters}

| Поле      | Тип         | Описание                                                                          |
|-----------|-------------|-----------------------------------------------------------------------------------|
| `success` | **boolean** | `true`, если запрос был успешным,`false` — в противном случае(`true` или `false`) |
| `message` | **string**  | Текстовое сообщение с подробностями выполнения или ошибкой                        |

### Пример тела ответа {#response-example-body}

```json
{
    "success": true,
    "message": "Webhook has been successfully deleted"
}
```
