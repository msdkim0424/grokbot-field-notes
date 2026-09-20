# -*- coding: utf-8 -*-
# Pages 9 to 16 for Korean Grok Bot Guide
from pages_part1 import get_header, get_footer

def render_page_09():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">07 · THE SOFTWARE FACTORY</div>
    <h1 class="page-title">433개의 PR이 머지된 비결</h1>
    <p class="page-intro">
      '소프트웨어 팩토리(Software Factory)'는 헤드라인을 장식한 수치를 만들어낸 핵심 패턴입니다. 개발팀은 이 용어를 썩 좋아하지 않았지만("솔직히 팩토리라는 단어 자체를 별로 안 좋아해요"), 결국 이 이름으로 정착되었습니다. 화려한 브랜딩을 걷어내면 본질은 단순한 루프입니다: 작업자 에이전트가 작은 변경 사항을 작성하고, 검증자 에이전트가 앱을 직접 실행해 깨뜨려 보려 시도하며, 그 검증을 통과해야만 코드가 머지되는 구조입니다.
    </p>

    <div class="section-label">핵심 개발 루프 (The Loop)</div>
    <div style="margin-bottom: 9pt;">
      <div class="num-item">
        <div class="num-badge">1</div>
        <div class="num-content">
          <strong>계획을 여러 단계(Phase)로 분할.</strong> 로렌의 Pstack 플러그인과 '포테이토 모드(Potato Mode)' 스킬이 이를 수행: <code>/potato mode</code> + "이 계획을 완전 자율(Full Autopilot)로 진행해 줘."
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">2</div>
        <div class="num-content">
          <strong>구현 에이전트들이 작은 단위의 PR을 작성.</strong> Cursor 클라우드 에이전트들이 각자 독립된 머신에서 범위가 제한된 변경 작업을 병렬 수행.
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">3</div>
        <div class="num-content">
          <strong>검증 에이전트들이 앱을 띄우고 퍼징(Fuzzing) 테스트 수행.</strong> '스웜(Swarm)' 스킬이 여러 에이전트를 소환하여 실제로 앱 화면을 클릭하며 결함을 추적.
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">4</div>
        <div class="num-content">
          <strong>CI 그린 통과 시 자동 머지.</strong> 사람이 코드 diff를 한 줄씩 읽는 대신, 자동 검증 통과 여부가 머지의 최종 관문이 됨.
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">5</div>
        <div class="num-content">
          <strong>플레이테스터 봇이 엔드투엔드로 전체 게임을 플레이.</strong> 'Chrome' 봇이 CI를 통과한 PR들을 감시하고, 실제 게임을 플레이하여 이상이 없을 때 비로소 배포 승인.
        </div>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">자율주행의 4단계 사다리</div>
        <div class="card-subtitle">실제 프로덕션 환경에 배포되자 로렌은 신중하게 물러섰습니다.</div>
        <ul class="custom-bullets">
          <li><strong>조사 전용 (Investigate only)</strong> — "아직 PR 열지 말고, 무슨 일이 일어나고 있는지 네 생각을 먼저 가져와."</li>
          <li><strong>드래프트 (Draft)</strong> — PR을 열어두고 사람의 검토를 대기.</li>
          <li><strong>오토파일럿 (Autopilot)</strong> — 구현과 검증을 수행하고, 테스트 통과 시 머지.</li>
          <li><strong>완전 자율주행 (Full autopilot)</strong> — 계획 수립, 단계 분할, 구현, 검증, 머지까지 전 과정 무인 수행.</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">아키텍트(Architect) 단계</div>
        <div class="card-subtitle">서로 다른 4개 모델 병렬 합의</div>
        <ul class="custom-bullets">
          <li>Pstack의 'architect' 스킬은 하나의 문제를 <strong>4개의 서로 다른 LLM 모델</strong>에 병렬로 던진 후, 판정(Judging) 단계를 거쳐 최선의 계획을 선정하거나 병합합니다.</li>
          <li>모델마다 서로 다른 제약 조건을 발견해 내므로 중요한 아키텍처 결정 시 충분한 가치가 있습니다.</li>
          <li>초기 프로토타입 단계에서는 의도적으로 건너뛰었습니다: "지금 단계에선 솔직히 아키텍처 따위는 아무래도 상관없으니까요."</li>
        </ul>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">⚠️</div>
      <div class="callout-body">
        <div class="callout-title">솔직하게 짚고 넘어가야 할 점</div>
        <p class="callout-text">
          로렌은 게임 개발 과정에 대해 솔직히 고백했습니다: "솔직히 말씀드리면, 전 코드 자체는 거의 쳐다보지도 않았어요. 그냥 포테이토 모드와 Pstack을 돌렸을 뿐이죠." 반면 실제 Grok Bot 제품 자체를 만드는 에릭(Eric)은 자신이 본래 프로덕션 코드베이스에서는 절대 이런 식으로 작업하지 않는다고 분명히 선을 그었습니다 — 그는 모든 PR을 꼼꼼히 읽고 안티패턴 규칙을 엄격히 적용합니다. 팩토리의 공격성은 <strong>위험 반경(Blast Radius)에 비례해 조절되어야 하며</strong>, 72시간짜리 데모 게임은 위험 반경이 극도로 작은 특수한 사례였습니다.
        </p>
      </div>
    </div>
    {get_footer(9)}
  </div>
    """

def render_page_10():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">08 · VERIFICATION</div>
    <h1 class="page-title">검증이 성패의 전부다</h1>
    <p class="page-intro">
      이번 3일간의 기록에서 단 하나의 지침만 가져가야 한다면, 바로 이 장을 챙겨보세요. 봇을 이용해 실제 의미 있는 성과를 낸 모든 발표자가 이 원칙을 강조했으며, 아직 검증 루프를 구축하지 못한 이들은 그것이 최대의 병목이라고 털어놓았습니다.
    </p>

    <div class="quote-box">
      <p class="quote-text">“검증은 정말이지 너무나 중요합니다. 봇들이 실제로 코드를 실행해 보고, 스크린샷을 찍어보게 만들어야 합니다. 그래야 봇이 문제를 진짜로 이해하고 있다는 확신을 가질 수 있습니다.”</p>
      <p class="quote-author">로렌(Lauren) · Day 3</p>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">검증 스킬에 실제로 들어가야 하는 것</div>
        <ul class="custom-bullets">
          <li><strong>에이전트가 직접 제어할 수 있는 CLI.</strong> 매번 일회성 스크립트를 새로 작성하게 하지 마세요 — 토큰이 낭비되고 재현성이 떨어집니다. 로렌: "봇들이 앱과 결정론적으로 상호작용할 수 있게 해주는 표준 CLI나 도구가 필요합니다. 저는 표준화된 도구 세트를 쥐여주는 쪽을 선호합니다."</li>
          <li><strong>피처 맵 (Feature Map).</strong> 앱의 주요 기능과 흐름을 머신이 읽을 수 있는 형태로 정리해 두어, 에이전트가 헤매지 않고 테스트할 화면으로 곧장 찾아갈 수 있게 해야 합니다. Thursday Arena는 한 걸음 더 나아가 <code>/rules</code> 페이지에 <code>llms.txt</code> 스타일의 엔드포인트를 제공하여 에이전트가 게임 규칙을 직접 읽게 했습니다.</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">팀이 철저하게 강제한 3가지 규칙</div>
        <ul class="custom-bullets">
          <li><strong>1. 수정하기 전에 버그부터 먼저 재현하라.</strong> "버그를 실제로 재현할 수 있을 때에만 에이전트가 문제를 제대로 이해했다고 신뢰할 수 있습니다." 상시 프롬프트: "코드를 작성하기 전에, 앱을 띄우고 정확한 버그와 동작을 확인한 다음 진행하라."</li>
          <li><strong>2. 증거를 PR에 반드시 첨부하라.</strong> UI 변경 시 스크린샷이나 녹화 영상, 백엔드 변경 시 성능 메트릭을 필수로 첨부하도록 명문화했습니다. 클라우드 에이전트는 자체 실행 화면을 영상으로 녹화해 첨부할 수 있습니다.</li>
          <li><strong>3. 스킬에 이름을 붙이고 이름으로 호출하라.</strong> 이 팀의 스킬명은 <code>/verify cupcake</code>이었으며, 모든 오토파일럿 지시문에서 협상 불가능한 필수 조건으로 지정되었습니다.</li>
        </ul>
      </div>
    </div>

    <div class="footnote">
      *검증 스킬이 없을 때 발생하는 전형적인 실패 양상은 매우 익숙합니다: 봇이 작업을 마친 뒤 "자, 이제 앱을 띄워서 여기저기 클릭해 보시고 잘 동작하는지 제게 알려주세요"라고 말하는 상황입니다. 바로 그 핑퐁 과정에서 인간의 시간이 다 날아갑니다.
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">일반화 가능한 자동화 테스트 기준</div>
        <p class="callout-text">
          무엇을 자동화할지 결정하는 에릭(Eric)의 휴리스틱: "당신의 업무 흐름을 살펴보고, '결과를 검증할 수 있는 루프'가 존재하는지 자문해 보세요 — 그곳이 바로 봇들을 마음껏 날뛰게(Go crazy) 풀어놓을 수 있는 영역입니다." 코딩이 대표적인 사례인 이유는 테스트, 빌드, 실행 중인 앱이 기계가 읽을 수 있는 확실한 신호를 제공하기 때문입니다. 그런 신호가 없는 작업이라면, 자율성을 부여하기 전에 검증 신호부터 먼저 발명해야 합니다.
        </p>
      </div>
    </div>
    {get_footer(10)}
  </div>
    """

