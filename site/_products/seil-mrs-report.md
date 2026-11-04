---
title: MRS Report
subtitle: 현미경 촬영 · 측정 · 바코드 · 엑셀 보고서 자동화
category: 머신비전
subcategory: Software
brand: SEIL TECHNO
order: 422
posted: 2026-11-03
published: false
image: /assets/img/software/mrs-report/main.jpg
summary: 바코드로 시료 정보를 읽고, 현미경 사진을 찍고, 측정한 결과와 사진을 엑셀 시트에 바로 채워 넣는 검사 보고서 소프트웨어입니다. 손으로 옮겨 적던 기록 작업을 줄입니다.
tags: [자체 개발, 바코드 자동 입력, 엑셀 자동 삽입]
highlights:
  - title: 바코드로 시료 정보 입력
    text: 주문·자재·형번·수량 같은 항목을 바코드 스캐너로 차례대로 읽어 들입니다. 입력 중인 항목은 강조되고, 잘못 읽으면 한 항목만 되돌리거나 전체를 다시 입력합니다.
  - title: 사진을 엑셀에 바로 삽입
    text: 열어 둔 엑셀 파일의 정해진 열에 순번·시료 정보와 촬영 이미지를 자동으로 기록합니다. 보고서 서식을 따로 정리할 필요가 없습니다.
  - title: 측정과 오버레이 저장
    text: 점·선·원(3점 이상 자동 피팅)과 거리·각도 계산, 캘리브레이션을 지원합니다. 측정선이 그려진 이미지를 그대로 저장할 수 있습니다.
  - title: 카메라·조명 제어
    text: 노출·게인·영상 반전 같은 카메라 설정과 2채널 조명 밝기 제어(RS-232)를 프로그램 안에서 합니다. 불량 유형 목록도 현장에 맞게 편집합니다.
shots_desc: 실제 프로그램 화면입니다.
shots:
  - {src: /assets/img/software/mrs-report/main.jpg, title: "메인 화면", desc: "라이브 영상, 바코드 입력 현황, 측정 결과 표가 한 화면에 있습니다.", wide: true}
  - {src: /assets/img/software/mrs-report/excel.jpg, title: "엑셀 자동 기록", desc: "시료 정보와 촬영 이미지가 지정한 엑셀 열에 차례대로 들어갑니다."}
  - {src: /assets/img/software/mrs-report/camera-settings.jpg, title: "카메라 설정", desc: "자동 노출, 노출 시간, 게인, 좌우·상하 반전을 설정합니다."}
  - {src: /assets/img/software/mrs-report/light-control.jpg, title: "조명 제어", desc: "조명 컨트롤러와 직렬 포트로 연결해 채널별 밝기를 조절합니다."}
specs:
  - {label: 개발, value: "㈜세일테크노 (자체 개발)"}
  - {label: 입력, value: "USB 바코드 스캐너 (항목 구성은 현장 맞춤)"}
  - {label: 측정, value: "점·선·원, 거리·각도, 캘리브레이션"}
  - {label: 보고서, value: "Excel 시트 자동 기록 (시료 정보 + 촬영 이미지)"}
  - {label: 카메라, value: "TUCSEN, HIKROBOT"}
  - {label: 조명, value: "2채널 조명 밝기 제어 (RS-232)"}
  - {label: 운영 환경, value: "Windows 10 / 11 (64-bit), Microsoft Excel"}
  - {label: 공급, value: "PC별 라이선스, 현장 보고서 양식에 맞춰 수정"}
applications: [출하 검사 기록, 공구·부품 외관 검사 보고서, 시료 사진 관리, 바코드 기반 이력 관리]
---
**MRS Report**는 "사진 찍고, 측정하고, 엑셀에 붙여 넣는" 검사 기록 업무를 한 번에 처리하도록 만든 소프트웨어입니다. 바코드를 읽으면 다음 할 일(촬영)로 넘어가고, 촬영한 사진은 엑셀의 정해진 칸에 바로 들어갑니다.

보고서 양식과 바코드 항목은 고객사 업무에 맞춰 바꿔 드립니다. 기존 엑셀 양식을 그대로 쓰고 싶으신 경우에도 상담해 주세요.
