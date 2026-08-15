# Het Tientallig Stelsel — Onze Dagelijkse Basis

We gebruiken het **tientallig stelsel** elke dag. Maar heb je er wel eens bij stilgestaan dat dit slechts **één van de vele mogelijke stelsels** is? De keuze voor 10 cijfers heeft waarschijnlijk alles te maken met het feit dat we **10 vingers** hebben.

In deze module leggen we de basis. Straks ontdek je dat andere culturen en computers helemaal andere stelsels gebruikten — met 2, 12, 20 of zelfs 60 als basis!

## Het getal 2345,678

In ons stelsel heeft **elke positie** een waarde die een macht van 10 is:

<div style="display: flex; gap: 4px; justify-content: center; flex-wrap: wrap; margin: 20px 0; font-family: monospace;">
  <div style="text-align: center; padding: 8px; background: #dbeafe; border-radius: 6px; min-width: 50px;">
    <div style="font-size: 11px; color: #2563eb;">10³</div>
    <div style="font-size: 20px; font-weight: bold;">2</div>
    <div style="font-size: 10px; color: #64748b;">duizendtallen</div>
  </div>
  <div style="text-align: center; padding: 8px; background: #dbeafe; border-radius: 6px; min-width: 50px;">
    <div style="font-size: 11px; color: #2563eb;">10²</div>
    <div style="font-size: 20px; font-weight: bold;">3</div>
    <div style="font-size: 10px; color: #64748b;">honderdtallen</div>
  </div>
  <div style="text-align: center; padding: 8px; background: #dbeafe; border-radius: 6px; min-width: 50px;">
    <div style="font-size: 11px; color: #2563eb;">10¹</div>
    <div style="font-size: 20px; font-weight: bold;">4</div>
    <div style="font-size: 10px; color: #64748b;">tientallen</div>
  </div>
  <div style="text-align: center; padding: 8px; background: #bfdbfe; border: 2px solid #2563eb; border-radius: 6px; min-width: 50px;">
    <div style="font-size: 11px; color: #2563eb;">10⁰</div>
    <div style="font-size: 20px; font-weight: bold;">5</div>
    <div style="font-size: 10px; color: #64748b;">eenheden</div>
  </div>
  <div style="font-size: 24px; color: #2563eb; font-weight: bold; padding: 0 4px; align-self: center;">,</div>
  <div style="text-align: center; padding: 8px; background: #fef3c7; border-radius: 6px; min-width: 50px;">
    <div style="font-size: 11px; color: #d97706;">10⁻¹</div>
    <div style="font-size: 20px; font-weight: bold;">6</div>
    <div style="font-size: 10px; color: #64748b;">tienden</div>
  </div>
  <div style="text-align: center; padding: 8px; background: #fef3c7; border-radius: 6px; min-width: 50px;">
    <div style="font-size: 11px; color: #d97706;">10⁻²</div>
    <div style="font-size: 20px; font-weight: bold;">7</div>
    <div style="font-size: 10px; color: #64748b;">honderdsten</div>
  </div>
  <div style="text-align: center; padding: 8px; background: #fef3c7; border-radius: 6px; min-width: 50px;">
    <div style="font-size: 11px; color: #d97706;">10⁻³</div>
    <div style="font-size: 20px; font-weight: bold;">8</div>
    <div style="font-size: 10px; color: #64748b;">duizendsten</div>
  </div>
</div>

**2345,678** = 2×10³ + 3×10² + 4×10¹ + 5×10⁰ + 6×10⁻¹ + 7×10⁻² + 8×10⁻³

## De komma verschuift

Dit is de sleutel tot **alle** positiestelsels — niet alleen het tientallige:

- **× 10** → komma 1 plaats naar **rechts** (groter)
- **× 100** → komma 2 plaatsen naar **rechts** (groter)
- **× 0,1** → komma 1 plaats naar **links** (kleiner)
- **× 0,01** → komma 2 plaatsen naar **links** (kleiner)

> 💡 **Vooruitblik:** Bij het binaire stelsel (basis 2) verschuift de komma ook — maar dan per **factor 2**. Bij het twaalftallige (basis 12) per **factor 12**.

---

## 🎯 Oefenmodus

Oefen hier tot je **8 van de 10** vragen goed hebt. Pas dan wordt de officiële toets vrijgegeven.

