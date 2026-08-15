# De Grote Sprong: km³ → mm³

Dit is de uitdaging waar je mee begon. Van **kubieke kilometer** naar **kubieke millimeter**.

## Het probleem

<div style="background: #fef2f2; border-radius: 10px; padding: 16px; margin: 20px 0; font-family: monospace; font-size: 0.9rem;">
  <div style="color: #991b1b; font-weight: bold; margin-bottom: 8px;">1 km³ = 1.000.000.000.000.000.000 mm³</div>
  <div style="color: #64748b; font-size: 0.8rem;">Dat is een 1 met 18 nullen!</div>
</div>

De komma verschuift **18 plaatsen**. Dat is onmogelijk in één keer te overzien.

## De oplossing: werk in stappen via m³

<div style="background: white; border-radius: 10px; padding: 16px; margin: 20px 0; font-family: monospace; font-size: 0.85rem; line-height: 1.8;">
  <strong>Stap 1:</strong> km³ → m³<br>
  &nbsp;&nbsp;1 km = 10³ m<br>
  &nbsp;&nbsp;1 km³ = (10³ m)³ = <strong>10⁹ m³</strong><br>
  &nbsp;&nbsp;Komma verschuift <strong>9 plaatsen</strong><br><br>

  <strong>Stap 2:</strong> m³ → mm³<br>
  &nbsp;&nbsp;1 m = 10³ mm<br>
  &nbsp;&nbsp;1 m³ = (10³ mm)³ = <strong>10⁹ mm³</strong><br>
  &nbsp;&nbsp;Komma verschuift <strong>9 plaatsen</strong><br><br>

  <strong>Totaal:</strong> 10⁹ × 10⁹ = <strong>10¹⁸</strong><br>
  &nbsp;&nbsp;Komma verschuift <strong>18 plaatsen</strong>!
</div>

## Wetenschappelijke notatie

Voor hele grote getallen gebruiken we **wetenschappelijke notatie**:

- 1.000.000 = **1 × 10⁶**
- 1.000.000.000 = **1 × 10⁹**
- 1.000.000.000.000.000.000 = **1 × 10¹⁸**

---

## 🎯 Oefenmodus

Oefen hier tot je **8 van de 10** vragen goed hebt. Pas dan wordt de officiële toets vrijgegeven.

<div id="fase5-oefen" style="background: #fef2f2; border-radius: 12px; padding: 20px; margin-top: 20px; border: 2px solid #dc2626;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
    <strong>Oefening <span id="f5-vraagnr">1</span>/10</strong>
    <span style="color: #64748b;">Score: <span id="f5-score">0</span>/10 (nodig: 8/10)</span>
  </div>
  <div id="f5-som" style="text-align: center; font-size: 1.1rem; margin: 16px 0;"></div>
  <div style="text-align: center; font-size: 0.8rem; color: #64748b; margin-bottom: 8px;">Tip: werk eerst om naar m³</div>
  <div id="f5-opties" style="display: flex; gap: 8px; justify-content: center; flex-wrap: wrap;"></div>
  <div id="f5-feedback" style="margin-top: 12px; padding: 10px; border-radius: 8px; display: none;"></div>
  <div id="f5-klaar" style="display: none; text-align: center; padding: 20px; background: #dcfce7; border-radius: 10px; margin-top: 12px;">
    <div style="font-size: 2rem;">🏆<p style="color: #166534; margin-top: 8px;">📝 Scroll naar beneden voor de officiële toets!</p>
  </div>
    <strong style="color: #166534; font-size: 1.1rem;">Alles behaald!</strong>
    <p style="color: #166534;">Je hebt het metrieke stelsel volledig onder de knie.</p>
    <div style="font-size: 3rem;">🎓🌱🎉</div>
  </div>
</div>

<script>
(function() {
  let current = 0, correct = 0;
  const somEl = document.getElementById('f5-som');
  const optiesEl = document.getElementById('f5-opties');
  const feedbackEl = document.getElementById('f5-feedback');
  const scoreEl = document.getElementById('f5-score');
  const vraagnrEl = document.getElementById('f5-vraagnr');
  const klaarEl = document.getElementById('f5-klaar');

  function genSom() {
    const getal = Math.floor(Math.random() * 9 + 1);
    const van = 'km';
    const naar = 'mm';
    const plaatsen = 18;
    const antwoord = getal * Math.pow(10, plaatsen);
    const opties = [
      antwoord.toExponential(1),
      (getal * Math.pow(10, 6)).toExponential(1),
      (getal * Math.pow(10, 12)).toExponential(1),
      (getal * Math.pow(10, 9)).toExponential(1)
    ].sort(() => Math.random() - 0.5);

    somEl.innerHTML = 'Reken uit: <strong>' + getal + ' ' + van + '³ = ? ' + naar + '³</strong>';
    optiesEl.innerHTML = '';
    feedbackEl.style.display = 'none';

    opties.forEach((opt) => {
      const btn = document.createElement('button');
      btn.textContent = opt;
      btn.style.cssText = 'padding: 10px 16px; border-radius: 8px; border: 2px solid #e2e8f0; background: white; cursor: pointer; font-size: 0.9rem; font-family: monospace;';
      btn.onmouseenter = () => { if (!btn.disabled) btn.style.borderColor = '#dc2626'; };
      btn.onmouseleave = () => { if (!btn.disabled) btn.style.borderColor = '#e2e8f0'; };
      btn.onclick = () => check(opt, antwoord.toExponential(1), van, naar, plaatsen, btn);
      optiesEl.appendChild(btn);
    });
  }

  function check(gekozen, antwoord, van, naar, plaatsen, btn) {
    const isGoed = gekozen === antwoord;
    Array.from(optiesEl.children).forEach(b => { b.disabled = true; b.style.opacity = '0.5'; });
    btn.style.opacity = '1';
    if (isGoed) {
      btn.style.borderColor = '#22c55e'; btn.style.background = '#dcfce7';
      correct++;
      feedbackEl.innerHTML = '✅ Goed! De komma verschoof ' + plaatsen + ' plaatsen. ' + van + '³ → m³ = ×10⁹, m³ → ' + naar + '³ = ×10⁹, totaal = ×10¹⁸.';
      feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #dcfce7; color: #166534;';
    } else {
      btn.style.borderColor = '#ef4444'; btn.style.background = '#fee2e2';
      feedbackEl.innerHTML = '❌ Niet goed. Werk via m³: ' + van + '³ → m³ (9 plaatsen) → ' + naar + '³ (9 plaatsen) = ' + plaatsen + ' plaatsen totaal.';
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
      nextBtn.style.cssText = 'margin-top: 8px; padding: 6px 16px; background: #dc2626; color: white; border: none; border-radius: 6px; cursor: pointer;';
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