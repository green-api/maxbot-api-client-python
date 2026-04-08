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

* Ссылка на синхронный пример: [get_bot.py](./examples/sync/get_bot.py)

```python
with API(cfg) as bot:
    response = bot.bots.get_bot()
```

* Ссылка на асинхронный пример: [get_bot_async.py](./examples/async/get_bot_async.py)

```python
async with API(cfg) as bot:
    response = await bot.bots.get_bot_async()
```

**Как отправить сообщение:**

* Ссылка на синхронный пример: [send_message.py](./examples/sync/send_message.py)


```python
with API(cfg) as bot:
    response = bot.messages.get_messages(
        user_id=1234567890,
        text="Hello world!"
    )
```

* Ссылка на асинхронный пример: [get_messages_async.py](./examples/async/get_messages_async.py)

```python
async with API(cfg) as bot:
    response = await bot.messages.get_messages_async(
        user_id=1234567890,
        text="Hello world from Async!"
    )
```

**Как легко отправить файл (по ссылке или локальный):**

* Ссылка на синхронный пример: [send_file.py](./examples/sync/send_file.py)

```python
with API(cfg) as bot:
    response = bot.helpers.send_file(
        chat_id=1234567890,
        text="Check this!",
        file_source="https://storage.yandexcloud.net/sw-prod-03-test/ChatBot/corgi.jpg"
    )
```
* Ссылка на асинхронный пример: [send_file_async.py](./examples/async/send_file_async.py)

```python
async with API(cfg) as bot:
    response = await bot.helpers.send_file_async(
        chat_id=1234567890,
        text="Посмотри на этот файл!",
        file_source="https://storage.yandexcloud.net/sw-prod-03-test/ChatBot/corgi.jpg"
    )
```

**Как вручную загрузить файл (для кастомных вложений):**

* Ссылка на синхронный пример: [upload_file.py](./examples/sync/upload_file.py)

```python
from maxbot_api_client_python.types.constants import UploadType

with API(cfg) as bot:
    response = bot.uploads.upload_file(
        type=UploadType.image,
        file_path="examples/assets/file.jpg"
    )
```

* Ссылка на асинхронный пример: [upload_file_async.py](./examples/async/upload_file_async.py)

```python
from maxbot_api_client_python.types.constants import UploadType

async with API(cfg) as bot:
    response = await bot.uploads.upload_file_async(
        type=UploadType.image,
        file_path="examples/assets/file.jpg"
    )
```

**Как получить входящее уведомление (Long Polling):**

* Ссылка на синхронный пример: [get_updates.py](./examples/sync/get_updates.py)

```python
with API(cfg) as bot:
    response = bot.subscriptions.get_updates(
        marker=0,
        timeout=30
    )
```

* Ссылка на асинхронный пример: [get_updates_async.py](./examples/async/get_updates_async.py)

```python
async with API(cfg) as bot:
    response = await bot.subscriptions.get_updates_async(
        marker=0,
        timeout=30
    )
```

-----

## Список примеров

| Описание                                       | Ссылка на пример                                                 |
| ---------------------------------------------- | ---------------------------------------------------------------- |
| Как отправить сообщение                        | [send_message.py](./examples/sync/send_message.py)               |
| Как отправить сообщение *асинхронно*           | [get_messages_async.py](./examples/async/get_messages_async.py)  |
| Как получить информацию о боте                 | [get_bot.py](./examples/sync/get_bot.py)                         |
| Как получить информацию о боте *асинхронно*    | [get_bot_async.py](./examples/async/get_bot_async.py)            |
| Как загрузить файл                             | [upload_file.py](./examples/sync/upload_file.py)                 |
| Как загрузить файл *асинхронно*                | [upload_file_async.py](./examples/async/upload_file_async.py)    |
| Как отправить файл                             | [send_file.py](./examples/sync/send_file.py)                     |
| Как отправить файл *асинхронно*                | [send_file_async.py](./examples/async/send_file_async.py)        |
| Как получить входящее уведомление              | [get_updates.py](./examples/sync/get_updates.py)                 |
| Как получить входящее уведомление *асинхронно* | [get_updates_async.py](./examples/async/get_updates_async.py)    |

