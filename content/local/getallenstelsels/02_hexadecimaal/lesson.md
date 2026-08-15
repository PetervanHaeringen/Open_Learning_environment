# Het Hexadecimale Stelsel

Programmeurs en ontwerpers gebruiken vaak **hexadecimaal** (basis 16). Waarom? Omdat het een perfecte tussenweg is tussen het mensvriendelijke decimaal en het computer-vriendelijke binair.

## Van 10 naar 16 cijfers

In het hexadecimale stelsel heb je 16 cijfers:

| Decimaal | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|----------|---|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|
| Hex | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | A | B | C | D | E | F |

## Het verband met binair

Dit is het mooiste: **1 hexadecimaal cijfer = precies 4 bits**.

| Hex | Binair | Decimaal |
|-----|--------|----------|
| 0 | 0000 | 0 |
| 5 | 0101 | 5 |
| A | 1010 | 10 |
| F | 1111 | 15 |

Een byte (8 bits) past dus precies in **2 hex-cijfers**: `FF` = `11111111` = 255.

## Kleuren in hex

Op het web worden kleuren vaak in hex geschreven: `#RRGGBB`.

<div style="display: flex; justify-content: center; gap: 16px; margin: 24px 0; flex-wrap: wrap;">
  <div style="text-align: center;">
    <div style="width: 80px; height: 80px; background: #FF0000; border-radius: 12px; border: 2px solid #e2e8f0;"></div>
    <div style="font-size: 0.8rem; color: #64748b; margin-top: 6px;">#FF0000<br>Rood</div>
  </div>
  <div style="text-align: center;">
    <div style="width: 80px; height: 80px; background: #00FF00; border-radius: 12px; border: 2px solid #e2e8f0;"></div>
    <div style="font-size: 0.8rem; color: #64748b; margin-top: 6px;">#00FF00<br>Groen</div>
  </div>
  <div style="text-align: center;">
    <div style="width: 80px; height: 80px; background: #0000FF; border-radius: 12px; border: 2px solid #e2e8f0;"></div>
    <div style="font-size: 0.8rem; color: #64748b; margin-top: 6px;">#0000FF<br>Blauw</div>
  </div>
  <div style="text-align: center;">
    <div style="width: 80px; height: 80px; background: #FFFFFF; border-radius: 12px; border: 2px solid #e2e8f0;"></div>
    <div style="font-size: 0.8rem; color: #64748b; margin-top: 6px;">#FFFFFF<br>Wit</div>
  </div>
  <div style="text-align: center;">
    <div style="width: 80px; height: 80px; background: #000000; border-radius: 12px; border: 2px solid #e2e8f0;"></div>
    <div style="font-size: 0.8rem; color: #64748b; margin-top: 6px;">#000000<br>Zwart</div>
  </div>
</div>

Elk kanaal (Rood, Groen, Blauw) krijgt 2 hex-cijfers = 1 byte = 256 mogelijkheden.

---

## 🎯 Oefenmodus

Oefen hier tot je **8 van de 10** vragen goed hebt. Pas dan wordt de officiële toets vrijgegeven.

<div id="hex-oefen" style="background: #faf5ff; border-radius: 12px; padding: 20px; margin-top: 20px; border: 2px solid #7c3aed;">
  <div style="display: flex; justify-content: space-between; margin-bottom: 12px;">
    <strong>Oefening <span id="h-vraagnr">1</span>/10</strong>
    <span style="color: #64748b;">Score: <span id="h-score">0</span>/10 (nodig: 8/10)</span>
  </div>
  <div id="h-opdracht" style="text-align: center; font-size: 1.1rem; margin: 16px 0;"></div>
  <div id="h-gebied" style="margin: 16px 0;"></div>
  <div id="h-feedback" style="margin-top: 12px; padding: 10px; border-radius: 8px; display: none;"></div>
  <div id="h-klaar" style="display: none; text-align: center; padding: 20px; background: #dcfce7; border-radius: 10px; margin-top: 12px;">
    <div style="font-size: 2rem;">🎉<p style="color: #166534; margin-top: 8px;">📝 Scroll naar beneden voor de officiële toets!</p>
  </div>
    <strong style="color: #166534;">Je beheerst hexadecimaal!</strong>
    <p style="color: #166534;">Beantwoord nu de vragen hieronder.</p>
  </div>
</div>

