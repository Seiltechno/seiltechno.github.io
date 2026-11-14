---
title: EVOCAM HALO Controller
subtitle: EVO Cam HALO 디지털 현미경 제어 · 측정 · 코드 인식 · 리포트
category: 머신비전
subcategory: Software
brand: SEIL TECHNO
order: 425
posted: 2026-11-03
published: true
image: /assets/img/software/evocam-halo/overview.jpg
summary: EVO Cam HALO 디지털 현미경을 PC에서 제어하고, 촬영·측정·캘리브레이션·검사 리포트 작성까지 한 화면에서 처리하는 소프트웨어입니다. 화면에 보이는 QR·바코드·Data Matrix도 바로 읽습니다.
tags: [자체 개발, 화면 속 코드 인식, Excel 리포트 2가지 방식, 영상 사용 가이드]
setups_title: 구성 예
setups_desc: "EVO Cam HALO와 모니터 2대를 함께 쓰는 구성 예입니다. 사진을 누르면 크게 볼 수 있습니다."
setups:
  - {src: /assets/img/software/evocam-halo/setup-endmill.jpg, cap: "엔드밀 날 관찰 — 위: 라이브 영상 모니터 / 아래: PC 소프트웨어 화면"}
  - {src: /assets/img/software/evocam-halo/setup-mlcc.jpg, cap: "MLCC 칩 관찰 — 위: EVOCAM HALO Controller 화면 / 아래: 라이브 영상 모니터"}
highlights:
  - title: 현미경 제어
    text: 줌·포커스·노출·조명을 PC에서 조작하고, 자동/수동 초점과 포커스 스태킹(다중 초점 합성)을 지원합니다.
  - title: 화면 속 코드 인식
    text: 라이브 영상에 보이는 QR·1D 바코드·Data Matrix(레이저 점각 포함)를 버튼 하나로 읽어 입력합니다. 리더기로 읽기 어려운 부품 표면 코드에 유용합니다.
  - title: 두 가지 리포트 방식
    text: 바코드 스캔 → 캡처 → 행 추가를 반복해 한 번에 내보내는 레시피 방식과, 열어 둔 Excel 서식의 선택한 셀에 값·이미지를 바로 넣는 템플릿 방식을 고릅니다.
  - title: 정밀 캘리브레이션
    text: 2점 클릭 외에 엣지 선·엣지 원·눈금자 자동 인식 방식으로 렌즈·줌 배율별 캘리브레이션을 저장합니다.
shots_desc: 실제 프로그램 화면입니다.
shots:
  - {src: /assets/img/software/evocam-halo/live.jpg, title: "라이브 측정 화면", desc: "HALO 현미경 영상 위에서 바로 측정하고 캡처합니다.", wide: true}
  - {src: /assets/img/software/evocam-halo/overview.jpg, title: "전체 화면 구성", desc: "상단 툴바, 왼쪽 제어 탭(Zoom·Focus·Exposure·Light·Measure·Report), 가운데 라이브 영상, 오른쪽 캡처 목록."}
  - {src: /assets/img/software/evocam-halo/report-recipe.jpg, title: "리포트 — 레시피 방식", desc: "바코드 입력과 Scan 버튼으로 세션을 쌓아 Excel 하나로 내보냅니다."}
  - {src: /assets/img/software/evocam-halo/report-template.jpg, title: "리포트 — 템플릿 방식", desc: "열려 있는 Excel 서식의 선택한 셀에 값과 이미지를 바로 넣습니다."}
