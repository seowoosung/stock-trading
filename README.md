# stock-trading

### 사용법

* python3.7 32bit 설치

http://blog.quantylab.com/anaconda32env.html 참고

* Git bash 다운

https://gbsb.tistory.com/10 참고

* 소스코드 다운받기
1. Git bash 실행
2. $ git clone https://github.com/tvengers/stock-trading.git

* EBest open api 다운받기

* RES파일 다운받기
https://wikidocs.net/3683 참고

* 소스코드에 기본적인 셋팅하기
1. Git bash 실행
2. 다운받은 python32 bit 실행(anaconda3 실행) 
3. 명령어 입력
```bash
$ cd stock-trading/stock_trading
$ pip install -r requirements.txt
$ cp .env-example .env
# .env가서 아이디 비번 등 설정
```

* 실행명령어
```bash
$ python manage.py runserver
```
