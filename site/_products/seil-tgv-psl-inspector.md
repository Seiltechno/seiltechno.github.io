---
title: TGV PSL Inspector
subtitle: TGV 유리기판 PSL 파티클 자동 검출·카운팅
category: 머신비전
subcategory: Software
brand: SEIL TECHNO
order: 426
posted: 2026-11-03
published: false
image: /assets/img/software/tgv-psl/main.jpg
summary: 유리기판(TGV) 세정 공정 평가를 위해, 현미경 이미지에서 홀을 자동으로 찾고 홀 주변의 PSL 파티클을 자동으로 세는 소프트웨어입니다. 세정 전·후 결과를 Excel로 바로 비교합니다.
tags: [자체 개발, 홀 자동 마스크, 폴더 일괄 검사]
highlights:
  - title: 홀 자동 검출과 마스크
    text: 이미지 속 원형 홀의 위치·반경을 자동으로 찾아 검사 대상에서 빼고, 기판 가장자리의 반원 홀도 따로 처리합니다.
  - title: 할로 영역에서도 파티클 검출
    text: 배경 대비(Local Residual) 방식으로 홀 주변의 밝은 조명 번짐 속에서도 작은 PSL 입자를 찾습니다. 파라미터를 바꾸면 이진화 미리보기가 바로 바뀝니다.
  - title: 배율별 레시피
    text: x50부터 x1000까지 배율마다 최적 파라미터와 캘리브레이션을 저장해, 배율을 고르면 검사 조건이 자동으로 바뀝니다.
  - title: 보정과 일괄 보고서
    text: 확대 보기에서 파티클을 추가·제거해 결과를 다듬고, 폴더 전체를 한 번에 검사해 파티클 번호·좌표·크기를 Excel로 저장합니다.
shots_desc: 실제 프로그램 화면입니다.
shots:
  - {src: /assets/img/software/tgv-psl/main.jpg, title: "메인 화면", desc: "왼쪽 파일 목록·배율별 레시피, 가운데 원본·이진화 미리보기·검출 결과 3단 패널, 아래 파라미터와 결과 표.", wide: true}
  - {src: /assets/img/software/tgv-psl/retouch.jpg, title: "확대 보기 · 수동 보정", desc: "초록 점은 검출 파티클, 파란 원은 홀 마스크, 주황 원(E)은 가장자리 반원입니다."}
  - {src: /assets/img/software/tgv-psl/crop.jpg, title: "이미지 자르기", desc: "8개 핸들로 검사 영역을 정하고, 원본은 자동 백업되어 언제든 복원합니다."}
  - {src: /assets/img/software/tgv-psl/batch.jpg, title: "폴더 일괄 검사", desc: "폴더 안 이미지를 순서대로 검사하고 결과를 Excel로 저장합니다.", wide: true}
specs:
  - {label: 개발, value: "㈜세일테크노 (자체 개발)"}
  - {label: 대상, value: "TGV(Through Glass Via) 유리기판, PSL 표준 입자"}
  - {label: 검출, value: "홀 자동 검출·마스크, 가장자리 반원 처리, 배경 대비 파티클 검출"}
  - {label: 조건 설정, value: "파라미터 11종 실시간 조정, 배율별 레시피 (x50 ~ x1000)"}
  - {label: 편집, value: "이미지 자르기, 제외 영역 지정, 파티클 추가·제거"}
  - {label: 보고서, value: "폴더 일괄 검사, Excel 자동 저장 (번호·좌표·크기)"}
  - {label: 운영 환경, value: "Windows, 단일 실행 파일(EXE)"}
  - {label: 공급, value: "고배율 비접촉 측정기와 패키지 공급"}
applications: [TGV 세정 공정 평가, 파티클 카운팅, 유리기판 청정도 검사, 세정 전·후 비교]
---
**TGV PSL Inspector**는 TGV 공정에서 미세홀 안팎의 잔류 입자를 없애는 세정 공정을 숫자로 평가하기 위해 만들었습니다. 세정 전 기판에 붙인 PSL 입자 수와 세정 후 남은 입자 수를 비교하려면, 현미경 이미지 속 입자를 정확하고 빠르게 세는 것이 핵심입니다.

세일테크노의 고배율 비접촉 측정기와 함께 공급되어, 촬영부터 검출·카운팅·보고서까지 하나의 흐름으로 이어집니다.
