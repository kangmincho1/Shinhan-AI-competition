## 신한AI, 보다 나은 금융 생활을 위한 AI 서비스 아이디어 경진대회


### Overview
코로나19의 엔데믹이 다가오면서 해외여행을 계획하는 사람들이 많아지고 있습니다. 이에 따라, 많은 사람들이 해외여행을 고려하고 있습니다. 해외여행을 하는데에 있어서 환전은 필수적이며, 저렴하게 환전을 할 수 있다면 좋을 것입니다.
이 프로젝트의 목적은 여행객들에게 최적의 환전 타이밍을 제공하여 환전을 도와줌으로써, 금전적인 손실을 최소화하여 여행에 대한 부담을 덜어주고, 신한은행의 환전서비스를 이용하게끔 유도하는 것입니다.
저희는 크게 두가지의 서비스에 대한 아이디어를 제시합니다.

- 환전 타이밍 추천 서비스: 여행객들이 가고자하는 국가의 환율을 예측하여, 환율이 저렴한 시점을 추천해 그 시점에 환전을 하게끔 하는 서비스
![image](https://github.com/kangmincho1/ShinhanAI-competition/assets/72463778/19663055-448e-42dc-a13a-9a4ca77024e0)

- 특정 기간의 저렴한 환율 국가 추천 서비스: 아직 여행지를 정하지 못한 여행객들을 위하여, 여러 국가의 환율을 예측하여 특정 기간에서 환율이 저렴한 국가를 추천해주는 서비스
![image](https://github.com/kangmincho1/ShinhanAI-competition/assets/72463778/d507cefe-aa5d-455f-9ac1-63e04d8b43c1)

### Data
데이터는 한국, 미국, 일본, 유로존, 영국의 2013년 1월 1일부터 2022년 12월 31일까지의 환율, 국가별 주식시장, 국채금리(1~3년), 국가별 GDP, 소비자 물가 지수(CPI), 소비자 신뢰 지수(CCI), 실업률로 이루어져있습니다.

데이터의 출처는 인베스팅닷컴, 야후파이낸스입니다.
- https://kr.investing.com/
- https://finance.yahoo.com/

### Models and Evaluation
- Nerwork: CNN
- Metrics: MSE, MAE, MAPE, DTW

### Rank
A total of 1196 participants
22nd out of 67 teams
