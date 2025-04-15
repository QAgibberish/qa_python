# Тестирование класса BooksCollector
## Реализованные тесты
- `test_add_new_book_once` - проверяет возможность добавления книги в словарь
- `test_add_new_book_same_books` - проверяет невозможность добавления дубликатов книг
- `test_set_book_genre_to_existing_book` - проверяет возможность установки жанра для книги
- `test_get_books_with_specific_genre_two_books` - проверяет вывод списка книг по жанру
- `test_get_books_with_specific_genre_nonexistent_genre` - проверяет вывод пустого списка книг по несуществующему жанру
- `test_get_books_genre_two_different_genres` - проверяет получение словаря жанров
- `test_get_books_for_children_one_book` - проверяет вывод книг, которые подходят для детского чтения
- `test_add_book_in_favorites_once` - проверяет возможность добавления книги в избранное
- `test_delete_book_from_favorites_one_book` - проверяет удаление книги из избранного
- `test_get_list_of_favorite_books_one_book` - проверяет вывод списка избранного
- `test_get_list_of_favorites_books_empty_list` - проверяет вывод пустого списка избранного
- `test_get_books_with_specific_genre` (параметризованный) - проверяет фильтрацию по жанрам
- `test_get_book_genre_for_existing_genre` - проверяет вывод жанра книги по её имени