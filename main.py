import argparse


def main():
    parser = argparse.ArgumentParser(description='Инструмент визуализации графа зависимостей для менеджера пакетов')
    parser.add_argument('-n', '--packet_name', type=str, help='Имя анализируемого пакета')
    parser.add_argument('-u', '--url_link_repo', type=str,
                        help='URL-адрес репозитория или путь к файлу тестового репозитория')
    parser.add_argument('-m', '--repo_work_mode', type=str, help='Режим работы с тестовым репозиторием')
    parser.add_argument('-v', '--packet_version', type=str, help='Версия пакета')
    parser.add_argument('-a', '--ascii_tree', action='store_true',
                        help='Режим вывода зависимостей в формате ASCII-дерева')
    parser.add_argument('-f', '--packet_filter', type=str, help='Подстрока для фильтрации пакетов')

    args = parser.parse_args()

    print("Параметры, настраиваемые пользователем:")
    print(f"Имя анализируемого пакета: {args.packet_name}")
    print(f"URL-адрес репозитория или путь к файлу тестового репозитория: {args.url_link_repo}")
    print(f"Режим работы с тестовым репозиторием: {args.repo_work_mode}")
    print(f"Версия пакета: {args.packet_version}")
    print(f"Режим вывода зависимостей в формате ASCII-дерева: {'Включен' if args.ascii_tree else 'Выключен'}")
    print(f"Подстрока для фильтрации пакетов: {args.packet_filter}")
    print()

    errors = []

    if args.packet_name is None:
        errors.append("Не указано имя анализируемого пакета")

    if args.url_link_repo is None:
        errors.append("Не указан URL-адрес репозитория или путь к файлу тестового репозитория")

    if args.repo_work_mode is None:
        errors.append("Не указан режим работы с тестовым репозиторием")

    if args.packet_version is None:
        errors.append("Не указана версия пакета")

    if args.packet_filter is None:
        errors.append("Не указана подстрока для фильтрации пакетов")

    if args.packet_name and len(args.packet_name.strip()) == 0:
        errors.append("Имя пакета не может быть пустым")

    if args.url_link_repo and len(args.url_link_repo.strip()) == 0:
        errors.append("URL-адрес репозитория не может быть пустым")

    if args.repo_work_mode and args.repo_work_mode not in ['test', 'production']:
        errors.append("Режим работы с репозиторием должен быть 'test' или 'production'")

    if errors:
        print("Обнаружены ошибки в параметрах:")
        for error in errors:
            print(f"- {error}")
        exit(1)
    else:
        print("Все параметры корректны")


if __name__ == "__main__":
    main()