guide_title: 사용 가이드
guide_tab: 사용 가이드
guide_desc: "사용자 매뉴얼(v3.0)을 기능별로 나눠 실제 조작 영상과 화면으로 보여 드립니다. 영상은 화면에 보이면 소리 없이 자동 재생되고, 화면 캡처는 누르면 크게 볼 수 있습니다."
guide:
  - title: "화면 구성"
    text: "상단 툴바, 왼쪽 제어판(탭), 가운데 라이브 영상, 오른쪽 캡처 이미지 목록으로 구성됩니다. 장비 연결부터 촬영·측정·리포트까지 한 화면에서 처리합니다."
    points:
      - "HALO Port / Cap Connect — HALO 장치(COM 포트)와 카메라 연결"
      - "Capture · Save + Overlay — 현재 화면 캡처, 측정선이 포함된 이미지 저장"
      - "DATE — 저장 이미지 오른쪽 위에 촬영 날짜·시간 표시"
      - "왼쪽 탭 — Zoom · Focus · Exposure · Light · Save · Measure · Annotate · Report"
      - "오른쪽 캡처 목록의 썸네일을 누르면 원본 크기로 확대"
    images:
      - {src: /assets/img/software/evocam-halo/guide/full-shot.jpg, cap: "프로그램 전체 화면"}
  - title: "렌즈 · 줌 배율"
    text: "Zoom 탭에서 렌즈 배율과 카메라 줌 비율을 정하고, Quick Zoom 버튼으로 자주 쓰는 배율에 바로 이동합니다."
    points:
      - "렌즈 배율 선택 후 카메라 줌 비율 입력·적용"
      - "Quick Zoom 버튼으로 원하는 배율로 즉시 이동"
      - "라이브 화면 왼쪽 위에 현재 배율과 초점·노출 상태 표시"
    video: {src: /assets/img/software/evocam-halo/guide/lens-magnification.mp4, poster: /assets/img/software/evocam-halo/guide/lens-magnification.jpg, len: "0:43"}
  - title: "포커스 · 포커스 스태킹"
    text: "자동(AF)과 수동(MF) 초점을 전환하고, 높낮이가 있는 시료는 여러 초점의 이미지를 합성하는 Focus Stacking으로 전체가 선명한 이미지를 얻습니다."
    points:
      - "Auto / Manual 포커스 전환"
      - "Focus Stacking — 다중 초점 합성"
    video: {src: /assets/img/software/evocam-halo/guide/focus.mp4, poster: /assets/img/software/evocam-halo/guide/focus.jpg, len: "0:50"}
  - title: "노출 · 조명"
    text: "Exposure 탭과 Light 탭에서 밝기와 조명을 시료에 맞게 조정합니다. 카메라 모드·좌우 반전·노이즈·색 보정은 Image Settings에서 바꿉니다."
    points:
      - "노출 설정, 조명 밝기·조사 방향 조정"
      - "Image Settings — 카메라 모드, Mirror/Flip, 노이즈 감소, 색 보정"
    video: {src: /assets/img/software/evocam-halo/guide/exposure-light.mp4, poster: /assets/img/software/evocam-halo/guide/exposure-light.jpg, len: "1:06"}
    images:
      - {src: /assets/img/software/evocam-halo/guide/setting-image_setting.png, cap: "Image Settings 대화상자"}
  - title: "프리셋 저장 · 불러오기"
    text: "자주 쓰는 관찰 조건을 Preset 1~3에 저장해 두고 버튼 하나로 다시 불러옵니다. 같은 부품을 반복 검사할 때 조건을 매번 맞출 필요가 없습니다."
    video: {src: /assets/img/software/evocam-halo/guide/preset.mp4, poster: /assets/img/software/evocam-halo/guide/preset.jpg, len: "1:10"}
  - title: "측정 — 길이 · 각도 · 원"
    text: "Measure 탭에서 클릭 2번으로 길이·각도·원을 측정합니다. 결과는 아래 측정 목록에 쌓이고, Save + Overlay로 측정선이 들어간 이미지를 저장합니다."
    points:
      - "Distance · Angle · Circle 등 측정 도구"
      - "Calibrated zoom 버튼으로 캘리브레이션한 배율에 바로 이동"
      - "측정선 색·두께, 소수점 자리, 단위는 Settings › Measurement에서 설정"
    video: {src: /assets/img/software/evocam-halo/guide/measure.mp4, poster: /assets/img/software/evocam-halo/guide/measure.jpg, len: "2:19"}
    images:
      - {src: /assets/img/software/evocam-halo/guide/measure-capture.jpg, cap: "측정선이 포함된 저장 이미지"}
      - {src: /assets/img/software/evocam-halo/guide/setting-measure.png, cap: "Settings › Measurement"}
  - title: "엣지 검출 측정"
    text: "경계(엣지)를 자동으로 찾아 측정해 클릭 위치에 따른 오차를 줄입니다. 원형 구멍처럼 경계가 뚜렷한 형상의 지름·위치를 빠르게 잽니다."
    video: {src: /assets/img/software/evocam-halo/guide/measure-edge_circle.mp4, poster: /assets/img/software/evocam-halo/guide/measure-edge_circle.jpg, len: "0:27"}
    images:
      - {src: /assets/img/software/evocam-halo/guide/measure-circle.jpg, cap: "여러 크기의 원 측정"}
      - {src: /assets/img/software/evocam-halo/guide/measure-edge_circle2.jpg, cap: "엣지 원 측정과 원 사이 거리"}
  - title: "주석 (Annotate)"
    text: "Annotate 탭에서 텍스트·도형·화살표로 결함 위치나 설명을 표시합니다. Select로 선택한 뒤 드래그하면 이동합니다."
    points:
      - "색, 선 두께, 글자 크기, 양방향 화살표는 Settings › Annotation에서 설정"
    video: {src: /assets/img/software/evocam-halo/guide/annotate.mp4, poster: /assets/img/software/evocam-halo/guide/annotate.jpg, len: "0:59"}
    images:
      - {src: /assets/img/software/evocam-halo/guide/setting-annotation.png, cap: "Settings › Annotation"}
  - title: "검사 리포트 (Report)"
    text: "두 가지 방식 중 상황에 맞게 고릅니다. Recipe 모드는 바코드 스캔 → 캡처 → 행 추가를 반복해 세션을 Excel 하나로 내보내고, Excel Template 모드는 열어 둔 서식의 선택한 셀에 값과 이미지를 바로 넣습니다."
    points:
      - "Recipe Editor에서 컬럼 구성(날짜, 바코드, 입력값, 결함 유형, 이미지 등) 지정"
      - "Start Session → 바코드 스캔 후 Enter 또는 Add Row → Export…"
      - "Scan 버튼 — 라이브 화면의 QR·바코드·Data Matrix(레이저 점각 포함)를 바로 인식"
      - "Excel Template 모드는 PC에 Microsoft Excel 필요"
    video: {src: /assets/img/software/evocam-halo/guide/report.mp4, poster: /assets/img/software/evocam-halo/guide/report.jpg, len: "1:01"}
    images:
      - {src: /assets/img/software/evocam-halo/guide/report-recipe-add.png, cap: "Recipe Editor — 컬럼 추가"}
      - {src: /assets/img/software/evocam-halo/guide/report-recipe-defect.png, cap: "결함 유형(Defect Type) 목록 지정"}
      - {src: /assets/img/software/evocam-halo/guide/report-result.jpg, cap: "내보낸 Excel 리포트"}
      - {src: /assets/img/software/evocam-halo/report-template.jpg, cap: "Excel Template 모드"}
  - title: "캘리브레이션"
    text: "Calibrations 메뉴에서 렌즈·줌 배율 조합마다 캘리브레이션을 만들어 저장합니다. 2점 클릭(Manual) 외에 Edge Line · Edge Circle · Ruler(눈금 자동 인식) 방식을 지원합니다."
    points:
      - "배율을 바꾸면 해당 배율의 캘리브레이션이 있는지 확인"
      - "Manage에서 배율별 캘리브레이션 확인 · Jump로 바로 이동"
      - "배율 게이지의 노란 눈금 = 캘리브레이션 지점"
    images:
      - {src: /assets/img/software/evocam-halo/guide/calibration.png, cap: "Calibrations 메뉴"}
      - {src: /assets/img/software/evocam-halo/guide/calibration-2points.jpg, cap: "Manual (2점 클릭)"}
      - {src: /assets/img/software/evocam-halo/guide/calibration-edge_line.jpg, cap: "Edge Line (엣지 선 자동 검출)"}
      - {src: /assets/img/software/evocam-halo/guide/calibration-ruller.jpg, cap: "Ruler (눈금 자동 인식)"}
      - {src: /assets/img/software/evocam-halo/guide/calibration-manager.png, cap: "Manage Calibrations — 배율별 목록과 Jump"}
      - {src: /assets/img/software/evocam-halo/guide/calibration-new-MF.jpg, cap: "새 캘리브레이션 준비 화면"}
  - title: "저장 설정 · 백업"
    text: "Settings › Save에서 저장 폴더, 캡처할 때마다 자동 저장 여부, 파일 형식(PNG 무손실 / JPEG 용량 절약)을 정합니다. 캘리브레이션·설정·리포트 레시피는 zip 하나로 백업하고 복원할 수 있습니다."
    points:
      - "Calibrations › Backup All Settings… / Restore Settings…"
      - "복원 직전 상태는 자동 보관되어 되돌릴 수 있음"
      - "캘리브레이션은 장비·렌즈 조합별 값이므로 다른 장비에 복원하면 맞지 않을 수 있음"
    images:
      - {src: /assets/img/software/evocam-halo/guide/setting-save.png, cap: "Settings › Save"}
