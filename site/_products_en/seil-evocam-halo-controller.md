---
# 영문 페이지 — 글만 적습니다. 사진·영상 경로는 한국어 파일(site/_products/같은 이름.md)에서 순서대로 가져옵니다.
# guide / shots 의 개수와 순서는 한국어 파일과 같아야 합니다. caps = 그 단계 사진 설명(사진 순서대로).
title: EVOCAM HALO Controller
subtitle: Control, measurement, code reading and inspection reports for the EVO Cam HALO digital microscope
category: Machine Vision
subcategory: Software
summary: PC software that controls the EVO Cam HALO digital microscope and handles imaging, measurement, calibration and inspection reports in a single window. It also reads QR codes, barcodes and Data Matrix codes straight from the live image.
tags: [In-house software, Code reading from the live image, Two Excel report modes, Video user guide]
setups_title: Setup examples
setups_desc: "Examples of EVO Cam HALO used with two monitors. Click a photo to enlarge it."
setups_caps:
  - "Inspecting end mill flutes — top: live video monitor / bottom: PC software screen"
  - "Inspecting MLCC chips — top: EVOCAM HALO Controller screen / bottom: live video monitor"
highlights:
  - title: Microscope control
    text: Operate zoom, focus, exposure and lighting from the PC, with auto / manual focus and Focus Stacking (merging several focus levels).
  - title: Code reading from the image
    text: One click reads the QR code, 1D barcode or Data Matrix (including laser dot-peen marks) visible in the live image — useful for codes marked directly on parts that a reader cannot scan.
  - title: Two report modes
    text: Recipe mode collects "scan, capture, add row" into one session and exports a single Excel file; Excel Template mode writes values and images straight into the selected cell of an open template.
  - title: Precise calibration
    text: Besides two-click calibration, Edge Line, Edge Circle and Ruler (automatic scale detection) methods save a calibration for each lens and zoom combination.
shots_title: Screenshots
shots_desc: Actual screens of the software.
shots:
  - {title: "Live measurement", desc: "Measure and capture directly on the HALO live image."}
  - {title: "Main window", desc: "Top toolbar, control tabs on the left (Zoom · Focus · Exposure · Light · Measure · Report), live video in the center, captured images on the right."}
  - {title: "Report — Recipe mode", desc: "Build up a session with the Barcode field and Scan button, then export it to one Excel file."}
  - {title: "Report — Excel Template mode", desc: "Insert values and images directly into the selected cell of an open Excel template."}
