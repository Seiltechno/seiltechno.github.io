---
title: AiTCD
subtitle: AI 절삭공구 상태진단 솔루션 (AI for Tool Condition Diagnosis)
category: AI 검사·측정
subcategory: 기상 AI분석
brand: AIMS
partner:
  name: ㈜에임즈 (AIMS)
  desc: AI 비전 기반 스마트 제조 솔루션 기업
  url: https://aims.kr/
  logo: /assets/img/partners/aims.png
order: 212
image: /assets/img/products/aims/tcd-3.jpg
summary: 기상 카메라로 찍은 공구 이미지를 딥러닝이 분석해 새 공구·정상 마모·파손을 자동으로 판정합니다. 작업자 감에 의존하던 공구 교체를 데이터로 바꿉니다.
tags: [공구 상태진단, CNN 딥러닝, 새 공구·마모·파손 판정]

highlights:
  - title: 딥러닝 자동 진단
    text: CNN 기반 딥러닝 모델이 공구 이미지를 분석해 마모 상태, 손상 여부, 수명 단계를 자동으로 판단합니다.
  - title: 가공 중 비접촉 진단
    text: 공구를 탈착하지 않고 기상 카메라 이미지로 바로 진단하므로 측정 때문에 가공을 오래 멈출 필요가 없습니다.
  - title: 대규모 공구 이미지 데이터
    text: 대구기계부품연구원과의 공동연구로 모은 절삭공구 이미지 데이터를 바탕으로 학습한 모델입니다.
  - title: 교체 시점 예측
    text: 진단 결과와 마모 이력을 플랫폼에서 함께 관리해 불필요한 조기 교체와 파손 후 교체를 모두 줄입니다.
specs:
  - {label: 진단 방식, value: "이미지 기반 CNN 딥러닝 모델"}
  - {label: 판정 항목, value: "새 공구(New) / 정상 마모(Worn) / 파손 등 공구 상태"}
  - {label: 이미지 입력, value: "On-Machine Vision System 카메라 모듈 또는 사용자 이미지 입력"}
  - {label: 진행 단계, value: "① 공구 이미지 획득 → ② 사전 학습된 딥러닝 모델 판정 → ③ 공구 상태진단(자동화)"}
  - {label: 데이터 관리, value: "진단 결과·마모 이력 플랫폼 통합 관리"}
  - {label: 연동, value: "On-Machine Vision System, 로봇 시스템"}
  - {label: 학습 데이터, value: "공구 이미지 + 센서 신호 데이터 (각 진단 결과가 일치할 때 최종 판정)"}
  - {label: 상세 사양, value: "적용 공구·판정 등급 구성은 협의 (문의)"}
applications: [CNC 가공 공구 관리, 공구 교체 시점 판단, 무인 가공 중 파손 감지, 공구 품질 기록]
process:
  - img: /assets/img/products/aims/tcd-1.jpg
    step: "STEP 01"
    title: "실시간 공구 이미지 획득"
    text: "공구를 회전시키며 측정 날의 여유면이 카메라 정면에 오는 순간을 촬영합니다."
  - img: /assets/img/products/aims/tcd-2.jpg
    step: "STEP 02"
    title: "딥러닝 기반 판정 모델"
    text: "공구 이미지와 센서 신호 데이터로 각각 학습한 모델의 진단 결과를 함께 비교해, 결과가 같을 때 최종 판정해 신뢰성을 높입니다."
  - img: /assets/img/products/aims/tcd-3.jpg
    step: "STEP 03"
    title: "공구 상태진단 (자동화)"
    text: "날마다 새 공구 · 정상 마모 · 파손을 자동으로 판정하고, 측정 주기별 결과와 이미지를 저장합니다."
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

AiTCD는 협력사 **에임즈(AIMS)**의 AI 기반 절삭공구 상태진단 솔루션입니다.
기상 카메라로 얻은 공구 이미지를 딥러닝 모델이 분석해, 지금 이 공구가 새 공구인지, 정상적으로 마모되고 있는지, 파손되었는지를 자동으로 판정합니다.

지금까지 공구 교체는 작업자의 경험이나 정해진 가공 수량에 맞춰 이루어지는 경우가 많았습니다.
AiTCD는 실제 공구 이미지를 근거로 판단하므로 아직 쓸 수 있는 공구를 일찍 버리거나, 파손된 공구로 계속 가공하는 일을 줄여 줍니다.
