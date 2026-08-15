# Romeinse Cijfers

De Romeinen bouwden bruggen, aquaducten en een rijk dat heel Europa besloeg. Maar hun getallenstelsel? Dat was **niet hun sterkste punt**.

## De cijfers

<div style="display: flex; justify-content: center; gap: 8px; margin: 24px 0; flex-wrap: wrap; font-family: monospace; font-size: 1.1rem;">
  <div style="text-align: center; padding: 10px; background: #f5f5f4; border-radius: 8px; min-width: 50px;">
    <div style="font-size: 1.5rem; font-weight: bold; color: #57534e;">I</div>
    <div style="font-size: 0.75rem; color: #78716c;">1</div>
  </div>
  <div style="text-align: center; padding: 10px; background: #f5f5f4; border-radius: 8px; min-width: 50px;">
    <div style="font-size: 1.5rem; font-weight: bold; color: #57534e;">V</div>
    <div style="font-size: 0.75rem; color: #78716c;">5</div>
  </div>
  <div style="text-align: center; padding: 10px; background: #f5f5f4; border-radius: 8px; min-width: 50px;">
    <div style="font-size: 1.5rem; font-weight: bold; color: #57534e;">X</div>
    <div style="font-size: 0.75rem; color: #78716c;">10</div>
  </div>
  <div style="text-align: center; padding: 10px; background: #f5f5f4; border-radius: 8px; min-width: 50px;">
    <div style="font-size: 1.5rem; font-weight: bold; color: #57534e;">L</div>
    <div style="font-size: 0.75rem; color: #78716c;">50</div>
  </div>
  <div style="text-align: center; padding: 10px; background: #f5f5f4; border-radius: 8px; min-width: 50px;">
    <div style="font-size: 1.5rem; font-weight: bold; color: #57534e;">C</div>
    <div style="font-size: 0.75rem; color: #78716c;">100</div>
  </div>
  <div style="text-align: center; padding: 10px; background: #f5f5f4; border-radius: 8px; min-width: 50px;">
    <div style="font-size: 1.5rem; font-weight: bold; color: #57534e;">D</div>
    <div style="font-size: 0.75rem; color: #78716c;">500</div>
  </div>
  <div style="text-align: center; padding: 10px; background: #f5f5f4; border-radius: 8px; min-width: 50px;">
    <div style="font-size: 1.5rem; font-weight: bold; color: #57534e;">M</div>
    <div style="font-size: 0.75rem; color: #78716c;">1000</div>
  </div>
</div>

## De regels

- **Optellen:** als een kleiner cijfer rechts staat: VI = 5 + 1 = 6
- **Aftrekken:** als een kleiner cijfer links staat: IV = 5 − 1 = 4

## Het probleem

In het **Romeinse stelsel** telt de positie **niet mee** voor de waarde. Een X is altijd 10, of hij nu links of rechts staat. Vergelijk dat met ons stelsel: in **105** staat de 1 links en is die 100 waard, maar in **501** staat de 1 rechts en is die maar 1 waard.

<div style="background: #fef2f2; border-radius: 10px; padding: 16px; margin: 20px 0; border-left: 4px solid #dc2626;">
  <strong style="color: #991b1b;">Waarom het tientallig stelsel zo veel beter is:</strong>
  <ul style="margin: 8px 0 0 0; color: #7f1d1d;">
    <li>Romeins: CXXVII × XLIII = ??? (probeer het maar eens uit je hoofd)</li>
    <li>Tientallig: 127 × 43 = 5461 (met de komma-verschuif-regel)</li>
  </ul>
</div>

---

## 🎯 Oefenmodus

Oefen hier tot je **8 van de 10** vragen goed hebt. Pas dan wordt de officiële toets vrijgegeven.

<div id="romeins-oefen" style="background: #fafaf9; border-radius: 12px; padding: 20px; margin-top: 20px; border: 2px solid #78716c;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
    <strong>Oefening <span id="r-vraagnr">1</span>/10</strong>
    <span style="color: #64748b;">Score: <span id="r-score">0</span>/10 (nodig: 8/10)</span>
  </div>
  <div id="r-opdracht" style="text-align: center; font-size: 1.1rem; margin: 16px 0;"></div>
  <div id="r-gebied" style="margin: 16px 0;"></div>
  <div id="r-feedback" style="margin-top: 12px; padding: 10px; border-radius: 8px; display: none;"></div>
  <div id="r-klaar" style="display: none; text-align: center; padding: 20px; background: #dcfce7; border-radius: 10px; margin-top: 12px;">
    <div style="font-size: 2rem;">🏆<p style="color: #166534; margin-top: 8px;">📝 Scroll naar beneden voor de officiële toets!</p>
  </div>
    <strong style="color: #166534;">Je hebt alle getallenstelsels doorlopen!</strong>
    <p style="color: #166534;">Beantwoord nu de laatste vragen.</p>
    <div style="font-size: 3rem;">🎓🌱🎉</div>
  </div>
</div>