guide_title: User guide
guide_tab: User guide
guide_desc: "The user manual (v3.0), feature by feature, with real operation videos and screenshots. Videos play silently when they scroll into view; click a screenshot to enlarge it."
guide:
  - title: "Screen layout"
    text: "Top toolbar, control panel (tabs) on the left, live video in the center and the captured image list on the right. From connecting the device to imaging, measuring and reporting, everything happens in one window."
    points:
      - "HALO Port / Cap Connect — connect the HALO device (COM port) and the camera"
      - "Capture · Save + Overlay — capture the current frame, or save it with the measurement overlay"
      - "DATE — stamps the capture date and time in the top-right corner of saved images"
      - "Left tabs — Zoom · Focus · Exposure · Light · Save · Measure · Annotate · Report"
      - "Click a thumbnail in the captured list to open it at full resolution"
    caps: ["Main window"]
  - title: "Lens · zoom"
    text: "In the Zoom tab, set the lens and the camera zoom ratio, and jump to frequently used magnifications with the Quick Zoom buttons."
    points:
      - "Select the lens, then enter and apply the camera zoom ratio"
      - "Quick Zoom buttons move to a preset magnification instantly"
      - "The live image shows the current magnification and focus / exposure status in the top-left corner"
  - title: "Focus · Focus Stacking"
    text: "Switch between auto (AF) and manual (MF) focus. For samples with height differences, Focus Stacking merges several focus levels into one image that is sharp all over."
    points:
      - "Auto / Manual focus"
      - "Focus Stacking — merging several focus levels"
  - title: "Exposure · lighting"
    text: "Adjust brightness and lighting for the sample in the Exposure and Light tabs. Camera mode, mirror / flip, noise reduction and color gain are changed in Image Settings."
    points:
      - "Exposure settings, lighting brightness and direction"
      - "Image Settings — camera mode, Mirror / Flip, noise reduction, color gain"
    caps: ["Image Settings dialog"]
  - title: "Saving and loading presets"
    text: "Save frequently used viewing conditions to Preset 1–3 and recall them with one button, so you do not have to set them up again for every part in repetitive inspection."
  - title: "Measurement — length · angle · circle"
    text: "In the Measure tab, measure length, angle and circles with two clicks. Results collect in the measurement list below, and Save + Overlay saves the image with the measurement lines."
    points:
      - "Distance · Angle · Circle and other measurement tools"
      - "Calibrated zoom buttons jump straight to a calibrated magnification"
      - "Line color and width, decimal places and unit are set in Settings › Measurement"
    caps: ["Saved image with measurement overlay", "Settings › Measurement"]
  - title: "Edge-detection measurement"
    text: "The software finds the edge automatically, reducing errors caused by where you click. It quickly measures the diameter and position of features with clear edges, such as round holes."
    caps: ["Measuring circles of several sizes", "Edge circles and the distance between them"]
  - title: "Annotate"
    text: "Mark defect locations or add notes with text, shapes and arrows in the Annotate tab. Click with Select and drag to move them."
    points:
      - "Color, line width, font size and double-headed arrows are set in Settings › Annotation"
    caps: ["Settings › Annotation"]
  - title: "Inspection reports (Report)"
    text: "Choose the mode that suits your workflow. Recipe mode repeats \"scan barcode, capture image, add row\" and exports the session to one Excel file; Excel Template mode inserts values and images into the selected cell of a template that is already open."
    points:
      - "Define the columns (date, barcode, input, defect type, image, etc.) in the Recipe Editor"
      - "Start Session → scan, then Enter or Add Row → Export…"
      - "Scan button — reads the QR code / barcode / Data Matrix (including dot-peen marks) in the live image"
      - "Excel Template mode requires Microsoft Excel on the PC"
    caps: ["Recipe Editor — adding columns", "Setting the Defect Type list", "Exported Excel report", "Excel Template mode"]
  - title: "Calibration"
    text: "Create calibrations from the Calibrations menu; they are stored per lens and zoom combination. Besides the two-click (Manual) method, Edge Line, Edge Circle and Ruler (automatic scale detection) are supported."
    points:
      - "When you change magnification, check that a calibration exists for it"
      - "Manage lists the calibrations by magnification — Jump moves to one directly"
      - "Yellow marks on the zoom gauge show the calibration points"
    caps: ["Calibrations menu", "Manual (two clicks)", "Edge Line (automatic edge detection)", "Ruler (automatic scale detection)", "Manage Calibrations — list by magnification and Jump", "Preparing a new calibration"]
  - title: "Save settings · backup"
    text: "In Settings › Save, choose the save folder, whether every Capture is saved automatically, and the file format (PNG lossless / JPEG smaller files). Calibrations, settings and report recipes can be backed up to one zip file and restored."
    points:
      - "Calibrations › Backup All Settings… / Restore Settings…"
      - "The state just before a restore is kept automatically, so it can be undone"
      - "Calibrations belong to a specific device and lens; restoring them onto another device may give values that do not fit"
    caps: ["Settings › Save"]
specs:
  - {label: Developer, value: "SEIL TECHNO CORP. (in-house)"}
  - {label: Device, value: "Vision Engineering EVO Cam HALO"}
  - {label: Control, value: "Zoom, focus (auto / manual), exposure, lighting, Focus Stacking"}
  - {label: Measurement, value: "Length, angle, circle; edge-detection measurement"}
  - {label: Code reading, value: "QR, 1D barcode, Data Matrix (read from the image)"}
  - {label: Reports, value: "Recipe (session) / Excel Template (live cell insert)"}
  - {label: System, value: "Windows 10 / 11; Excel Template mode requires Microsoft Excel"}
applications: [Visual inspection of electronic parts, Part code reading and traceability, Inspection reporting, Microscope measurement]
---
**EVOCAM HALO Controller** is PC software developed by SEIL TECHNO to make the Vision Engineering **EVO Cam HALO** digital microscope easier to use. Microscope control, measurement and inspection records are brought together in one window instead of separate tools.

Codes that ordinary readers struggle with — such as Data Matrix marks made directly on parts — can be read from the microscope image and recorded in the report together with the measurement results.
