# Het Twintigtallige Stelsel

Sommige culturen telden niet tot 10, maar tot **20**. Waarom? Omdat ze hun **vingers én tenen** gebruikten!

## Het Franse twintigtallig stelsel

In het Frans zie je nog restanten van het twintigtallig stelsel:

<div style="background: #f0fdf4; border-radius: 10px; padding: 16px; margin: 20px 0; font-family: monospace; font-size: 0.95rem; line-height: 1.8;">
  <div><strong>vingt</strong> = 20</div>
  <div><strong>quarante</strong> = 40 (2×20)</div>
  <div><strong>soixante</strong> = 60 (3×20)</div>
  <div><strong>soixante-dix</strong> = 70 (3×20+10)</div>
  <div><strong>quatre-vingt</strong> = 80 (4×20)</div>
  <div><strong>quatre-vingt-dix</strong> = 90 (4×20+10)</div>
</div>

Opvallend: na 60 gaat het Frans weer "tientallig" tellen met twintigtallige woorden!

## De Maya's

De Maya-beschaving (Midden-Amerika, ~250 n.Chr.) gebruikte een **positiestelsel met basis 20**. Hun cijfers:

<div style="display: flex; justify-content: center; gap: 16px; margin: 24px 0; flex-wrap: wrap;">
  <div style="text-align: center;">
    <div style="width: 40px; height: 40px; background: white; border: 2px solid #16a34a; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem;">•</div>
    <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">1 punt = 1</div>
  </div>
  <div style="text-align: center;">
    <div style="width: 40px; height: 40px; background: white; border: 2px solid #16a34a; display: flex; align-items: center; justify-content: center; font-size: 1.2rem;">—</div>
    <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">1 streep = 5</div>
  </div>
  <div style="text-align: center;">
    <div style="width: 40px; height: 40px; background: white; border: 2px solid #16a34a; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 0.9rem; gap: 2px;"><span>••</span><span>—</span></div>
    <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">7 = 5+2</div>
  </div>
  <div style="text-align: center;">
    <div style="width: 40px; height: 40px; background: white; border: 2px solid #16a34a; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">𝍖</div>
    <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">schelp = 0</div>
  </div>
</div>

De Maya's hadden zelfs een **concept van nul** — eeuwen voor Europa dat had!

---

## 🎯 Oefenmodus

Oefen hier tot je **8 van de 10** vragen goed hebt. Pas dan wordt de officiële toets vrijgegeven.

<div id="twintig-oefen" style="background: #f0fdf4; border-radius: 12px; padding: 20px; margin-top: 20px; border: 2px solid #16a34a;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
    <strong>Oefening <span id="tw-vraagnr">1</span>/10</strong>
    <span style="color: #64748b;">Score: <span id="tw-score">0</span>/10 (nodig: 8/10)</span>
  </div>
  <div id="tw-opdracht" style="text-align: center; font-size: 1.1rem; margin: 16px 0;"></div>
  <div id="tw-gebied" style="margin: 16px 0;"></div>
  <div id="tw-feedback" style="margin-top: 12px; padding: 10px; border-radius: 8px; display: none;"></div>
  <div id="tw-klaar" style="display: none; text-align: center; padding: 20px; background: #dcfce7; border-radius: 10px; margin-top: 12px;">
    <div style="font-size: 2rem;">🎉<p style="color: #166534; margin-top: 8px;">📝 Scroll naar beneden voor de officiële toets!</p>
  </div>
    <strong style="color: #166534;">Je beheerst het twintigtallig stelsel!</strong>
    <p style="color: #166534;">Beantwoord nu de vragen hieronder.</p>
  </div>
</div>