specs:
  - {label: 개발, value: "㈜세일테크노 (자체 개발)"}
  - {label: 대상 장비, value: "Vision Engineering EVO Cam HALO"}
  - {label: 제어, value: "줌, 포커스(자동·수동), 노출, 조명, 포커스 스태킹"}
  - {label: 측정, value: "길이·각도·원, 엣지 검출 측정"}
  - {label: 코드 인식, value: "QR, 1D 바코드, Data Matrix (화면 촬영으로 인식)"}
  - {label: 리포트, value: "레시피(세션 누적) / Excel 템플릿(실시간 셀 삽입)"}
  - {label: 운영 환경, value: "Windows 10 / 11, 템플릿 방식은 Microsoft Excel 필요"}
applications: [전자부품 외관 검사, 부품 코드 판독·이력 관리, 검사 리포트 작성, 현미경 측정]
---
**EVOCAM HALO Controller**는 세일테크노가 공급하는 Vision Engineering **EVO Cam HALO** 디지털 현미경을 더 편하게 쓰도록 만든 PC 소프트웨어입니다. 현미경 제어와 측정, 검사 기록이 따로 놀지 않도록 한 화면에 모았습니다.

부품에 직접 찍힌 Data Matrix처럼 일반 리더기로 읽기 어려운 코드를 현미경 영상으로 읽어, 측정 결과와 함께 리포트에 남길 수 있습니다.
