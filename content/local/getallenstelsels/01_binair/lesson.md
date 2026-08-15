# Het Binaire Stelsel

Computers denken anders dan wij. Wij gebruiken 10 cijfers (0 t/m 9), maar een computer kent maar **twee toestanden**: aan of uit. Daarom gebruikt een computer het **binaire stelsel** — met slechts de cijfers **0** en **1**.

## Van decimaal naar binair

In het tientallig stelsel is elke positie een macht van 10:

| Positie | 3 | 2 | 1 | 0 |
|---------|---|---|---|---|
| Waarde | 1000 | 100 | 10 | 1 |

In het **binaire** stelsel is elke positie een macht van **2**:

| Positie | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|---------|---|---|---|---|---|---|---|---|
| Waarde | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

Een rij van 8 bits noemen we een **byte**. Met 1 byte kun je getallen van 0 tot 255 maken.

## Een byte in beeld

<div style="display: flex; justify-content: center; gap: 8px; margin: 24px 0; flex-wrap: wrap;" id="byte-display">
  <div style="text-align: center;" data-bit="7">
    <div class="lampje" style="width: 50px; height: 50px; border-radius: 50%; background: #e2e8f0; border: 3px solid #94a3b8; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: bold; color: #64748b;">0</div>
    <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">128</div>
  </div>
  <div style="text-align: center;" data-bit="6">
    <div class="lampje" style="width: 50px; height: 50px; border-radius: 50%; background: #e2e8f0; border: 3px solid #94a3b8; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: bold; color: #64748b;">0</div>
    <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">64</div>
  </div>
  <div style="text-align: center;" data-bit="5">
    <div class="lampje" style="width: 50px; height: 50px; border-radius: 50%; background: #e2e8f0; border: 3px solid #94a3b8; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: bold; color: #64748b;">0</div>
    <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">32</div>
  </div>
  <div style="text-align: center;" data-bit="4">
    <div class="lampje" style="width: 50px; height: 50px; border-radius: 50%; background: #e2e8f0; border: 3px solid #94a3b8; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: bold; color: #64748b;">0</div>
    <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">16</div>
  </div>
  <div style="text-align: center;" data-bit="3">
    <div class="lampje" style="width: 50px; height: 50px; border-radius: 50%; background: #e2e8f0; border: 3px solid #94a3b8; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: bold; color: #64748b;">0</div>
    <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">8</div>
  </div>
  <div style="text-align: center;" data-bit="2">
    <div class="lampje" style="width: 50px; height: 50px; border-radius: 50%; background: #e2e8f0; border: 3px solid #94a3b8; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: bold; color: #64748b;">0</div>
    <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">4</div>
  </div>
  <div style="text-align: center;" data-bit="1">
    <div class="lampje" style="width: 50px; height: 50px; border-radius: 50%; background: #e2e8f0; border: 3px solid #94a3b8; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: bold; color: #64748b;">0</div>
    <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">2</div>
  </div>
  <div style="text-align: center;" data-bit="0">
    <div class="lampje" style="width: 50px; height: 50px; border-radius: 50%; background: #e2e8f0; border: 3px solid #94a3b8; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: bold; color: #64748b;">0</div>
    <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;">1</div>
  </div>
</div>

<div style="text-align: center; font-size: 1.5rem; font-family: monospace; margin: 16px 0;">
  Totaal: <strong id="byte-totaal" style="color: #2563eb;">0</strong>
</div>

<div style="text-align: center; color: #64748b; font-size: 0.85rem; margin-bottom: 24px;">
  Klik op de lampjes om ze aan of uit te zetten.
</div>

## Voorbeeld: 13 in binair

<div style="background: #f8fafc; border-radius: 10px; padding: 16px; margin: 20px 0;">
  <p style="margin: 0 0 12px 0;">13 = 8 + 4 + 1 = <strong>00001101</strong></p>
  <div style="display: flex; gap: 4px; justify-content: center;">
    <div style="width: 36px; height: 36px; border-radius: 50%; background: #e2e8f0; display: flex; align-items: center; justify-content: center; font-size: 0.8rem;">0</div>
    <div style="width: 36px; height: 36px; border-radius: 50%; background: #e2e8f0; display: flex; align-items: center; justify-content: center; font-size: 0.8rem;">0</div>
    <div style="width: 36px; height: 36px; border-radius: 50%; background: #e2e8f0; display: flex; align-items: center; justify-content: center; font-size: 0.8rem;">0</div>
    <div style="width: 36px; height: 36px; border-radius: 50%; background: #e2e8f0; display: flex; align-items: center; justify-content: center; font-size: 0.8rem;">0</div>
    <div style="width: 36px; height: 36px; border-radius: 50%; background: #fbbf24; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: bold;">1</div>
    <div style="width: 36px; height: 36px; border-radius: 50%; background: #fbbf24; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: bold;">1</div>
    <div style="width: 36px; height: 36px; border-radius: 50%; background: #e2e8f0; display: flex; align-items: center; justify-content: center; font-size: 0.8rem;">0</div>
    <div style="width: 36px; height: 36px; border-radius: 50%; background: #fbbf24; display: flex; align-items: center; justify-content: center; font-size: 0.8rem; font-weight: bold;">1</div>
  </div>
</div>

---

## 🎯 Oefenmodus

Oefen hier tot je **8 van de 10** vragen goed hebt. Pas dan wordt de officiële toets vrijgegeven.

