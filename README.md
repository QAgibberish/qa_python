# Тестирование класса BooksCollector
## Реализованные тесты
- `test_add_new_book_same_books` - проверяет невозможность добавления дубликатов книг
- `test_set_book_genre_to_nonexistent_book` - проверяет невозможность установки жанра для несуществующей книги
- `test_get_book_genre_for_book_without_genre` - проверяет невозможность получения жанра для книги, которой жанр не задан
- `test_get_books_with_specific_genre_nonexistent_genre` - проверяет вывод пустого списка книг по несуществующему жанру
- `test_get_books_genre_two_different_genres` - проверяет получение словаря жанров
- `test_get_books_for_children_adult_book` - проверяет исключение книг со "взрослым" возрастным рейтингом 
- `test_add_book_in_favorites_twice` - проверяет невозможность повторного добавления книги в избранное
- `test_delete_book_from_favorites_one_book` - проверяет удаление книги из избранного
- `test_get_list_of_favorites_books_empty_list` - проверяет вывод пустого списка избранного
- `test_get_books_with_specific_genre` (параметризованный) - проверяет фильтрацию по жанрам