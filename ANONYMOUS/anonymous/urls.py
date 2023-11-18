from django.urls import path
from board.views import board

urlpatterns = [
    # path('url', function), # ''로 들어오면, function을 실행시켜 줘
    path("", board, name="board"), # 아무것도 없는 주소로 들어오면 ? board라는 함수를 실행시켜. 이름은 board로 지정 ?
]
