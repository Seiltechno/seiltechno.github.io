---
title: MRS-MC
subtitle: 현미경 측정 + 칼로테스트(CaloTest) 코팅 두께 계산
category: 머신비전
subcategory: Software
brand: SEIL TECHNO
order: 423
posted: 2026-11-03
published: false
image: /assets/img/software/mrs-mc/main.jpg
summary: 현미경 이미지에서 길이·원·각도를 측정하고, 칼로테스트로 연마한 자국에서 코팅 두께를 계산해 엑셀 리포트로 내보내는 소프트웨어입니다.
tags: [자체 개발, 칼로테스트 두께 계산, 다층 코팅]
highlights:
  - title: 칼로테스트 코팅 두께 계산
    text: 볼로 연마한 크레이터의 지름을 측정하면 코팅 두께를 바로 계산합니다. 간이식과 정밀식 결과를 함께 보여 줍니다.
  - title: 다층 코팅 지원
    text: 여러 층으로 이루어진 코팅도 층마다 지름을 찍어 각 층의 두께를 따로 구합니다.
  - title: 기본 측정 도구
    text: 선·원(최소제곱 원 피팅)·각도 측정과 캘리브레이션을 지원하고, 여러 장의 이미지를 탭으로 나눠 관리합니다.
  - title: 리포트 출력
    text: 측정 오버레이가 그려진 이미지 저장, CSV·Excel 리포트로 결과를 정리합니다. 카메라 없이 이미지 파일만으로도 모든 측정이 가능합니다.
shots:
  - {src: /assets/img/software/mrs-mc/main.jpg, title: "측정 화면", desc: "이미지 위에 선·원·각도를 측정하고 결과 표에 기록합니다.", wide: true}
  - {src: /assets/img/software/mrs-mc/calotest.jpg, title: "칼로테스트 패널", desc: "볼 반경과 크레이터 지름을 입력·측정하면 층별 코팅 두께가 계산됩니다."}
  - {src: /assets/img/software/mrs-mc/report.jpg, title: "Excel 리포트", desc: "측정값과 오버레이 이미지를 정리한 리포트입니다."}
specs:
  - {label: 개발, value: "㈜세일테크노 (자체 개발)"}
  - {label: 측정, value: "선·원·각도, 캘리브레이션"}
  - {label: 칼로테스트, value: "간이식·정밀식 두께 계산, 다층 코팅"}
  - {label: 출력, value: "오버레이 이미지(PNG), CSV, Excel 리포트"}
  - {label: 카메라, value: "TUCSEN, USB·HDMI 캡처(WDM) — 카메라 없이 이미지 파일도 가능"}
  - {label: 운영 환경, value: "Windows 10 / 11 (64-bit)"}
applications: [코팅 두께 측정(칼로테스트), 절삭공구 코팅 품질 관리, 표면처리 평가, 현미경 치수 측정]
---
**MRS-MC**는 Measurement(측정)와 CaloTest(칼로테스트)의 앞 글자를 딴 이름입니다. 코팅 두께를 확인하려고 칼로테스트 자국을 현미경으로 찍고, 지름을 재고, 계산기로 두께를 따로 구하던 과정을 한 프로그램에서 끝냅니다.

> 사용 중인 칼로테스터의 볼 크기와 측정 현미경을 알려 주시면 맞춰서 설정해 드립니다.
