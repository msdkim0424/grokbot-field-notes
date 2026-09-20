# -*- coding: utf-8 -*-
# Pages 1 to 8 for Korean Grok Bot Guide

def get_header():
    return """
    <div class="header">
      <div class="header-left">
        <span class="dot"></span>
        <span>GROK BOT</span>
      </div>
      <div class="header-right">가이드 · XAI</div>
    </div>
    """

def get_footer(pno):
    return f"""
    <div class="footer">
      <div>{pno:02d}/24</div>
      <div>x.ai/bot</div>
    </div>
    """

def render_page_01():
    return """
  <div class="page cover">
    <div class="cover-header">
      <h1 class="cover-title">SpaceX 엔지니어들의<br>Grok Bot 가이드</h1>
      <p class="cover-sub">72시간의 실시간 스트리밍, 3일간의 기록.</p>
    </div>
    <div class="cover-image-container">
      <img src="cover-people.png" class="cover-image" />
    </div>
  </div>
    """

def render_page_02():
    items = [
        ("01", "실 험", "3일간의 실시간 스트리밍이 실제로 만들어낸 결과물"),
        ("02", "멘탈 모델", "태스크가 아니라 동료(팀원)로 대하기 — 관점의 변화가 설정을 바꾼다"),
        ("03", "봇이 실제로 부여받는 환경", "자체 컴퓨터, 독립된 메모리, 그리고 공유 파일시스템"),
        ("04", "첫 번째 팀 구성하기", "하나의 봇, 하나의 역할 — 그리고 봇 증식의 함정 피하기"),
        ("05", "봇을 만드는 봇", "닥터 에그봇(Dr. Eggbot), 영혼으로서의 디스크립션, 과적합된 역할 수정"),
        ("06", "스킬과 루틴", "시연을 통한 교육과 오류 교정의 축적"),
        ("07", "소프트웨어 팩토리", "포테이토 모드, 에이전트 스웜, 그리고 완전 자율주행"),
        ("08", "검증이 성패의 전부다", "가장 먼저 구축해야 할 최고의 레버리지"),
        ("09", "검증된 7가지 프롬프트 패턴", "실전에서 거듭 확인된 핵심 프롬프트 기법"),
        ("10", "실전 프롬프트 라이브러리", "생방송 현장에서 그대로 건져 올린 프롬프트 원문"),
        ("11", "확장 가능한 오케스트레이션", "비서실장, 플레이북 전파, 스태프 미팅, 하위 봇 군단"),
        ("12", "실제 소요 비용과 경제성", "실제 비용 데이터와 돈이 새어 나가는 4대 구멍"),
        ("13", "승인 절차와 위험 반경 통제", "자동 리뷰, 보안 금고(Vault), 인젝션 방어, 서버 권한"),
        ("14", "케이스 스터디: Thursday Arena", "72시간 만에 제로에서 실제 게임 출시까지"),
        ("15", "실제 투입된 봇 팀 명단", "실제 팀에 투입된 모든 봇들의 명단과 담당 역할"),
        ("16", "실무 현장의 6가지 봇 조합", "실제 업무 현장에서 가동 중인 6가지 실전 구성"),
        ("17", "라이브 방송 중 발생한 실패", "방송 중에 터진 10가지 사고들과 그로부터 얻은 교훈"),
        ("18", "현재의 한계와 향후 로드맵", "아직 지원되지 않는 기능들과 앞으로 출시될 기능들"),
        ("19", "팀의 솔직한 회고", "72시간의 끝에서 엔지니어들이 털어놓은 날것의 진실"),
        ("20", "첫 주 실천 가이드", "바로 오늘 시작할 수 있는 실천 체크리스트"),
    ]
    
    rows_html = ""
    for num, title, desc in items:
        rows_html += f"""
      <div class="toc-item">
        <span class="toc-num">{num}</span>
        <span class="toc-title">{title}</span>
        <span class="toc-desc">{desc}</span>
      </div>
        """
    
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">TABLE OF CONTENTS</div>
    <h1 class="page-title">가이드 목차 및 개요</h1>
    <div class="toc-list">
      {rows_html}
    </div>
    {get_footer(2)}
  </div>
    """

def render_page_03():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">01 · THE EXPERIMENT</div>
    <h1 class="page-title">3일간의 실시간 스트리밍, 하나의 회사를 세우다</h1>
    <p class="page-intro">
      Grok Bot 팀의 세 엔지니어 — <strong>맷 팔머(Matt Palmer)</strong>, <strong>로샨(Roshan)</strong>, 그리고 <strong>로렌(Lauren, 일명 "Potato")</strong> — 가 빈 GitHub 조직, 빈 Slack, 빈 Notion, 그리고 아무런 사업 아이디어도 없는 상태로 샌프란시스코의 한 스튜디오에 모였습니다. 그리고 72시간 후, 수천 명의 사용자가 플레이하는 실제 라이브 프로덕트가 탄생했습니다. 이 가이드의 모든 내용은 그 3일간의 실전 스트리밍에서 도출되었습니다.
    </p>

    <div class="grid-3col">
      <div class="card">
        <div class="card-title">Day 1 — 아이디어 도출</div>
        <div class="card-body">
          레스토랑 팝업 기획에서 팝업 플랫폼으로, 다시 아트 전시회로, 그리고 굿즈 팝업으로 하루 만에 네 번 피벗. 소프트웨어 구현은 결코 병목이 아니었습니다. 무엇을 만들지에 합의하는 것이 진짜 병목이었습니다.
        </div>
      </div>
      <div class="card">
        <div class="card-title">Day 2 — 본격 개발</div>
        <div class="card-body">
          게임 스튜디오로 전격 피벗. 'Cupcake'이라는 코드명의 오토배틀러 게임을 순수 HTML 프로토타입으로 제작해 실시간으로 플레이 — 스탯 버그, 실시간 치팅 시연까지 날것 그대로 진행되었습니다.
        </div>
      </div>
      <div class="card">
        <div class="card-title">Day 3 — 공식 출시</div>
        <div class="card-body">
          밤사이에 봇 팩토리가 170개의 PR을 머지했습니다. 오전 10시, 게임은 <strong>Thursday Arena</strong>라는 이름으로 공식 런칭되었습니다. 방송 종료 시점: 머지된 PR 433개, 페이지뷰 약 30,000회, 경기 수 약 6,000회, 매출 $0.
        </div>
      </div>
    </div>

    <div class="grid-4col">
      <div class="stat-card">
        <div class="stat-val">433</div>
        <div class="stat-desc">3일간 머지된 풀 리퀘스트(PR) 수</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">~2,000</div>
        <div class="stat-desc">출시 당일 로그인한 실제 플레이어 수</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">~30k</div>
        <div class="stat-desc">출시된 게임의 총 페이지뷰 수</div>
      </div>
      <div class="stat-card">
        <div class="stat-val">$0</div>
        <div class="stat-desc">실제 매출 — 가감 없는 솔직한 수치</div>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">왜 라이브 스트리밍 기반 가이드가 읽을 가치가 있는가</div>
        <p class="callout-text">
          공식 프로덕트 문서는 기능이 무엇을 하는지만 설명합니다. 하지만 편집되지 않은 72시간의 라이브 개발 과정은 사람들이 극심한 시간 압박 속에서 <strong>실제로 무엇을 하는지</strong> 보여줍니다 — 어떤 패턴이 끝까지 살아남고, 어떤 패턴이 과도한 비용을 초래하며, 어떤 패턴이 조용히 망가지는지를 말이죠. 여기에 정리된 거의 모든 내용은 누군가의 설명이 아닌, 실제 행동에서 추출한 실전 프랙티스입니다.
        </p>
      </div>
    </div>

    <div class="footnote">
      *이름 표기에 대한 참고: 자동 자막 트랜스크립트에서는 이 제품을 "GrokBot", "Rockbot", "Brockbot"으로, 회사를 "SpaceX AI" 등으로 표기하기도 하지만 모두 동일한 대상을 의미합니다. 수치는 스트리밍 중에 직접 언급된 것으로 당일 기준입니다.
    </div>
    {get_footer(3)}
  </div>
    """

