from .models import Page
import random  # random 모듈 import


def validate_pages():
    pages = Page.objects.all()
    for page in pages:
        if page.score < 0 or page.score > 10:  # 만약 범위를 벗어난다면
            page.score = random.randint(0, 10)  # 0~10 사이의 무작위 정수로 수정하고
            page.save()  # 저장합니다.
