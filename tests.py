from main import BooksCollector
import pytest
class TestBooksCollector:

    def test_add_new_book_once(self):
        collector = BooksCollector()
        collector.add_new_book('Философский камень')
        assert 'Философский камень' in collector.books_genre

    def test_add_new_book_same_books(self):
        collector = BooksCollector()
        collector.add_new_book('Муму')
        collector.add_new_book('Муму')
        assert len(collector.books_genre) == 1

    def test_set_book_genre_to_existing_book(self):
        collector = BooksCollector()
        collector.books_genre = {'Кубок Огня': ''}
        collector.set_book_genre('Кубок Огня', 'Фантастика')
        assert collector.books_genre['Кубок Огня'] == 'Фантастика'

    def test_get_books_with_specific_genre_two_books(self):
        collector = BooksCollector()
        collector.books_genre = {
            'Малыш и Карлсон': 'Мультфильмы',
            'Маленький принц': 'Мультфильмы'
        }
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Малыш и Карлсон', 'Маленький принц']

    def test_get_books_with_specific_genre_nonexistent_genre(self):
        collector = BooksCollector()
        collector.books_genre = {'Шестерка воронов': 'Фантастика'}
        result = collector.get_books_with_specific_genre('Комикс')
        assert result == []

    def test_get_books_genre_two_different_genres(self):
        collector = BooksCollector()
        collector.books_genre = {
            'Ведьмак': 'Фантастика',
            'Утраченный символ': 'Детективы'
        }
        result = {'Ведьмак': 'Фантастика', 'Утраченный символ': 'Детективы'}
        assert collector.get_books_genre() == result

    def test_get_books_for_children_one_book(self):
        collector = BooksCollector()
        collector.books_genre = {'Три поросенка': 'Мультфильмы'}
        assert 'Три поросенка' in collector.get_books_for_children()

    def test_add_book_in_favorites_once(self):
        collector = BooksCollector()
        collector.books_genre = {'Властелин колец': 'Фантастика'}
        collector.add_book_in_favorites('Властелин колец')
        assert 'Властелин колец' in collector.favorites

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()
        collector.favorites = ['Остров сокровищ']
        collector.delete_book_from_favorites('Остров сокровищ')
        assert 'Остров сокровищ' not in collector.favorites

    def test_get_list_of_favorites_books_one_book(self):
        collector = BooksCollector()
        collector.favorites = ['Орден феникса']
        assert collector.get_list_of_favorites_books() == ['Орден феникса']

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
        collector.books_genre = {
            'Тайная комната': 'Фантастика',
            'Узник Азкабана': 'Фантастика',
            'Оно': 'Ужасы'
        }
        assert len(collector.get_books_with_specific_genre(genre)) == count