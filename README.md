# proportion-of-stocks-above-MA
이평선 위에 있는 종목 비율 계산/ 데이터 확인용
<br>
<br>

### 메인아이디어

>주가가 이평선위에 존재한다면 대부분의 시장참여자가 이득을 보고 있다고 생각할 수 있다. 시장에 이런 종목이 얼마나 많이 있는가를 지표로 시장의 방향성을 확인한다.
본 프로그램의 목표는 다음과 같은 것들을 확인하는 것이다.<br>
ex) 주가가 10일 이평선 위에 있는 NASDAQ 종목의 비율.
해당 비율이 90%가 넘어가면 매도포지션, 10%에 가까워지면 매수포지션으로 변경하는 등 포지션 변경에 도움이 될 지표계산기다.

<br>
<br>

### 실행
```bash
$ python -m venv venv
$ pip install requirements.txt
$ cd core
$ python ma.py
```
<br>
<br>

### 결과 (2022-11-04)
![image](https://user-images.githubusercontent.com/67510613/199876345-035ec6ab-af50-4853-bc64-361623e62e99.png)

