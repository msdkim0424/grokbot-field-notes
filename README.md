[![Grok Bot Guide by SpaceX Engineers](guide/cover.png)](guide/grok-bot-guide-by-spacex-engineers-ko.pdf)

# Grok Bot 실전 필드 노트 (Grok Bot Field Notes)

> 🇰🇷 **한국어 에디션 (Korean Edition)**  
> 본 저장소는 [@unicodef1wn](https://github.com/unicodef1wn)님의 [unicodef1wn/grokbot-field-notes](https://github.com/unicodef1wn/grokbot-field-notes)를 기반으로 번역 및 제작된 한국어 포크 저장소입니다.  
> 원작자의 72시간 라이브 스트리밍 현장 기록 정리에 깊은 감사를 표합니다. (All credits for compiling the original field notes go to [@unicodef1wn](https://github.com/unicodef1wn).)
> - 📕 **한국어 완본 PDF (24p)**: [`guide/grok-bot-guide-by-spacex-engineers-ko.pdf`](guide/grok-bot-guide-by-spacex-engineers-ko.pdf)
> - 🌐 **웹 소스 HTML**: [`guide/grok-bot-guide-ko.html`](guide/grok-bot-guide-ko.html)
> - 🇺🇸 [English README (영문 원본 보기)](README.en.md)

xAI의 Grok Bot 팀 엔지니어 3명([Roshan Sadanani](https://www.linkedin.com/in/roshansadanani) (제품), [Lauren Tan](https://www.linkedin.com/in/laurenelizabethtan) (엔지니어링, PStack 개발자), [Matt Palmer](https://www.linkedin.com/in/matt-palmer) (개발자 경험))이 자체 에이전트 플랫폼을 활용해 72시간 동안 빈 레포에서 실제 제품을 라이브 스트리밍으로 빌드하고 출시했습니다. 이 저장소는 그 3일간의 기록에서 도출된 핵심 자산들을 모은 것입니다: 24페이지 완본 디자인 가이드, 내 코딩 에이전트에 바로 적용할 수 있는 하우스 룰, 9가지 직무별 플레이북, 69개 봇 역할 정의 목록, 그리고 생방송 중에 터진 실패 일지.

## 저장소 구성 및 파일 안내 (What's here)

| 경로 | 내용 설명 |
|---|---|
| `AGENTS.md` | **코딩 에이전트를 위한 하우스 룰.** 내 레포 루트에 복사해 두면 에이전트(Cursor, Claude Code 등)가 자동으로 읽고 규칙을 준수합니다. |
| `ANTIPATTERNS.md` | **방송 중에 실제로 터진 40가지 실패 일지.** 각각 무엇이 깨졌고, 왜 깨졌으며, 어떤 영구적 규칙이 도출되었는지 정리. |
| `agents/` | `AGENTS.md`가 가리키는 상세 참조 레퍼런스: 검증(Verification), 오케스트레이션(Orchestration), 스킬 및 루틴, 프롬프트 라이브러리. |
| `roster/` | **69개 에이전트 역할 정의** (각 역할별 1개 파일). 봇의 책임 영역, 접근 가능한 도구/데이터, 승인 필요 항목, 복사해 쓸 수 있는 디스크립션 수록. |
| `playbooks/` | **9개 직무별 실전 워크숍:** 엔지니어링, PM, 창업자, 세일즈 엔지니어링, 영업, SDR, 고객지원, 포스트세일즈, 마케팅. 투입된 봇 팀, 워크플로우, 프롬프트, 루틴, 실제 수치 수록. |
| `guide/` | 📕 [**SpaceX 엔지니어들의 Grok Bot 가이드 (한국어 완본 24p PDF)**](guide/grok-bot-guide-by-spacex-engineers-ko.pdf) ([HTML 소스](guide/grok-bot-guide-ko.html))<br>[영문 원본 PDF](guide/grok-bot-guide-by-spacex-engineers.pdf): 멘탈 모델, 소프트웨어 팩토리, 사례 연구, 실패 일지, 경제성 분석을 하나의 이야기로 엮은 완성형 가이드. |
| `reference/` | 핵심 참조 문서 2편: `ECONOMICS.md` (실제 소요 비용 및 지표, 4대 토큰 누수 지점), `PRODUCT.md` (Grok Bot의 제품 구조: 메모리, 복제/공유 시 전속 규칙, 격리, 권한). |
| `notes/` | 3일간의 일차별 구조화된 원문 노트. 제품 팩트, 워크플로우, 프롬프트, 실패, 수치, 인물 정보. |

## 어디서부터 시작해야 할까요? (Where to start)

- **내 에이전트에게 즉각 적용할 규칙이 필요할 때**: [`AGENTS.md`](AGENTS.md)를 내 레포 루트에 복사하십시오.
- **에이전트가 "직접 돌려보고 알려달라"며 일을 떠넘길 때**: [`agents/VERIFICATION.md`](agents/VERIFICATION.md).
- **단일 봇 프롬프트를 넘어 에이전트 팀을 설계할 때**: [`agents/ORCHESTRATION.md`](agents/ORCHESTRATION.md).
- **현장에서 진짜로 검증된 프롬프트 문구가 필요할 때**: [`agents/PROMPTS.md`](agents/PROMPTS.md).
- **바로 복사해 쓸 수 있는 봇의 역할 정의가 필요할 때**: [`roster/`](roster/) (시작점: [`roster/README.md`](roster/README.md)).
- **고객지원이나 영업 등 내 직무에 맞는 봇 설정을 원할 때**: [`playbooks/`](playbooks/) (시작점: [`playbooks/README.md`](playbooks/README.md)).
- **실전에서 어떤 사고가 터지는지 미리 알고 싶을 때**: [`ANTIPATTERNS.md`](ANTIPATTERNS.md).
- **실제 비용이 얼마나 들고 토큰이 어디로 새는지 알고 싶을 때**: [`reference/ECONOMICS.md`](reference/ECONOMICS.md).
- **메모리에 넣을 내용과 디스크립션에 넣을 내용을 결정할 때**: [`reference/PRODUCT.md`](reference/PRODUCT.md).
- **3일간의 전체 이야기를 한 권의 책처럼 읽고 싶을 때**: 📕 [한국어 완본 PDF 가이드](guide/grok-bot-guide-by-spacex-engineers-ko.pdf) 또는 [영문 원본 PDF](guide/grok-bot-guide-by-spacex-engineers.pdf).
- **특정 사실관계를 교차 검증하고 싶을 때**: [`notes/`](notes/).

## 핵심 요약 (In one paragraph)

각 에이전트에게 좁은 단일 역할과 이름을 부여하십시오. 두 번째 에이전트를 만들기 전에 검증 루프부터 먼저 구축하십시오.

에이전트가 버그를 고치기 전에 반드시 먼저 재현하게 만들고, 모든 작업물에 검증 증거를 첨부하게 하십시오. 틀렸을 때는 지엽적인 사건의 스토리가 아닌 일반 원칙을 기록하십시오.

빈도(Frequency)가 곧 비용이므로 루틴을 매주 감사하십시오. 자동화 루프가 아무리 잘 돌아가더라도 마이그레이션, 배포, 결제, 권한에는 반드시 사람의 승인 관문을 유지하십시오.

## 라이선스 (License)

MIT. 이 저장소의 모든 내용은 자유롭게 여러분의 레포지토리에 복사해 사용할 수 있습니다.
