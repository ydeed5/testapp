Админка: admin/admin

Редирект на оплату идет сразу из функции checkout (buy/views), как написано здесь: https://stripe.com/docs/checkout/quickstart ("Prebuilt Checkout page").

## Копируем
```python
git clone https://github.com/ydeed5/testapp.git
cd testapp
```

## Запуск:
a) docker:
```python
sudo docker-compose up --build
```
или

b) обычный python:
```python
pip install -i requirements.txt
python project/manage.py runserver
```
(venv загружать не стал)


## Теперь проверяем в браузере:
1) https://127.0.0.1:8000/item/2 и нажать checkout,
2) перенаправит на страницу оплаты, номер карты 4242 4242 4242 4242, остальное - любые значения (https://stripe.com/docs/testing).



