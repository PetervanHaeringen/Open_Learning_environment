# Inhoud omrekenen (3D)

Bij inhoud werken we in **drie dimensies**: lengte × breedte × hoogte.

## Waarom 3 plaatsen per trede?

<div style="display: flex; align-items: center; justify-content: center; gap: 20px; margin: 20px 0; flex-wrap: wrap;">
  <div style="text-align: center;">
    <div style="width: 60px; height: 60px; background: #ffedd5; border: 2px solid #ea580c; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; color: #c2410c;">1 dm³</div>
    <div style="font-size: 0.8rem; color: #64748b; margin-top: 4px;">1 dm³</div>
  </div>
  <div style="font-size: 1.5rem; color: #ea580c;">=</div>
  <div style="text-align: center;">
    <div style="width: 60px; height: 60px; background: #fff7ed; border: 2px solid #f97316; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; color: #c2410c;">1000 cm³</div>
    <div style="font-size: 0.8rem; color: #64748b; margin-top: 4px;">1000 cm³</div>
  </div>
</div>

**1 dm³ = 1000 cm³**

De komma verschuift **3 plaatsen** per trede, want:
- 1 dm = 10 cm
- 1 dm³ = (10 cm)³ = **1000 cm³**

## De regel

| Van → Naar | Aantal treden | Komma verschuift |
|------------|---------------|------------------|
| km³ → m³   | 3 treden      | 3 × 3 = **9 plaatsen** |
| m³ → cm³   | 2 treden      | 2 × 3 = **6 plaatsen** |
| dm³ → mm³  | 2 treden      | 2 × 3 = **6 plaatsen** |

---

## 🎯 Oefenmodus

Oefen hier tot je **8 van de 10** vragen goed hebt. Pas dan wordt de officiële toets vrijgegeven.

<div id="fase4-oefen" style="background: #fff7ed; border-radius: 12px; padding: 20px; margin-top: 20px; border: 2px solid #ea580c;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
    <strong>Oefening <span id="f4-vraagnr">1</span>/10</strong>
    <span style="color: #64748b;">Score: <span id="f4-score">0</span>/10 (nodig: 8/10)</span>
  </div>
  <div id="f4-som" style="text-align: center; font-size: 1.2rem; margin: 16px 0;"></div>
  <div id="f4-opties" style="display: flex; gap: 8px; justify-content: center; flex-wrap: wrap;"></div>
  <div id="f4-feedback" style="margin-top: 12px; padding: 10px; border-radius: 8px; display: none;"></div>
  <div id="f4-klaar" style="display: none; text-align: center; padding: 20px; background: #dcfce7; border-radius: 10px; margin-top: 12px;">
    <div style="font-size: 2rem;">🎉<p style="color: #166534; margin-top: 8px;">📝 Scroll naar beneden voor de officiële toets!</p>
  </div>
    <strong style="color: #166534;">Je beheerst inhoud!</strong>
    <p style="color: #166534;">Beantwoord nu de vragen hieronder.</p>
  </div>
</div>

<script>
(function() {
  let current = 0, correct = 0;
  const eenheden = [
    { naam: 'm', waarde: 0 }, { naam: 'dm', waarde: -1 },
    { naam: 'cm', waarde: -2 }, { naam: 'mm', waarde: -3 }
  ];
  const somEl = document.getElementById('f4-som');
  const optiesEl = document.getElementById('f4-opties');
  const feedbackEl = document.getElementById('f4-feedback');
  const scoreEl = document.getElementById('f4-score');
  const vraagnrEl = document.getElementById('f4-vraagnr');
  const klaarEl = document.getElementById('f4-klaar');

  function genSom() {
    const getal = Math.floor(Math.random() * 20 + 1);
    let van, naar;
    do {
      van = eenheden[Math.floor(Math.random() * eenheden.length)];
      naar = eenheden[Math.floor(Math.random() * eenheden.length)];
    } while (van.naam === naar.naam || Math.abs(van.waarde - naar.waarde) > 1);
    const factor = (van.waarde - naar.waarde) * 3;
    const antwoord = getal * Math.pow(10, factor);
    const verkeerd = [antwoord * 10, antwoord / 10, antwoord * 1000];
    const opties = [antwoord, ...verkeerd].map(x => {
      if (Math.abs(x) >= 10000000 || (Math.abs(x) < 0.000001 && x !== 0)) return x.toExponential(1);
      return parseFloat(x.toPrecision(5));
    }).sort(() => Math.random() - 0.5);

    somEl.innerHTML = 'Reken uit: <strong>' + getal + ' ' + van.naam + '³ = ? ' + naar.naam + '³</strong>';
    optiesEl.innerHTML = '';
    feedbackEl.style.display = 'none';

    opties.forEach((opt) => {
      const btn = document.createElement('button');
      btn.textContent = opt;
      btn.style.cssText = 'padding: 10px 20px; border-radius: 8px; border: 2px solid #e2e8f0; background: white; cursor: pointer; font-size: 1rem; font-family: monospace;';
      btn.onmouseenter = () => { if (!btn.disabled) btn.style.borderColor = '#ea580c'; };
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
      feedbackEl.innerHTML = '✅ Goed! Bij inhoud is de factor 10³ = 1000 per trede. Totaal: ' + Math.abs(factor) + ' plaatsen.';
      feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #dcfce7; color: #166534;';
    } else {
      btn.style.borderColor = '#ef4444'; btn.style.background = '#fee2e2';
      feedbackEl.innerHTML = '❌ Niet goed. Tip: inhoud = lengte³, dus de factor is 10³ = 1000 per trede (' + Math.abs(factor) + ' plaatsen).';
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
      nextBtn.style.cssText = 'margin-top: 8px; padding: 6px 16px; background: #ea580c; color: white; border: none; border-radius: 6px; cursor: pointer;';
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