## Список всех методов библиотеки

| Метод API       | Описание                | Ссылка на документацию MAX                     | Ссылка на документацию MAX BOT API           |
|-----------------|-------------------------|------------------------------------------------|----------------------------------------------|
| `bots.get_bot`    | Получает информацию о боте | [get_bot](https://dev.max.ru/docs-api/methods/GET/me) | [GetBot](https://green-api.com/max-bot-api/docs/api/bots/GetBot/) |
| `bots.patch_bot`  | Изменяет информацию о боте | | [PatchBot](https://green-api.com/max-bot-api/docs/api/bots/PatchBot/) |
| `chats.get_chats` | Возвращает список групповых чатов, в которых участвовал бот | [get_chats](https://dev.max.ru/docs-api/methods/GET/chats) | [GetChats](https://green-api.com/max-bot-api/docs/api/chats/GetChats/) |
| `chats.get_chat`  | Возвращает информацию о групповом чате по его ID | [get_chat](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-) | [GetChat](https://green-api.com/max-bot-api/docs/api/chats/GetChat/) |
| `chats.edit_chat` | Позволяет редактировать информацию о групповом чате | [edit_chat](https://dev.max.ru/docs-api/methods/PATCH/chats/-chatId-) | [EditChat](https://green-api.com/max-bot-api/docs/api/chats/EditChat/) |
| `chats.delete_chat` | Удаляет групповой чат для всех участников | [delete_chat](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-) | [DeleteChat](https://green-api.com/max-bot-api/docs/api/chats/DeleteChat/) |
| `chats.send_action` | Позволяет отправлять следующие действия бота в групповой чат | [send_action](https://dev.max.ru/docs-api/methods/POST/chats/-chatId-/actions) | [SendAction](https://green-api.com/max-bot-api/docs/api/chats/SendAction) |
| `chats.get_pinned_message` | Возвращает закрепленное сообщение в чате | [get_pinned_message](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-/pin) | [GetPinnedMessage](https://green-api.com/max-bot-api/docs/api/chats/GetPinnedMessage) |
| `chats.pin_message` | Закрепляет сообщение в групповом чате | [pin_message](https://dev.max.ru/docs-api/methods/PUT/chats/-chatId-/pin) | [PinMessage](https://green-api.com/max-bot-api/docs/api/chats/PinMessage) |
| `chats.unpin_message` | Удаляет закрепленное сообщение в групповом чате | [unpin_message](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/pin) | [UnpinMessage](https://green-api.com/max-bot-api/docs/api/chats/UnpinMessage) |
| `chats.get_chat_membership` | Возвращает членство бота в групповом чате | [get_chat_membership](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-/members/me) | [GetChatMembership](https://green-api.com/max-bot-api/docs/api/chats/GetChatMembership) |
| `chats.leave_chat` | Удаляет бота из группового чата | [leave_chat](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members/me) | [LeaveChat](https://green-api.com/max-bot-api/docs/api/chats/LeaveChat) |
| `chats.get_chat_admins` | Возвращает список всех администраторов группового чата | [get_chat_admins](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-/members/admins) | [GetChatAdmins](https://green-api.com/max-bot-api/docs/api/chats/GetChatAdmins) |
| `chats.set_chat_admins` | Назначает участника группы администратором | [set_chat_admins](https://dev.max.ru/docs-api/methods/POST/chats/-chatId-/members/admins) | [SetChatAdmins](https://green-api.com/max-bot-api/docs/api/chats/SetChatAdmins) |
| `chats.delete_admin` | Отменяет права администратора пользователя в групповом чате | [delete_admin](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members/admins/-userId-) | [DeleteAdmin](https://green-api.com/max-bot-api/docs/api/chats/DeleteAdmin) |
| `chats.get_chat_members`     | Возвращает список участников группового чата | [get_chat_members](https://dev.max.ru/docs-api/methods/GET/chats/-chatId-/members) | [GetChatMembers](https://green-api.com/max-bot-api/docs/api/chats/GetChatMembers) |
| `chats.add_members`         | Добавляет участников в групповой чат | [add_members](https://dev.max.ru/docs-api/methods/POST/chats/-chatId-/members) | [AddMembers](https://green-api.com/max-bot-api/docs/api/chats/AddMembers) |
| `chats.delete_member` | Удаляет участника из группового чата | [delete_member](https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members) | [DeleteMember](https://green-api.com/max-bot-api/docs/api/chats/DeleteMember) |
| `subscriptions.get_subscriptions` | Возвращает список подписок на уведомления веб-хуков | [get_subscriptions](https://dev.max.ru/docs-api/methods/GET/subscriptions) | [GetSubscriptions](https://green-api.com/max-bot-api/docs/api/subscriptions/GetSubscriptions) |
| `subscriptions.subscribe`        | Настраивает доставку событий бота через веб-хук | [subscribe](https://dev.max.ru/docs-api/methods/POST/subscriptions) | [Subscribe](https://green-api.com/max-bot-api/docs/api/subscriptions/Subscribe.md)  |
| `subscriptions.unsubscribe` | Отменяет подписку бота на получение обновлений через веб-хук | [unsubscribe](https://dev.max.ru/docs-api/methods/DELETE/subscriptions) | [Unsubscribe](https://green-api.com/max-bot-api/docs/api/subscriptions/Unsubscribe) |
| `subscriptions.get_updates` | Получает входящие обновления | [get_updates](https://dev.max.ru/docs-api/methods/GET/updates) | [GetUpdates](https://green-api.com/max-bot-api/docs/api/subscriptions/GetUpdates) |
| `upload.upload_file` | Загружает файл на серверы MAX для последующей передачи | [upload_file](https://dev.max.ru/docs-api/methods/POST/uploads) | [UploadFile](https://green-api.com/max-bot-api/docs/upload/UploadFile) |
| `helpers.send_file` | Упрощает отправку файлов, автоматически определяя URL или путь | | [SendFile](https://green-api.com/max-bot-api/docs/helpers/SendFile) |
| `messages.get_messages` | Возвращает информацию о сообщении или массив сообщений из чата | [get_messages](https://dev.max.ru/docs-api/methods/GET/messages) | [GetMessages](https://green-api.com/max-bot-api/docs/api/messages/GetMessages) |
| `messages.send_message` | Отправляет текстовое или медиа-сообщение указанному пользователю или в чат | [send_message](https://dev.max.ru/docs-api/methods/POST/messages) | [SendMessage](https://green-api.com/max-bot-api/docs/api/messages/SendMessage) |
| `messages.edit_message` | Редактирует текст или медиафайл ранее отправленного сообщения | [edit_message](https://dev.max.ru/docs-api/methods/PUT/messages) | [EditMessage](https://green-api.com/max-bot-api/docs/api/messages/EditMessage) |
| `messages.delete_message` | Удаляет сообщение из чата | [delete_message](https://dev.max.ru/docs-api/methods/DELETE/messages) | [DeleteMessage](https://green-api.com/max-bot-api/docs/api/messages/DeleteMessage) |
| `messages.get_message` | Извлекает содержимое и метаданные конкретного сообщения по его ID | [get_message](https://dev.max.ru/docs-api/methods/GET/messages/-messageId-) | [GetMessage](https://green-api.com/max-bot-api/docs/api/messages/GetMessage) |
| `messages.get_video_info` | Возвращает подробную информацию о прикрепленном видео | [get_video_info](https://dev.max.ru/docs-api/methods/GET/videos/-videoToken-) | [GetVideoInfo](https://green-api.com/max-bot-api/docs/api/messages/GetVideoInfo) |
| `messages.answer_callback` | Отправляет ответ после того, как пользователь нажмет кнопку | [answer_callback](https://dev.max.ru/docs-api/methods/POST/answers) | [AnswerCallback](https://green-api.com/max-bot-api/docs/api/messages/AnswerCallback )|