def render_page_04():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">02 · MENTAL MODEL</div>
    <h1 class="page-title">태스크가 아니라 동료(팀원)로 대하기</h1>
    <p class="page-intro">
      제품 기획자 중 한 명인 로만(Roman)은 첫 번째 스트리밍의 문을 열며 전체 제품을 관통하는 핵심 명제를 제시했습니다: <strong>"우리는 사용자가 Grok Bot을 쓸 때, 마치 실제 직장 동료나 팀원과 함께 일하는 것처럼 느끼기를 진심으로 바랐습니다."</strong> 인터페이스가 의도적으로 iMessage 형태로 디자인된 이유도 바로 여기에 있으며, 그 형태가 이 가이드의 모든 모범 사례를 이끕니다.
    </p>

    <div class="section-label">제품을 지탱하는 3가지 기본 전제</div>
    <div style="margin-bottom: 11pt;">
      <div class="num-item">
        <div class="num-badge">1</div>
        <div class="num-content">
          <strong>태스크 패러다임이 아닌, 동료(Teammate) 패러다임.</strong> 봇은 한번 쓰고 버리는 일회성 대화 스레드가 아닙니다. 몇 달 동안 계속해서 다시 찾아가는, 이름이 있는 동료입니다. 지식과 맥락이 계속 축적됩니다.
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">2</div>
        <div class="num-content">
          <strong>모든 봇에게 자체 컴퓨터가 주어진다.</strong> 브라우저가 탑재된 독립된 Linux 가상머신(VM)입니다. 레거시 소프트웨어, 정부 포털, API가 전혀 없는 사이트 등 마우스와 화면으로 사람이 할 수 있는 모든 작업을 수행할 수 있습니다.
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">3</div>
        <div class="num-content">
          <strong>모든 것이 클라우드에서 실행된다.</strong> 노트북 덮개를 닫아도 작업은 중단되지 않습니다. "당신이 휴가를 떠나 있거나 잠든 밤 사이에도 봇은 묵묵히 일을 계속합니다."
        </div>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">실무에서 달라지는 점</div>
        <ul class="custom-bullets">
          <li><strong>설정하는 것이 아니라, 채용하는 것이다.</strong> 봇의 범위를 정의하는 일은 설정 페이지를 채우는 것보다 채용 직무 기술서(JD)를 작성하는 것에 훨씬 가깝습니다.</li>
          <li><strong>피드백은 복리로 누적된다.</strong> 봇이 왜 틀렸는지 이유를 가르쳐주는 것은 귀찮은 방해가 아니라 미래를 위한 투자입니다.</li>
          <li><strong>완성된 작업물로 돌아온다.</strong> 암리타(Amrita)의 명언: "이미 완성된 작업물을 확인하는 순간이야말로 Grok Bot 최고의 경험입니다."</li>
          <li><strong>중간에 개입해도 괜찮다.</strong> 봇이 작업 중일 때 방향을 수정해 주는 것은 지극히 정상이며 적극 권장됩니다.</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">모델(Model) vs 하네스(Harness)</div>
        <div class="card-body">
          <p>로샨(Roshan)은 작업이 어디서 이루어져야 하는지 명확한 경계선을 그었습니다:</p>
          <ul class="custom-bullets" style="margin-top: 4pt;">
            <li><strong>Grok</strong>은 파운데이션 모델이다.</li>
            <li><strong>Grok Bot</strong>은 하네스(Harness)다 — 의도적으로 가볍게 설계되어 오케스트레이션, 도구 활용, 의사결정 및 판단에 최적화되어 있습니다.</li>
            <li><strong>Cursor 클라우드 에이전트</strong>는 무거운 코딩을 담당하는 하네스다 — 실제 소프트웨어 엔지니어링 작업이 필요할 때 Grok Bot이 작업을 위임하는 대상입니다.</li>
          </ul>
          <p style="margin-top: 5pt; font-weight: 600; color: #111;">*Grok Bot 안에서 프로토타입을 만들고, 클라우드 에이전트를 통해 배포하십시오.*</p>
        </div>
      </div>
    </div>

    <div class="quote-box">
      <p class="quote-text">“90% 수준까지 도달하는 것과, 사람이 손 하나 대지 않고 처음부터 끝까지 완전하게 끝내는 것의 차이는 정말 엄청납니다. 실로 마법 같은 경험이죠.”</p>
      <p class="quote-author">로만(Roman) · Grok Bot 101, Day 1</p>
    </div>
    {get_footer(4)}
  </div>
    """

def render_page_05():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">03 · ARCHITECTURE</div>
    <h1 class="page-title">봇이 실제로 부여받는 환경</h1>
    <p class="page-intro">
      여러분들이 만든 봇들 사이에 <strong>무엇이 공유되고 무엇이 공유되지 않는지</strong> 명확히 아는 것은, 스트리밍 참가자들이 겪은 수많은 놀라운 현상(긍정적이든 부정적이든)을 이해하는 열쇠입니다.
    </p>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">🖥 자체 컴퓨터 (Linux VM)</div>
        <ul class="custom-bullets">
          <li>봇마다 브라우저, 터미널, 설치 가능한 앱이 포함된 전용 <strong>Linux VM</strong>이 제공됩니다.</li>
          <li>한 봇이 다른 봇의 화면을 들여다볼 수 없습니다 — 이 격리 덕분에 두 봇이 같은 슬라이드 덱의 서로 다른 페이지를 동시에 편집할 수 있습니다.</li>
          <li>로그인, 2FA 인증, 캡차(CAPTCHA) 등 직접 통제하고 싶은 순간에는 사용자가 화면을 가로채 직접 조작할 수 있습니다.</li>
          <li>VM이 Linux 기반이므로, <strong>Linux와 호환되지 않거나 MCP로 제공되지 않는 도구는 아예 사용할 수 없습니다.</strong> (Q&A에서 명확히 밝혀짐).</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">🧠 독립된 메모리</div>
        <ul class="custom-bullets">
          <li>메모리는 <strong>봇마다 개별적으로</strong> 부여되며, 오래 유지되고 직접 편집할 수 있습니다. 한 번 지정한 사용자 선호도는 영구히 유지됩니다.</li>
          <li>각 봇은 고유한 <strong>컨텍스트 한계(Context Limit)</strong>를 가집니다 — 업무를 여러 세부 역할로 쪼개야 하는 가장 현실적인 이유입니다.</li>
          <li>필요 없는 맥락은 잊어버리라고(Forget) 명령할 수 있으며, 이를 통해 토큰 비용을 절감합니다.</li>
          <li><strong>봇을 복제(Duplicate)하면</strong> 페르소나는 복사되지만 메모리는 0에서 새로 시작합니다.</li>
        </ul>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">📁 공유 파일시스템</div>
        <ul class="custom-bullets">
          <li>봇들은 컨텍스트는 공유하지 않지만 <strong>파일은 공유합니다</strong> — "하나의 VM 위에 여러 개의 서로 다른 데스크톱 창을 띄워둔 것과 같은 구조입니다."</li>
          <li><strong>스킬은 전역(Global)으로 적용됩니다.</strong> 한 봇에게 가르쳐준 스킬은 조직 내의 모든 봇이 즉시 사용할 수 있습니다.</li>
          <li>브라우저 로그인 세션은 머신 상에 저장되어 서로 다른 작업 사이에서도 유지됩니다.</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">🔌 도구에 접근하는 두 가지 방식</div>
        <ul class="custom-bullets">
          <li><strong>커넥터 / MCP</strong> — "에이전트를 위한 API." 훨씬 빠르고 저렴하며 권한 허용 목록(화이트리스트) 관리가 쉽습니다. 존재하는 경우 무조건 우선 사용하십시오.</li>
          <li><strong>컴퓨터 유즈 (Computer Use)</strong> — API가 없는 모든 작업을 위한 보편적 대체재입니다. 단, 속도가 느리고 비용이 더 많이 듭니다.</li>
          <li>봇에게 MCP URL을 알려주면 <strong>알아서 커넥터를 직접 설치합니다.</strong></li>
        </ul>
      </div>
    </div>

    <div class="callout">
      <div class="callout-icon">⚠️</div>
      <div class="callout-body">
        <div class="callout-title">공유 파일시스템은 보안 경계가 아닙니다</div>
        <p class="callout-text">
          메모리는 분리되어 있지만 파일과 브라우저 세션은 공유되므로, 봇을 나눈다고 해서 권한(Access)이 분리되는 것이 아니라 단지 <strong>관심사(Attention)가 분리될 뿐</strong>입니다. 진정한 보안 경계가 필요하다면 다른 봇을 만들 것이 아니라 로그아웃, 커넥터 범위 제한, 계정 권한 분리를 통해 명시적 경계를 그어야 합니다.
        </p>
      </div>
    </div>

    <div class="footnote">
      *3일간 확인된 지원 플랫폼: macOS, Windows, Linux, iOS, iPadOS, Android. 설정에는 클라우드 VM 대신 로컬 머신에서 봇이 작동하도록 하는 로컬 실행 토글이 있지만, 팀은 병렬 처리 능력과 로컬 앱의 포커스 탈취 문제를 고려해 클라우드 환경을 강력히 권장합니다.
    </div>
    {get_footer(5)}
  </div>
    """