<script>
(function() {
  let current = 0, correct = 0;
  const opdrachtEl = document.getElementById('r-opdracht');
  const gebiedEl = document.getElementById('r-gebied');
  const feedbackEl = document.getElementById('r-feedback');
  const scoreEl = document.getElementById('r-score');
  const vraagnrEl = document.getElementById('r-vraagnr');
  const klaarEl = document.getElementById('r-klaar');

  function naarRomeins(num) {
    const waardes = [
      [1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
      [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'],
      [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']
    ];
    let result = '';
    for (const [waarde, symbool] of waardes) {
      while (num >= waarde) {
        result += symbool;
        num -= waarde;
      }
    }
    return result;
  }

  function vanRomeins(romeins) {
    const map = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
    let totaal = 0;
    for (let i = 0; i < romeins.length; i++) {
      const huidig = map[romeins[i]];
      const volgend = map[romeins[i + 1]] || 0;
      if (volgend > huidig) totaal -= huidig;
      else totaal += huidig;
    }
    return totaal;
  }

  function genSom() {
    const mode = Math.random() > 0.5 ? 'naar-romeins' : 'van-romeins';

    if (mode === 'naar-romeins') {
      const getal = [14, 19, 24, 39, 42, 49, 58, 67, 74, 83, 91, 99][Math.floor(Math.random() * 12)];
      const romeins = naarRomeins(getal);
      const verkeerd = [naarRomeins(getal + 1), naarRomeins(getal - 1), naarRomeins(getal + 10)].filter(x => x !== romeins);
      const opties = [romeins, ...verkeerd].sort(() => Math.random() - 0.5);

      opdrachtEl.innerHTML = 'Schrijf <strong style="color: #78716c;">' + getal + '</strong> als Romeins cijfer.';
      gebiedEl.innerHTML = '';
      opties.forEach((opt) => {
        const btn = document.createElement('button');
        btn.textContent = opt;
        btn.style.cssText = 'padding: 10px 20px; border-radius: 8px; border: 2px solid #e2e8f0; background: white; cursor: pointer; font-size: 1.2rem; font-family: serif; margin: 4px;';
        btn.onmouseenter = () => { if (!btn.disabled) btn.style.borderColor = '#78716c'; };
        btn.onmouseleave = () => { if (!btn.disabled) btn.style.borderColor = '#e2e8f0'; };
        btn.onclick = () => {
          Array.from(gebiedEl.children).forEach(b => { b.disabled = true; b.style.opacity = '0.5'; });
          btn.style.opacity = '1';
          const isGoed = opt === romeins;
          if (isGoed) {
            btn.style.borderColor = '#22c55e'; btn.style.background = '#dcfce7';
            correct++;
            feedbackEl.innerHTML = '✅ Goed! ' + getal + ' = <strong>' + romeins + '</strong>.';
            feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #dcfce7; color: #166534;';
          } else {
            btn.style.borderColor = '#ef4444'; btn.style.background = '#fee2e2';
            feedbackEl.innerHTML = '❌ Niet goed. ' + getal + ' = <strong>' + romeins + '</strong>.';
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
      const getal = [14, 19, 24, 39, 42, 49, 58, 67, 74, 83, 91, 99][Math.floor(Math.random() * 12)];
      const romeins = naarRomeins(getal);
      const verkeerd = [getal + 1, getal - 1, getal + 10].filter(x => x > 0 && x < 100);
      const opties = [getal, ...verkeerd].sort(() => Math.random() - 0.5);

      opdrachtEl.innerHTML = 'Wat is de decimale waarde van <strong style="font-family: serif; font-size: 1.5rem; color: #78716c;">' + romeins + '</strong>?';
      gebiedEl.innerHTML = '';
      opties.forEach((opt) => {
        const btn = document.createElement('button');
        btn.textContent = opt;
        btn.style.cssText = 'padding: 10px 20px; border-radius: 8px; border: 2px solid #e2e8f0; background: white; cursor: pointer; font-size: 1rem; margin: 4px;';
        btn.onmouseenter = () => { if (!btn.disabled) btn.style.borderColor = '#78716c'; };
        btn.onmouseleave = () => { if (!btn.disabled) btn.style.borderColor = '#e2e8f0'; };
        btn.onclick = () => {
          Array.from(gebiedEl.children).forEach(b => { b.disabled = true; b.style.opacity = '0.5'; });
          btn.style.opacity = '1';
          const isGoed = opt === getal;
          if (isGoed) {
            btn.style.borderColor = '#22c55e'; btn.style.background = '#dcfce7';
            correct++;
            feedbackEl.innerHTML = '✅ Goed! ' + romeins + ' = <strong>' + getal + '</strong>.';
            feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #dcfce7; color: #166534;';
          } else {
            btn.style.borderColor = '#ef4444'; btn.style.background = '#fee2e2';
            feedbackEl.innerHTML = '❌ Niet goed. ' + romeins + ' = <strong>' + getal + '</strong>.';
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
      nextBtn.style.cssText = 'margin-top: 8px; padding: 6px 16px; background: #78716c; color: white; border: none; border-radius: 6px; cursor: pointer;';
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