def render_page_11():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">09 · PROMPT PATTERNS</div>
    <h1 class="page-title">실전에서 검증된 7가지 프롬프트 패턴</h1>
    <p class="page-intro">
      이것들은 얄팍한 프롬프트 기교가 아닙니다. 3일간 6~7명의 서로 다른 발표자들이 각자 독립적으로 자연스럽게 사용했던, 실전에서 살아남은 소수의 핵심 습관들입니다.
    </p>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">1. 자신의 언어로 되짚어 말하게 하기</div>
        <div class="card-subtitle">거의 모든 발표자가 필수 사용</div>
        <div class="card-body">
          길거나 복잡한 지시를 내린 후, 작업을 시작하기 전에 <strong>"이 내용을 네 말로 다시 요약해 봐"</strong>를 덧붙입니다. 비용이 들지 않는 시점에 오해를 즉시 잡아냅니다. 2일차 발표자는 이를 "내가 가장 좋아하는 패턴"이라고 불렀습니다.
        </div>
      </div>
      <div class="card">
        <div class="card-title">2. 막 쏟아내고, 그 뒤에 구조화하기</div>
        <div class="card-subtitle">음성 받아쓰기(Voice dictation) 활용</div>
        <div class="card-body">
          마이크를 잡고 1~2분간 의식의 흐름대로 마구 이야기한 다음, 봇에게 이를 체계적으로 종합하라고 시킵니다. 나중에 다시 타이핑할 필요 없이 대화 중에 실시간으로 성장 아이디어를 포착했습니다.
        </div>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">3. 핵심만 추출한 뒤 추론하기</div>
        <div class="card-subtitle">매우 긴 입력값 처리 시</div>
        <div class="card-body">
          장문의 음성 프롬프트가 주어졌을 때, 봇에게 먼저 핵심 사실들만 추려내게 하고, 오직 그 요약본을 바탕으로 추론을 진행하게 합니다. 두서없는 장문에서 발생하는 환각을 막는 블레이크의 비결입니다.
        </div>
      </div>
      <div class="card">
        <div class="card-title">4. 최종 결과물부터 정의하기</div>
        <div class="card-subtitle">암리타(Amrita)의 기법</div>
        <div class="card-body">
          "내가 만들고자 하는 최종 결과물은 이것이다"로 시작하여 봇이 역산하여 작업하게 합니다. 세부 단계를 일일이 나열하는 것보다 최종 산출물과 합격 기준(Acceptance Criteria)을 명시하는 편이 훨씬 낫습니다.
        </div>
      </div>
    </div>

    <div class="grid-3col" style="margin-bottom: 8pt;">
      <div class="card">
        <div class="card-title" style="font-size:8.8pt;">5. 손대기 전 조사부터</div>
        <div class="card-body" style="font-size:7.8pt;">
          로샨: "원인을 파고들어 무슨 일인지 파악해라. 아직 PR은 열지 말고, 네 분석 내용만 먼저 가져와라."
        </div>
      </div>
      <div class="card">
        <div class="card-title" style="font-size:8.8pt;">6. 중간에 개입하고 툭 치기</div>
        <div class="card-body" style="font-size:7.8pt;">
          링 시: 봇이 궤도를 벗어날 때 중간에 방향을 틀어주는 것은 일상적입니다. 몇 분마다 상태를 묻는 것이 낫습니다.
        </div>
      </div>
      <div class="card">
        <div class="card-title" style="font-size:8.8pt;">7. 음성 메모로 직무 덤프</div>
        <div class="card-body" style="font-size:7.8pt;">
          블레이크: 15분 음성 메모로 업무를 쏟아내고, 봇에게 "나를 위한 업무 시스템을 설계해 줘"라고 맡깁니다.
        </div>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">7가지 패턴 아래 깔려 있는 공통의 본질</div>
        <p class="callout-text">
          이 패턴들의 본질은 하나입니다: <strong>봇이 내 돈과 토큰을 쓰기 전에, 자신이 무엇을 해야 하는지 이해했음을 먼저 증명하게 만드는 것</strong>입니다. 첫 출근한 유능한 신입사원에게 우리가 자연스럽게 기대하는 방식과 정확히 같습니다 — 그리고 이는 우연이 아니라, 제품 전체가 바로 이 '동료 비유' 위에 세워져 있기 때문입니다.
        </p>
      </div>
    </div>
    {get_footer(11)}
  </div>
    """

def render_page_12():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">10 · PROMPT LIBRARY</div>
    <h1 class="page-title">실전 프롬프트 원문</h1>
    <p class="page-intro">
      스트리밍 현장에서 사용된 프롬프트들을 거의 손질하지 않고 날것 그대로 수록했습니다. 중요한 것은 프롬프트의 형태입니다: <strong>목표 결과물, 제약 조건, 신뢰할 수 있는 출처, 그리고 작업 완료 시 취할 행동</strong>이 어떻게 결합되어 있는지 주목해 보세요.
    </p>

    <div class="prompt-card">
      <div class="prompt-label">비서실장(Chief of Staff) 봇 생성 프롬프트</div>
      <div class="prompt-content">
        “네 역할은 Email Ethan, Slide Sonia, Data Dan에게 연락해서 각자 지금 무슨 작업을 하고 있는지 업데이트를 받는 것이다.”
      </div>
      <div class="prompt-meta">
        → 뒤이어 등록된 루틴: "2시간마다 팀원들에게 진행 상황을 묻고, 병목이나 차단 요소(Blocker)가 있는지 확인해라."
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">조용히 대기하는 노션 지식창고 봇</div>
      <div class="prompt-content">
        “이 봇의 임무는 다른 모든 봇들의 대화를 모니터링하는 것이지만, 구체적으로 호출되지 않는 한 아무것도 하지 않고 대기하는 것이다. 메시지가 네게 올 때까지 기다려라. 우리는 노션(Notion)을 선별적으로만 업데이트하길 원한다. 모든 정보를 무작정 쏟아붓고 싶지 않다. 그러니 반드시 내게 먼저 확인할 것.”
      </div>
      <div class="prompt-meta">
        — 로샨(Roshan). 이 프롬프트의 핵심은 절제(Restraint) 조항입니다. 다른 곳에서는 이를 "마치 git log처럼 다루라"고 표현했습니다.
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">매번 소리치는 대신 한 번 정의해 두는 P0 긴급 대응 방침</div>
      <div class="prompt-content">
        “5분마다 클라우드 에이전트들을 점검하는 루틴을 설정해라. 에이전트들이 궤도를 이탈했는지 확인하라 — 예를 들어 sleep 300 같은 긴 대기 상태에 빠졌거나, 원래 목표에서 벗어났거나, 지나치게 소극적으로 변했는지. 이상을 발견하는 즉시 개입하여 주의를 환기하고 바로잡아라.”
      </div>
      <div class="prompt-meta">
        — 링 시(Ling Shi). 그의 핵심 통찰: 에이전트에게 매번 "이거 긴급해!"라고 소리치면 단계를 건너뛰고 억측을 남발합니다. 잘 정의된 정책은 그렇지 않습니다.
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">프로덕션 버그를 신중하게 다루는 법</div>
      <div class="prompt-content">
        “우리 ELO 시스템이나 매치메이킹이 꼬인 것 같아. ThursdayArena.com에서 게임을 할 때마다 다른 플레이어의 덱 대신 AI 플레이어와 매칭되는데, 리더보드의 ELO 점수는 요동치고 있어. 무슨 일인지 원인을 파악해 봐. 포테이토 모드를 사용하고, 조사는 Cursor 클라우드 에이전트를 써라. 아직 PR은 열지 마. 무슨 상황인지 네 분석 내용만 먼저 가져와.”
      </div>
      <div class="prompt-meta">
        — 로샨. 증상, 증거, 사용할 도구, 그리고 코드 작성 전 명시적인 정지 명령까지 완벽한 구조입니다.
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">⚠️</div>
      <div class="callout-body">
        <div class="callout-title">안전 조항이 포함된 피드백 파이프라인 구축</div>
        <p class="callout-text">
          “위 링크는 유저 피드백이 들어오는 우리 슬랙 채널이야. 피드백을 살펴보고, 분류(Triage)하고, 이슈 재현을 시도한 다음 노션 데이터베이스에 티켓을 등록하는 팩토리 워크플로우를 구축하고 싶어. 매우 중요한 점은, <strong>AI를 사용해 피드백을 검토할 때는 프롬프트 인젝션(Prompt Injection) 공격에 주의하도록 AI에게 반드시 지시해야 한다는 거야.</strong> … 이해한 내용을 네 말로 요약해 봐.”<br>
          — 로렌. 유저가 제출한 텍스트는 신뢰할 수 없는 외부 입력입니다. 파이프라인을 구축하는 프롬프트에 이 보안 경고를 반드시 명시하세요.
        </p>
      </div>
    </div>
    {get_footer(12)}
  </div>
    """