<script>
(function() {
  let current = 0, correct = 0;
  const opdrachtEl = document.getElementById('h-opdracht');
  const gebiedEl = document.getElementById('h-gebied');
  const feedbackEl = document.getElementById('h-feedback');
  const scoreEl = document.getElementById('h-score');
  const vraagnrEl = document.getElementById('h-vraagnr');
  const klaarEl = document.getElementById('h-klaar');

  function naarHex(n) {
    return n.toString(16).toUpperCase();
  }

  function genSom() {
    const mode = Math.random() > 0.5 ? 'naar-hex' : 'kleur-raden';

    if (mode === 'naar-hex') {
      const getal = Math.floor(Math.random() * 250 + 5);
      const hex = naarHex(getal);
      opdrachtEl.innerHTML = 'Zet het decimale getal <strong style="color: #7c3aed;">' + getal + '</strong> om naar hexadecimaal.<br><span style="font-size: 0.85rem; color: #64748b;">Typ het hexadecimale antwoord (bijvoorbeeld A3 of FF):</span>';
      gebiedEl.innerHTML = '<span style="font-size: 1.5rem; color: #7c3aed; font-weight: bold;">#</span><input type="text" id="h-input" maxlength="2" style="font-family: monospace; font-size: 1.3rem; padding: 10px 16px; border: 2px solid #e2e8f0; border-radius: 8px; text-align: center; width: 80px; text-transform: uppercase;" placeholder="00">' +
        '<button id="h-check" style="margin-left: 8px; padding: 10px 20px; background: #7c3aed; color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 1rem;">Controleer</button>';
      document.getElementById('h-check').onclick = () => {
        const input = document.getElementById('h-input').value.trim().toUpperCase();
        const isGoed = input === hex;
        document.getElementById('h-check').disabled = true;
        if (isGoed) {
          correct++;
          feedbackEl.innerHTML = '✅ Goed! ' + getal + ' = <strong>#' + hex + '</strong> in hexadecimaal.';
          feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #dcfce7; color: #166534;';
        } else {
          feedbackEl.innerHTML = '❌ Niet goed. ' + getal + ' = <strong>#' + hex + '</strong>. Tip: deel door 16, de rest is het rechter cijfer.';
          feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #fee2e2; color: #991b1b;';
        }
        scoreEl.textContent = correct;
        current++;
        vraagnrEl.textContent = current + 1;
        nextStep();
      };
    } else {
      const r = Math.floor(Math.random() * 256);
      const g = Math.floor(Math.random() * 256);
      const b = Math.floor(Math.random() * 256);
      const hexR = naarHex(r).padStart(2, '0');
      const hexG = naarHex(g).padStart(2, '0');
      const hexB = naarHex(b).padStart(2, '0');
      const hexKleur = '#' + hexR + hexG + hexB;
      opdrachtEl.innerHTML = 'Welke hex-kleur zie je hier?<br><span style="font-size: 0.85rem; color: #64748b;">Typ de volledige hex-code (bijvoorbeeld #FF5733):</span>';
      gebiedEl.innerHTML = '<div style="width: 120px; height: 120px; margin: 0 auto 12px; border-radius: 12px; border: 2px solid #e2e8f0;" style="background: ' + hexKleur + ';"></div>' +
        '<input type="text" id="h-input" maxlength="7" style="font-family: monospace; font-size: 1.3rem; padding: 10px 16px; border: 2px solid #e2e8f0; border-radius: 8px; text-align: center; width: 140px; text-transform: uppercase;" placeholder="#000000">' +
        '<button id="h-check" style="margin-left: 8px; padding: 10px 20px; background: #7c3aed; color: white; border: none; border-radius: 8px; cursor: pointer; font-size: 1rem;">Controleer</button>';
      document.getElementById('h-check').onclick = () => {
        const input = document.getElementById('h-input').value.trim().toUpperCase();
        const isGoed = input === hexKleur;
        document.getElementById('h-check').disabled = true;
        if (isGoed) {
          correct++;
          feedbackEl.innerHTML = '✅ Goed! De kleur is inderdaad <strong>' + hexKleur + '</strong>.';
          feedbackEl.style.cssText = 'margin-top: 12px; padding: 10px; border-radius: 8px; display: block; background: #dcfce7; color: #166534;';
        } else {
          feedbackEl.innerHTML = '❌ Niet goed. De kleur was <strong>' + hexKleur + '</strong>.';
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
      nextBtn.style.cssText = 'margin-top: 8px; padding: 6px 16px; background: #7c3aed; color: white; border: none; border-radius: 6px; cursor: pointer;';
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