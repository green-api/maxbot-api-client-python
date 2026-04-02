# MaxBot API Client (Python)

`maxbot-api-client-python` — это библиотека для интеграции с API MAX Bot. Этот проект предоставляет структурированный интерфейс для взаимодействия с конфигурациями бота, управления сообщениями, отправки медиафайлов и подписки на события через long-polling.

Для использования библиотеки потребуется получить токен бота в консоли разработчика MAX bot.

## API

Документацию по REST API MAX можно найти по ссылке https://dev.max.ru/docs-api. Библиотека является оберткой для REST API, поэтому документация по указанной выше ссылке также применима к используемым здесь моделям и параметрам запроса.

## Поддержка

[![Support](https://img.shields.io/badge/support@green--bot.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:support@green-bot.com)
[![Support](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/greenapi_support_ru_bot)
[![Support](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/77780739095)

## Руководства и новости

[![Guides](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@green-api)
[![News](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/green_api)
[![News](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029VaHUM5TBA1f7cG29nO1C)


## Установка

**Убедитесь, что у вас установлен Python версии 3.8 или выше:**

```shell
python --version
```

**Установите библиотеку:**

```bash
pip install -e .
```

**Импорт:**

```python
from maxbot_api_client_python import API, Config
```

## Использование и примеры

**Как инициализировать клиент:**

```python
try:
    bot = API(Config(
    base_url="https://platform-bot.max.ru",  # Base url for MAX API requests
    token="YOUR_BOT_TOKEN",                  # Max bot token
    global_rps=25,
    timeout=35
))
except ValueError as e:
    print(f"Initialization error: {e}")
```

**Как получить информацию о боте:**

* Ссылка на синхронный пример: [GetBot.py](./examples/sync/GetBot.py)

```python
response = bot.bots.GetBot()
```

* Ссылка на асинхронный пример: [GetBotAsync.py](./examples/async/GetBotAsync.py)

```python

response = await bot.bots.GetBotAsync()
```

**Как отправить сообщение:**

* Ссылка на синхронный пример: [SendMessage.py](./examples/sync/SendMessage.py)

```python
response = bot.messages.SendMessage(SendMessageReq(
    user_id=1234567890,
    text="Hello world!"
))
```

* Ссылка на асинхронный пример: [SendMessage.py](./examples/async/SendMessageAsync.py)

```python
response = await bot.messages.SendMessageAsync(SendMessageReq(
    user_id=1234567890,
    text="Hello world from Async!"
))
```

**Как легко отправить файл (по ссылке или локальный):**

* Ссылка на синхронный пример: [SendFile.py](./examples/sync/SendFile.py)

```python
response = bot.helpers.SendFile(SendFileReq(
    chat_id=1234567890,
    text="Check this!",
    file_source="https://example.com/image.png"
))
```

* Ссылка на асинхронный пример: [SendFileAsync.py](./examples/async/SendFileAsync.py)

```python
response = await bot.helpers.SendFileAsync(SendFileReq(
    chat_id=1234567890,
    text="Посмотри на этот файл!",
    file_source="https://example.com/image.png"
))
```

**Как вручную загрузить файл (для кастомных вложений):**

* Ссылка на синхронный пример: [UploadFile.py](./examples/sync/UploadFile.py)

```python
response = bot.uploads.UploadFile(UploadFileReq(
    type=UploadType.IMAGE,
    file_path="examples/assets/file.png"
))
```

* Ссылка на асинхронный пример: [UploadFileAsync.py](./examples/async/UploadFileAsync.py)

```python
response = await bot.uploads.UploadFileAsync(UploadFileReq(
    type=UploadType.IMAGE,
    file_path="examples/assets/file.png"
))
```

**Как получить входящее уведомление:**

* Ссылка на синхронный пример: [GetUpdates.py](./examples/sync/GetUpdates.py)

```python
response = bot.subscriptions.GetUpdates(GetUpdatesReq(
    marker=0,
    timeout=30
))
```

* Ссылка на асинхронный пример: [GetUpdatesAsync.py](./examples/async/GetUpdatesAsync.py)

```python
response = await bot.subscriptions.GetUpdatesAsync(GetUpdatesReq(
    marker=0,
    timeout=30
))
```

-----

## Список примеров

| Описание                                       | Ссылка на пример                                             |
| ---------------------------------------------- | ------------------------------------------------------------ |
| Как отправить сообщение                        | [SendMessage.py](./examples/sync/SendMessage.py)             |
| Как отправить сообщение *асинхронно*           | [SendMessageAsync.py](./examples/async/SendMessageAsync.py)  |
| Как получить информацию о боте                 | [GetBot.py](./examples/sync/GetBot.py)                       |
| Как получить информацию о боте *асинхронно*    | [GetBotAsync.py](./examples/async/GetBotAsync.py)            |
| Как загрузить файл                             | [UploadFile.py](./examples/sync/UploadFile.py)               |
| Как загрузить файл *асинхронно*                | [UploadFileAsync.py](./examples/async/UploadFileAsync.py)    |
| Как отправить файл                             | [SendFile.py](./examples/sync/SendFile.py)                   |
| Как отправить файл *асинхронно*                | [SendFileAsync.py](./examples/async/SendFileAsync.py)        |
| Как получить входящее уведомление              | [GetUpdates.py](./examples/sync/GetUpdates.py)               |
| Как получить входящее уведомление *асинхронно* | [GetUpdates.py](./examples/async/GetUpdatesAsync.py)         |

## Список всех методов библиотеки

| Метод API       | Описание                | Ссылка на документацию MAX                     | Ссылка на документацию библиотеки            |
|-----------------|-------------------------|------------------------------------------------|----------------------------------------------|
| `Bots.GetBot` | Получает информацию о боте | [GetBot](https://dev.max.ru/docs-api/methods/GET/me) | [GetBot](./docs/bots/GetBot.md) |
| `Bots.PatchBot` | Изменяет информацию о боте | | [PatchBot](./docs/bots/PatchBot.md) |
| `Chats.GetChats` | Возвращает список групповых чатов, в которых участвовал бот | [GetChats](https://dev.max.ru/docs-api/methods/GET/chats) | [GetChats](./docs/chats/GetChats.md) |
| `Chats.GetChat` | Возвращает информацию о групповом чате по его ID | [GetChat](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-) | [GetChat](./docs/chats/GetChat..md) |
| `Chats.EditChat` | Позволяет редактировать информацию о групповом чате | [EditChat](https://dev.max.ru/docs-api/methods/PATCH/chats/-chatId-) | [EditChat](./docs/chats/EditChat.md) |
| `Chats.DeleteChat` | Удаляет групповой чат для всех участников | [DeleteChat](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-) | [DeleteChat](./docs/chats/DeleteChat.md) |
| `Chats.SendAction` | Позволяет отправлять следующие действия бота в групповой чат | [SendAction](https://dev.max.ru/docs-api/methods/POST/chats/-chatId-/actions) | [SendAction](./docs/chats/SendAction.md) |
| `Chats.GetPinnedMessage` | Возвращает закрепленное сообщение в чате | [GetPinnedMessage](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-/pin) | [GetPinnedMessage](./docs/chats/GetPinnedMessage.md) |
| `Chats.PinMessage` | Закрепляет сообщение в групповом чате | [PinMessage](https://dev.max.ru/docs-api/methods/PUT/chats/-chatId-/pin) | [PinMessage](./docs/chats/PinMessage.md) |
| `Chats.UnpinMessage` | Удаляет закрепленное сообщение в групповом чате | [UnpinMessage](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/pin) | [UnpinMessage](./docs/chats/UnpinMessage.md) |
| `Chats.GetChatMembership` | Возвращает членство бота в групповом чате | [GetChatMembership](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-/members/me) | [GetChatMembership](./docs/chats/GetChatMembership.md) |
| `Chats.LeaveChat` | Удаляет бота из группового чата | [LeaveChat](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members/me) | [LeaveChat](./docs/chats/LeaveChat.md) |
| `Chats.GetChatAdmins` | Возвращает список всех администраторов группового чата | [GetChatAdmins](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-/members/admins) | [GetChatAdmins](./docs/chats/GetChatAdmins.md) |
| `Chats.SetChatAdmins` | Назначает участника группы администратором | [SetChatAdmins](https://dev.max.ru/docs-api/methods/POST/chats/-chatId-/members/admins) | [SetChatAdmins](./docs/chats/SetChatAdmins.md) |
| `Chats.DeleteAdmin` | Отменяет права администратора пользователя в групповом чате | [DeleteAdmin](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members/admins/-userId-) | [DeleteAdmin](./docs/chats/DeleteAdmin.md) |
| `Chats.GetChatMembers` | Возвращает список участников группового чата | [GetChatMembers](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-/members) | [GetChatMembers](./docs/chats/GetChatMembers.md) |
| `Chats.AddMembers` | Добавляет участников в групповой чат | [AddMembers](https://dev.max.ru/docs-api/methods/POST/chats/-chatId-/members) | [AddMembers](./docs/chats/AddMembers.md) |
| `Chats.DeleteMember` | Удаляет участника из группового чата | [DeleteMember](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members) | [DeleteMember](./docs/chats/DeleteMember.md) |
| `Subscriptions.GetSubscriptions` | Возвращает список подписок на уведомления веб-хуков | [GetSubscriptions](https://dev.max.ru/docs-api/methods/GET/subscriptions) | [GetSubscriptions](./docs/subscriptions/GetSubscriptions.md) |
| `Subscriptions.Subscribe` | Настраивает доставку событий бота через веб-хук | [Subscribe](https://dev.max.ru/docs-api/methods/POST/subscriptions) | [Subscribe](./docs/subscriptions/Subscribe.md) |
| `Subscriptions.Unsubscribe` | Отменяет подписку бота на получение обновлений через веб-хук | [Unsubscribe](https://dev.max.ru/docs-api/methods/DELETE/subscriptions) | [Unsubscribe](./docs/subscriptions/Unsubscribe.md)|
| `Subscriptions.GetUpdates` | Получает входящие обновления | [GetUpdates](https://dev.max.ru/docs-api/methods/GET/updates) | [GetUpdates](./docs/subscriptions/GetUpdates.md) |
| `Upload.UploadFile` | Загружает файл на серверы MAX для последующей передачи | [UploadFile](https://dev.max.ru/docs-api/methods/POST/uploads) | [UploadFile](./docs/upload/UploadFile.md) |
| `Helpers.SendFile` | Упрощает отправку файлов, автоматически определяя URL или путь | | [SendFile](./docs/helpers/SendFile.md) |
| `Messages.GetMessages` | Возвращает информацию о сообщении или массив сообщений из чата | [GetMessages](https://dev.max.ru/docs-api/methods/GET/messages) | [GetMessages](./docs/messages/GetMessages.md) |
| `Messages.SendMessage` | Отправляет текстовое или медиа-сообщение указанному пользователю или в чат | [SendMessage](https://dev.max.ru/docs-api/methods/POST/messages) | [SendMessage](./docs/messages/SendMessage.md) |
| `Messages.EditMessage` | Редактирует текст или медиафайл ранее отправленного сообщения | [EditMessage](https://dev.max.ru/docs-api/methods/PUT/messages) | [EditMessage](./docs/messages/EditMessage.md) |
| `Messages.DeleteMessage` | Удаляет сообщение из чата | [DeleteMessage](https://dev.max.ru/docs-api/methods/DELETE/messages) | [DeleteMessage](./docs/messages/DeleteMessage.md) |
| `Messages.GetMessage` | Извлекает содержимое и метаданные конкретного сообщения по его ID | [GetMessage](https://dev.max.ru/docs-api/methods/GET/messages/-messageId-) | [GetMessage](./docs/messages/GetMessage.md) |
| `Messages.GetVideoInfo` | Возвращает подробную информацию о прикрепленном видео | [GetVideoInfo](https://dev.max.ru/docs-api/methods/GET/videos/-videoToken-) | [GetVideoInfo](./docs/messages/GetVideoInfo.md) |
| `Messages.AnswerCallback` | Отправляет ответ после того, как пользователь нажмет кнопку | [AnswerCallback](https://dev.max.ru/docs-api/methods/POST/answers) | [AnswerCallback](./docs/messages/AnswerCallback.md)|