def render_page_13():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">10 · PROMPT LIBRARY, CONTINUED</div>
    <h1 class="page-title">리서치, 개발 및 시장 진출</h1>

    <div class="prompt-card">
      <div class="prompt-label">프로토타이핑 전문가 봇 소환하기</div>
      <div class="prompt-content">
        “Cupcake 저장소에 만든 클라이언트 앱을 위해 프론트엔드 UI 탐색을 더 해보고 싶어. 앱을 극도로 가볍게 유지하면서도 3D 애니메이션을 더 많이 추가할 수 있는 프로토타입 제작 전담 봇을 하나 띄워줄래? 이 봇은 작업을 수행하기 위해 Cursor 클라우드 에이전트를 쓸 수 있어야 해. 여러 프론트엔드 작업에 걸쳐 포테이토 모드로 에이전트 스웜을 돌릴 수 있으면 좋겠어.”
      </div>
      <div class="prompt-meta">
        — 로렌이 닥터 에그봇에게 보낸 프롬프트. 산출물이 아니라 제약 조건("극도로 가볍게")과 실행 메커니즘을 명시한 점에 주목해 보세요.
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">최종 산출물을 명시한 경쟁사 리서치</div>
      <div class="prompt-content">
        “샌프란시스코 최고의 레스토랑 경영자들을 전부 뽑아내고, 그중 가장 훌륭한 웹사이트 5개를 골라줘. 그다음 그 웹사이트들에서 가장 뛰어난 팝업 페이지 5개를 찾아내. 그다음 지난 6~12개월간 주요 대도시에서 진행된 최고의 팝업 레스토랑 사례 5개를 찾아줘. 그리고 그 결과들을 하나의 문서로 깔끔하게 정리해 줘.”
      </div>
      <div class="prompt-meta">
        — 코디 산체스(Cody Sanchez). 단계마다 범위가 좁혀지는 체이닝(Chaining) 기법과 명확한 산출물 문서 지정.
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">요약으로 끝나지 않고 전략적 포지셔닝으로 이어지는 시장 조사</div>
      <div class="prompt-content">
        “우리 웹사이트를 분석해서 제품이 무엇이고 우리가 어떤 시장에서 플레이하는지 깊이 있게 이해해 봐. 이제 경쟁사 분석을 수행해라: 경쟁사들을 식별하고 깊이 있게 이해하며, 그들의 마케팅 웹사이트와 포지셔닝을 분석해. 그리고 가장 중요하게, 우리가 그들에 맞서 전략적, 경쟁우위적 포지셔닝을 취할 수 있는 기회와 틈새(Gaps)를 도출해 내라.”
      </div>
      <div class="prompt-meta">
        — 조시 킴(Josh Kim). 단순 정보 나열 리서치 리포트를 실질적인 전략 실행 문서로 탈바꿈시키는 마지막 문장.
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">명명된 스킬을 통해 에이전트 스웜에 작업 위임하기</div>
      <div class="prompt-content">
        “이 광고 슬롯에 누구를 넣어야 할지 ICP(이상적 고객 프로필)를 찾는 걸 도와줘. 너한테 'FindMyICP'라는 스킬이 있어. … 우리가 도출한 타깃 페르소나를 Clay MCP에 넣고, 기업 및 인물 데이터베이스를 검색해서 이 조건에 맞는 기업 10곳의 구체적인 목록을 뽑아줘.”
      </div>
      <div class="prompt-meta">
        — 명명된 스킬 호출, 명시적인 커넥터 지정, 범위가 한정된 산출물 요구.
      </div>
    </div>

    <div class="prompt-card">
      <div class="prompt-label">메모리에 영구적인 선호도 각인시키기</div>
      <div class="prompt-content">
        “앞으로 나를 부를 때 내 성과 이름을 함께 부르지 말고, 오직 내 이름(First name)으로만 부르도록 해.”
      </div>
      <div class="prompt-meta">
        — 암리타. 한 번만 말하면 영구 메모리에 저장되어 이후 모든 대화에 지속 적용됩니다.
      </div>
    </div>

    <div class="footnote">
      *이 모든 프롬프트들을 관통하는 공통 패턴: <strong>신뢰할 수 있는 단일 출처(Source of Truth)를 명명하세요.</strong> "모든 주장은 Sherlock 봇의 데이터를 기반으로 할 것"이라는 문구가 봇의 역할 정의에 포함되었습니다. 전문가 봇에게 어떤 동료의 말이 권위 있는 출처인지 알려줄 때, 환각은 갈 곳을 잃고 소멸합니다.
    </div>
    {get_footer(13)}
  </div>
    """

def render_page_14():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">11 · ORCHESTRATION</div>
    <h1 class="page-title">도구가 아닌 팀을 운영하는 법</h1>
    <p class="page-intro">
      봇이 대략 5개를 넘어가기 시작하면, 사용자가 모든 메시지를 일일이 중계하고 라우팅하는 것이 시스템 최대의 병목이 됩니다. 이를 극복하기 위해 스트리밍에서 반복적으로 등장한 <strong>4가지 오케스트레이션 패턴</strong>이 있습니다.
    </p>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">1 · 비서실장 (The Chief of Staff)</div>
        <ul class="custom-bullets">
          <li>사용자가 거의 전적으로 대화하는 단 하나의 총괄 봇; 세부 전문가들에게 업무를 라우팅하고 결과를 취합해 보고합니다.</li>
          <li>새로운 봇이 생성되면 비서실장이 직접 온보딩을 진행 — 맥락과 플레이북을 전달하므로 사용자가 말을 반복할 필요가 없습니다.</li>
          <li>사이먼의 원칙: 모든 하위 봇을 비서실장을 통해 생성하여, 비서실장이 각 봇의 존재 목적을 정확히 알게 하라.</li>
          <li>블레이크는 중간 관리자 없이 단 한 명의 비서실장 아래 15~20명의 전문가 봇을 직속으로 운영했습니다.</li>
          <li>단, 만능은 아닙니다 — 섭(Shub)은 전문가와 직접 대화하는 것을 선호한다고 밝혔습니다.</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">2 · 플레이북 브로드캐스트</div>
        <ul class="custom-bullets">
          <li>하나의 봇이 노션(Notion) 등에 저장된 팀의 '살아있는 플레이북(규정집)'을 총괄 소유합니다.</li>
          <li>새로운 팀 기준이 생기면 이 봇에게 단 한 번만 말해주고, 봇이 전체 팀원에게 이를 전파합니다.</li>
          <li>"당신은 무엇을 해야 할지 딱 한 번만 생각하면 됩니다… 모든 엔지니어 봇이 당신이 일일이 말하지 않아도 그 규칙을 알게 됩니다."</li>
          <li>표준 규칙 예시: 모든 PR은 UI의 경우 스크린샷, 백엔드의 경우 성능 지표를 필수로 첨부해야 한다.</li>
        </ul>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">3 · 스태프 미팅 (The Staff Meeting)</div>
        <ul class="custom-bullets">
          <li>중요한 결정을 내릴 때 서로 다른 관점을 가진 여러 봇을 하나의 그룹 스레드에 초대하여 토론시킵니다.</li>
          <li>블레이크는 봇들에게 항상 반대 의견을 내라고 지시했습니다 — "다들 찬성만 하면 부른 의미가 없으니까요."</li>
          <li>비서실장이 난상토론을 종합하여 사용자에게 최종 추천안을 보고합니다.</li>
          <li><strong>경고: 그룹 채팅은 매우 수다스럽고 비쌉니다.</strong> 일상 업무가 아니라 의사결정이 필요할 때에만 제한적으로 사용하세요.</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">4 · 하위 봇 군단 (Sub-bot Army)</div>
        <ul class="custom-bullets">
          <li>중간급 봇 하나가 컨텍스트가 가벼운 대규모 워커 봇 군단에게 대용량 배치 작업을 위임합니다.</li>
          <li>사이먼의 '솔저(Soldiers)' 봇들은 공유 그룹 스레드를 통해 100~200개 기업 어카운트를 병렬로 동시 조사했습니다.</li>
          <li>확장이 매우 용이하며, 산출물은 총괄 봇 한 곳으로 모여 검수를 거칩니다.</li>
          <li>엔지니어링 스웜과 동일한 구조: 한 명의 오케스트레이터와 수많은 일회용 일꾼들.</li>
        </ul>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">아무도 완전히 해결하지 못한 현실적 고민</div>
        <p class="callout-text">
          수많은 에이전트를 병렬로 돌리는 소감이 어떠냐는 질문에 매튜 버먼(Matthew Berman)은 이렇게 답했습니다: "그 어느 때보다 많은 일을 해내고 있습니다. <strong>하지만 동시에, 그 어느 때보다 바쁩니다.</strong>" 동시에 돌아가는 수십 개의 에이전트 사이를 오가며 컨텍스트를 전환하는 것은 현실적이며 아직 완벽히 해결되지 않은 인지적 비용입니다. 비서실장 패턴은 현재 우리가 취할 수 있는 최선의 해법이지만, 이는 완벽한 치료제가 아니라 고통을 줄여주는 완화책일 뿐입니다.
        </p>
      </div>
    </div>
    {get_footer(14)}
  </div>
    """

