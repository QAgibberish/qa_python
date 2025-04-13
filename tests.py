from main import BooksCollector
import pytest
class TestBooksCollector:

    def test_add_new_book_same_books(self):
        collector = BooksCollector()
        collector.add_new_book('Муму')
        collector.add_new_book('Муму')
        assert len(collector.books_genre) == 1

    def test_set_book_genre_to_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Этой книги нет', 'Фантастика')
        assert 'Этой книги нет' not in collector.books_genre

    def test_get_book_genre_for_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Маугли')
        assert collector.get_book_genre('Маугли') == ''

    def test_get_books_with_specific_genre_nonexistent_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Шестерка воронов')
        collector.set_book_genre('Шестерка воронов','Фантастика')
        result = collector.get_books_with_specific_genre('Комикс')
        assert result == []

    def test_get_books_genre_two_different_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Ведьмак')
        collector.add_new_book('Утраченный символ')
        collector.set_book_genre('Ведьмак', 'Фантастика')
        collector.set_book_genre('Утраченный символ', 'Детективы')
        result = {'Ведьмак': 'Фантастика', 'Утраченный символ': 'Детективы'}
        assert collector.get_books_genre() == result

    def test_get_books_for_children_adult_book(self):
        collector = BooksCollector()
        collector.add_new_book('Зов Ктулху')
        collector.set_book_genre('Зов Ктулху', 'Ужасы')
        assert 'Зов Ктулху' not in collector.get_books_for_children()

    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.add_book_in_favorites('Хоббит')
        collector.add_book_in_favorites('Хоббит')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Хоббит']
        assert len(favorites) == 1

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Остров сокровищ')
        collector.add_book_in_favorites('Остров сокровищ')
        collector.delete_book_from_favorites('Остров сокровищ')
        assert 'Остров сокровищ' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_empty_list(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize(
        'genre, count',
        [
            ['Фантастика', 2],
            ['Ужасы', 1]
        ]
    )
    def test_get_books_with_specific_genre_three_books(self, genre, count):
        collector = BooksCollector()
        collector.add_new_book('Тайная комната')
        collector.add_new_book('Узник Азкабана')
        collector.add_new_book('Оно')
        collector.set_book_genre('Тайная комната','Фантастика')
        collector.set_book_genre('Узник Азкабана', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')
        assert len(collector.get_books_with_specific_genre(genre)) == count