<div id="binair-oefen" style="background: #eff6ff; border-radius: 12px; padding: 20px; margin-top: 20px; border: 2px solid #2563eb;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
    <strong>Oefening <span id="b-vraagnr">1</span>/10</strong>
    <span style="color: #64748b;">Score: <span id="b-score">0</span>/10 (nodig: 8/10)</span>
  </div>
  <div id="b-opdracht" style="text-align: center; font-size: 1.1rem; margin: 16px 0;"></div>
  <div id="b-gebied" style="margin: 16px 0;"></div>
  <div id="b-feedback" style="margin-top: 12px; padding: 10px; border-radius: 8px; display: none;"></div>
  <div id="b-klaar" style="display: none; text-align: center; padding: 20px; background: #dcfce7; border-radius: 10px; margin-top: 12px;">
    <div style="font-size: 2rem;">🎉<p style="color: #166534; margin-top: 8px;">📝 Scroll naar beneden voor de officiële toets!</p>
  </div>
    <strong style="color: #166534;">Je beheerst binair!</strong>
    <p style="color: #166534;">Beantwoord nu de vragen hieronder.</p>
  </div>
</div>

<script>
(function() {
  const lampjes = document.querySelectorAll('#byte-display .lampje');
  const totaalEl = document.getElementById('byte-totaal');
  let byteWaarde = 0;
  const waardes = [128, 64, 32, 16, 8, 4, 2, 1];

  lampjes.forEach((lamp, idx) => {
    const bitWaarde = waardes[idx];
    lamp.addEventListener('click', () => {
      const isAan = lamp.textContent === '1';
      if (isAan) {
        lamp.textContent = '0';
        lamp.style.background = '#e2e8f0';
        lamp.style.color = '#64748b';
        byteWaarde -= bitWaarde;
      } else {
        lamp.textContent = '1';
        lamp.style.background = '#fbbf24';
        lamp.style.color = '#92400e';
        byteWaarde += bitWaarde;
      }
      totaalEl.textContent = byteWaarde;
    });
  });

  let current = 0, correct = 0;
  const opdrachtEl = document.getElementById('b-opdracht');
  const gebiedEl = document.getElementById('b-gebied');
  const feedbackEl = document.getElementById('b-feedback');
  const scoreEl = document.getElementById('b-score');
  const vraagnrEl = document.getElementById('b-vraagnr');
  const klaarEl = document.getElementById('b-klaar');

  function naarBinair(n) {
    return n.toString(2).padStart(8, '0');
  }

  function genSom() {
    const mode = Math.random() > 0.5 ? 'naar-binair' : 'naar-decimaal';
    const getal = Math.floor(Math.random() * 200 + 1);
    const binair = naarBinair(getal);

    if (mode === 'naar-binair') {
      opdrachtEl.innerHTML = 'Zet het decimale getal <strong style="color: #2563eb;">' + getal + '</strong> om naar binair.<br><span style="font-size: 0.85rem; color: #64748b;">Typ het 8-bits binaire getal:</span>';
      gebiedEl.innerHTML = '<input type="text" id="b-input" maxlength="8" style="font-family: monospace; font-size: 1.3rem; padding: 10px 16px; border: 2px solid #e2e8f0; border-radius: 8px; text-align: center; width: 160px; letter-spacing: 4px;" placeholder="00000000">' +
        '<button id="b-check" style="margin-left: 8px; padding: 10px 20px; background: #2563eb; color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 1rem;">Controleer</button>';
      document.getElementById('b-check').onclick = () => {
        const input = document.getElementById('b-input').value.trim();
        const isGoed = input === binair;
        document.getElementById('b-check').disabled = true;
        if (isGoed) {
          correct++;
          feedbackEl.innerHTML = '✅ Goed! ' + getal + ' = <strong>' + binair + '</strong>.';
          feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #dcfce7; color: #166534;';
        } else {
          feedbackEl.innerHTML = '❌ Niet goed. ' + getal + ' = <strong>' + binair + '</strong>.';
          feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #fee2e2; color: #991b1b;';
        }
        scoreEl.textContent = correct;
        current++;
        vraagnrEl.textContent = current + 1;
        nextStep();
      };
    } else {
      opdrachtEl.innerHTML = 'Wat is de decimale waarde van dit binaire getal?<br><strong style="font-family: monospace; font-size: 1.5rem; color: #2563eb; letter-spacing: 4px;">' + binair + '</strong>';
      gebiedEl.innerHTML = '<input type="number" id="b-input" style="font-family: monospace; font-size: 1.3rem; padding: 10px 16px; border: 2px solid #e2e8f0; border-radius: 8px; text-align: center; width: 120px;" placeholder="0">' +
        '<button id="b-check" style="margin-left: 8px; padding: 10px 20px; background: #2563eb; color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 1rem;">Controleer</button>';
      document.getElementById('b-check').onclick = () => {
        const input = parseInt(document.getElementById('b-input').value.trim());
        const isGoed = input === getal;
        document.getElementById('b-check').disabled = true;
        if (isGoed) {
          correct++;
          feedbackEl.innerHTML = '✅ Goed! ' + binair + ' = <strong>' + getal + '</strong>.';
          feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #dcfce7; color: #166534;';
        } else {
          feedbackEl.innerHTML = '❌ Niet goed. ' + binair + ' = <strong>' + getal + '</strong>.';
          feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #fee2e2; color: #991b1b;';
        }
        scoreEl.textContent = correct;
        current++;
        vraagnrEl.textContent = current + 1;
        nextStep();
      };
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