def render_page_15():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">12 · ECONOMICS</div>
    <h1 class="page-title">실제 소요 비용과 비용 누수 방지</h1>
    <p class="page-intro">
      과금은 사용량 기반입니다: 봇과 나누는 대화 토큰 비용과 봇 자체의 컴퓨터 사용(Computer-use VM) 연산 비용을 지불합니다. 다음은 방송 중에 직접 언급된 실제 비용 수치들과, 참가자들이 돈을 낭비하는 것으로 목격된 4가지 핵심 누수 지점입니다.
    </p>

    <div class="grid-4col">
      <div class="stat-card">
        <div class="stat-val">$20–30</div>
        <div class="stat-desc">세일즈 케이스 스터디 슬라이드 덱 1편 제작 (수작업 시 4~5시간 분량)</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">$1–2</div>
        <div class="stat-desc">중간 난이도 고객 지원 티켓 1건 엔드투엔드 처리</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">$0.20</div>
        <div class="stat-desc">단순 케이스 버킷 분류 및 배치 스크립트 적용 후 티켓당 비용</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">~$1,000</div>
        <div class="stat-desc">봇이 더 저렴한 전기 요금제를 찾아 아낀 연간 절감액 (인간 시간 60초)</div>
      </div>
    </div>

    <div class="section-label">비용이 새어 나가는 4대 구멍 (The Four Leaks)</div>
    <div style="margin-bottom: 9pt;">
      <div class="num-item">
        <div class="num-badge">1</div>
        <div class="num-content">
          <strong>과도하게 잦은 루틴.</strong> 압도적인 비용 누수 1위 요인. "15분마다 실행되는 루틴이 3개만 있어도 하루에 수백 건의 메시지가 발생합니다." 실행 빈도를 감사하고, 정기 스케줄보다 이벤트 트리거를 쓰며, 일상 업무는 하루 1~2회로 충분합니다.
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">2</div>
        <div class="num-content">
          <strong>API가 존재하는데 브라우저 자동화를 쓰는 경우.</strong> 컴퓨터 유즈로 웹 폼을 클릭하는 것은 네이티브 API 호출보다 훨씬 비쌉니다. 섭(Shub)의 노하우: 봇이 브라우저로 작업하는 것을 한 번 지켜본 뒤, 트리거된 네트워크 요청을 분석하게 하여 다음부터는 해당 엔드포인트를 직접 호출하게 만드세요.
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">3</div>
        <div class="num-content">
          <strong>방치된 그룹 채팅.</strong> 그룹 챗의 봇들은 서로의 말을 받아치며 끝없이 수다를 떨어 토큰을 순식간에 태웁니다. 일상 업무는 1:1 멘션 호출을 유지하세요.
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">4</div>
        <div class="num-content">
          <strong>봇의 무분별한 증식 (Bot Sprawl).</strong> 봇이 늘어날수록 더 많은 루틴이 돌고, 컨텍스트가 중복되며, 혼선이 가중됩니다. 군살 없는 슬림한 팀이 가장 경제적인 팀입니다.
        </div>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">실제로 조절 가능한 비용 레버</div>
        <ul class="custom-bullets">
          <li>봇의 응답 길이(Verbosity) 조정 — 말투와 장황함의 정도가 토큰 소비에 직결됩니다.</li>
          <li>더 이상 필요 없는 지난 맥락은 봇에게 잊으라고(Forget) 지시하세요.</li>
          <li>Grok Bot 자체에게 현재 설정 중 비용 최적화할 부분이 있는지 진단을 요청해 보세요.</li>
          <li>다른 봇들의 루틴과 스킬 효율을 지속적으로 감사하고 최적화하는 전담 봇을 두세요.</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">조절할 수 없는 부분</div>
        <div class="card-body">
          <p>
            컴퓨터 유즈 자체의 연산 단가는 사용자가 직접 튜닝할 수 없습니다. 비용을 줄이는 유일한 방법은 <strong>덜 쓰는 것</strong>입니다: MCP 커넥터가 있다면 연결하고, 다른 대안이 도저히 없을 때에만 최후의 수단으로 브라우저 조작을 사용하세요.
          </p>
        </div>
      </div>
    </div>
    {get_footer(15)}
  </div>
    """

def render_page_16():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">13 · APPROVALS AND BLAST RADIUS</div>
    <h1 class="page-title">브레이크가 있는 자율성</h1>
    <p class="page-intro">
      매튜(Matthew)의 정리는 가장 명쾌했습니다: <strong>"봇을 신뢰하고 그들에게 주도권(Agency)을 부여하세요. 그리고 동시에 가드레일을 쳐두세요. 무언가를 세상에 배포하기 전에 봇이 반드시 당신에게 확인을 받으러 올 것임을 알기에, 일이 파국으로 치닫지 않는다는 확신을 가질 수 있습니다."</strong>
    </p>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">오토 리뷰와 명시적 규칙</div>
        <ul class="custom-bullets">
          <li>내장 분류기가 작업의 위험도를 평가하여 위험한 행동 전에는 사용자에게 질문합니다.</li>
          <li>그 위에 명시적 규칙을 얹습니다: "내 승인 없이 이메일 보내지 마라", "슬라이드 작성은 자유롭게 해도 좋다."</li>
          <li>액션 타입별 토글 — 예: 프로덕션 배포는 항상 먼저 물어볼 것.</li>
          <li>조심스러운 기본값: 한 봇은 폼을 생성하기 전 개인정보(PII)를 수집하는지부터 스스로 검토했습니다.</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">자격증명과 보안 금고 (Vault)</div>
        <ul class="custom-bullets">
          <li>보안 폼을 통해 시크릿을 저장소에 보관하며, 에이전트는 절대 원본 비밀번호를 직접 보지 못합니다.</li>
          <li>행사 도중 1Password 연동이 출시되어 봇이 금고를 통해 안전하게 재인증할 수 있게 되었습니다.</li>
          <li>공유 템플릿에는 메모리, 설정, 스킬, 루틴만 복사되며 비밀번호나 대화 내역은 제외됩니다.</li>
          <li>위임하고 싶지 않은 중요 로그인은 사용자가 직접 화면을 제어하세요.</li>
        </ul>
      </div>
    </div>

    <div class="section-label">실전 방송에서 뼈아프게 배운 3가지 교훈</div>
    <div style="margin-bottom: 9pt;">
      <div class="num-item">
        <div class="num-badge">1</div>
        <div class="num-content">
          <strong>경쟁 요소가 있는 기능은 반드시 서버 권한(Server-authoritative)이어야 한다.</strong> 게임 로직이 클라이언트에 남아있자 맷은 개발자 도구를 열고 실시간으로 자기 스탯을 조작했습니다. 클라이언트에 아예 관련 코드가 없어야 합니다.
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">2</div>
        <div class="num-content">
          <strong>유저가 제출한 텍스트는 전부 공격 표면(Attack Surface)이다.</strong> 피드백 파이프라인에 클라이언트 길이 제한, 욕설 필터, 입력값 살균, LLM 가드, 레이트 리밋, 프롬프트 인젝션 방어 지침을 전부 탑재해야 했습니다.
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">3</div>
        <div class="num-content">
          <strong>자율적 버그 수정이 프로덕션을 마비시킬 수 있다.</strong> 실제로 팩토리가 잘못 작성한 SQL 쿼리가 방송 도중 라이브 게임을 다운시켰습니다. 마이그레이션과 배포에는 아무리 자동화가 훌륭해도 사람의 승인 관문을 유지해야 합니다.
        </div>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">신규 봇을 위한 기어가기-걷기-뛰기 사다리 (Crawl-Walk-Run)</div>
        <p class="callout-text">
          고객 지원에서 데이비드(David)가 보여준 단계적 접근법은 모든 분야에 적용됩니다: 처음에는 오직 문서를 읽고 요약만 하는 봇으로 시작하고, 그 다음엔 내부 메모 형태로 초안만 작성하게 하며, 신뢰가 충분히 쌓인 후에야 비로소 직접 발송하고 행동하도록 권한을 엽니다 — 이때도 고객 대면 지식창고 수정과 같이 <strong>위험 반경(Blast Radius)이 가장 큰 행동에는 사람의 승인을 필수 요건으로 유지</strong>합니다. "단순하게 시작하세요. 봇을 여러분의 기존 업무 방식에 맞추려 해야지, 그 반대가 되어서는 안 됩니다."
        </p>
      </div>
    </div>
    {get_footer(16)}
  </div>
    """