<div id="fase1-oefen" style="background: #f8fafc; border-radius: 12px; padding: 20px; margin-top: 20px;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
    <strong>Oefening <span id="f1-vraagnr">1</span>/10</strong>
    <span style="color: #64748b;">Score: <span id="f1-score">0</span>/10 (nodig: 8/10)</span>
  </div>
  <div id="f1-som" style="text-align: center; font-size: 1.2rem; margin: 16px 0;"></div>
  <div id="f1-opties" style="display: flex; gap: 8px; justify-content: center; flex-wrap: wrap;"></div>
  <div id="f1-feedback" style="margin-top: 12px; padding: 10px; border-radius: 8px; display: none;"></div>
  <div id="f1-klaar" style="display: none; text-align: center; padding: 20px; background: #dcfce7; border-radius: 10px; margin-top: 12px;">
    <div style="font-size: 2rem;">🎉<p style="color: #166534; margin-top: 8px;">📝 Scroll naar beneden voor de officiële toets!</p>
  </div>
    <strong style="color: #166534;">Je bent er klaar voor!</strong>
    <p style="color: #166534;">Je beheerst het tientallig stelsel. Nu gaan we ontdekken hoe andere stelsels werken...</p>
  </div>
</div>

<script>
(function() {
  let current = 0, correct = 0;
  const somEl = document.getElementById('f1-som');
  const optiesEl = document.getElementById('f1-opties');
  const feedbackEl = document.getElementById('f1-feedback');
  const scoreEl = document.getElementById('f1-score');
  const vraagnrEl = document.getElementById('f1-vraagnr');
  const klaarEl = document.getElementById('f1-klaar');

  function genSom() {
    const getal = Math.floor(Math.random() * 90 + 10);
    const machten = [-2, -1, 1, 2, 3];
    const macht = machten[Math.floor(Math.random() * machten.length)];
    const antwoord = getal * Math.pow(10, macht);
    const verkeerd = [antwoord * 10, antwoord / 10, antwoord * 100, antwoord / 100];
    const opties = [antwoord, ...verkeerd].map(x => {
      if (Math.abs(x) >= 10000 || (Math.abs(x) < 0.001 && x !== 0)) return x.toExponential(1);
      return parseFloat(x.toPrecision(4));
    }).sort(() => Math.random() - 0.5);

    somEl.innerHTML = 'Hoeveel is <strong>' + getal + ' × 10<sup>' + macht + '</sup></strong>?';
    optiesEl.innerHTML = '';
    feedbackEl.style.display = 'none';

    opties.forEach((opt, i) => {
      const btn = document.createElement('button');
      btn.textContent = opt;
      btn.style.cssText = 'padding: 10px 20px; border-radius: 8px; border: 2px solid #e2e8f0; background: white; cursor: pointer; font-size: 1rem; font-family: monospace;';
      btn.onmouseenter = () => { if (!btn.disabled) btn.style.borderColor = '#2563eb'; };
      btn.onmouseleave = () => { if (!btn.disabled) btn.style.borderColor = '#e2e8f0'; };
      btn.onclick = () => check(opt, antwoord, macht, btn);
      optiesEl.appendChild(btn);
    });
  }

  function check( gekozen, antwoord, macht, btn ) {
    const isGoed = parseFloat(gekozen) === parseFloat(antwoord);
    Array.from(optiesEl.children).forEach(b => { b.disabled = true; b.style.opacity = '0.5'; });
    btn.style.opacity = '1';
    if (isGoed) {
      btn.style.borderColor = '#22c55e';
      btn.style.background = '#dcfce7';
      correct++;
      feedbackEl.innerHTML = '✅ Goed! De komma verschoof ' + Math.abs(macht) + ' plaatsen naar ' + (macht > 0 ? 'rechts' : 'links') + '.';
      feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #dcfce7; color: #166534;';
    } else {
      btn.style.borderColor = '#ef4444';
      btn.style.background = '#fee2e2';
      feedbackEl.innerHTML = '❌ Niet goed. Tip: 10<sup>' + macht + '</sup> betekent de komma ' + Math.abs(macht) + ' plaatsen ' + (macht > 0 ? 'rechts' : 'links') + '.';
      feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #fee2e2; color: #991b1b;';
    }
    scoreEl.textContent = correct;
    current++;
    vraagnrEl.textContent = current + 1;

    if (current >= 10) {
      optiesEl.innerHTML = '';
      somEl.innerHTML = '';
      feedbackEl.style.display = 'none';
      klaarEl.style.display = 'block';
      const toetsSection = document.querySelector('section');
      const toetsLock = document.getElementById('toets-lock');
      if (toetsSection) toetsSection.style.display = '';
      if (toetsLock) toetsLock.style.display = 'none';
    } else {
      const nextBtn = document.createElement('button');
      nextBtn.textContent = 'Volgende →';
      nextBtn.style.cssText = 'margin-top: 8px; padding: 6px 16px; background: #2563eb; color: white; border: none; border-radius: 6px; cursor: pointer;';
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