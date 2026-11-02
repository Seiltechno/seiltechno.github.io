---
title: AiTWM
subtitle: AI 절삭공구 마모량 계측 솔루션 (AI Tool Wear Measurement)
category: AI 검사·측정
subcategory: 기상 AI분석
brand: AIMS
partner:
  name: ㈜에임즈 (AIMS)
  desc: AI 비전 기반 스마트 제조 솔루션 기업
  url: https://aims.kr/
  logo: /assets/img/partners/aims.png
order: 213
image: /assets/img/products/aims/twm-3.jpg
summary: 공구 이미지에서 여유면 마모량(VBmean·VBmax)을 딥러닝으로 자동 계측합니다. 공구를 빼지 않고 마모를 숫자로 관리해 공구 수명을 예측합니다.
tags: [마모량 계측, VBmean·VBmax, 공구 수명 예측]

highlights:
  - title: 마모를 숫자로
    text: 공구 이미지에서 평균 여유면 마모(VBmean)와 최대 여유면 마모(VBmax)를 자동으로 계측합니다.
  - title: 공구 탈착 없는 자동 측정
    text: 가공 중 기상 카메라 이미지로 측정하므로 공구를 빼서 측정 현미경으로 옮길 필요가 없습니다.
  - title: 측정 편차 감소
    text: 딥러닝 모델이 같은 기준으로 계측해 작업자에 따른 측정 오차를 줄이고 결과를 일관되게 유지합니다.
  - title: 이력 관리와 수명 예측
    text: 측정값이 자동 저장되고 공구별 마모 추이를 보여 주어, 교체 시점과 공구 수명을 미리 판단할 수 있습니다.
specs:
  - {label: 계측 항목, value: "평균 여유면 마모(VBmean), 최대 여유면 마모(VBmax)"}
  - {label: 계측 방식, value: "이미지 기반 딥러닝 예측 모델"}
  - {label: 진행 단계, value: "① 실시간 공구 이미지 획득 → ② 사전 학습된 딥러닝 모델 계측 → ③ 공구 마모량 계측"}
  - {label: 이미지 입력, value: "On-Machine Vision System 카메라 모듈 또는 사용자 이미지 입력"}
  - {label: 데이터 관리, value: "측정값 자동 저장, 공구별 마모 추이 시각화"}
  - {label: 연동, value: "On-Machine Vision System, 로봇, 각종 센서"}
  - {label: 시스템 구성, value: "카메라 시스템 → 엣지 서버 → 메인 서버(AI 모델) ↔ 사용자 PC"}
  - {label: 통신, value: "영상·이미지 TCP/UDP 전송, Flask API로 계측 요청·결과 수신"}
  - {label: 상세 사양, value: "계측 범위·분해능은 공구와 광학 구성에 따라 협의 (문의)"}
applications: [공구 마모 정량 관리, 공구 수명 시험, 가공 조건 최적화, 공구 교체 주기 설정]
process:
  - img: /assets/img/products/aims/twm-1.jpg
    step: "STEP 01"
    title: "실시간 공구 이미지 획득"
    text: "기상계측 카메라 모듈 또는 사용자가 입력한 이미지로 공구 날의 여유면을 촬영합니다."
  - img: /assets/img/products/aims/twm-2.jpg
    step: "STEP 02"
    title: "딥러닝 기반 예측 모델"
    text: "카메라 시스템이 엣지 서버를 거쳐 메인 서버의 AI 모델로 이미지를 보내고, 사용자 PC에서 계측을 요청하고 결과를 받습니다."
  - img: /assets/img/products/aims/twm-3.jpg
    step: "STEP 03"
    title: "공구 마모량 계측"
    text: "날마다 최대 여유면 마모(VBmax)를 표시하고, 측정 시각별 값과 평균을 표로 기록합니다."
compare:
  title: AiTCD와 AiTWM, 무엇이 다른가요?
  cols:
    - {name: AiTCD, sub: 공구 상태진단, slug: aims-aitcd}
    - {name: AiTWM, sub: 공구 마모량 계측, slug: aims-aitwm}
  rows:
    - ["알려 주는 것", "공구가 어떤 상태인지 (등급 판정)", "마모가 얼마나 진행됐는지 (수치 계측)"]
    - ["결과 형태", "새 공구(New) / 정상 마모(Worn) / 파손(Breakage)", "평균 여유면 마모 VBmean, 최대 여유면 마모 VBmax (mm)"]
    - ["판단 근거", "공구 이미지 + 센서 신호 데이터로 학습한 딥러닝 모델", "공구 이미지로 학습한 딥러닝 예측 모델"]
    - ["이럴 때", "파손 공구를 놓치지 않고, 교체 시점을 판단할 때", "공구 수명 관리, 마모 추이 분석, 가공 조건 비교"]
---

AiTWM은 협력사 **에임즈(AIMS)**의 AI 기반 절삭공구 마모량 계측 솔루션입니다.
상태를 '좋다/나쁘다'로 나누는 데서 그치지 않고, 공구 날의 여유면 마모를 평균값(VBmean)과 최댓값(VBmax)으로 계측해 숫자로 보여 줍니다.

측정값은 공구별로 자동 저장되어 마모가 얼마나 빠르게 진행되는지 추이로 확인할 수 있습니다.
이 데이터를 바탕으로 공구 교체 시점과 수명을 예측하고, 가공 조건을 바꿨을 때 마모가 어떻게 달라지는지도 비교할 수 있습니다.
