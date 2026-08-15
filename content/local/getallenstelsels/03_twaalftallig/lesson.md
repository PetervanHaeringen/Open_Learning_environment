# Het Twaalftallige Stelsel

Waarom zitten er **12 eieren** in een doos? Waarom heeft een dag **2×12 uren**? Waarom zijn er **12 maanden** in een jaar? Het antwoord ligt in het **twaalftallige stelsel**.

## Waarom 12?

Het getal 12 is **veel beter deelbaar** dan 10:

| Delen door | 10 | 12 |
|------------|----|----|
| 2 | 5 ✓ | 6 ✓ |
| 3 | 3,33... ✗ | 4 ✓ |
| 4 | 2,5 ✗ | 3 ✓ |
| 6 | 1,67... ✗ | 2 ✓ |

12 heeft **meer delers** dan 10. Dat maakt het ideaal voor handel, bakken, en verdelen.

## Dozijn en gros

<div style="display: flex; justify-content: center; gap: 24px; margin: 24px 0; flex-wrap: wrap;">
  <div style="text-align: center; background: #fff7ed; border-radius: 12px; padding: 16px; border: 2px solid #ea580c; min-width: 140px;">
    <div style="font-size: 2.5rem; margin-bottom: 4px;">🥚</div>
    <div style="font-size: 1.3rem; font-weight: bold; color: #c2410c;">1 dozijn</div>
    <div style="font-size: 0.9rem; color: #64748b;">= 12 stuks</div>
  </div>
  <div style="text-align: center; background: #fff7ed; border-radius: 12px; padding: 16px; border: 2px solid #ea580c; min-width: 140px;">
    <div style="font-size: 2.5rem; margin-bottom: 4px;">📦</div>
    <div style="font-size: 1.3rem; font-weight: bold; color: #c2410c;">1 gros</div>
    <div style="font-size: 0.9rem; color: #64748b;">= 12 dozijn<br>= 144 stuks</div>
  </div>
</div>

## Restanten in onze taal

- **Twaalf maanden** in een jaar
- **24 uur** in een dag (2×12)
- **360 graden** in een cirkel (30×12)
- **Een dozijn** en **een gros** in de handel
- **Twaalf apostelen**, **twaalf olympische goden**

In het Engels: **dozen** en **gross**. In het Frans: **douzaine**.

---

## 🎯 Oefenmodus

Oefen hier tot je **8 van de 10** vragen goed hebt. Pas dan wordt de officiële toets vrijgegeven.

<div id="twaalf-oefen" style="background: #fff7ed; border-radius: 12px; padding: 20px; margin-top: 20px; border: 2px solid #ea580c;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
    <strong>Oefening <span id="t-vraagnr">1</span>/10</strong>
    <span style="color: #64748b;">Score: <span id="t-score">0</span>/10 (nodig: 8/10)</span>
  </div>
  <div id="t-opdracht" style="text-align: center; font-size: 1.1rem; margin: 16px 0;"></div>
  <div id="t-gebied" style="margin: 16px 0;"></div>
  <div id="t-feedback" style="margin-top: 12px; padding: 10px; border-radius: 8px; display: none;"></div>
  <div id="t-klaar" style="display: none; text-align: center; padding: 20px; background: #dcfce7; border-radius: 10px; margin-top: 12px;">
    <div style="font-size: 2rem;">🎉<p style="color: #166534; margin-top: 8px;">📝 Scroll naar beneden voor de officiële toets!</p>
  </div>
    <strong style="color: #166534;">Je beheerst het twaalftallig stelsel!</strong>
    <p style="color: #166534;">Beantwoord nu de vragen hieronder.</p>
  </div>
</div>

