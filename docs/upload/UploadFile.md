# UploadFile

[dev.max.ru/docs-api/methods/POST/uploads](https://dev.max.ru/docs-api/methods/POST/uploads)

Загружает файл на сервер MAX.   

## Запрос {#request}

### Поля запроса {#request-parameters}

| Поле         | Тип        | Обязательный | Описание                                                                                                             |
|--------------|------------|--------------|----------------------------------------------------------------------------------------------------------------------|
| `type`       | **string** | Да           | Тип вложения. Допустимые значения:                                                                                   |
|              |            |              | `image` - JPG, JPEG, PNG, GIF, TIFF, BMP, HEIC                                                                       |
|              |            |              | `video` - MP4, MOV, MKV, WEBM, MATROSKA                                                                              | 
|              |            |              | `audio` - MP3, WAV, M4A и другие                                                                                     |
|              |            |              | `file` - любые типы файлов                                                                                           |
| `file_path`  | **string** | Да           | Абсолютный или относительный путь к файлу на локальном диске.                                                        |
| <nobr>`upload_url`<nobr> | **string** | Нет | Используется только для прямой загрузки, если URL уже получен. При вызове `upload_file` заполняется автоматически. |

### Пример запроса {#request-example}

*Синхронный запрос:*

```python
response = bot.uploads.upload_file(
    type=UploadType.IMAGE,
    file_path="./photos/cat.png"
)
```

*Асинхронный запрос:* 

```python
response = await bot.uploads.upload_file_async(
    type=UploadType.IMAGE,
    file_path="./photos/cat.png"
)
```

## Ответ {#response}

### Поля ответа  {#response-parameters}

| Поле      | Тип         | Описание                                                                                                                        |
|-----------|-------------|---------------------------------------------------------------------------------------------------------------------------------|
| `file_id` | **integer** | Уникальный числовой идентификатор файла на сервере. <br>*Возвращается для типов `file`, `video` и `audio`*                      |
| `token`   | **string**  | Строковый токен доступа, необходимый для прикрепления файла к сообщению. <br>*Возвращается для типов `file`, `video` и `audio`* |
| `photos`  | [**array**](#поля-объекта-photodata-photodata) | Словарь версий изображений. Ключ — уникальный хеш-идентификатор версии. <br>*Возвращается для типа `image`*         |

### Поля объекта `PhotoData` {#PhotoData}

| Поле      | Тип         | Описание                                       |
|-----------|-------------|------------------------------------------------|
| `token`   | **string**  | Токен загруженного изображения для отправки    |

### Пример тела ответа {#response-example-body}

**Пример ответа на загрузку изображения:**

```json
{
  "photos": {
    "3JJvlQgoPpDgwtDEnxfLhI9pXye9WNfuMYfhNsaldssWmWt+o4h5tQ==": {
      "token": "9+eyCStTAIyomEW0h0PzC3/2FMn6jnei4sbeAHAHzEAQPw5R+QRmK6fI2i8m2g385JIOot9+dE50Zpu2C8rWpdL3lqBMBwKZg1LgN6LAi+L7RMzvuMlRQBGMRVsHIM3qCYjJVz9rZ3bJC2BKsTpwGFT2zeZD65ubBd8t+paTYZFhHQTAHjP3XMxDQF5b201h1MnTVAJwIbBOQi3emv+C4/zX+iKFArgxeFJdUr/8UEo="
    }
  }
}
```
**Пример ответа на загрузку файла:**

```json
{
  "file_id": 2947318223,
  "token": "f9LHodD0cOKN7LWyX9hfc2icprCO5CThP_QcGNvMN5wvpD7BvhUOjNkvsdVTR5qxMvgJwgwwvqLLqXcnEGSE"
}
```