def render_page_06():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">04 · BUILDING A ROSTER</div>
    <h1 class="page-title">하나의 봇, 하나의 역할</h1>
    <p class="page-intro">
      이것은 3일간 모든 발표자가 입을 모아 가장 많이 반복했던 단 하나의 조언입니다. 모든 것을 다 하는 만능 비서 하나가 아니라, 각자의 고유한 이름이 있는 <strong>세부 전문가들로 구성된 명단(Roster)</strong>을 운영하라는 것입니다.
    </p>

    <div class="section-label">단일 역할 봇이 훨씬 뛰어난 4가지 이유</div>
    <div style="margin-bottom: 10pt;">
      <div class="num-item">
        <div class="num-badge">1</div>
        <div class="num-content">
          <strong>컨텍스트 범위가 좁게 유지된다.</strong> 각 봇마다 고유한 컨텍스트 한도가 있습니다. 4가지 무관한 작업을 동시에 저글링하는 제너럴리스트 봇은 금세 토큰을 소진하고 이전 내용을 망각하기 시작합니다.
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">2</div>
        <div class="num-content">
          <strong>누구에게 물어볼지 뇌가 쉽게 기억한다.</strong> 링 시(Ling Shi)의 비유: "사람의 뇌도 소설책 전체를 외울 수 없습니다. 정확히 누구를 참조해야 할지 아는 것이 핵심입니다."
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">3</div>
        <div class="num-content">
          <strong>명확한 역할이 주어질 때 모델의 성능이 극대화된다.</strong> 피드백이 실질적인 의미를 가지려면 업무 범위가 충분히 좁아야 하며, 이때 학습 루프가 날카롭게 정렬됩니다.
        </div>
      </div>
      <div class="num-item">
        <div class="num-badge">4</div>
        <div class="num-content">
          <strong>공짜로 병렬 처리를 얻는다.</strong> 5명의 전문가 봇에게 동시에 작업을 던져두고, 각자 일하게 한 뒤 나중에 결과를 취합하면 됩니다 — 사람이 일하는 '회의 → 분과별 실행 → 재동기화' 패턴과 완벽히 일치합니다.
        </div>
      </div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">좋은 역할 정의에 담겨야 할 내용</div>
        <ul class="custom-bullets">
          <li>모호한 "일반 보조"를 피하고 좁게 정의하십시오: 인재 발굴(Talent Scout), 경비 관리자(Expense Manager), 버그 재현 전문가(Bug Reproduction).</li>
          <li>이름 붙일 수 있을 만큼 명확하고 단일한 책임 영역.</li>
          <li>해당 봇이 사용 가능한 구체적인 도구 및 데이터 소스.</li>
          <li>단순히 어떤 일인지가 아니라 업무에 접근하는 사고방식.</li>
          <li>작업을 실행하기 전에 반드시 사용자 승인이 필요한 항목.</li>
          <li>정기적으로 반복해야 하는 업무인 경우 그 일정.</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">사이드바를 체계적으로 정리하기</div>
        <ul class="custom-bullets">
          <li>조직도처럼 섹션별로 봇을 묶으십시오 — 리더십(Leadership), 엔지니어링(Engineering), 워룸(War Room).</li>
          <li>라벨은 각 봇의 전문 분야를 시각적으로 상기시켜 주는 필수 요소입니다. 특히 음식 이름으로 봇을 부를 때는 더욱 중요합니다.</li>
          <li>사이먼(Simon)은 기능별로 색상을 지정했습니다: 리서치(주황), 고객 어카운트(초록), 아웃바운드(기타) — 스레드 색상만 보고도 파이프라인의 어느 단계인지 즉시 파악할 수 있습니다.</li>
          <li>매일 실제로 사용하는 핵심 봇 3~4개를 상단에 고정하십시오.</li>
        </ul>
      </div>
    </div>

    <div class="footnote">
      *이름 짓기는 단순한 장식이 아닙니다. 팀은 시청자 채팅을 통해 테이터(Tater), 위스크(Whisk), 베이크(Bake), 닥터 에그봇(Dr. Eggbot) 같은 이름을 붙였고, 이는 작업에 대해 소통하는 방식을 완전히 바꾸어 놓았습니다. 이름을 가진 봇에게는 자연스럽게 일을 위임하지만, '태스크 3' 같은 봇은 미세 관리(마이크로매니징)하게 됩니다.
    </div>

    <div class="callout">
      <div class="callout-icon">⚠️</div>
      <div class="callout-body">
        <div class="callout-title">봇 증식(Bot Sprawl)의 함정</div>
        <p class="callout-text">
          스트리밍에서 가장 거대한 봇 팀을 운영했던 사이먼(Simon)은 솔직하게 털어놓았습니다: "저도 한때 봇을 너무 많이 만들었던 적이 있습니다. 솔직히 말해서 훨씬 더 혼란스러웠습니다. '새로운 봇이 이 일을 해야 할 진짜 이유가 있는가?'를 매번 의심해야 합니다." 블레이크(Blake) 역시 동일하게 조언했습니다: "팀을 슬림하게 유지하십시오. 45개의 봇은 절대 필요 없습니다." 봇을 새로 생성하는 건 쉽고 재미있기에 더욱 규칙이 필요합니다. 새 직원을 뽑기 전에, 기존 전문가에게 새로운 스킬이나 루틴을 추가할 수 있는지 먼저 검토하십시오.
        </p>
      </div>
    </div>
    {get_footer(6)}
  </div>
    """

def render_page_07():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">05 · THE META-BOT</div>
    <h1 class="page-title">봇을 만드는 봇</h1>
    <p class="page-intro">
      3일간 가장 많이 호출된 봇은 엔지니어도, 리서처도 아니었습니다. 바로 다른 봇들을 생성하고, 검토하고, 개선하는 일만을 전담하는 메타 봇 <strong>닥터 에그봇(Dr. Eggbot)</strong>이었습니다. 스트리밍에 등장한 거의 모든 새로운 동료 봇은 에그봇에게 던진 한 문장에서 태어났습니다.
    </p>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">메타 봇이 수행하는 핵심 업무</div>
        <ul class="custom-bullets">
          <li>일상적인 자연어 설명으로부터 새로운 봇을 생성.</li>
          <li>시스템 프롬프트 역할을 하는 디스크립션(Description)을 작성.</li>
          <li>팀 명단을 감사(Audit): "우리 봇들을 전체 검토해 봐. 어디가 병목이지?"</li>
          <li>찰떡같은 작명. 두 사람이 서로 다른 방에서 따로 요청했는데 둘 다 "Ping"이라는 이름을 추천받았을 정도입니다.</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">디스크립션은 봇의 영혼이다</div>
        <ul class="custom-bullets">
          <li>디스크립션 필드는 단순한 메모 라벨이 아닙니다. 로렌(Lauren)의 표현대로 "누군가는 영혼(Soul) 또는 시스템 프롬프트라고 부르는 것"입니다.</li>
          <li>봇의 말투, 의사결정 기준, 하위 작업 위임 방식이 완전히 달라집니다.</li>
          <li>특정 사고 사례가 아닌 일반적인 <strong>원칙</strong>으로 작성하십시오.</li>
          <li>봇이 무엇을 소유하고 무엇을 다른 이에게 넘겨야 하는지 명시하십시오.</li>
          <li>신뢰할 수 있는 단일 출처(Source of Truth)를 명시적으로 지정하십시오.</li>
        </ul>
      </div>
    </div>

    <div class="card" style="margin-bottom: 9pt;">
      <div class="card-title">과적합(Overfitting)의 실패 — 그리고 올바른 해결책</div>
      <div class="card-body">
        <div class="prompt-label" style="color:#555;">닥터 에그봇이 처음에 작성했던 디스크립션</div>
        <div class="prompt-content" style="background:#fff; border-radius:5px; padding:6pt 8pt; margin-bottom:5pt; border:1px solid #e2ded9;">
          “우리 게임 스튜디오의 전체적인 맥락 파악. 단 하나의 업무: Pstack의 포테이토 모드와 클라우드 에이전트를 통해 개발 작업을 오케스트레이션하고, 이를 감독 및 검증하여 엔지니어링 결과물을 책임진다. 플레이북과 일치시키고 준수할 것.”
        </div>
        <p style="font-size:7.8pt; color:#666; margin-bottom:6pt;">
          → 로렌의 평가: <strong>지나치게 구체적이다.</strong> 오늘의 툴체인과 오늘 발생한 특정 사건을 봇의 영구적인 정체성으로 하드코딩해 버렸다.
        </p>
        <div class="prompt-label" style="color:#e4402e;">교정 지시 (The Correction)</div>
        <div class="prompt-content" style="background:#fff; border-radius:5px; padding:6pt 8pt; margin-bottom:4pt; border:1px solid #e2ded9;">
          “포테이토 모드를 다시 정독하고, 지나치게 지엽적인 이슈들에 매몰되는 대신 Cupcake 엔지니어가 따라야 할 일반 원칙들을 도출해 내라.”
        </div>
        <p style="font-size:7.8pt; color:#333; font-weight:600;">
          → 이것은 봇 디스크립션뿐만 아니라 당신이 작성하는 모든 스킬과 규칙에 적용되는 대원칙입니다.
        </p>
      </div>
    </div>

    <div class="footnote">
      *적합한 것이 있다면 마켓플레이스 템플릿에서 시작하십시오. 템플릿은 메모리, 루틴, 연동 설정을 담고 있으며, 공유 시 자격증명과 대화 내역은 안전하게 제거됩니다. 팀 역시 이미 존재하는 템플릿이 있다면 바닥부터 만들지 말고 거기서 시작하라고 권장했습니다.
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">요청하면 봇들이 스스로 팀원을 채용한다</div>
        <p class="callout-text">
          둘째 날 암리타(Amrita)는 두 개의 기존 봇에게 물었습니다: "너희가 지금 하고 있는 일을 바탕으로 볼 때, 계속해서 훌륭한 성과를 내기 위해 어떤 봇이 더 있으면 도움이 되겠니? 필요한 봇들을 직접 생성해 줘." 그러자 봇들은 즉시 세 명의 새로운 전문가 — 배틀카드 블레어(Battle Card Blair), 데모 드레이크(Demo Drake), AI 레이더(AI Radar) — 를 만들어냈으며, 각각 고유한 업무 정의와 권위 있는 데이터 출처까지 완비했습니다. 봇 명단에게 무엇이 부족한지 직접 묻는 것은 대단히 강력한 실전 테크닉입니다.
        </p>
      </div>
    </div>
    {get_footer(7)}
  </div>
    """

