# MAX BOT API Client (Python)

`maxbot-api-client-python` — это библиотека для интеграции с **MAX BOT API**. Этот проект предоставляет структурированный интерфейс для взаимодействия с конфигурациями бота, управления сообщениями, отправки медиафайлов и подписки на события через *long-polling*.  

Для использования библиотеки потребуется получить токен бота в консоли разработчика MAX bot.    
Ознакомиться с инструкцией можно [по ссылке](https://green-api.com/max-bot-api/docs/before-start/).     

## API

Документацию по **REST API MAX** можно найти по ссылке [dev.max.ru/docs-api](https://dev.max.ru/docs-api). Библиотека является оберткой для REST API, поэтому документация по указанной выше ссылке также применима к используемым здесь моделям.

Документацию по **MAX BOT API** можно найти по ссылке [green-api.com/max-bot-api/docs](https://green-api.com/max-bot-api/docs/).

## Поддержка

[![Support](https://img.shields.io/badge/support@green--bot.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:support@green-bot.com)
[![Support](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/greenapi_support_ru_bot)
[![Support](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/77780739095)

## Руководства и новости

[![Guides](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://www.youtube.com/@green-api)
[![News](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/green_api)
[![News](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029VaHUM5TBA1f7cG29nO1C)

## Установка

**Убедитесь, что у вас установлен Python версии 3.12 или выше:**

```shell
python --version
````

**Установите библиотеку:**

```bash
pip install maxbot-api-client-python
```

**Импорт:**

```python
from maxbot_api_client_python import API, Config
```

## Использование и примеры

**Параметры конфигурации:** 

- `base_url` - Базовый URL-адрес серверов платформы MaxBot. Все методы API будут отправляться по этому корневому адресу. Актуальный адрес указан в [официальной документации](https://dev.max.ru/docs-api).
- `token` - Уникальный секретный ключ авторизации (API-ключ) вашего бота. Получить его можно в личном кабинете после [регистрации или создании бота](https://green-api.com/max-bot-api/docs/before-start/) на платформе [business.max.ru](https://business.max.ru/).
- `ratelimiter` - Встроенный ограничитель частоты запросов. Он контролирует количество исходящих запросов в секунду (RPS), защищая бота от блокировки со стороны сервера за превышение лимитов. Рекомендуемое значение — не менее 25.
- `timeout` - Максимальное время ожидания ответа от сервера (в секундах). Если сервер не ответит в течение этого времени, запрос будет завершен с ошибкой. Оптимальное значение — 30 секунд.

**Как инициализировать клиент:**

Использование контекстного менеджера (`with` / `async with`) гарантирует, что все сетевые соединения будут автоматически и безопасно закрыты по завершении работы.

```python
from maxbot_api_client_python import API, Config

cfg = Config(
    base_url="https://platform-api.max.ru",
    token="YOUR_BOT_TOKEN",
    ratelimiter=25,
    timeout=30
)
# Синхронный режим:
with API(cfg) as bot:
    pass
# Асинхронный режим:
async with API(cfg) as bot:
    pass
```

**Как получить информацию о боте:**

* Ссылка на синхронный пример: [GetBot.py](./examples/sync/GetBot.py)

```python
with API(cfg) as bot:
    response = bot.bots.GetBot()
```

* Ссылка на асинхронный пример: [GetBotAsync.py](./examples/async/GetBotAsync.py)

```python
async with API(cfg) as bot:
    response = await bot.bots.GetBotAsync()
```

**Как отправить сообщение:**

* Ссылка на синхронный пример: [SendMessage.py](./examples/sync/SendMessage.py)


```python
with API(cfg) as bot:
    response = bot.messages.SendMessage(
        user_id=1234567890,
        text="Hello world!"
    )
```

* Ссылка на асинхронный пример: [SendMessageAsync.py](./examples/async/SendMessageAsync.py)

```python
async with API(cfg) as bot:
    response = await bot.messages.SendMessageAsync(
        user_id=1234567890,
        text="Hello world from Async!"
    )
```

**Как легко отправить файл (по ссылке или локальный):**

* Ссылка на синхронный пример: [SendFile.py](./examples/sync/SendFile.py)

```python
with API(cfg) as bot:
    response = bot.helpers.SendFile(
        chat_id=1234567890,
        text="Check this!",
        file_source="[https://http.cat/200.jpg](https://http.cat/200.jpg)"
    )
```
* Ссылка на асинхронный пример: [SendFileAsync.py](./examples/async/SendFileAsync.py)

```python
async with API(cfg) as bot:
    response = await bot.helpers.SendFileAsync(
        chat_id=1234567890,
        text="Посмотри на этот файл!",
        file_source="[https://http.cat/200.jpg](https://http.cat/200.jpg)"
    )
```

**Как вручную загрузить файл (для кастомных вложений):**

* Ссылка на синхронный пример: [UploadFile.py](./examples/sync/UploadFile.py)

```python
from maxbot_api_client_python.types.constants import UploadType

with API(cfg) as bot:
    response = bot.uploads.UploadFile(
        type=UploadType.image,
        file_path="examples/assets/file.jpg"
    )
```

* Ссылка на асинхронный пример: [UploadFileAsync.py](./examples/async/UploadFileAsync.py)

```python
from maxbot_api_client_python.types.constants import UploadType

async with API(cfg) as bot:
    response = await bot.uploads.UploadFileAsync(
        type=UploadType.image,
        file_path="examples/assets/file.jpg"
    )
```

**Как получить входящее уведомление (Long Polling):**

* Ссылка на синхронный пример: [GetUpdates.py](./examples/sync/GetUpdates.py)

```python
with API(cfg) as bot:
    response = bot.subscriptions.GetUpdates(
        marker=0,
        timeout=30
    )
```

* Ссылка на асинхронный пример: [GetUpdatesAsync.py](./examples/async/GetUpdatesAsync.py)

```python
async with API(cfg) as bot:
    response = await bot.subscriptions.GetUpdatesAsync(
        marker=0,
        timeout=30
    )
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
| Как получить входящее уведомление *асинхронно* | [GetUpdatesAsync.py](./examples/async/GetUpdatesAsync.py)    |

## Список всех методов библиотеки

| Метод API       | Описание                | Ссылка на документацию MAX                     | Ссылка на документацию библиотеки            |
|-----------------|-------------------------|------------------------------------------------|----------------------------------------------|
| `Bots.GetBot`    | Получает информацию о боте | [GetBot](https://dev.max.ru/docs-api/methods/GET/me) | [GetBot](https://green-api.com/max-bot-api/docs/api/bots/GetBot/) |
| `Bots.PatchBot`  | Изменяет информацию о боте | | [PatchBot](https://green-api.com/max-bot-api/docs/api/bots/PatchBot/) |
| `Chats.GetChats` | Возвращает список групповых чатов, в которых участвовал бот | [GetChats](https://dev.max.ru/docs-api/methods/GET/chats) | [GetChats](https://green-api.com/max-bot-api/docs/api/chats/GetChats) |
| `Chats.GetChat`  | Возвращает информацию о групповом чате по его ID | [GetChat](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-) | [GetChat](https://green-api.com/max-bot-api/docs/api/chats/GetChat) |
| `Chats.EditChat` | Позволяет редактировать информацию о групповом чате | [EditChat](https://dev.max.ru/docs-api/methods/PATCH/chats/-chatId-) | [EditChat](https://green-api.com/max-bot-api/docs/api/chats/EditChat) |
| `Chats.DeleteChat` | Удаляет групповой чат для всех участников | [DeleteChat](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-) | [DeleteChat](https://green-api.com/max-bot-api/docs/api/chats/DeleteChat) |
| `Chats.SendAction` | Позволяет отправлять следующие действия бота в групповой чат | [SendAction](https://dev.max.ru/docs-api/methods/POST/chats/-chatId-/actions) | [SendAction](https://green-api.com/max-bot-api/docs/api/chats/SendAction) |
| `Chats.GetPinnedMessage` | Возвращает закрепленное сообщение в чате | [GetPinnedMessage](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-/pin) | [GetPinnedMessage](https://green-api.com/max-bot-api/docs/api/chats/GetPinnedMessage) |
| `Chats.PinMessage` | Закрепляет сообщение в групповом чате | [PinMessage](https://dev.max.ru/docs-api/methods/PUT/chats/-chatId-/pin) | [PinMessage](https://green-api.com/max-bot-api/docs/api/chats/PinMessage) |
| `Chats.UnpinMessage` | Удаляет закрепленное сообщение в групповом чате | [UnpinMessage](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/pin) | [UnpinMessage](https://green-api.com/max-bot-api/docs/api/chats/UnpinMessage) |
| `Chats.GetChatMembership` | Возвращает членство бота в групповом чате | [GetChatMembership](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-/members/me) | [GetChatMembership](https://green-api.com/max-bot-api/docs/api/chats/GetChatMembership) |
| `Chats.LeaveChat` | Удаляет бота из группового чата | [LeaveChat](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members/me) | [LeaveChat](https://green-api.com/max-bot-api/docs/api/chats/LeaveChat) |
| `Chats.GetChatAdmins` | Возвращает список всех администраторов группового чата | [GetChatAdmins](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-/members/admins) | [GetChatAdmins](https://green-api.com/max-bot-api/docs/api/chats/GetChatAdmins) |
| `Chats.SetChatAdmins` | Назначает участника группы администратором | [SetChatAdmins](https://dev.max.ru/docs-api/methods/POST/chats/-chatId-/members/admins) | [SetChatAdmins](https://green-api.com/max-bot-api/docs/api/chats/SetChatAdmins) |
| `Chats.DeleteAdmin` | Отменяет права администратора пользователя в групповом чате | [DeleteAdmin](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members/admins/-userId-) | [DeleteAdmin](https://green-api.com/max-bot-api/docs/api/chats/DeleteAdmin) |
| `Chats.GetChatMembers`     | Возвращает список участников группового чата | [GetChatMembers](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-/members) | [GetChatMembers](https://green-api.com/max-bot-api/docs/api/chats/GetChatMembers) |
| `Chats.AddMembers`         | Добавляет участников в групповой чат | [AddMembers](https://dev.max.ru/docs-api/methods/POST/chats/-chatId-/members) | [AddMembers](https://green-api.com/max-bot-api/docs/api/chats/AddMembers) |
| `Chats.DeleteMember` | Удаляет участника из группового чата | [DeleteMember](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members) | [DeleteMember](https://green-api.com/max-bot-api/docs/api/chats/DeleteMember) |
| `Subscriptions.GetSubscriptions` | Возвращает список подписок на уведомления веб-хуков | [GetSubscriptions](https://dev.max.ru/docs-api/methods/GET/subscriptions) | [GetSubscriptions](https://green-api.com/max-bot-api/docs/api/subscriptions/GetSubscriptions) |
| `Subscriptions.Subscribe`        | Настраивает доставку событий бота через веб-хук | [Subscribe](https://dev.max.ru/docs-api/methods/POST/subscriptions) | [Subscribe](https://green-api.com/max-bot-api/docs/api/subscriptions/Subscribe.md)  |
| `Subscriptions.Unsubscribe` | Отменяет подписку бота на получение обновлений через веб-хук | [Unsubscribe](https://dev.max.ru/docs-api/methods/DELETE/subscriptions) | [Unsubscribe](https://green-api.com/max-bot-api/docs/api/subscriptions/Unsubscribe) |
| `Subscriptions.GetUpdates` | Получает входящие обновления | [GetUpdates](https://dev.max.ru/docs-api/methods/GET/updates) | [GetUpdates](https://green-api.com/max-bot-api/docs/api/subscriptions/GetUpdates) |
| `Upload.UploadFile` | Загружает файл на серверы MAX для последующей передачи | [UploadFile](https://dev.max.ru/docs-api/methods/POST/uploads) | [UploadFile](https://green-api.com/max-bot-api/docs/upload/UploadFile) |
| `Helpers.SendFile` | Упрощает отправку файлов, автоматически определяя URL или путь | | [SendFile](https://green-api.com/max-bot-api/docs/helpers/SendFile) |
| `Messages.GetMessages` | Возвращает информацию о сообщении или массив сообщений из чата | [GetMessages](https://dev.max.ru/docs-api/methods/GET/messages) | [GetMessages](https://green-api.com/max-bot-api/docs/api/messages/GetMessages) |
| `Messages.SendMessage` | Отправляет текстовое или медиа-сообщение указанному пользователю или в чат | [SendMessage](https://dev.max.ru/docs-api/methods/POST/messages) | [SendMessage](https://green-api.com/max-bot-api/docs/api/messages/SendMessage) |
| `Messages.EditMessage` | Редактирует текст или медиафайл ранее отправленного сообщения | [EditMessage](https://dev.max.ru/docs-api/methods/PUT/messages) | [EditMessage](https://green-api.com/max-bot-api/docs/api/messages/EditMessage) |
| `Messages.DeleteMessage` | Удаляет сообщение из чата | [DeleteMessage](https://dev.max.ru/docs-api/methods/DELETE/messages) | [DeleteMessage](https://green-api.com/max-bot-api/docs/api/messages/DeleteMessage) |
| `Messages.GetMessage` | Извлекает содержимое и метаданные конкретного сообщения по его ID | [GetMessage](https://dev.max.ru/docs-api/methods/GET/messages/-messageId-) | [GetMessage](https://green-api.com/max-bot-api/docs/api/messages/GetMessage) |
| `Messages.GetVideoInfo` | Возвращает подробную информацию о прикрепленном видео | [GetVideoInfo](https://dev.max.ru/docs-api/methods/GET/videos/-videoToken-) | [GetVideoInfo](https://green-api.com/max-bot-api/docs/api/messages/GetVideoInfo) |
| `Messages.AnswerCallback` | Отправляет ответ после того, как пользователь нажмет кнопку | [AnswerCallback](https://dev.max.ru/docs-api/methods/POST/answers) | [AnswerCallback](https://green-api.com/max-bot-api/docs/api/messages/AnswerCallback )|