<script>
(function() {
  let current = 0, correct = 0;
  const opdrachtEl = document.getElementById('tw-opdracht');
  const gebiedEl = document.getElementById('tw-gebied');
  const feedbackEl = document.getElementById('tw-feedback');
  const scoreEl = document.getElementById('tw-score');
  const vraagnrEl = document.getElementById('tw-vraagnr');
  const klaarEl = document.getElementById('tw-klaar');

  function genSom() {
    const mode = Math.random() > 0.5 ? 'frans' : 'maya';

    if (mode === 'frans') {
      const twintigtallen = [
        { frans: 'vingt', waarde: 20 },
        { frans: 'trente', waarde: 30 },
        { frans: 'quarante', waarde: 40 },
        { frans: 'cinquante', waarde: 50 },
        { frans: 'soixante', waarde: 60 },
        { frans: 'soixante-dix', waarde: 70 },
        { frans: 'quatre-vingt', waarde: 80 },
        { frans: 'quatre-vingt-dix', waarde: 90 }
      ];
      const item = twintigtallen[Math.floor(Math.random() * twintigtallen.length)];
      const verkeerd = [item.waarde + 10, item.waarde - 10, item.waarde + 20];
      const opties = [item.waarde, ...verkeerd].sort(() => Math.random() - 0.5);

      opdrachtEl.innerHTML = 'Wat is de decimale waarde van <strong style="color: #16a34a;">' + item.frans + '</strong>?';
      gebiedEl.innerHTML = '';
      opties.forEach((opt) => {
        const btn = document.createElement('button');
        btn.textContent = opt;
        btn.style.cssText = 'padding: 10px 20px; border-radius: 8px; border: 2px solid #e2e8f0; background: white; cursor: pointer; font-size: 1rem; margin: 4px;';
        btn.onmouseenter = () => { if (!btn.disabled) btn.style.borderColor = '#16a34a'; };
        btn.onmouseleave = () => { if (!btn.disabled) btn.style.borderColor = '#e2e8f0'; };
        btn.onclick = () => {
          Array.from(gebiedEl.children).forEach(b => { b.disabled = true; b.style.opacity = '0.5'; });
          btn.style.opacity = '1';
          const isGoed = opt === item.waarde;
          if (isGoed) {
            btn.style.borderColor = '#22c55e'; btn.style.background = '#dcfce7';
            correct++;
            feedbackEl.innerHTML = '✅ Goed! ' + item.frans + ' = <strong>' + item.waarde + '</strong>.';
            feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #dcfce7; color: #166534;';
          } else {
            btn.style.borderColor = '#ef4444'; btn.style.background = '#fee2e2';
            feedbackEl.innerHTML = '❌ Niet goed. ' + item.frans + ' = <strong>' + item.waarde + '</strong>.';
            feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #fee2e2; color: #991b1b;';
          }
          scoreEl.textContent = correct;
          current++;
          vraagnrEl.textContent = current + 1;
          nextStep();
        };
        gebiedEl.appendChild(btn);
      });
    } else {
      const getal = Math.floor(Math.random() * 19 + 1);
      const strepen = Math.floor(getal / 5);
      const punten = getal % 5;
      let mayaVis = '';
      for (let i = 0; i < strepen; i++) mayaVis += '— ';
      for (let i = 0; i < punten; i++) mayaVis += '•';
      const verkeerd = [getal + 1, getal - 1, getal + 5].filter(x => x > 0 && x < 20);
      const opties = [getal, ...verkeerd].sort(() => Math.random() - 0.5);

      opdrachtEl.innerHTML = 'Wat is dit Maya-getal?<br><strong style="font-size: 1.5rem; color: #16a34a;">' + mayaVis.trim() + '</strong>';
      gebiedEl.innerHTML = '';
      opties.forEach((opt) => {
        const btn = document.createElement('button');
        btn.textContent = opt;
        btn.style.cssText = 'padding: 10px 20px; border-radius: 8px; border: 2px solid #e2e8f0; background: white; cursor: pointer; font-size: 1rem; margin: 4px;';
        btn.onmouseenter = () => { if (!btn.disabled) btn.style.borderColor = '#16a34a'; };
        btn.onmouseleave = () => { if (!btn.disabled) btn.style.borderColor = '#e2e8f0'; };
        btn.onclick = () => {
          Array.from(gebiedEl.children).forEach(b => { b.disabled = true; b.style.opacity = '0.5'; });
          btn.style.opacity = '1';
          const isGoed = opt === getal;
          if (isGoed) {
            btn.style.borderColor = '#22c55e'; btn.style.background = '#dcfce7';
            correct++;
            feedbackEl.innerHTML = '✅ Goed! ' + mayaVis.trim() + ' = <strong>' + getal + '</strong>.';
            feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #dcfce7; color: #166534;';
          } else {
            btn.style.borderColor = '#ef4444'; btn.style.background = '#fee2e2';
            feedbackEl.innerHTML = '❌ Niet goed. ' + mayaVis.trim() + ' = <strong>' + getal + '</strong> (— = 5, • = 1).';
            feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #fee2e2; color: #991b1b;';
          }
          scoreEl.textContent = correct;
          current++;
          vraagnrEl.textContent = current + 1;
          nextStep();
        };
        gebiedEl.appendChild(btn);
      });
    }
    feedbackEl.style.display = 'none';
  }

  function nextStep() {
    if (current >= 10) {
      gebiedEl.innerHTML = '';
      opdrachtEl.innerHTML = '';
      feedbackEl.style.display = 'none';
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