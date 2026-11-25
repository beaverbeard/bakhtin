[Русский](README.md) · [English](README.en.md)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand/cover-ru-dark.svg">
  <img src="assets/brand/cover-ru-light.svg" alt="Бахтин — Специально для русского языка." width="1280">
</picture>

# Бахтин

**Специально для русского языка.** Пишет посты, письма и статьи по вашему брифу и материалам, учитывая нужный стиль.

[Как установить?](#как-установить) · [Примеры задач](#примеры-задач)

## Как это работает

Вы рассказываете, что хотите написать, для кого и зачем, и прикладываете материалы. Бахтин уточняет недостающее, продумывает, как раскрыть мысль, и пишет текст с учётом нужного стиля. Вы получаете черновик, который можно обсудить и доработать.


## Примеры задач

### Написать пост по заметкам

> Используй Бахтина. Напиши пост по моим заметкам для начинающих руководителей. Сначала уточни, чего не хватает для задачи. Не выдумывай факты и личный опыт.

### Подготовить письмо

> Напиши письмо клиенту по этому брифу. Объясни изменение сроков, что мы уже сделали и какое решение нужно от клиента. Сохрани спокойный и прямой тон.

### Объяснить сложную тему

> Подготовь статью по этим материалам для читателя без специальных знаний. Развивай одну мысль за раз, используй примеры из источников и отметь пробелы.


## Как установить?

### Для агентов

Claude Code, Codex / ChatGPT Desktop, Cursor, GitHub Copilot, Gemini CLI — отдайте агенту команду:

```text
Установи скилл «Бахтин»:
https://github.com/beaverbeard/bakhtin

Используй его, когда мы пишем или редактируем тексты.
```

<details>
<summary>Ещё варианты</summary>

Настройка для каждого агента: [Claude Code](docs/OTHER-APPS.ru.md#claude-code), [ChatGPT Desktop / Codex](docs/OTHER-APPS.ru.md#codex), [Cursor](docs/OTHER-APPS.ru.md#cursor), [GitHub Copilot](docs/OTHER-APPS.ru.md#copilot), [Gemini CLI](docs/OTHER-APPS.ru.md#gemini-cli).

### ChatGPT, Claude или Gemini в браузере

Скачайте [пакет этого скилла](docs/downloads/bakhtin.zip). Внутри — инструкции, скрипты и ресурсы.

- **ChatGPT:** создайте проект и добавьте инструкции и ресурсы из распакованного пакета. [По шагам](docs/OTHER-APPS.ru.md#chatgpt).
- **Claude:** включите выполнение кода и загрузите ZIP в Customize → Skills. [По шагам](docs/OTHER-APPS.ru.md#claude).
- **Gemini:** откройте Customize → Skills → Create → Upload и загрузите пакет. [По шагам](docs/OTHER-APPS.ru.md#gemini).

Доступные этапы зависят от инструментов приложения. [Как проверить готовность](docs/OTHER-APPS.ru.md#readiness).

### А лучше — вся Редколлегия

Установите [Редколлегию](https://github.com/beaverbeard/redkollegiya) вместе со всеми восемью скиллами: она подключит нужные инструменты для написания, редактуры и вычитки текста. Отдайте агенту команду:

```text
Установи Редколлегию и весь комплект из восьми редакционных скиллов:
https://github.com/beaverbeard/redkollegiya

Используй их, когда мы пишем или редактируем тексты.
```

</details>


## Когда понадобится ваше решение

Если неясны цель, читатель или исходные факты, Бахтин уточнит задачу. Проверьте черновик перед публикацией; полную редактуру и вычитку можно поручить [Редколлегии](https://github.com/beaverbeard/redkollegiya).

## Что внутри

Бахтин выполняет свою часть работы с текстом. Для полного процесса начните с [Редколлегии](https://github.com/beaverbeard/redkollegiya): она подключает нужные инструменты.

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/brand/system-map-ru-dark-narrow.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand/system-map-ru-dark.svg">
  <source media="(max-width: 600px)" srcset="assets/brand/system-map-ru-light-narrow.svg">
  <img src="assets/brand/system-map-ru-light.svg" alt="Взаимодействие редакционных скиллов: Бахтин" width="1280">
</picture>

Вся система состоит из восьми скиллов. Ниже — задачи каждого и ссылки на их репозитории.

| Скилл | Чем поможет |
|---|---|
| [Редколлегия / Redkollegiya](https://github.com/beaverbeard/redkollegiya) | Пишет и редактирует тексты. Помогает пройти путь от первого черновика до проверки фактов и финальной вычитки. |
| [Виноградов / Vinogradov](https://github.com/beaverbeard/vinogradov) | Помогает ИИ писать в вашем стиле: изучает ваши тексты и собирает профиль авторского голоса. |
| [Бахтин / Bakhtin](https://github.com/beaverbeard/bakhtin) | Пишет посты, письма и статьи по вашему брифу и материалам, учитывая нужный стиль. |
| [Чуковский / Chukovsky](https://github.com/beaverbeard/chukovsky) | Редактирует тексты. Выстраивает мысль, исправляет провалы в логике и убирает канцелярит. |
| [Аграновский / Agranovsky](https://github.com/beaverbeard/agranovsky) | Скилл-фактчекер для текстов. Проверяет цифры, даты, цитаты и ссылки, показывает источники. |
| [Слопотрон / Slopotron](https://github.com/beaverbeard/slopotron) | Очищает тексты от нейрослопа и AI-клише, которые всех бесят. |
| [Розенталь / Rozental](https://github.com/beaverbeard/rozental) | Скилл-корректор: проверяет и исправляет тексты. Находит ошибки в орфографии, пунктуации и грамматике. |
| [Мильчин / Milchin](https://github.com/beaverbeard/milchin) | Скилл-типограф: приводит текст к нормам русской типографики. Проверяет и исправляет кавычки, тире и пробелы. |

## Рассылка «рИИдактор»

В «рИИдакторе» мы разбираем, как писать и редактировать тексты с ИИ.

Учимся давать понятные задания, сохранять свой голос и замечать то, что нейросеть придумала за вас. Берите приёмы в работу, чтобы тратить меньше времени на переделки и увереннее выпускать тексты.

[Подписаться на рассылку →](https://redaktozavr.ru/rAIdactor?utm_source=skills)


## Совместимость и исходники

При подключении проверьте доступные инструменты выбранного приложения. Английская страница содержит перевод документации.

[SKILL.md](https://github.com/beaverbeard/bakhtin/blob/f966bd1ff0e632755141d989a30ff0dc9d662474/.claude/skills/bakhtin/SKILL.md) · [MIT](https://github.com/beaverbeard/bakhtin/blob/f966bd1ff0e632755141d989a30ff0dc9d662474/LICENSE)
