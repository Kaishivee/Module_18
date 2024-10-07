# from django.shortcuts import render
# from django.views.generic import TemplateView


def main_page(request):
    title = 'Главная страница'
    text1 = 'Главная'
    text2 = 'Магазин'
    text3 = 'Корзина'
    context = {
        'title': title,
        'text1': text1,
        'text2': text2,
        'text3': text3,
    }
    return render(request, 'third_task/platform.html', context)


def games_list(request):
    title = 'Игры'
    game1 = 'Genshin Impact'
    game2 = 'Fortnight'
    game3 = 'Rust'
    context = {
        'title': title,
        'game1': game1,
        'game2': game2,
        'game3': game3,
    }
    return render(request, 'third_task/games.html', context)


def show_cart(request):
    title = 'Корзина'
    empty_cart = 'Извините, Ваша корзина пуста'
    back_home = 'Вернуться обратно'
    context = {
        'title': title,
        'empty_cart': empty_cart,
        'back_home': back_home,
    }
    return render(request, 'third_task/cart.html', context)