<script>
(function() {
  let current = 0, correct = 0;
  const opdrachtEl = document.getElementById('t-opdracht');
  const gebiedEl = document.getElementById('t-gebied');
  const feedbackEl = document.getElementById('t-feedback');
  const scoreEl = document.getElementById('t-score');
  const vraagnrEl = document.getElementById('t-vraagnr');
  const klaarEl = document.getElementById('t-klaar');

  function genSom() {
    const mode = Math.random() > 0.5 ? 'dozijn' : 'gros';

    if (mode === 'dozijn') {
      const dozijn = Math.floor(Math.random() * 20 + 1);
      const antwoord = dozijn * 12;
      const verkeerd = [dozijn * 10, dozijn * 20, antwoord + 12];
      const opties = [antwoord, ...verkeerd].sort(() => Math.random() - 0.5);

      opdrachtEl.innerHTML = 'Een bakker verkoopt <strong>' + dozijn + ' dozijn</strong> broodjes.<br>Hoeveel broodjes zijn dat in totaal?';
      gebiedEl.innerHTML = '';
      opties.forEach((opt) => {
        const btn = document.createElement('button');
        btn.textContent = opt;
        btn.style.cssText = 'padding: 10px 20px; border-radius: 8px; border: 2px solid #e2e8f0; background: white; cursor: pointer; font-size: 1rem; margin: 4px;';
        btn.onmouseenter = () => { if (!btn.disabled) btn.style.borderColor = '#ea580c'; };
        btn.onmouseleave = () => { if (!btn.disabled) btn.style.borderColor = '#e2e8f0'; };
        btn.onclick = () => {
          Array.from(gebiedEl.children).forEach(b => { b.disabled = true; b.style.opacity = '0.5'; });
          btn.style.opacity = '1';
          const isGoed = opt === antwoord;
          if (isGoed) {
            btn.style.borderColor = '#22c55e'; btn.style.background = '#dcfce7';
            correct++;
            feedbackEl.innerHTML = '✅ Goed! ' + dozijn + ' × 12 = <strong>' + antwoord + '</strong> broodjes.';
            feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #dcfce7; color: #166534;';
          } else {
            btn.style.borderColor = '#ef4444'; btn.style.background = '#fee2e2';
            feedbackEl.innerHTML = '❌ Niet goed. ' + dozijn + ' × 12 = <strong>' + antwoord + '</strong>.';
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
      const gros = Math.floor(Math.random() * 5 + 1);
      const antwoord = gros * 144;
      const verkeerd = [gros * 100, gros * 12, gros * 24];
      const opties = [antwoord, ...verkeerd].sort(() => Math.random() - 0.5);

      opdrachtEl.innerHTML = 'Een groothandel koopt <strong>' + gros + ' gros</strong> potloden.<br>Hoeveel potloden zijn dat in totaal?';
      gebiedEl.innerHTML = '';
      opties.forEach((opt) => {
        const btn = document.createElement('button');
        btn.textContent = opt;
        btn.style.cssText = 'padding: 10px 20px; border-radius: 8px; border: 2px solid #e2e8f0; background: white; cursor: pointer; font-size: 1rem; margin: 4px;';
        btn.onmouseenter = () => { if (!btn.disabled) btn.style.borderColor = '#ea580c'; };
        btn.onmouseleave = () => { if (!btn.disabled) btn.style.borderColor = '#e2e8f0'; };
        btn.onclick = () => {
          Array.from(gebiedEl.children).forEach(b => { b.disabled = true; b.style.opacity = '0.5'; });
          btn.style.opacity = '1';
          const isGoed = opt === antwoord;
          if (isGoed) {
            btn.style.borderColor = '#22c55e'; btn.style.background = '#dcfce7';
            correct++;
            feedbackEl.innerHTML = '✅ Goed! ' + gros + ' × 144 = <strong>' + antwoord + '</strong> potloden.';
            feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #dcfce7; color: #166534;';
          } else {
            btn.style.borderColor = '#ef4444'; btn.style.background = '#fee2e2';
            feedbackEl.innerHTML = '❌ Niet goed. ' + gros + ' × 144 = <strong>' + antwoord + '</strong> (1 gros = 12×12 = 144).';
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