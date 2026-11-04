---
title: MRSm
subtitle: 현미경 측정 · 드릴 외경 자동 측정 · 인서트 코너 R 자동 측정
category: 머신비전
subcategory: Software
brand: SEIL TECHNO
order: 421
posted: 2026-11-03
published: false
image: /assets/img/software/mrsm/main.jpg
summary: 세일테크노가 직접 개발한 현미경 측정 소프트웨어입니다. 선·원·각도 측정과 엣지 자동 검출에 더해, 절삭공구 현장에서 많이 요청받는 드릴 외경과 인서트 코너 R을 카메라 영상에서 자동으로 측정합니다.
tags: [자체 개발, 드릴 외경 자동 측정, 인서트 코너 R 자동 측정]
highlights:
  - title: 드릴 외경 자동 측정
    text: 백라이트 실루엣에서 드릴 영역을 스스로 찾고, 열마다 가장 급한 밝기 변화를 외곽으로 잡아 서브픽셀 단위로 외경을 계산합니다. 날(플루트) 모양이나 조명 기울기에 덜 흔들립니다.
  - title: 인서트 코너 R 자동 측정
    text: 직선부를 먼저 확정하고 두 직선의 이등분선을 기준으로 고정 각도 구간만 원 피팅합니다. 접점 판정의 흔들림이 R 값으로 번지지 않아 반복 측정이 안정적입니다. ISO 형번(CNMG·DNMG·VNMG·SNMG·TNMG·WNMG)별 조건을 내장했습니다.
  - title: 엣지 검출 측정 도구
    text: 점·선·원·각도 수동 측정에 더해, 스캔 라인 기반 엣지 검출로 선·원·호를 자동 피팅합니다. 클릭 위치가 조금 달라도 같은 값이 나옵니다.
  - title: 리포트와 다양한 카메라
    text: 레시피 기반 세션 리포트와 엑셀 출력, 포커스 스태킹, 조명 제어를 지원합니다. TUCSEN·HIKROBOT·IDS·USB/HDMI 캡처 장치를 한 프로그램에서 씁니다.
shots_desc: 실제 프로그램 화면입니다. 측정 예시 이미지는 화면 설명용 시험 이미지입니다.
shots:
  - {src: /assets/img/software/mrsm/main.jpg, title: "측정 화면", desc: "원·선 측정과 엣지 검출 도구. 아래 표에 결과가 쌓이고, 캘리브레이션으로 mm 단위로 바뀝니다.", wide: true}
  - {src: /assets/img/software/mrsm/drill-live.jpg, title: "드릴 외경 자동 측정 (라이브)", desc: "카메라 영상에서 드릴 외경과 최대 외경을 실시간으로 표시합니다."}
  - {src: /assets/img/software/mrsm/corner-r-live.jpg, title: "인서트 코너 R 자동 측정 (라이브)", desc: "코너 R, 기준 대비 편차, 피팅 잔차와 OK/NG 판정을 함께 보여 줍니다."}
  - {src: /assets/img/software/mrsm/report.jpg, title: "리포트 모드", desc: "레시피를 고르고 바코드로 세션을 시작해 측정 결과를 엑셀로 모읍니다."}
  - {src: /assets/img/software/mrsm/corner-r-principle.jpg, title: "코너 R 측정 원리", desc: "직선부 확정 → 이등분선(대칭축) → 고정 각도 구간 → 원 피팅. 접점은 마지막에 계산되는 결과값입니다.", wide: true}
specs:
  - {label: 개발, value: "㈜세일테크노 (자체 개발)"}
  - {label: 측정, value: "점·선·원·각도, 거리·선간 각도, 엣지 선·원·호 자동 피팅"}
  - {label: 자동 측정, value: "드릴 외경 / 인서트 코너 R (ISO 형번별 조건)"}
  - {label: 카메라, value: "TUCSEN, HIKROBOT, IDS, USB·HDMI 캡처(WDM)"}
  - {label: 리포트, value: "레시피 기반 세션 리포트, Excel 출력, 오버레이 이미지 저장"}
  - {label: 기타, value: "캘리브레이션·배율 프리셋, 포커스 스태킹, 조명 제어"}
  - {label: 운영 환경, value: "Windows 10 / 11 (64-bit)"}
  - {label: 공급, value: "현미경·측정 장비와 함께 공급, 현장 맞춤 수정 가능"}
applications: [드릴 외경 측정, 인서트 코너 R 측정, 절삭공구 품질 검사, 부품 치수 측정, 검사 리포트 작성]
---
**MRSm**은 세일테크노가 현미경 측정 현장의 요청을 받아 직접 만든 소프트웨어입니다. 기본 측정 기능은 물론, 드릴과 인서트처럼 반복 측정이 많은 절삭공구 검사를 **자동 측정**으로 바꾸는 데 초점을 맞췄습니다.

코너 R은 직선과 원호의 경계가 분명하지 않아 사람이 접점을 정하면 측정할 때마다 값이 흔들립니다. MRSm은 접점을 찾지 않고 **직선부 → 대칭축 → 고정 각도 구간 → 원 피팅** 순서로 계산해, 접점 판정 오차가 R 값에 들어가지 않도록 했습니다.

> 측정 대상과 사용하시는 현미경·카메라를 알려 주시면 샘플 이미지로 먼저 측정해 보여 드립니다.
