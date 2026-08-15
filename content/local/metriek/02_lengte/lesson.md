# Lengte omrekenen (1D)

Nu we het tientallig stelsel begrijpen, kunnen we de **namen** toekennen aan de machten van 10.

## De metrische ladder voor lengte

<div style="display: flex; gap: 2px; justify-content: center; flex-wrap: wrap; margin: 20px 0;">
  <div style="text-align: center; padding: 8px 12px; background: #dcfce7; border-radius: 6px; min-width: 50px;">
    <div style="font-size: 13px; color: #16a34a; font-weight: bold;">km</div>
    <div style="font-size: 11px; color: #15803d;">10³ m</div>
  </div>
  <div style="text-align: center; padding: 8px 12px; background: #dcfce7; border-radius: 6px; min-width: 50px;">
    <div style="font-size: 13px; color: #16a34a; font-weight: bold;">hm</div>
    <div style="font-size: 11px; color: #15803d;">10² m</div>
  </div>
  <div style="text-align: center; padding: 8px 12px; background: #dcfce7; border-radius: 6px; min-width: 50px;">
    <div style="font-size: 13px; color: #16a34a; font-weight: bold;">dam</div>
    <div style="font-size: 11px; color: #15803d;">10¹ m</div>
  </div>
  <div style="text-align: center; padding: 8px 16px; background: #bbf7d0; border: 2px solid #16a34a; border-radius: 6px; min-width: 50px;">
    <div style="font-size: 13px; color: #16a34a; font-weight: bold;">m</div>
    <div style="font-size: 11px; color: #15803d;">10⁰ m</div>
  </div>
  <div style="text-align: center; padding: 8px 12px; background: #fef3c7; border-radius: 6px; min-width: 50px;">
    <div style="font-size: 13px; color: #d97706; font-weight: bold;">dm</div>
    <div style="font-size: 11px; color: #b45309;">10⁻¹ m</div>
  </div>
  <div style="text-align: center; padding: 8px 12px; background: #fef3c7; border-radius: 6px; min-width: 50px;">
    <div style="font-size: 13px; color: #d97706; font-weight: bold;">cm</div>
    <div style="font-size: 11px; color: #b45309;">10⁻² m</div>
  </div>
  <div style="text-align: center; padding: 8px 12px; background: #fef3c7; border-radius: 6px; min-width: 50px;">
    <div style="font-size: 13px; color: #d97706; font-weight: bold;">mm</div>
    <div style="font-size: 11px; color: #b45309;">10⁻³ m</div>
  </div>
</div>

**Regel:** per trede op de ladder verschuift de komma **1 plaats**.

- 2,5 km = **2500** m (3 treden → 3 plaatsen naar rechts)
- 450 cm = **4,50** m (2 treden → 2 plaatsen naar links)

---

## 🎯 Oefenmodus

Oefen hier tot je **8 van de 10** vragen goed hebt. Pas dan wordt de officiële toets vrijgegeven.

<div id="fase2-oefen" style="background: #f0fdf4; border-radius: 12px; padding: 20px; margin-top: 20px; border: 2px solid #16a34a;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
    <strong>Oefening <span id="f2-vraagnr">1</span>/10</strong>
    <span style="color: #64748b;">Score: <span id="f2-score">0</span>/10 (nodig: 8/10)</span>
  </div>
  <div id="f2-som" style="text-align: center; font-size: 1.2rem; margin: 16px 0;"></div>
  <div id="f2-opties" style="display: flex; gap: 8px; justify-content: center; flex-wrap: wrap;"></div>
  <div id="f2-feedback" style="margin-top: 12px; padding: 10px; border-radius: 8px; display: none;"></div>
  <div id="f2-klaar" style="display: none; text-align: center; padding: 20px; background: #dcfce7; border-radius: 10px; margin-top: 12px;">
    <div style="font-size: 2rem;">🎉<p style="color: #166534; margin-top: 8px;">📝 Scroll naar beneden voor de officiële toets!</p>
  </div>
    <strong style="color: #166534;">Je beheerst lengte!</strong>
    <p style="color: #166534;">Beantwoord nu de vragen hieronder.</p>
  </div>
</div>