def render_page_08():
    return f"""
  <div class="page">
    {get_header()}
    <div class="eyebrow">06 · AUTOMATION</div>
    <h1 class="page-title">스킬과 루틴</h1>
    <p class="page-intro">
      자동화를 이루는 두 개의 블록. <strong>스킬(Skill)</strong>은 어떤 일을 '어떻게' 수행하는가를 정의합니다. <strong>루틴(Routine)</strong>은 그 일이 '언제' 일어나는가를 결정합니다. 스트리밍에서 살아남은 거의 모든 지속 가능한 워크플로우는 바로 이 순서대로 구축되었으며, 사람이 최소 한 번 이상 직접 손으로 해보기 전에는 결코 자동화하지 않았습니다.
    </p>

    <div class="flow-row">
      <div class="flow-step">1. 직접 손으로 해보기</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">2. 안정적 결과 도출</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">3. 스킬로 저장하기</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">4. 루틴 등록하기</div>
    </div>

    <div class="grid-2col">
      <div class="card">
        <div class="card-title">스킬이 생성되는 3가지 방식</div>
        <div class="card-subtitle">스킬은 전역(Global)입니다: 한 봇에게 가르치면 모든 봇이 공유합니다.</div>
        <ul class="custom-bullets">
          <li><strong>직접 시연하기 (By demonstration).</strong> "태스크 가르치기(Teach a task)"를 누르고 작업을 직접 한 번 수행하면, 봇이 화면 녹화를 재사용 가능한 스킬로 변환합니다. 슬라이드 애니메이션 제작과 경쟁사 블로그 스캔을 가르칠 때 실제로 쓰였습니다.</li>
          <li><strong>오류 교정하기 (By correction).</strong> 가장 가치 있는 방식입니다 (아래 콜아웃 참조).</li>
          <li><strong>직접 작성하기 (By writing it).</strong> 프로세스에 복잡한 조건 분기, 예외 처리, 사람의 승인 단계가 포함된 경우 한 번의 시연만으로는 봇이 이를 유추할 수 없습니다. 이때는 손으로 직접 로직을 작성해야 합니다.</li>
        </ul>
      </div>
      <div class="card">
        <div class="card-title">루틴 정의 시 반드시 필요한 항목</div>
        <div class="card-subtitle">실행 빈도는 비용 누수의 1순위 주범입니다 — 섹션 12 참조.</div>
        <ul class="custom-bullets">
          <li>어떤 봇이 해당 루틴을 소유하고 실행하는가</li>
          <li>실행 스케줄 및 타임존 — 또는 웹훅/이벤트 트리거</li>
          <li>입력 데이터가 유입되는 출처</li>
          <li>기대하는 최종 산출물 포맷</li>
          <li>사람의 승인이 필요한 명확한 경계선</li>
          <li>실패 시 처리 절차(Fallback)</li>
          <li>보고할 내용이 없을 때 취할 조치 — 아무 변경 사항이 없다면 침묵을 지키도록 명시하십시오(No-op silence).</li>
        </ul>
      </div>
    </div>

    <div class="footnote">
      *루틴 빈도는 돈이 조용히 사라지는 곳입니다. 정기 스케줄보다는 이벤트 트리거를 선호하고, 15분마다 실행하기보다는 하루 1~2회를 기본값으로 삼으십시오.
    </div>

    <div class="callout">
      <div class="callout-icon">🎯</div>
      <div class="callout-body">
        <div class="callout-title">사고의 디테일이 아니라, 교정의 원칙을 기록하라</div>
        <p class="callout-text">
          로샨(Roshan)의 원칙: "에이전트가 잘못 생각하는 것을 목격할 때마다, 매번 프롬프트를 땜질하기보다 이를 영구히 교정할 스킬을 만들 좋은 기회로 삼아야 합니다." 링 시(Ling Shi)의 표현은 더 날카롭습니다. 배수관을 매번 뚫지 말고 한 단계 더 깊은 근본 원인으로 내려가라는 것입니다. 하지만 반대편에도 함정이 있습니다. 특정 세션의 실패에 대응해 규칙을 쓸 때, "에이전트들은 그 세션의 사소한 디테일까지 전부 규칙에 집어넣는 경향이 있으며, 그러면 규칙이 지나치게 과적합되어 재사용성이 떨어집니다." 사건의 스토리는 지우고, 일반적인 원칙만 남기십시오.
        </p>
      </div>
    </div>
    {get_footer(8)}
  </div>
    """