<script>
(function() {
  let current = 0, correct = 0;
  const eenheden = [
    { naam: 'km', waarde: 3 }, { naam: 'hm', waarde: 2 }, { naam: 'dam', waarde: 1 },
    { naam: 'm', waarde: 0 }, { naam: 'dm', waarde: -1 }, { naam: 'cm', waarde: -2 }, { naam: 'mm', waarde: -3 }
  ];
  const somEl = document.getElementById('f2-som');
  const optiesEl = document.getElementById('f2-opties');
  const feedbackEl = document.getElementById('f2-feedback');
  const scoreEl = document.getElementById('f2-score');
  const vraagnrEl = document.getElementById('f2-vraagnr');
  const klaarEl = document.getElementById('f2-klaar');

  function genSom() {
    const getal = Math.floor(Math.random() * 900 + 100) / 10;
    let van, naar;
    do {
      van = eenheden[Math.floor(Math.random() * eenheden.length)];
      naar = eenheden[Math.floor(Math.random() * eenheden.length)];
    } while (van.naam === naar.naam || Math.abs(van.waarde - naar.waarde) > 3);
    const factor = van.waarde - naar.waarde;
    const antwoord = getal * Math.pow(10, factor);
    const verkeerd = [antwoord * 10, antwoord / 10, antwoord * 100];
    const opties = [antwoord, ...verkeerd].map(x => {
      if (Math.abs(x) >= 100000 || (Math.abs(x) < 0.0001 && x !== 0)) return x.toExponential(1);
      return parseFloat(x.toPrecision(5));
    }).sort(() => Math.random() - 0.5);

    somEl.innerHTML = 'Reken uit: <strong>' + getal + ' ' + van.naam + ' = ? ' + naar.naam + '</strong>';
    optiesEl.innerHTML = '';
    feedbackEl.style.display = 'none';

    opties.forEach((opt) => {
      const btn = document.createElement('button');
      btn.textContent = opt;
      btn.style.cssText = 'padding: 10px 20px; border-radius: 8px; border: 2px solid #e2e8f0; background: white; cursor: pointer; font-size: 1rem; font-family: monospace;';
      btn.onmouseenter = () => { if (!btn.disabled) btn.style.borderColor = '#16a34a'; };
      btn.onmouseleave = () => { if (!btn.disabled) btn.style.borderColor = '#e2e8f0'; };
      btn.onclick = () => check(opt, antwoord, van.naam, naar.naam, factor, btn);
      optiesEl.appendChild(btn);
    });
  }

  function check(gekozen, antwoord, van, naar, factor, btn) {
    const isGoed = Math.abs(parseFloat(gekozen) - antwoord) < 0.0001;
    Array.from(optiesEl.children).forEach(b => { b.disabled = true; b.style.opacity = '0.5'; });
    btn.style.opacity = '1';
    if (isGoed) {
      btn.style.borderColor = '#22c55e'; btn.style.background = '#dcfce7';
      correct++;
      feedbackEl.innerHTML = '✅ Goed! Van ' + van + ' naar ' + naar + ' is ' + Math.abs(factor) + ' trede(s), dus de komma verschoof ' + Math.abs(factor) + ' plaatsen.';
      feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #dcfce7; color: #166534;';
    } else {
      btn.style.borderColor = '#ef4444'; btn.style.background = '#fee2e2';
      feedbackEl.innerHTML = '❌ Niet goed. Van ' + van + ' naar ' + naar + ' is ' + Math.abs(factor) + ' trede(s) op de ladder.';
      feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #fee2e2; color: #991b1b;';
    }
    scoreEl.textContent = correct;
    current++;
    vraagnrEl.textContent = current + 1;

    if (current >= 10) {
      optiesEl.innerHTML = ''; somEl.innerHTML = ''; feedbackEl.style.display = 'none';
      klaarEl.style.display = 'block';
      const toetsSection = document.querySelector('section');
      const toetsLock = document.getElementById('toets-lock');
      if (toetsSection) toetsSection.style.display = '';
      if (toetsLock) toetsLock.style.display = 'none';
    } else {
      const nextBtn = document.createElement('button');
      nextBtn.textContent = 'Volgende →';
      nextBtn.style.cssText = 'margin-top: 8px; padding: 6px 16px; background: #16a34a; color: white; border: none; border-radius: 6px; cursor: pointer;';
      nextBtn.onclick = genSom;
      feedbackEl.appendChild(document.createElement('br'));
      feedbackEl.appendChild(nextBtn);
    }
  }

  genSom();
})();
</script>

<div id="toets-lock" style="text-align:center; padding:40px; background:#f8fafc; border-radius:12px; border:2px dashed #cbd5e1; margin:20px 0;">
  <div style="font-size:2rem;">🔒</div>
  <strong style="color:#475569; font-size:1.1rem;">Toets nog niet beschikbaar</strong>
  <p style="color:#64748b; margin:8px 0;">Behaal eerst 8/10 in de oefenmodus hierboven.</p>
</div>
<script id="toets-init-hide">
(function() {
  // Verberg de officiële toets tot de oefening is voltooid
  const toets = document.getElementById('official-test');
  if (toets) toets.style.display = 'none';
})();
</script>